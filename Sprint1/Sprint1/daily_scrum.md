# Daily Scrum - Sprint 1
Tarih: 19 Haziran – 5 Temmuz 2026
Ekip: Ekip-116 | Churn Prediction & Müşteri Segmentasyon

---

## Gün 1 – 19 Haziran 2026

**Ne yapıldı:**
- Ekip rolleri belirlendi (Product Owner, Scrum Master, Developer x3)
- Ekip iletişim kanalı kuruldu (WhatsApp grubu)
- Proje konusu tartışmaya açıldı

**Ne yapılacak:**
- Proje fikri araştırılacak, kararlaştırılacak
- Veri seti araştırması yapılacak

**Engel:** Yok

---

## Gün 2 – 20 Haziran 2026

**Ne yapıldı:**
- Farklı proje fikirleri değerlendirildi
- Churn Prediction & Müşteri Segmentasyon projesi önerildi

**Ne yapılacak:**
- Proje fikri netleştirilecek
- Veri seti araştırması devam edecek

**Engel:** Yok

---

## Gün 3 – 21 Haziran 2026

**Ne yapıldı:**
- Proje konusu kesinleşti: Churn Prediction & Müşteri Segmentasyon
- Proje fikri bootcamp formuna iletildi
- Kaggle'da uygun veri seti araştırması yapıldı

**Ne yapılacak:**
- E-ticaret churn veri seti incelenecek
- GitHub reposu oluşturulacak

**Engel:** Yok

---

## Gün 4 – 24 Haziran 2026

**Ne yapıldı:**
- GitHub reposu oluşturuldu
- Kaggle'dan E-ticaret Churn veri seti seçildi
- Veri seti Google Drive ortak klasörüne aktarıldı

**Ne yapılacak:**
- Veri temizliği yapılacak
- Eksik değerler incelenecek

**Engel:** Yok

---

## Gün 5 – 25 Haziran 2026

**Ne yapıldı:**
- Veri seti incelendi (5.630 müşteri, 20 özellik)
- Eksik değerler tespit edildi (Tenure: 264, DaySinceLastOrder: 307 vb.)
- Kategorik sütunlardaki tutarsızlıklar belirlendi

**Ne yapılacak:**
- Eksik değerler doldurulacak
- Kategorik düzeltmeler yapılacak

**Engel:** Yok

---

## Gün 6 – 26 Haziran 2026

**Ne yapıldı:**
- Eksik değerler medyan ile dolduruldu
- Kategorik tutarsızlıklar düzeltildi (Phone → Mobile Phone, CC → Credit Card vb.)
- Veri temizliği tamamlandı

**Ne yapılacak:**
- EDA grafikleri oluşturulacak
- Churn dağılımı görselleştirilecek

**Engel:** Yok

---

## Gün 7 – 28 Haziran 2026

**Ne yapıldı:**
- EDA grafikleri oluşturuldu
- Churn dağılımı görselleştirildi: 4.682 kalan, 948 terk eden müşteri
- Kritik bulgu: Mobile Phone kategorisinde churn oranı diğer kategorilere göre belirgin şekilde yüksek

**Ne yapılacak:**
- One-Hot Encoding yapılacak
- Model eğitimine hazırlanılacak

**Engel:** Yok

---

## Gün 8 – 30 Haziran 2026

**Ne yapıldı:**
- One-Hot Encoding tamamlandı
- Veri modele hazır hale getirildi
- Train/Test ayrımı yapıldı (%80/%20)

**Ne yapılacak:**
- Random Forest modeli kurulacak ve eğitilecek

**Engel:** Yok

---

## Gün 9 – 5 Temmuz 2026 (Sprint 1 Son Gün)

**Ne yapıldı:**
- Random Forest modeli kuruldu ve eğitildi
- Model doğruluk oranı: %97.4
- Precision: %98, Recall: %86
- Sprint 1 Review ve Retrospective hazırlandı

**Ne yapılacak:**
- Sprint 2'de müşteri segmentasyonu yapılacak
- Streamlit arayüzü geliştirilecek
- YZ aksiyon öneri asistanı eklenecek

**Engel:** Yok
