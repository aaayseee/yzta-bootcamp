# 🛒 E-Ticaret Churn (Müşteri Kaybı) Tahmin Projesi

Bu depo, **YZTA Bootcamp** kapsamında geliştirilen, e-ticaret müşterilerinin şirketi terk etme (churn) olasılığını tahmin eden ve risk seviyesine göre aksiyon önerileri sunan bir yapay zeka projesidir.

## 👥 Takım Üyeleri

- Halil İbrahim ARİ — Product Owner
- Zeynep Yağmur TÜRKELİ — Scrum Master
- Ayşe ULAŞLI — Developer
- Tümer GÜNEŞ — Developer

---

## 🎯 Proje Amacı

- Müşteri churn (kayıp) olasılığını yüksek doğrulukla tahmin etmek
- Müşterileri risk seviyelerine göre segmentlere ayırmak (yüksek / orta / düşük risk)
- Sonuçları kolay kullanılabilir bir arayüzde (Streamlit) sunmak
- Yapay zeka destekli aksiyon önerileri ile churn riskini azaltacak stratejiler önermek

---

## 🚀 Özellikler

- Kaggle üzerinden alınan gerçek e-ticaret müşteri verisi
- Eksik veri temizliği ve kategorik düzeltmeler
- Keşifsel Veri Analizi (EDA)
- Random Forest ile churn tahmin modeli (%97.4 doğruluk)
- Müşteri segmentasyonu (Sprint 2)
- Streamlit tabanlı kullanıcı arayüzü (Sprint 2)
- LLM destekli aksiyon önerisi asistanı (Sprint 2)

## 🏗️ Proje Mimarisi

​```
Kaggle Veri Seti (5.630 müşteri, 20 özellik)
       │
       ▼
  Veri Temizliği (eksik değer, kategorik düzeltme)
       │
       ▼
  Keşifsel Veri Analizi (EDA)
       │
       ▼
     Encoding
       │
       ▼
 Random Forest Modeli (%97.4 doğruluk)
       │
       ▼
 ┌─────────────────────┬────────────────────┐
 │ Müşteri Segmentasyonu │ Streamlit Arayüzü │
 └─────────────────────┴────────────────────┘
       │
       ▼
  YZ Destekli Aksiyon Önerisi (LLM)
​```

## 📂 Proje Yapısı

​```
.
├── Sprint1/
│   ├── sprint1_review.md
│   └── sprint1_retrospective.md
├── Sprint2/
│   ├── product_backlog.md
│   └── daily_scrum.md
├── YZTA_Churn_Tahmin_Modeli.ipynb
└── README.md
​```

## 🛠️ Kullanılan Teknolojiler

| Teknoloji / Araç | Projedeki Rolü |
|---|---|
| Python | Veri işleme ve model geliştirme |
| Pandas / NumPy | Veri temizliği ve manipülasyonu |
| Scikit-learn | Random Forest modeli ve değerlendirme |
| Matplotlib / Seaborn | EDA görselleştirmeleri |
| Streamlit | Kullanıcı arayüzü (Sprint 2) |
| LLM (aksiyon önerisi) | Müşteriye özel öneri üretimi (Sprint 2) |
| Git & GitHub | Sürüm kontrolü ve ekip iş birliği |

---

## 📅 Sprint 1 Çıktıları

* Veri seti Kaggle'dan çekildi (5.630 müşteri, 20 özellik)
* Eksik değerler medyan ile dolduruldu, kategorik düzeltmeler yapıldı
* Keşifsel Veri Analizi (EDA) tamamlandı
* Encoding işlemi tamamlandı
* Random Forest modeli kuruldu — **%97.4 doğruluk**
* GitHub reposu ve Scrum tahtası oluşturuldu

### Backlog Düzeni ve Sprint Board
<img width="1915" height="827" alt="image" src="https://github.com/user-attachments/assets/ae075312-b8a1-4720-a4ad-0f3b6119b748" />

### Daily Scrum
<img width="825" height="1184" alt="photo_5931537556371608684_y" src="https://github.com/user-attachments/assets/16245dc4-d272-4d5e-b0a4-e2414d94176d" />

### Ürün Durumu (Product Increment)
<img width="1916" height="940" alt="image" src="https://github.com/user-attachments/assets/a6e925a6-2415-4b17-8bb0-e3694113b591" />

---

## 🔎 Sprint 1 Review

**Tamamlananlar:** Veri setinin entegrasyonu, GitHub repo ve Scrum tahtasının kurulumu, EDA aşaması ve Random Forest modelinin eğitilmesi.

**Mevcut Durum:** Sprint 1 için planlanan tüm hedeflere beklenenden kısa sürede ulaşıldı. Modelin %97.4 doğruluk göstermesi, projenin temelinin sağlam atıldığını gösteriyor. (Not: Yüksek doğruluk oranı overfitting ihtimaline karşı Sprint 2'de cross-validation ile doğrulanacak.)

---

## 🔁 Sprint 1 Retrospective

**Ne İyi Gitti:** Disiplinli ve planlı ilerleme zaman yönetimini kolaylaştırdı. Colab–GitHub entegrasyonu sorunsuz çalıştı.

**Neler Zorladı:** GitHub reposunu ayağa kaldırırken küçük bir yetkilendirme adımı zaman aldı, hızlıca çözüldü.

**Sprint 2 Aksiyon Planı:** Model backend'i sağlam olduğuna göre; müşteri segmentasyonu, Streamlit arayüzü ve YZ aksiyon önerisi geliştirmelerine odaklanılacak.

---

## 📌 Sprint 2 Hedefleri

| User Story | Durum |
|---|---|
| US-04 Müşteri Segmentasyonu | 🔲 To Do |
| US-05 Streamlit Arayüzü | 🔲 To Do |
| US-06 YZ Aksiyon Öneri Asistanı | 🔲 To Do |

---

## 📈 Proje Durumu

🟡 **Geliştirme Aşamasında** — Sprint 1 başarıyla tamamlandı, Sprint 2'de segmentasyon ve arayüz çalışmaları sürüyor.

---

> Bu proje, Scrum metodolojisi kullanılarak ekip çalışması kapsamında geliştirilmektedir.


