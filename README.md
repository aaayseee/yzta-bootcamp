# 🛒 E-Ticaret Churn (Müşteri Kaybı) Tahmin & Segmentasyon Projesi (LoyalCart)

Bu depo, **YZTA Bootcamp** kapsamında geliştirilen, e-ticaret müşterilerinin şirketi terk etme (churn) olasılığını tahmin eden, 3D interaktif arayüz sunan ve risk seviyesine göre yapay zeka destekli aksiyon önerileri sunan **LoyalCart** projesidir.

## 👥 Takım Üyeleri

- Halil İbrahim ARİ — Product Owner
- Zeynep Yağmur TÜRKELİ — Scrum Master
- Ayşe ULAŞLI — Developer
- Tümer GÜNEŞ — Developer

---

## 🎯 Proje Amacı

- Müşteri churn (kayıp) olasılığını yüksek doğrulukla tahmin etmek
- Müşterileri risk seviyelerine göre segmentlere ayırmak (yüksek / orta / düşük risk)
- 3D Parallax & Holografik cam görünümlü canlı bir Streamlit arayüzünde tüm metrikleri sunmak
- Yapay zeka destekli otomatik aksiyon önerileri ve simülasyonlar ile churn riskini azaltacak stratejiler geliştirmek

---

## 🚀 Özellikler & Yenilikler (Sprint 2)

- **3D Interactive Parallax Viewport:** Farenin hareketine duyarlı 3 boyutlu bükülebilir holografik sayfa plakası.
- **Dynamic 3D Money Rain Canvas:** Ekranın arkasında süzülen 3 boyutlu Matrix para yağmuru animasyonu.
- **Adaptive Dual-Theme Engine:** Kullanıcının Streamlit açık (Light) veya koyu (Dark) tema seçimine göre anlık saydamlaşan cam (glassmorphism) tasarımı.
- **Floating Glass Island Sidebar:** Sol tarafta ekrandan bağımsız süzülen, kayan navigasyon butonlarına sahip modern menü adası.
- **9 Gelişmiş Analitik Sayfa Modülü:**
  1. 📊 Genel Durum (Dashboard)
  2. 🔮 Churn Simülasyonu (What-If ROI Analizi)
  3. 🚨 Erken Uyarı & Otomatik Aksiyon Merkezi
  4. 📈 Kohort Analiz Raporu (Retention Matrisi & LTV/CAC)
  5. 💬 Şikayet & Bilet Yönetimi (SLA Analizi)
  6. ⭐ NPS & Müşteri Bağlılık Ligi
  7. 🔍 Bireysel Müşteri Churn Analiz Paneli
  8. 👥 Müşteri Segmentasyonu & Davranış Analizi
  9. 📋 Geçmiş Tahmin Kayıtları & Denetim Günlüğü

---

## 🏗️ Proje Mimarisi

```
Kaggle Veri Seti (5.630 müşteri, 20 özellik)
       │
       ▼
  Veri Temizliği (eksik değer, kategorik düzeltme)
       │
       ▼
  Keşifsel Veri Analizi (EDA) & Encoding
       │
       ▼
  Random Forest Modeli (%97.4 doğruluk)
       │
       ▼
  ┌─────────────────────────────────────────────────────────┐
  │                 FastAPI Backend Server                  │
  │                   (main.py / :8000)                     │
  └────────────────────────────┬────────────────────────────┘
                               │
                               ▼
  ┌─────────────────────────────────────────────────────────┐
  │             LoyalCart Streamlit Frontend                │
  │                  (arayuz.py / :8501)                    │
  ├────────────────────────────┬────────────────────────────┤
  │ 3D Parallax & Money Rain   │ Dynamic Light/Dark Glass   │
  │ Floating Island Sidebar    │ 9 Modular Page Renderers   │
  └────────────────────────────┴────────────────────────────┘
```

---

## 📂 Modüler Proje Yapısı

```
.
├── main.py                     # FastAPI backend sunucusu
├── arayuz.py                   # Streamlit ana giriş ve yönlendirici (~80 satır)
├── styles.py                   # CSS stilleri ve 3D JS animasyon kodları
├── data_loader.py              # Sentetik veri üretici, cache ve tahmin geçmişi yönetimi
├── components/                 # Yeniden kullanılabilir UI bileşenleri
│   ├── plotly_theme.py         # Plotly grafik şablonu
│   └── sidebar.py              # Yüzen Cam Ada menü bileşeni
├── pages_views/                # Bağımsız 9 analitik sayfa modülü
│   ├── dashboard.py
│   ├── customer_analysis.py
│   ├── segmentation.py
│   ├── history.py
│   ├── simulation.py
│   ├── early_warning.py
│   ├── cohort.py
│   ├── complaints.py
│   └── nps_league.py
├── Sprint1/
│   ├── sprint1_review.md
│   └── sprint1_retrospective.md
├── Sprint2/
│   ├── product_backlog.md
│   └── daily_scrum.md
├── YZTA_Churn_Tahmin_Modeli.ipynb
├── requirements.txt
└── README.md
```

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji / Araç | Projedeki Rolü |
|---|---|
| Python 3.12 | Veri işleme, backend ve arayüz geliştirme |
| FastAPI / Uvicorn | RESTful API tahmin sunucusu |
| Scikit-learn / Joblib | Random Forest churn tahmin modeli |
| Streamlit | 3D Etkileşimli kullanıcı portalı |
| HTML5 / CSS3 / Vanilla JS | 3D Parallax Viewport, Matrix para yağmuru tuvali ve Glassmorphism |
| Plotly Express | Şeffaf ve etkileşimli veri görselleştirme |
| Pandas / NumPy | Veri manipülasyonu ve sentetik veri motoru |
| Git & GitHub | Sürüm kontrolü ve modüler proje paylaşımı |

---

## 📅 SPRINT 1 ÇIKTILARI

* Veri seti Kaggle'dan çekildi (5.630 müşteri, 20 özellik)
* Eksik değerler medyan ile dolduruldu, kategorik düzeltmeler yapıldı
* Keşifsel Veri Analizi (EDA) tamamlandı
* Encoding işlemi tamamlandı
* Random Forest modeli kuruldu — **%97.4 doğruluk**
* GitHub reposu ve Scrum tahtası oluşturuldu

# Backlog Düzeni ve Sprint Board
!(617209818-ae075312-b8a1-4720-a4ad-0f3b6119b748.png)

# Daily Scrum
![alt text](617210017-16245dc4-d272-4d5e-b0a4-e2414d94176d.jpg)

# Ürün Durumu (Product Increment)
![alt text](617210096-a6e925a6-2415-4b17-8bb0-e3694113b591.png)

# 🔎 Sprint 1 Review
**Tamamlananlar:** Veri setinin entegrasyonu, GitHub repo ve Scrum tahtasının kurulumu, EDA aşaması ve Random Forest modelinin eğitilmesi.

**Mevcut Durum:** Sprint 1 için planlanan tüm hedeflere beklenenden kısa sürede ulaşıldı. Modelin %97.4 doğruluk göstermesi, projenin temelinin sağlam atıldığını gösteriyor. (Not: Yüksek doğruluk oranı overfitting ihtimaline karşı Sprint 2'de cross-validation ile doğrulanacak.)

# 🔁 Sprint 1 Retrospective
**Ne İyi Gitti:** Disiplinli ve planlı ilerleme zaman yönetimini kolaylaştırdı. Colab–GitHub entegrasyonu sorunsuz çalıştı.

**Neler Zorladı:** GitHub reposunu ayağa kaldırırken küçük bir yetkilendirme adımı zaman aldı, hızlıca çözüldü.

**Sprint 2 Aksiyon Planı:** Model backend'i sağlam olduğuna göre; müşteri segmentasyonu, Streamlit arayüzü ve YZ aksiyon önerisi geliştirmelerine odaklanılacak.

# 📌 Sprint 2 Hedefleri
| User Story | Durum |
| :--- | :--- |
| US-04 Müşteri Segmentasyonu | 🔲 To Do |
| US-05 Streamlit Arayüzü | 🔲 To Do |
| US-06 YZ Aksiyon Öneri Asistanı | 🔲 To Do |

# 📈 Proje Durumu
🟡 Geliştirme Aşamasında — Sprint 1 başarıyla tamamlandı, Sprint 2'de segmentasyon ve arayüz çalışmaları sürüyordu.

*Bu proje, Scrum metodolojisi kullanılarak ekip çalışması kapsamında geliştirilmektedir.*

## 📅 SPRINT 2 SCRUM & TESLİMAT DOSYASI

> ℹ️ **Not:** Makine öğrenmesi churn tahmin modeli (Random Forest) Sprint 1 aşamasında tamamlanmış olup, **Sprint 2'deki tüm geliştirmeler VS Code ortamında** sistem mimarisi, FastAPI backend entegrasyonu, 3D arayüz (UI/UX) ve modüler kod refactoring üzerine gerçekleştirilmiştir.

### 💬 1. Daily Scrum Notları

####  3D Görsellik & Parallaks Arayüzü
> **- Neler yaptık?:** KPI kartlarının sayfa yenilemede oturumu kapatma hatasını çözdük.
> **- Neler yapacağız?:** Dashboard'a farenin hareketine duyarlı 3D Parallax tilt efekti ve arka planda süzülen 3D Matrix para yağmuru animasyonunu entegre edeceğiz.
> **- Engel/Blocker Var mı?:** Yok.

####  Açık Mod (Light Mode) Uyum ve Gelişmiş Modüller
> **- Neler yaptık?:** 3D bükülme efektini ve 5 yeni gelişmiş analitik modülü (What-If Simülasyonu, Erken Uyarı Merkezi, Kohort Raporu, Şikayet Yönetimi, NPS Ligi) tamamladık.
> **- Neler yapacağız?:** Streamlit açık tema (Light Mode) seçildiğinde oluşan okunamayan metin hatalarını giderip çift-tema uyumlu cam (glassmorphism) tasarımını yayına alacağız.
> **- Engel/Blocker Var mı?:** Yok, arayüz testleri devam ediyor.

####  Yüzen Cam Ada Menü & Kod Temizliği (Refactoring)
> **- Neler yaptık?:** Açık ve koyu temayı dinamik algılayan JS tuval döngüsünü ekledim. Sol navigasyon panelini ekrandan bağımsız yüzen bir cam kapsüle (Floating Glass Island) dönüştürdüm.
> **- Neler yapacağız?:** 1.500 satırlık arayüz kodunu temizleyip modüler Python dosyalarına (`styles.py`, `data_loader.py`, `components/`, `pages_views/`) ayıracağım ve projeyi GitHub'a push edeceğim.
> **- Engel/Blocker Var mı?:** Yok, Sprint 2 hedefleri tamamlanıyor.

![alt text](5974166515533680199.jpg)
![alt text](5974166515533680200.jpg)
---

### 🎯 2. Backlog Dağıtma Mantığı (Sprint 2 Backlog Rasyoneli)

* **Sprint 2 Amacı (Sprint Goal):** LoyalCart platformunu statik bir panelden, fare hareketleriyle etkileşime giren 3D bükülmeli, çift-tema uyumlu, modüler kod yapısına sahip ve 9 farklı analitik modülü barındıran kurumsal bir yönetici portalına dönüştürmek.
* **Görev Dağılımı ve Önceliklendirme Mantığı:**
  1. **Yüksek Öncelik (P0 - Visual & UX Overhaul):** 3D Parallax Viewport, Matrix para yağmuru ve yüzen cam ada menüsü.
  2. **Yüksek Öncelik (P0 - Dark/Light Theme Engine):** Kullanıcının tema tercihine göre arka plan tuvalinin ve metin renklerinin anlık değişmesi.
  3. **Orta Öncelik (P1 - Advanced Business Analytics):** What-If ROI Simülatörü, Erken Uyarı Otomasyonu, Kohort Retention Matrisi.
  4. **Teknik Öncelik (P1 - Code Architecture):** Monolitik `arayuz.py` dosyasını modüler paket yapısına kavuşturma.

---

### 📋 3. Sprint Board / Breadboard Updates (VS Code Görev Durumu)

| Task ID | Görev Adı | İlgili Kişi | Durum (Status) |
| :--- | :--- | :--- | :--- |
| **TSK-11** | 3D Viewport Parallax Tilt & Fare Takip Algoritması | Front-end / AI | **DONE ✅** |
| **TSK-12** | Matrix Para Yağmuru 3D Tuval Animasyonu | Front-end | **DONE ✅** |
| **TSK-13** | Açık/Koyu Tema Dinamik Algılayıcı (Light Mode CSS Fix) | Front-end | **DONE ✅** |
| **TSK-14** | Yüzen Cam Ada (Floating Glass Island) Sol Menü | UI/UX | **DONE ✅** |
| **TSK-15** | What-If Churn Simülasyonu & ROI Hesaplayıcı | Full-stack | **DONE ✅** |
| **TSK-16** | Erken Uyarı & Otomatik Kupon Aksiyon Merkezi | Backend | **DONE ✅** |
| **TSK-17** | Kod Tabanı Temizliği & Modüler Python Mimarisi | Architecture | **DONE ✅** |
| **TSK-18** | GitHub Repository Entegrasyonu ve Push | DevOps | **DONE ✅** |

# Backlog Düzeni ve Sprint Board
![alt text](<Ekran görüntüsü 2026-07-19 213644.png>)
![alt text](<Ekran görüntüsü 2026-07-19 213737.png>)
![alt text](<Ekran görüntüsü 2026-07-19 213824.png>)
---

### 📦 4. Ürün Durumu (Product Increment Status)

Sprint 2 sonunda teslim edilen **LoyalCart v2.5 Executive Pro** güncel sürüm özellikleri:
* **Canlı Backend:** FastAPI Makine Öğrenmesi Tahmin Sunucusu (`http://127.0.0.1:8000`)
* **Canlı Portalı:** Streamlit 3D Holografik Panel (`http://localhost:8501`)
* **Modüler Dosya Yapısı:** `styles.py`, `data_loader.py`, `components/`, `pages_views/` klasör ayrımıyla %100 temiz Python mimarisi.
* **Gelişmiş 9 Analitik Modül:** Dashboard, What-If Simülasyonu, Erken Uyarı, Kohort Matrisi, Şikayet SLA, NPS Ligi, Bireysel Analiz, Segmentasyon ve Geçmiş Kayıtlar.

![alt text](<Ekran görüntüsü 2026-07-19 214048.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214147.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214255.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214400.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214529.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214632.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214710.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214811.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214848.png>)
![alt text](<Ekran görüntüsü 2026-07-19 214916.png>)

---

### 🔍 5. Sprint 2 Review (Sprint İnceleme Raporu)

* **Toplantı Katılımcıları:** Scrum Ekibi, Product Owner, Paydaşlar.
* **Sunulan Ürün:** Ekranın 3D olarak büküldüğü, açık/koyu mod seçimine göre arka planın anında değiştiği ve tüm kodların modüler `.py` dosyalarına ayrıldığı canlı portal demosu yapıldı.
* **Geri Bildirimler:** Paydaşlar visual parallax efektinden, açık mod kontrast düzeltmesinden ve kodun okunabilir modüler yapısından tam memnuniyet bildirdi.
* **Kabul Edilen Hikayeler:** Sprint 2 hedefleri arasındaki tüm User Story'ler kabul edildi.

---

### 🔄 6. Sprint 2 Retrospective (Sprint Retrospektifi)

#### 👍 What Went Well? (Ne İyi Gitti?)
* 3D Parallax ve Matrix para yağmuru ile benzersiz bir kullanıcı deneyimi (UX) yakalandı.
* 1.500 satırlık tek dosya yerine modüler Python yapısına geçilerek kod kalitesi yükseltildi.
* Açık/koyu tema hataları tamamen giderildi.

#### 💡 What Can Be Improved? (Ne Geliştirilebilir?)
* Gelecek sprintlerde backend tahmin sürelerini daha da hızlandırmak için asenkron (async) API çağrıları eklenebilir.
* Docker konteynırlaştırma ile canlı sunucuya canlı dağıtım (deployment) yapılabilir.

#### 🎯 Action Items (Aksiyon Maddeleri)
1. Proje reposunu arkadaşların `Collaborator` olarak eklenmesiyle ortak geliştirmeye açık tutmak.
2. Sprint 3 için gerçek müşteri veri seti entegrasyonu hazırlıklarına başlamak.

---

## 📌 Sprint User Story Durumu

| User Story | Durum |
|---|---|
| US-01 Veri Temizliği & EDA | ✅ SPRINT 1 DONE |
| US-02 Random Forest Modeli (%97.4) | ✅ SPRINT 1 DONE |
| US-04 Müşteri Segmentasyonu & Gelişmiş Modüller | ✅ SPRINT 2 DONE |
| US-05 Streamlit 3D & Çift-Tema Arayüzü | ✅ SPRINT 2 DONE |
| US-06 YZ Aksiyon Öneri & What-If Simülatörü | ✅ SPRINT 2 DONE |

---

## 📈 Proje Durumu

🟢 **Sprint 2 Başarıyla Tamamlandı** — LoyalCart v2.5 Executive Pro sürümü yayında ve tüm modülleriyle GitHub reposunda günceldir.

---

> Bu proje, Scrum metodolojisi kullanılarak YZTA Bootcamp ekibi tarafından geliştirilmektedir.
