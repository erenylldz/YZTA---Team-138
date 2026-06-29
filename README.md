# AI Destekli Fikir Doğrulama Asistanı

## Takım İsmi

Belirlenecek.

---

## Takım Üyeleri ve Rolleri

| İsim             | Rol           |
| ---------------- | ------------- |
| Eren Yıldız      | Scrum Master  |
| Sema Yeşilkaya   | Product Owner |
| Semiha Çıtırkı   | Developer     |
| Mücahit Ayyıldız | Developer     |
| Berker Öner      | Developer     |

---

## Ürün İsmi

AI Destekli Fikir Doğrulama Asistanı

---

## Ürün Açıklaması

Bu proje, girişimci adaylarının iş fikirlerini doğrulamasına yardımcı olan AI destekli bir fikir doğrulama panelidir.

Kullanıcı iş fikrini sisteme girer. Sistem bu fikri analiz eder, en riskli varsayımları belirler, müşteri görüşmeleri için doğru sorular üretir, MVP kapsamını daraltır ve kullanıcıya adım adım doğrulama yol haritası sunar.

Bu ürünün amacı, girişimci adaylarının fikirlerini doğrudan ürüne dönüştürmeden önce daha sistemli, ölçülebilir ve kanıta dayalı şekilde doğrulamalarına yardımcı olmaktır.

---

## Ürün Vizyonu

Belirlenecek.

---

## Problem

Girişimci adayları çoğu zaman iş fikirlerini yeterince doğrulamadan ürün geliştirme sürecine başlar. Bu durum zaman, emek ve kaynak kaybına yol açabilir.

Bu projede hedeflenen problem; kullanıcıların iş fikirlerindeki en riskli varsayımları fark edememesi, doğru müşteri görüşme sorularını hazırlayamaması ve MVP kapsamını gereğinden fazla geniş tutmasıdır.

---

## Çözüm

AI destekli fikir doğrulama asistanı, kullanıcının iş fikrini analiz ederek fikir doğrulama sürecini adım adım yönlendiren bir panel sunar.

Sistem; riskli varsayımları çıkarır, müşteri görüşmesi için uygun sorular üretir, MVP kapsamını daraltmaya yardımcı olur ve kullanıcıya uygulanabilir bir doğrulama yol haritası oluşturur.

---

## Hedef Kitle

* Erken aşama girişimci adayları
* Üniversite öğrencileri
* Bootcamp ve hackathon katılımcıları
* İş fikrini doğrulamak isteyen ekipler
* MVP geliştirmeden önce fikrini test etmek isteyen kullanıcılar

---

## Ürün Özellikleri

* Fikir analizi
* Riskli varsayım analizi
* Mom Test prensiplerine uygun müşteri görüşme soruları
* MoSCoW yöntemi ile MVP kapsam daraltma
* Doğrulama yol haritası oluşturma
* Görüşme notu ve kanıt analizi
* Final validasyon raporu

---

## Product Backlog

| ID    | Backlog Item                                  | Öncelik      | Sprint       | Durum        |
| ----- | --------------------------------------------- | ------------ | ------------ | ------------ |
| PB-01 | Kullanıcının iş fikrini sisteme girebilmesi   | Belirlenecek | Sprint 1     | Belirlenecek |
| PB-02 | Girilen fikrin temel analizinin yapılması     | Belirlenecek | Sprint 1     | Belirlenecek |
| PB-03 | Riskli varsayımların çıkarılması              | Belirlenecek | Belirlenecek | Belirlenecek |
| PB-04 | Müşteri görüşme sorularının üretilmesi        | Belirlenecek | Belirlenecek | Belirlenecek |
| PB-05 | MVP kapsamının MoSCoW yöntemiyle daraltılması | Belirlenecek | Belirlenecek | Belirlenecek |
| PB-06 | Doğrulama yol haritası oluşturulması          | Belirlenecek | Belirlenecek | Belirlenecek |
| PB-07 | Görüşme notlarının analiz edilmesi            | Belirlenecek | Belirlenecek | Belirlenecek |
| PB-08 | Final validasyon raporu oluşturulması         | Belirlenecek | Belirlenecek | Belirlenecek |

---

## Product Backlog URL

Belirlenecek.

---

## Sprint Board URL

Belirlenecek.

---

## Planlanan Teknolojiler

| Alan             | Teknoloji                       |
| ---------------- | ------------------------------- |
| Frontend         | Belirlenecek                    |
| Backend          | Django                          |
| Database         | PostgreSQL                      |
| API              | Django REST Framework           |
| Containerization | Docker                          |
| AI               | LLM API                         |
| RAG              | Akademi girişimcilik içerikleri |
| Deployment       | Belirlenecek                    |

---

## Proje Yapısı

```text
.
├── backend/
│   ├── apps/
│   │   ├── users/
│   │   ├── ideas/
│   │   └── analyses/
│   ├── config/
│   ├── manage.py
│   └── requirements.txt
├── docs/
│   ├── product/
│   ├── sprint-1/
│   ├── sprint-2/
│   └── sprint-3/
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

## Kurulum

### 1. Repoyu klonlama

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Ortam değişkenlerini hazırlama

```bash
cp .env.example .env
```

### 3. Docker ile çalıştırma

```bash
docker compose up --build
```

### 4. Uygulamayı açma

```text
http://localhost:8000/
```

---

## Geliştirme Ortamı

Backend uygulaması Docker üzerinde Django ve PostgreSQL ile çalışacak şekilde yapılandırılmıştır.

Lokal geliştirme için:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

---

## Sprint Dokümantasyonu

* [Sprint 1](docs/sprint-1/)
* [Sprint 2](docs/sprint-2/)
* [Sprint 3](docs/sprint-3/)

---

## Sprint Sonu Beklenen Dokümanlar

Her sprint sonunda aşağıdaki başlıkların güncellenmesi hedeflenmektedir:

* Backlog dağıtma mantığı
* Daily Scrum notları
* Sprint board güncellemeleri
* Ürün durumu
* Sprint review
* Sprint retrospective

---

## Sprint 1

### Sprint Notları

Belirlenecek.

### Sprint Hedefi

Belirlenecek.

### Sprint Backlog

Belirlenecek.

### Daily Scrum Notları

Belirlenecek.

### Sprint Board Güncellemeleri

Belirlenecek.

### Ürün Durumu

Belirlenecek.

### Sprint Review

Belirlenecek.

### Sprint Retrospective

Belirlenecek.

---

## Sprint 2

### Sprint Notları

Belirlenecek.

### Sprint Hedefi

Belirlenecek.

### Sprint Backlog

Belirlenecek.

### Daily Scrum Notları

Belirlenecek.

### Sprint Board Güncellemeleri

Belirlenecek.

### Ürün Durumu

Belirlenecek.

### Sprint Review

Belirlenecek.

### Sprint Retrospective

Belirlenecek.

---

## Sprint 3

### Sprint Notları

Belirlenecek.

### Sprint Hedefi

Belirlenecek.

### Sprint Backlog

Belirlenecek.

### Daily Scrum Notları

Belirlenecek.

### Sprint Board Güncellemeleri

Belirlenecek.

### Ürün Durumu

Belirlenecek.

### Sprint Review

Belirlenecek.

### Sprint Retrospective

Belirlenecek.

---

## Proje Teslim Bilgileri

| Teslim Kalemi | Durum        |
| ------------- | ------------ |
| GitHub reposu | Hazır        |
| Public repo   | Belirlenecek |
| Ürün demosu   | Belirlenecek |
| Canlı link    | Belirlenecek |
| Proje videosu | Belirlenecek |
| Final raporu  | Belirlenecek |

---

## Lisans

Belirlenecek.
