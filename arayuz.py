"""LoyalCart Streamlit application entry point."""

import hmac
import os

import streamlit as st
import streamlit.components.v1 as components

from components.sidebar import render_sidebar
from data_loader import get_synthetic_data
from db.repository import (
    DuplicateUserError,
    authenticate_user,
    create_user,
    initialize_database,
    record_audit,
)
from db.security import (
    create_password_reset_token,
    initialize_security_tables,
    reset_password,
)
from services.email_service import send_password_reset_email
from pages_views.cohort import render_cohort_page
from pages_views.complaints import render_complaints_page
from pages_views.customer_analysis import render_customer_analysis_page
from pages_views.dashboard import render_dashboard_page
from pages_views.early_warning import render_early_warning_page
from pages_views.history import render_history_page
from pages_views.integrations import render_integrations_page
from pages_views.nps_league import render_nps_league_page
from pages_views.segmentation import render_segmentation_page
from pages_views.simulation import render_simulation_page
from styles import (
    get_3d_javascript,
    get_custom_css,
    get_login_css,
    get_login_javascript,
)


st.set_page_config(
    page_title="LoyalCart Yönetici Paneli",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def rerun() -> None:
    if hasattr(st, "rerun"):
        st.rerun()
    st.experimental_rerun()


def query_value(name: str):
    try:
        value = st.query_params.get(name)
    except AttributeError:
        value = st.experimental_get_query_params().get(name)
    if isinstance(value, list):
        value = value[0] if value else None
    return value


def query_flag(name: str) -> bool:
    return str(query_value(name)).lower() == "true"


def render_brand() -> None:
    st.markdown(
        """
        <div class="logo-container" style="text-align:center;margin-bottom:28px">
          <span class="logo-text" style="font-weight:900;font-size:44px">
            L<span class="logo-emoji-circle"
              style="background:linear-gradient(135deg,#10b981,#0ea5e9);
              width:48px;height:48px;border-radius:50%;display:inline-flex;
              align-items:center;justify-content:center;font-size:24px">🛒</span>yalCart
          </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_password_reset() -> None:
    render_brand()
    st.markdown(
        "<h1 style='font-size:28px;text-align:center'>Şifre Sıfırlama</h1>",
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        identifier = st.text_input(
            "Kullanıcı adı veya e-posta",
            placeholder="Kullanıcı adı veya e-posta",
            label_visibility="collapsed",
        )
        if st.button("Sıfırlama Talebi Oluştur", use_container_width=True):
            if not identifier:
                st.error("Lütfen kullanıcı adınızı veya e-posta adresinizi girin.")
            else:
                reset_request = create_password_reset_token(identifier)
                delivery_status = "account_not_found"
                if reset_request:
                    token, email = reset_request
                    try:
                        delivery_status = (
                            "email_sent"
                            if send_password_reset_email(email, token)
                            else "smtp_not_configured"
                        )
                    except Exception:
                        delivery_status = "email_failed"
                record_audit(
                    "password_reset_requested", delivery_status, identifier
                )
                st.info(
                    "Hesap kayıtlı ve e-posta servisi yapılandırılmışsa, "
                    "30 dakika geçerli sıfırlama bağlantısı gönderilmiştir."
                )
        st.markdown(
            '<p style="text-align:center"><a href="?forgot=false" '
            'target="_self">Giriş ekranına dön</a></p>',
            unsafe_allow_html=True,
        )


def render_new_password(token: str) -> None:
    render_brand()
    st.markdown(
        "<h1 style='font-size:28px;text-align:center'>Yeni Şifre Belirle</h1>",
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        password = st.text_input(
            "Yeni şifre", type="password", placeholder="En az 8 karakter"
        )
        confirmation = st.text_input("Yeni şifre tekrar", type="password")
        if st.button("Şifreyi Güncelle", use_container_width=True):
            if password != confirmation:
                st.error("Şifreler uyuşmuyor.")
            else:
                try:
                    if reset_password(token, password):
                        record_audit("password_reset_completed", "success")
                        st.success(
                            "Şifreniz güncellendi. Bu bağlantı tekrar kullanılamaz."
                        )
                        st.markdown(
                            '<p style="text-align:center"><a href="./" '
                            'target="_self">Giriş ekranına dön</a></p>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.error("Bağlantı geçersiz, kullanılmış veya süresi dolmuş.")
                except ValueError as exc:
                    st.error(str(exc))


def render_registration() -> None:
    render_brand()
    st.markdown(
        "<h1 style='font-size:28px;text-align:center'>Yönetici Kaydı</h1>",
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        username = st.text_input("Kullanıcı adı", placeholder="Kullanıcı adı")
        email = st.text_input("E-posta", placeholder="E-posta")
        password = st.text_input("Şifre", type="password", placeholder="En az 8 karakter")
        confirmation = st.text_input("Şifre tekrar", type="password")
        invite_code = st.text_input("Davet kodu", type="password")

        if st.button("Kayıt Ol", use_container_width=True):
            expected_invite = os.getenv("LOYALCART_INVITE_CODE")
            if not all((username, email, password, confirmation, invite_code)):
                st.error("Lütfen tüm alanları doldurun.")
            elif password != confirmation:
                st.error("Şifreler uyuşmuyor.")
            elif not expected_invite:
                st.error("Kayıt özelliği yönetici tarafından yapılandırılmamış.")
            elif not hmac.compare_digest(invite_code, expected_invite):
                st.error("Geçersiz davet kodu.")
            else:
                try:
                    create_user(username, email, password, role="manager")
                    record_audit("user_registered", "success", username)
                    st.success("Kullanıcı hesabı oluşturuldu.")
                except (DuplicateUserError, ValueError) as exc:
                    st.error(str(exc))

        st.markdown(
            '<p style="text-align:center"><a href="?register=false" '
            'target="_self">Giriş ekranına dön</a></p>',
            unsafe_allow_html=True,
        )


def render_login() -> None:
    render_brand()
    st.markdown(
        "<h1 style='font-size:28px;text-align:center'>Yönetici Girişi</h1>",
        unsafe_allow_html=True,
    )
    with st.container(border=False, key="login_form"):
        username = st.text_input(
            "Kullanıcı adı",
            placeholder="Kullanıcı adınızı girin",
            key="login_user_input",
        )
        password = st.text_input(
            "Şifre",
            type="password",
            placeholder="Şifrenizi girin",
            key="login_pwd_input",
        )
        st.caption("Kimlik bilgileri tarayıcı depolamasında veya URL'de saklanmaz.")
        st.markdown(
            '<p style="text-align:right"><a href="?forgot=true" '
            'target="_self">Şifremi unuttum</a></p>',
            unsafe_allow_html=True,
        )

        if st.button("Giriş Yap", use_container_width=True):
            if not username.strip() or not password:
                st.error("Lütfen kullanıcı adı ve şifre alanlarını doldurun.")
            elif user := authenticate_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = user["username"]
                st.session_state.role = user["role"]
                record_audit("login", "success", user["username"])
                rerun()
            else:
                record_audit("login", "failed", username or None)
                st.error("Geçersiz kullanıcı adı veya şifre.")

        if not os.getenv("LOYALCART_ADMIN_PASSWORD"):
            st.caption(
                "İlk yönetici hesabı için LOYALCART_ADMIN_PASSWORD ortam "
                "değişkenini ayarlayın."
            )
        st.markdown(
            '<p style="text-align:center">Hesabınız yok mu? '
            '<a href="?register=true" target="_self">Kayıt ol</a></p>',
            unsafe_allow_html=True,
        )


try:
    initialize_database()
    initialize_security_tables()
except Exception as exc:
    st.error(f"Veritabanı başlatılamadı: {exc}")
    st.stop()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown(get_login_css(), unsafe_allow_html=True)
    components.html(get_login_javascript(), height=1, width=1)
    _, login_column, _ = st.columns([1, 1.8, 1])
    with login_column:
        reset_token = query_value("reset_token")
        if reset_token:
            render_new_password(str(reset_token))
        elif query_flag("forgot"):
            render_password_reset()
        elif query_flag("register"):
            render_registration()
        else:
            render_login()
    st.stop()

st.markdown(get_custom_css(), unsafe_allow_html=True)
st.markdown(get_3d_javascript(), unsafe_allow_html=True)

synthetic_data = get_synthetic_data()
selected_menu = render_sidebar()

ROUTES = {
    "📊 Genel Durum (Dashboard)": lambda: render_dashboard_page(synthetic_data),
    "🔮 Churn Simülasyonu (What-If)": lambda: render_simulation_page(synthetic_data),
    "🚨 Erken Uyarı & Aksiyon Merkezi": lambda: render_early_warning_page(synthetic_data),
    "📈 Kohort Analiz Raporu": lambda: render_cohort_page(synthetic_data),
    "💬 Şikayet & Bilet Yönetimi": lambda: render_complaints_page(synthetic_data),
    "⭐ NPS & Müşteri Bağlılık Ligi": lambda: render_nps_league_page(synthetic_data),
    "🔍 Müşteri Analiz Paneli": lambda: render_customer_analysis_page(synthetic_data),
    "👥 Müşteri Segmentasyonu": lambda: render_segmentation_page(synthetic_data),
    "📋 Geçmiş Tahmin Kayıtları": render_history_page,
    "🔌 Sistem Entegrasyonları": render_integrations_page,
}

route = ROUTES.get(selected_menu)
if route:
    route()
