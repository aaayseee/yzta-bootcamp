# 🛒 LoyalCart — Churn Tahmin ve Müşteri Segmentasyon Platformu

LoyalCart, e-ticaret müşterilerinin kayıp (churn) olasılığını Random Forest
modeliyle tahmin eden; risk analizi, segmentasyon, aksiyon önerileri ve kalıcı
tahmin geçmişi sunan bir YZTA Bootcamp projesidir.

## Takım

- Halil İbrahim ARİ — Product Owner
- Zeynep Yağmur TÜRKELİ — Scrum Master
- Ayşe ULAŞLI — Developer
- Tümer GÜNEŞ — Developer

## Güncel durum

Sprint 4 ile proje aşağıdaki üretim temellerine taşındı:

- Güvenli, hashlenmiş kullanıcı parolaları
- `administrator`, `manager` ve `viewer` rolleri
- SQLite/MySQL ortak repository katmanı
- FastAPI ve Streamlit tarafından paylaşılan tahmin servisi
- API kesintisinde yerel model fallback
- CSV yerine veritabanından okunan tahmin geçmişi
- API anahtarı koruması ve `/health` endpoint'i
- Gerçek Telegram Bot API bağlantısı ve kalıcı entegrasyon logları
- 30 dakika geçerli, tek kullanımlık şifre sıfırlama tokenları
- SMTP üzerinden şifre sıfırlama e-postası
- Docker Compose ve GitHub Actions CI
- Kullanıcı, veritabanı, API, Telegram ve Streamlit smoke testleri

WhatsApp ve Zendesk ekranları artık sahte başarı üretmez. Bu sağlayıcılar gerçek
hesap bilgileri ve servis sözleşmeleri hazır olduğunda ayrı adaptörlerle
etkinleştirilecektir.

## Özellikler

Portalda 10 modül bulunur:

1. 📊 Genel Durum Dashboard
2. 🔮 Churn Simülasyonu
3. 🚨 Erken Uyarı ve Aksiyon Merkezi
4. 📈 Kohort Analizi
5. 💬 Şikayet ve Bilet Yönetimi
6. ⭐ NPS ve Müşteri Bağlılık Ligi
7. 🔍 Bireysel Müşteri Analizi
8. 👥 Müşteri Segmentasyonu
9. 📋 Kalıcı Tahmin Geçmişi
10. 🔌 Sistem Entegrasyonları

Entegrasyon ekranı yalnızca `administrator` rolüne açıktır. Tahmin geçmişini
temizleme işlemi de administrator yetkisi gerektirir.

## Mimari

```text
                       ┌─────────────────────────┐
                       │  Streamlit / arayuz.py  │
                       │         :8501           │
                       └────────────┬────────────┘
                                    │ HTTP
                                    ▼
                       ┌─────────────────────────┐
                       │   FastAPI / main.py     │
                       │         :8000           │
                       └────────────┬────────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
       prediction_service.py   db/repository.py   Telegram / SMTP
                 │                  │
                 ▼                  ▼
          churn_modeli.pkl     SQLite veya MySQL
```

FastAPI erişilemezse Streamlit, modeli doğrudan
`prediction_service.py` üzerinden çalıştırır. Her iki yol da aynı tahmin
şemasını ve veritabanı repository katmanını kullanır.

## Proje yapısı

```text
.
├── arayuz.py                    # Streamlit giriş noktası ve güvenli oturum
├── main.py                      # FastAPI tahmin API'si
├── prediction_service.py        # Ortak model tahmin servisi
├── data_loader.py               # Sentetik veri ve DB geçmiş görünümü
├── churn_modeli.pkl             # Eğitilmiş Random Forest modeli
├── components/
│   ├── plotly_theme.py
│   └── sidebar.py
├── db/
│   ├── repository.py            # Kullanıcı ve tahmin repository'si
│   ├── security.py              # Reset tokenları ve entegrasyon logları
│   └── mysql_init.sql
├── services/
│   ├── telegram.py
│   └── email_service.py
├── pages_views/                 # 10 Streamlit sayfa modülü
├── scripts/create_mysql_db.py
├── tests/
├── Sprint1/
├── Sprint2/
├── Sprint3/
├── Sprint4/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Yerel kurulum

Python 3.12 önerilir.

### 1. Sanal ortam

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Ortam değişkenleri

`.env.example` dosyasını `.env` olarak kopyalayın ve örnek değerleri değiştirin.
Uygulama `.env` dosyasını kendiliğinden yüklemez; değişkenleri terminal,
deployment platformu veya Streamlit secrets alanı üzerinden sağlamalısınız.

En az şu değerler gereklidir:

```text
DB_ENGINE=sqlite
SQLITE_PATH=loyalcart.db
LOYALCART_ADMIN_PASSWORD=güçlü-bir-yönetici-şifresi
LOYALCART_INVITE_CODE=gizli-bir-davet-kodu
LOYALCART_API_KEY=gizli-bir-api-anahtarı
LOYALCART_API_URL=http://127.0.0.1:8000
```

İlk çalıştırmada admin hesabı `LOYALCART_ADMIN_USERNAME`,
`LOYALCART_ADMIN_EMAIL` ve `LOYALCART_ADMIN_PASSWORD` değerleriyle oluşturulur.
Parola kaynak koda veya veritabanına düz metin olarak yazılmaz.

### 3. Servisleri çalıştırma

Terminal 1 — FastAPI:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Terminal 2 — Streamlit:

```bash
streamlit run arayuz.py
```

Adresler:

- Streamlit: `http://localhost:8501`
- FastAPI: `http://localhost:8000`
- API dokümantasyonu: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

## Docker Compose

Docker kurulumu Streamlit, FastAPI ve MySQL servislerini birlikte başlatır.
Önce gerekli secret değerlerini terminalde veya `.env` dosyasında tanımlayın:

```text
LOYALCART_ADMIN_PASSWORD=...
LOYALCART_INVITE_CODE=...
LOYALCART_API_KEY=...
MYSQL_PASSWORD=...
MYSQL_ROOT_PASSWORD=...
```

Ardından:

```bash
docker compose up --build
```

MySQL verisi `loyalcart_mysql` adlı Docker volume içinde kalıcı tutulur.

## Telegram entegrasyonu

BotFather üzerinden bot oluşturduktan sonra:

```text
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
TELEGRAM_CHURN_THRESHOLD=70
```

Administrator hesabıyla **Sistem Entegrasyonları** sayfasına girip gerçek test
mesajı gönderebilirsiniz. Başarı yalnızca Telegram Bot API `ok=true` yanıtı
verdiğinde gösterilir. Başarılı ve başarısız denemeler `integration_events`
tablosunda saklanır.

## Şifre sıfırlama e-postası

Şifre sıfırlama bağlantısı göndermek için SMTP değişkenlerini ayarlayın:

```text
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=...
SMTP_PASSWORD=...
SMTP_FROM=LoyalCart <no-reply@example.com>
SMTP_USE_TLS=1
LOYALCART_APP_URL=https://uygulama-adresiniz.example.com
```

Reset tokenı:

- Veritabanında yalnızca SHA-256 özetiyle tutulur.
- 30 dakika geçerlidir.
- Başarılı parola değişiminden sonra yeniden kullanılamaz.
- Hesap sorgulamasını önlemek için kullanıcıya her durumda aynı genel mesaj gösterilir.

## API kullanımı

`LOYALCART_API_KEY` ayarlanmışsa isteklerde `X-API-Key` başlığı zorunludur.

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -H "X-API-Key: API_ANAHTARINIZ" \
  -d '{
    "Tenure": 4,
    "PreferredLoginDevice": "Mobile Phone",
    "CityTier": 1,
    "WarehouseToHome": 15,
    "PreferredPaymentMode": "Debit Card",
    "Gender": "Female",
    "HourSpendOnApp": 3,
    "NumberOfDeviceRegistered": 3,
    "PreferedOrderCat": "Laptop & Accessory",
    "SatisfactionScore": 2,
    "MaritalStatus": "Single",
    "NumberOfAddress": 2,
    "Complain": 1,
    "OrderAmountHikeFromlastYear": 15,
    "CouponUsed": 1,
    "OrderCount": 2,
    "DaySinceLastOrder": 12,
    "CashbackAmount": 160,
    "CustomerId": "CUSTOMER-1001",
    "CreatedBy": "admin"
  }'
```

## Veritabanı

Varsayılan geliştirme veritabanı SQLite'tır. MySQL için:

```text
DB_ENGINE=mysql
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=loyalcart
MYSQL_PASSWORD=...
MYSQL_DB=loyalcart
```

Kurulum betiği:

```bash
python scripts/create_mysql_db.py
```

Temel tablolar:

- `users`
- `predictions`
- `audit_logs`
- `password_reset_tokens`
- `integration_events`

## Testler

```bash
python -m compileall -q .
python -m unittest discover -s tests -v
```

Test paketi şunları doğrular:

- Parola hashleme ve kullanıcı doğrulama
- Kullanıcı/e-posta çakışma kontrolü
- Tahmin geçmişinin DB yazma/okuma akışı
- API health, API anahtarı ve tahmin kaydı
- Tek kullanımlık şifre reset tokenı
- Telegram başarı ve hata yanıtları
- Login sonrası 10 Streamlit sayfasının smoke testi

GitHub Actions yapılandırması her push ve pull request'te derleme ile testleri
otomatik çalıştırır.

## Sprint belgeleri

- [Sprint 1](Sprint1/)
- [Sprint 2](Sprint2/)
- [Sprint 3](Sprint3/)
- [Sprint 4](Sprint4/)

Sprint 1'de raporlanan model doğruluğu `%97.4` değeridir. Model
değerlendirmesinin yeniden üretilebilmesi için veri bölme yöntemi, sınıf
dengesi ve cross-validation sonuçlarının ayrıca sürümlenmesi önerilir.

## Güvenlik notları

- `.env`, yerel veritabanları ve üretilen log dosyaları Git tarafından izlenmez.
- Secret değerleri kaynak koda yazılmamalıdır.
- Canlı ortamda HTTPS kullanılmalıdır.
- Admin, API, SMTP ve Telegram secretları düzenli olarak döndürülmelidir.
- MySQL kullanıcısına yalnızca LoyalCart veritabanı için gerekli izinler verilmelidir.
