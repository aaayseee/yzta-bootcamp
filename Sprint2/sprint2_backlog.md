## Sprint 2 — Güncellenmiş Product Backlog
Tarih: 6 Temmuz – 19 Temmuz 2026

### Sprint 2 Başlangıç Durumu

| User Story | Açıklama | Durum |
|---|---|---|
| US-01 | Veri Seti Hazırlama | ✅ Done |
| US-02 | Keşifsel Veri Analizi (EDA) | ✅ Done |
| US-03 | Churn Tahmin Modeli (Random Forest) | ✅ Done |
| US-04 | Müşteri Segmentasyonu | 🔄 In Progress |
| US-05 | Streamlit Arayüzü | 🔲 To Do |
| US-06 | YZ Aksiyon Öneri Asistanı | 🔲 To Do |

### Sprint 2 Tamamlanan Görevler (Güncelleme)

**US-01 ✅ Veri Seti Hazırlama**
- Kaggle'dan e-ticaret churn veri seti seçildi
- 5.630 müşteri, 20 özellik içeren veri Google Drive'a aktarıldı

**US-02 ✅ Keşifsel Veri Analizi (EDA)**
- Eksik değerler medyanla dolduruldu
- Kategorik tutarsızlıklar düzeltildi (Phone → Mobile Phone gibi)
- Churn dağılımı görselleştirildi: 4.682 kalan, 948 terk eden müşteri
- Kritik bulgu: Mobile Phone kategorisinde churn oranı diğer kategorilere göre belirgin şekilde yüksek

**US-03 ✅ Churn Tahmin Modeli**
- Random Forest algoritması kullanıldı
- Doğruluk oranı: %97.4
- Precision: %98, Recall: %86
- Encoding (One-Hot) tamamlandı

### Sprint 2 Kalan Görevler

**US-04 🔄 Müşteri Segmentasyonu**
Kabul Kriterleri:
- [ ] Müşteriler risk seviyesine göre 3 gruba ayrılmalı (Düşük/Orta/Yüksek risk)
- [ ] Her segment için müşteri profili çıkarılmalı
- [ ] Segment dağılımı görselleştirilmeli

**US-05 🔲 Streamlit Arayüzü**
Kabul Kriterleri:
- [ ] Kullanıcı veri yükleyebilmeli
- [ ] Churn tahmini ekranda gösterilmeli
- [ ] Segment bilgisi listelenmeli
- [ ] Uygulama canlıya alınabilir olmalı

**US-06 🔲 YZ Aksiyon Öneri Asistanı**
Kabul Kriterleri:
- [ ] Her müşteri segmenti için LLM otomatik öneri üretmeli
- [ ] Örnek: "Yüksek riskli müşterilere özel indirim kampanyası başlatın"
- [ ] Öneriler mantıklı ve uygulanabilir olmalı
