# Sprint 1 Product Backlog
Tarih: 19 Haziran – 5 Temmuz 2026
Ekip: Ekip-116 | Churn Prediction & Müşteri Segmentasyon

---

## Backlog Durumu

| User Story | Açıklama | Durum |
|---|---|---|
| US-01 | Veri Seti Hazırlama | ✅ Done |
| US-02 | Keşifsel Veri Analizi (EDA) | ✅ Done |
| US-03 | Churn Tahmin Modeli | ✅ Done |
| US-04 | Müşteri Segmentasyonu | 🔲 Sprint 2'ye Taşındı |
| US-05 | Streamlit Arayüzü | 🔲 Sprint 2'ye Taşındı |
| US-06 | YZ Aksiyon Öneri Asistanı | 🔲 Sprint 2'ye Taşındı |

---

## Tamamlanan Görevler

**US-01 ✅ Veri Seti Hazırlama**
- Kaggle'dan e-ticaret churn veri seti seçildi
- 5.630 müşteri, 20 özellik
- Google Drive ortak klasörüne aktarıldı
- Eksik değerler medyanla dolduruldu
- Kategorik tutarsızlıklar düzeltildi

**US-02 ✅ Keşifsel Veri Analizi (EDA)**
- Churn dağılımı görselleştirildi (4.682 kalan, 948 terk eden)
- Giriş cihazı ve sipariş kategorisine göre churn analizi yapıldı
- Kritik bulgu: Mobile Phone kategorisinde churn oranı belirgin şekilde yüksek
- One-Hot Encoding tamamlandı

**US-03 ✅ Churn Tahmin Modeli**
- Random Forest algoritması kullanıldı
- Train/Test ayrımı yapıldı (%80/%20)
- Doğruluk oranı: %97.4
- Precision: %98, Recall: %86

---

## Sprint 2'ye Taşınan Görevler

- US-04: Müşteri Segmentasyonu (Düşük/Orta/Yüksek risk)
- US-05: Streamlit Arayüzü
- US-06: YZ Aksiyon Öneri Asistanı
