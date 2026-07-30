# Sprint 4 Review

Tarih: 30 Temmuz 2026  
Ekip: Ekip-116 — Churn Prediction & Müşteri Segmentasyon

## Sprint hedefi

LoyalCart uygulamasını güvenli kimlik doğrulama, merkezi veritabanı,
gerçek entegrasyonlar ve otomatik testlerle teslime hazır hâle getirmek.

## Tamamlanan ürün artımları

- PBKDF2 ile güvenli parola saklama ve kullanıcı doğrulama
- Administrator, manager ve viewer rollerine dayalı yetkilendirme
- SQLite ve MySQL destekli ortak repository katmanı
- API ve Streamlit tarafından paylaşılan tahmin servisi
- Tahmin geçmişinin merkezi veritabanına kaydedilmesi
- API anahtarıyla korunan FastAPI tahmin endpoint'i
- Tek kullanımlık ve süreli şifre sıfırlama tokenı
- SMTP üzerinden şifre sıfırlama e-postası
- Gerçek Telegram Bot API bağlantısı ve yüksek risk bildirimi
- Kalıcı entegrasyon ve güvenlik olay kayıtları
- Docker Compose ve GitHub Actions CI yapılandırması
- Mobil uyumlu ve doğrulama mesajları iyileştirilmiş login ekranı
- Repository, güvenlik, API, e-posta, Telegram ve Streamlit testleri

## Test ve kabul sonuçları

| Kabul kriteri | Sonuç |
|---|---|
| Python kaynakları hatasız derleniyor | Başarılı |
| Güvenli kullanıcı ve parola akışı çalışıyor | Başarılı |
| API anahtar kontrolü ve tahmin kaydı çalışıyor | Başarılı |
| Şifre sıfırlama tokenı tek kullanımlık | Başarılı |
| Telegram başarı ve hata yanıtları doğrulanıyor | Başarılı |
| Login ve 10 Streamlit sayfası hatasız açılıyor | Başarılı |
| Toplam 12 otomatik test geçiyor | Başarılı |
| GitHub Actions katı CI çalışması yeşil | Başarılı |

## Öne çıkan commitler

| Commit | Açıklama |
|---|---|
| `0d215b7` | Merkezi veritabanı ve ortak tahmin servisi |
| `d0fad90` | Ortam yapılandırması ve repository testleri |
| `991dc51` | Güvenlik, şifre sıfırlama ve entegrasyon kayıtları |
| `59c5edb` | Yüksek churn riski için Telegram bildirimi |
| `54772bf` | Docker ve GitHub Actions altyapısı |
| `48af7b3` | API testleri için eksik HTTP istemcisi bağımlılığı |
| `bfe8a53` | Streamlit testleri için kararlı PyArrow sürümü |
| `14390d7` | Login doğrulaması ve responsive görünüm iyileştirmesi |

## Sprint sonucu

Sprint backlog'undaki tüm maddeler tamamlandı. Ürün yerel testler ve GitHub
Actions üzerinde doğrulandı; README, ortam değişkenleri ve çalıştırma
talimatları teslim için güncellendi.
