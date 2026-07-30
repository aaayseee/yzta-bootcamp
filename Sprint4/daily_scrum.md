# Daily Scrum — Sprint 4

Tarih: 29–30 Temmuz 2026  
Ekip: Ekip-116 — Churn Prediction & Müşteri Segmentasyon

---

## Gün 1 — 29 Temmuz 2026

**Ne yapıldı:**

- Sprint 3 commitleri ve mevcut proje yapısı ayrıntılı olarak incelendi.
- SQLite/MySQL ortak repository ve tahmin geçmişi altyapısı tamamlandı.
- PBKDF2 parola hashleme, rol kontrolü ve güvenli admin oluşturma akışı eklendi.
- FastAPI ve Streamlit ortak tahmin servisine bağlandı.
- Süreli şifre sıfırlama tokenı ve SMTP e-posta servisi geliştirildi.
- Gerçek Telegram Bot API bağlantısı ve entegrasyon logları eklendi.
- Docker, GitHub Actions, ortam örneği ve README güncellendi.
- Repository, güvenlik, API, Telegram, e-posta ve Streamlit testleri oluşturuldu.

**Karşılaşılan engeller:**

- GitHub CI'da API testi, temiz ortamda `httpx` bulunmadığı için hata verdi.
- Streamlit smoke testi PyArrow sürüm uyumsuzluğu nedeniyle native olarak çöktü.

**Çözüm:**

- CI adımları ayrıştırılarak hata veren modüller tespit edildi.
- `httpx==0.28.1` ve `pyarrow==20.0.0` bağımlılıkları açıkça sabitlendi.
- Tanılama ayarları kaldırılarak katı CI yeniden etkinleştirildi.

---

## Gün 2 — 30 Temmuz 2026

**Ne yapıldı:**

- Login ekranındaki responsive yerleşim ve kaydırma sorunları giderildi.
- Kullanıcı adı ve şifre alanlarına kararlı anahtarlar eklendi.
- Boş alanlarla giriş için anlaşılır doğrulama mesajı eklendi.
- Login testi genişletildi ve tüm test paketi yeniden çalıştırıldı.
- Sprint 4 review, retrospective ve daily scrum belgeleri tamamlandı.

**Doğrulama:**

- 12 otomatik test başarıyla geçti.
- GitHub Actions derleme ve bütün test aşamalarını başarıyla tamamladı.
- `main` dalı ile GitHub deposu senkronize edildi.

**Engel:** Yok

---

## Sprint kapanışı

Sprint 4 backlog maddelerinin tamamı kabul kriterlerini karşıladı. Proje
güvenlik, veritabanı, entegrasyon, test, CI ve dokümantasyon açısından teslim
edilebilir duruma getirildi.
