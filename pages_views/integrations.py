import os

import pandas as pd
import requests
import streamlit as st

from db.security import (
    clear_integration_events,
    list_integration_events,
    record_integration_event,
)
from services.telegram import TelegramError, send_telegram_message


def render_integrations_page():
    if st.session_state.get("role") != "administrator":
        st.error("Bu sayfa için administrator rolü gerekir.")
        return

    st.markdown(
        """
        <div style="margin-bottom:25px">
          <h1 class="animated-gradient-text"
            style="font-size:34px;font-weight:800;margin:0">
            🔌 Sistem Entegrasyonları
          </h1>
          <p style="color:#94a3b8;margin:5px 0 0;font-size:15px">
            Telegram bağlantısını doğrulayın ve gerçek entegrasyon olaylarını izleyin
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    configuration, logs_column = st.columns([1, 1])
    with configuration:
        st.subheader("✈️ Telegram Bot")
        token_input = st.text_input(
            "Bot Token",
            type="password",
            placeholder="Boşsa TELEGRAM_BOT_TOKEN kullanılır",
        )
        chat_input = st.text_input(
            "Chat ID",
            placeholder="Boşsa TELEGRAM_CHAT_ID kullanılır",
        )
        threshold = st.slider(
            "Otomatik bildirim eşiği (%)",
            50,
            100,
            int(os.getenv("TELEGRAM_CHURN_THRESHOLD", "70")),
        )
        st.caption(
            f"Aktif eşik: %{threshold}. Canlı ortamda değerleri `.env` veya "
            "platform secrets alanından vermeniz önerilir."
        )

        if st.button(
            "Telegram'a Gerçek Test Mesajı Gönder",
            use_container_width=True,
            key="telegram_real_test",
        ):
            token = token_input or os.getenv("TELEGRAM_BOT_TOKEN", "")
            chat_id = chat_input or os.getenv("TELEGRAM_CHAT_ID", "")
            try:
                result = send_telegram_message(
                    token,
                    chat_id,
                    "✅ LoyalCart Telegram entegrasyonu başarıyla doğrulandı.",
                )
                telegram_message_id = result["result"]["message_id"]
                record_integration_event(
                    "telegram",
                    "connection_test",
                    "success",
                    f"Test mesajı gönderildi. message_id={telegram_message_id}",
                    st.session_state.get("username"),
                )
                st.success(
                    f"Telegram mesajı gönderildi. Mesaj ID: {telegram_message_id}"
                )
            except (TelegramError, KeyError) as exc:
                record_integration_event(
                    "telegram",
                    "connection_test",
                    "failed",
                    str(exc),
                    st.session_state.get("username"),
                )
                st.error(str(exc))
            except requests.RequestException as exc:
                message = f"Telegram bağlantı hatası: {exc}"
                record_integration_event(
                    "telegram",
                    "connection_test",
                    "failed",
                    message,
                    st.session_state.get("username"),
                )
                st.error(message)

        st.divider()
        st.subheader("WhatsApp ve Zendesk")
        st.info(
            "Bu sağlayıcılar demo başarı mesajı üretmez. Gerçek kimlik bilgileri "
            "ve sağlayıcı sözleşmeleri hazır olduğunda ayrı adaptörlerle etkinleştirilecektir."
        )

    with logs_column:
        st.subheader("📋 Kalıcı Entegrasyon Günlükleri")
        events = list_integration_events()
        if events:
            st.dataframe(pd.DataFrame(events), use_container_width=True)
        else:
            st.info("Henüz entegrasyon olayı bulunmuyor.")
        if st.button("Günlükleri Temizle", use_container_width=True):
            clear_integration_events()
            st.success("Entegrasyon günlükleri temizlendi.")
            st.rerun()
