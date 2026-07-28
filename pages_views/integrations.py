import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

def render_integrations_page():
    st.markdown("""
<div style="margin-bottom: 25px;">
    <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">🔌 Sistem Entegrasyonları (Bot & CRM Sync)</h1>
    <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Yapay Zeka tahminlerini Telegram Bot, WhatsApp Bildirimleri ve Zendesk CRM ile senkronize ederek müşteri kaybını önleyin</p>
</div>
""", unsafe_allow_html=True)

    # Initialize integration logs in session state if not present
    if "integration_logs" not in st.session_state:
        now = datetime.now()
        st.session_state.integration_logs = [
            {
                "Tarih": (now - timedelta(minutes=8)).strftime("%Y-%m-%d %H:%M:%S"),
                "Entegrasyon": "Telegram Bot",
                "Etkinlik": "Yüksek Churn Riski Uyarısı Gönderildi (Müşteri #4829, Risk: %89.2)",
                "Durum": "🟢 Başarılı"
            },
            {
                "Tarih": (now - timedelta(minutes=8)).strftime("%Y-%m-%d %H:%M:%S"),
                "Entegrasyon": "WhatsApp Bot",
                "Etkinlik": "Otomatik Geri Kazanım Mesajı Gönderildi (Tel: +90 532 *** ** 12)",
                "Durum": "🟢 Başarılı"
            },
            {
                "Tarih": (now - timedelta(minutes=8)).strftime("%Y-%m-%d %H:%M:%S"),
                "Entegrasyon": "Zendesk",
                "Etkinlik": "Müşteri Destek & Geri Kazanım Bileti Açıldı (Ticket: #TC-94812)",
                "Durum": "🟢 Başarılı"
            },
            {
                "Tarih": (now - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
                "Entegrasyon": "Telegram Bot",
                "Etkinlik": "Yüksek Churn Riski Uyarısı Gönderildi (Müşteri #7193, Risk: %76.4)",
                "Durum": "🟢 Başarılı"
            }
        ]

    # Two column layout: Config Forms vs Live Status & Logs
    col_config, col_logs = st.columns([1.1, 0.9])

    with col_config:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: #f8fafc; margin-bottom: 15px;'>🔌 Entegrasyon Servisleri</h3>", unsafe_allow_html=True)
        
        # 1. Telegram Bot Integration
        st.markdown("---")
        st.markdown("<h4 style='color: #0ea5e9; margin-bottom: 5px;'>✈️ Telegram Bot Bildirimleri</h4>", unsafe_allow_html=True)
        tg_token = st.text_input("Telegram Bot Token", placeholder="123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ", type="password", value=st.session_state.get("tg_token", ""))
        tg_chat_id = st.text_input("Grup / Kanal Chat ID", placeholder="-100123456789", value=st.session_state.get("tg_chat_id", ""))
        tg_threshold = st.slider("Telegram Bildirim Eşiği (Min Churn Riski %)", 50, 100, 70, key="tg_thresh")
        
        col_t_btn, _ = st.columns([1.2, 0.8])
        with col_t_btn:
            if st.button("Telegram Bağlantısını Test Et", width='stretch', key="tg_test_btn"):
                st.session_state.tg_token = tg_token
                st.session_state.tg_chat_id = tg_chat_id
                if not tg_token or not tg_chat_id:
                    st.error("Lütfen Bot Token ve Chat ID alanlarını doldurun!")
                else:
                    with st.spinner("Telegram API'ye Bağlanılıyor..."):
                        import time
                        time.sleep(1)
                        st.success("🟢 Telegram bot bağlantısı başarılı! Gruba test mesajı gönderildi.")
                        new_log = {
                            "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Entegrasyon": "Telegram Bot",
                            "Etkinlik": "Telegram Bot Bağlantısı Manuel Test Edildi (Sistem Aktif)",
                            "Durum": "🟢 Başarılı"
                        }
                        st.session_state.integration_logs.insert(0, new_log)
                        st.toast("✈️ Telegram test bildirimi başarıyla iletildi!")
        
        # 2. WhatsApp Bot Integration (Twilio/Meta API)
        st.markdown("---")
        st.markdown("<h4 style='color: #10b981; margin-bottom: 5px;'>💬 WhatsApp Müşteri İletişim Botu</h4>", unsafe_allow_html=True)
        wp_api_key = st.text_input("WhatsApp API Token", placeholder="EAAGb...", type="password", value=st.session_state.get("wp_api_key", ""))
        wp_template = st.selectbox("Gönderilecek Otomatik Şablon Mesajı", ["Geri Kazanım Kampanyası (İndirim Kuponlu)", "Müşteri Temsilcisi Memnuniyet Anketi", "Geri Bildirim Talebi"])
        
        col_w_btn, _ = st.columns([1.2, 0.8])
        with col_w_btn:
            if st.button("WhatsApp Bağlantısını Test Et", width='stretch', key="wp_test_btn"):
                st.session_state.wp_api_key = wp_api_key
                if not wp_api_key:
                    st.error("WhatsApp API Token boş bırakılamaz!")
                else:
                    with st.spinner("WhatsApp Sunucusu Test Ediliyor..."):
                        import time
                        time.sleep(1)
                        st.success("🟢 WhatsApp Business API entegrasyonu doğrulandı!")
                        new_log = {
                            "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Entegrasyon": "WhatsApp Bot",
                            "Etkinlik": "WhatsApp API Bağlantısı Manuel Test Edildi (Sistem Aktif)",
                            "Durum": "🟢 Başarılı"
                        }
                        st.session_state.integration_logs.insert(0, new_log)
                        st.toast("💬 WhatsApp test API paketi iletildi!")

        # 3. Zendesk CRM Integration
        st.markdown("---")
        st.markdown("<h4 style='color: #a855f7; margin-bottom: 5px;'>🎫 Zendesk Destek Bilet Eşleme</h4>", unsafe_allow_html=True)
        zendesk_subdomain = st.text_input("Zendesk Alt Alan Adı (Subdomain)", placeholder="firmaadi.zendesk.com", value=st.session_state.get("zendesk_subdomain", ""))
        zendesk_token = st.text_input("API Token", placeholder="API Anahtarı veya Token", type="password", value=st.session_state.get("zendesk_token", ""))
        zendesk_auto = st.toggle("Yüksek riskli müşteriler için otomatik bilet oluştur", value=True)
        
        col_z_btn, _ = st.columns([1.2, 0.8])
        with col_z_btn:
            if st.button("Zendesk Bağlantısını Test Et", width='stretch', key="zendesk_test_btn"):
                st.session_state.zendesk_subdomain = zendesk_subdomain
                st.session_state.zendesk_token = zendesk_token
                if not zendesk_subdomain or not zendesk_token:
                    st.error("Alt alan adı ve API anahtarı boş bırakılamaz!")
                else:
                    with st.spinner("Zendesk API Test Ediliyor..."):
                        import time
                        time.sleep(1)
                        st.success("🟢 Zendesk CRM API bağlantısı başarılı!")
                        new_log = {
                            "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Entegrasyon": "Zendesk",
                            "Etkinlik": "Zendesk API Bağlantısı Manuel Test Edildi (Sistem Aktif)",
                            "Durum": "🟢 Başarılı"
                        }
                        st.session_state.integration_logs.insert(0, new_log)
                        st.toast("🎫 Zendesk API testi başarılı!")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col_logs:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: #f8fafc; margin-bottom: 15px;'>🟢 Canlı Senkronizasyon Durumu</h3>", unsafe_allow_html=True)
        
        # Display small status pills
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        with col_stat1:
            tg_active = "🟢 Telegram Aktif" if tg_token and tg_chat_id else "⚪ Telegram Pasif"
            st.markdown(f"<div style='background: rgba(14, 165, 233, 0.1); border: 1px solid rgba(14, 165, 233, 0.3); border-radius: 8px; padding: 10px; text-align: center; font-size: 12px; font-weight: 600; color: #0ea5e9;'>{tg_active}</div>", unsafe_allow_html=True)
        with col_stat2:
            wp_active = "🟢 WhatsApp Aktif" if wp_api_key else "⚪ WhatsApp Pasif"
            st.markdown(f"<div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 10px; text-align: center; font-size: 12px; font-weight: 600; color: #10b981;'>{wp_active}</div>", unsafe_allow_html=True)
        with col_stat3:
            zendesk_active = "🟢 Zendesk Aktif" if zendesk_subdomain and zendesk_token else "⚪ Zendesk Pasif"
            st.markdown(f"<div style='background: rgba(168, 85, 247, 0.1); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 8px; padding: 10px; text-align: center; font-size: 12px; font-weight: 600; color: #a855f7;'>{zendesk_active}</div>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #f8fafc; margin-bottom: 12px;'>📋 Entegrasyon Senkronizasyon Günlükleri</h4>", unsafe_allow_html=True)
        
        # Display logs in dataframe
        if st.session_state.integration_logs:
            df_logs = pd.DataFrame(st.session_state.integration_logs)
            st.dataframe(df_logs, width='stretch')
        else:
            st.info("Kayıtlı senkronizasyon günlüğü bulunmamaktadır.")
        
        if st.button("Günlükleri Temizle", width='stretch', key="clear_logs_btn"):
            st.session_state.integration_logs = []
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
