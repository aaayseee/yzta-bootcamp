# Sprint 4 Product Backlog

## Sprint hedefi

LoyalCart'ı güvenli kimlik doğrulama, merkezi veritabanı ve test edilebilir
tahmin servisine geçirmek.

| Öncelik | İş | Kabul kriteri | Durum |
|---|---|---|---|
| P0 | Streamlit açılış uyumluluğu | Uygulama istisnasız açılır | Tamamlandı |
| P0 | Güvenli kullanıcı deposu | Parolalar PBKDF2 hash olarak tutulur | Tamamlandı |
| P0 | Güvenli oturum | Parola URL/localStorage içinde bulunmaz | Tamamlandı |
| P0 | Rol tabanlı erişim | Entegrasyon ekranı yalnızca administrator tarafından görülür | Tamamlandı |
| P0 | Merkezi tahmin geçmişi | API ve fallback aynı DB şemasını kullanır | Tamamlandı |
| P0 | SQLite/MySQL ortak repository | `DB_ENGINE` ile veritabanı seçilebilir | Tamamlandı |
| P1 | API health ve API anahtarı | `/health` çalışır, yapılandırılmışsa anahtar zorunludur | Tamamlandı |
| P1 | Otomatik testler | Kullanıcı, DB, API ve Streamlit açılışı doğrulanır | Tamamlandı |
| P1 | Gerçek Telegram entegrasyonu | Test mesajı gerçek Telegram yanıtına göre sonuçlanır | Tamamlandı |
| P2 | Süreli şifre reset tokenı ve e-posta | Tek kullanımlık token ile parola değişir | Tamamlandı |
| P2 | Docker Compose ve CI | Streamlit, FastAPI ve MySQL tek komutla başlar | Tamamlandı |
