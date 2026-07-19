# Sprint 2 Review
Tarih: 19 Temmuz 2026
Ekip: Ekip-116 | Churn Prediction & Müşteri Segmentasyon

---

## Tamamlanan Görevler

**US-03 ✅ Churn Tahmin Modeli**
- Random Forest modeli tamamlandı
- Doğruluk oranı: %97.4
- Model `churn_modeli.pkl` olarak kaydedildi
- Cross-validation kontrolü yapıldı

**US-04 ✅ Müşteri Segmentasyonu**
- Müşteriler 3 risk grubuna ayrıldı: Düşük / Orta / Yüksek
- Segment profilleri çıkarıldı
- Segmentasyon sonuçları arayüze entegre edildi
- `sentez_veri.csv` ile test edildi

**US-05 ✅ Streamlit Arayüzü**
- `arayuz.py` tamamlandı
- Kullanıcı veri yükleyebiliyor
- Churn tahmini ve segment bilgisi ekranda gösteriliyor
- Geçmiş tahminler özelliği eklendi
- Modüler yapı kuruldu (`components/`, `pages_views/`)
- `requirements.txt` hazırlandı

---

## Sprint 3'e Taşınan Görevler
- US-06: YZ Aksiyon Öneri Asistanı (LLM entegrasyonu)
- Ürünü canlıya alma

---

## Genel Değerlendirme
Sprint 2 teknik açıdan hedeflerin ötesinde ilerledi. Model, arayüz ve segmentasyon tamamlandı. Sprint 3'te YZ entegrasyonu ve canlıya alma odak noktası olacak.
