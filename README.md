
# 📦 Drone Filo Optimizasyonu

Bu proje, çok kısıtlı ortamlarda çalışan bir drone filosu için **dinamik teslimat planlaması** yapmayı hedeflemektedir. Teslimat öncelikleri, enerji kısıtları ve uçuşa yasak bölgeler gibi faktörleri dikkate alarak en uygun rotalar oluşturulmaktadır.

## 🛠 Proje İçeriği

- **A\*** algoritması ile rota bulma
- **Genetik algoritma** ile teslimat sıralaması optimizasyonu
- **No-Fly Zone (Uçuşa Yasak Bölge)** kontrolleri
- **Batarya ve yük kapasitesi** kısıtları
- **Teslimat önceliği** ve zaman pencere destekli yapı (Geliştirilebilir)
- **Matplotlib** ile rotaların görselleştirilmesi

## 📁 Klasör Yapısı

```
drone_optimization/
├── main.py
├── genetic.py
├── astar.py
├── drone.py, delivery.py
├── noflyzone.py
├── utils.py
├── plot_map.py
├── test_performance.py
├── requirements.txt
```

## 🚀 Kullanım

### 1. Gerekli Paketler:
```bash
pip install -r requirements.txt
```

### 2. Çalıştırmak için:
```bash
python main.py
```

## 📌 Senaryolar

| Senaryo | Açıklama |
|---------|----------|
| Senaryo 1 | 5 drone, 20 teslimat, 2 no-fly zone |
| Senaryo 2 | (Opsiyonel) 10 drone, 50 teslimat, dinamik no-fly zone |

## 📊 Görselleştirme Örneği

Matplotlib ile en iyi bulunan rota şu şekilde çizdirilir:

```python
from genetic import genetic_algorithm
from plot_map import plot_best_ga_route

best_route = genetic_algorithm(deliveries, drone, no_fly_zones)
plot_best_ga_route(drone, best_route, no_fly_zones)
```

## 🧠 A* vs Genetik Algoritma Karşılaştırması

| Özellik | A* | Genetik Algoritma |
|--------|----|-------------------|
| Yol doğruluğu | ✅ | ❌ (yaklaşık) |
| Çoklu hedef desteği | ❌ | ✅ |
| Performans | Hızlı | Daha yavaş |
| Optimizasyon | En kısa yol | Tüm rotayı optimize eder |

## 👨‍💻 Geliştiren
Bu proje, Kocaeli Üniversitesi Teknoloji Fakültesi Bilişim Sistemleri Mühendisliği öğrencisi tarafından TBL331 Yazılım Geliştirme Lab II dersi kapsamında hazırlanmıştır.
