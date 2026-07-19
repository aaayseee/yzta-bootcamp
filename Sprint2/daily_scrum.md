# Daily Scrum - Sprint 2
Tarih: 6 Temmuz – 19 Temmuz 2026
Ekip: Ekip-116 | Churn Prediction & Müşteri Segmentasyon

---

## Gün 1 – 6 Temmuz 2026

**Ne yapıldı:**
- Sprint 2 product backlog oluşturuldu
- GitHub reposu düzenlendi, klasör yapısı netleştirildi
- Cross-validation kontrolü planlandı

**Ne yapılacak:**
- Churn tahmin modelinde cross-validation kontrolü yapılacak
- Overfitting riski değerlendirilecek

**Engel:** Yok

---

## Gün 2 – 7 Temmuz 2026

**Ne yapıldı:**
- Random Forest modelinde cross-validation kontrolü yapıldı
- Model `.pkl` formatında kaydedildi (`churn_modeli.pkl`)
- `data_loader.py` dosyası oluşturuldu (veri yükleme fonksiyonları)

**Ne yapılacak:**
- Streamlit arayüzü geliştirilmeye başlanacak
- Müşteri segmentasyonu planlanacak

**Engel:** Yok

---

## Gün 3 – 8 Temmuz 2026

**Ne yapıldı:**
- Streamlit arayüzü (`arayuz.py`) geliştirilmeye başlandı
- `styles.py` dosyası oluşturuldu (arayüz stil tanımlamaları)
- `requirements.txt` hazırlandı (canlıya alma için gerekli kütüphaneler)

**Ne yapılacak:**
- Arayüzde tahmin ekranı tamamlanacak
- Müşteri segmentasyonu eklenecek

**Engel:** Yok

---

## Gün 4 – 9 Temmuz 2026

**Ne yapıldı:**
- Streamlit arayüzü büyük ölçüde tamamlandı
- Kullanıcı veri yükleme ve tahmin görüntüleme ekranı eklendi
- `main.py` oluşturuldu (uygulamanın ana çalıştırma dosyası)

**Ne yapılacak:**
- Müşteri segmentasyonu (Düşük/Orta/Yüksek risk) eklenecek
- Geçmiş tahminler özelliği planlanacak

**Engel:** Yok

---

## Gün 5 – 10 Temmuz 2026

**Ne yapıldı:**
- Müşteri segmentasyonu tamamlandı (Düşük/Orta/Yüksek risk grupları)
- Segmentasyon sonuçları arayüze entegre edildi
- `sentez_veri.csv` oluşturuldu (test ve demo için sentetik veri)

**Ne yapılacak:**
- Geçmiş tahminler özelliği geliştirilecek
- Arayüz testleri yapılacak

**Engel:** Yok

---

## Gün 6 – 11 Temmuz 2026

**Ne yapıldı:**
- `gecmis_tahminler.csv` ve `gecmis_tahminler_yeni.csv` oluşturuldu
- Geçmiş tahminleri görüntüleme özelliği arayüze eklendi
- Bileşen yapısı (`components/`) oluşturuldu, kod modüler hale getirildi

**Ne yapılacak:**
- Sayfa görünümleri (`pages_views/`) düzenlenecek
- Son testler yapılacak

**Engel:** Yok

---

## Gün 7 – 14 Temmuz 2026

**Ne yapıldı:**
- `pages_views/` klasörü oluşturuldu, sayfa görünümleri ayrıştırıldı
- Arayüzün tüm ekranları test edildi
- `.gitignore` dosyası eklendi

**Ne yapılacak:**
- YZ aksiyon öneri asistanı planlanacak
- Canlıya alma hazırlıkları başlayacak

**Engel:** Yok

---

## Gün 8 – 15 Temmuz 2026

**Ne yapıldı:**
- Uygulama son testlerden geçirildi
- Kod temizliği yapıldı
- Sprint 2 değerlendirmesi için hazırlıklar başladı

**Ne yapılacak:**
- Sprint 2 Review ve Retrospective hazırlanacak
- Sprint 3 planlaması yapılacak

**Engel:** Yok

---

## Gün 9 – 19 Temmuz 2026 (Sprint 2 Son Gün)

**Ne yapıldı:**
- Sprint 2 tüm teknik görevler tamamlandı
- Churn tahmin modeli: ✅ (%97.4 doğruluk)
- Müşteri segmentasyonu: ✅
- Streamlit arayüzü: ✅
- Geçmiş tahminler özelliği: ✅
- Modüler kod yapısı: ✅

**Ne yapılacak:**
- Sprint 3'te YZ aksiyon öneri asistanı eklenecek
- Canlıya alma tamamlanacak
- Final sunumu hazırlanacak

**Engel:** Yok
