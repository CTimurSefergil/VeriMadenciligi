# Ödev 1 — Veri Temizleme (Data Cleaning)

**Teslim tarihi:**
**Teslim edilecekler:** Excel olarak temizlenmiş veri setleri (`data/processed/*.xlsx`), kodlar (notebook'lar) ve rapor.

## Görev
`Is_ilanlari.csv` ve `Calisanlar.xlsx` veri setlerini temizlemek. Veriler metinsel/kategorik hatalar
(yazım hataları, yanlış formatlar) ve sayısal problemler (eksik veri, uç değerler) içeriyor.
Temizlenmiş veriler Excel dosyası olarak kaydedilecek.

## Puanlama listesi (100 puan)
- [ ] **1. Veriyi Keşfetme & İlk Analiz:** Yapısal bozukluklar, tutarsız harf kullanımları, fazla boşluklar ve yanlış veri tipleri eksiksiz tespit edilmiş.
- [ ] **2. Eksik Verilerin Tespiti ve Görselleştirilmesi:** Gizli eksik değerler (`?`, `null`, `n/a`, …) dahil tüm eksiklikler bulunmuş, ısı haritası veya grafiklerle raporlanmış.
- [ ] **3. Eksik Veri Stratejisi & Uygulama:** Doldurma (mean, median, KNN, …) veya silme kararları verinin dağılımına göre gerekçelendirilmiş ve doğru uygulanmış.
- [ ] **4. Aykırı Değer (Outlier) Analizi:** IQR veya Z-skoru ile tespit edilmiş, box plot ile gösterilmiş, baskılama veya silme doğru uygulanmış.
- [ ] **5. Temizlik Sonrası Dağılım Kontrolü:** Temizliğin orijinal dağılımı bozmadığı histogram ve mean/std kıyaslamasıyla gösterilmiş.
- [ ] **6. Kod Kalitesi & Tekrarlanabilirlik:** Kod düzenli, yorumlar açıklayıcı, baştan sona hatasız çalışıyor.
- [ ] **7. Raporlama ve Akademik Dil:** Tüm işlemler teknik bir dille, neden-sonuç ilişkisiyle, grafik ve tablolarla raporlanmış.

## Nasıl çalıştırılır
Kernel'i yeniden başlatıp `notebooks/` içindeki notebook'ları sırayla, baştan sona çalıştır.
`data/processed/` ve `figures/` içindeki her şey yeniden üretilir.

| Notebook | Girdi | Çıktı |
|---|---|---|
| `01_is_ilanlari.ipynb` | `data/raw/Is_ilanlari.csv` | `data/processed/Is_ilanlari_temiz.xlsx` |
| `02_calisanlar.ipynb` | `data/raw/Calisanlar.xlsx` | `data/processed/Calisanlar_temiz.xlsx` |
