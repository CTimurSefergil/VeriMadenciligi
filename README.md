# Veri Madenciliği

Veri Madenciliği dersi ödevleri. Bütün ödevler aynı Python ortamını kullanır, her ödev kendi klasöründedir.

| Ödev | Konu |
|---|---|
| [Ödev 1](odev01-veri-temizleme/) | Veri temizleme |

## Kurulum

Windows, macOS ve Linux'ta aynı adımlar geçerlidir. Bilgisayarda Python kurulu olması gerekmez,
[uv](https://docs.astral.sh/uv/) doğru Python sürümünü ve bütün kütüphaneleri kendisi indirir.

**1. uv'yi kur** (bir kez yapılır, sonra terminali kapatıp yeniden aç)

- Windows (PowerShell):
  ```
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- macOS / Linux:
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

**2. Projeyi indir ve kur**

```
git clone https://github.com/CTimurSefergil/VeriMadenciligi.git
cd VeriMadenciligi
uv sync
```

Git yoksa bu sayfadaki **Code → Download ZIP** ile indir, klasörü aç ve içinde `uv sync` çalıştır.

**3. Çalıştır**

```
uv run jupyter lab
```

Tarayıcıda Jupyter açılır. Bir ödevin `notebooks/` klasörüne girip notebook'ları sırayla çalıştır.
VS Code kullanıyorsan klasörü açman yeterli: önerilen Python ve Jupyter eklentilerini kur, `.venv` ortamını kendisi bulur.

## Geliştirme

- **Kütüphane eklemek:** `uv add <paket>`. `pip install` kullanma; `uv add` paketi `pyproject.toml` ve `uv.lock`
  dosyalarına yazar, böylece projeyi kuran herkes birebir aynı sürümleri alır.
- **Yeni ödev oluşturmak:** `uv run yeni_odev.py 2 kumeleme ~/Downloads/Assignment2`
  → `odev02-kumeleme/` klasörünü oluşturur. `.docx`/`.pdf` dosyaları `assignment/` içine,
  diğer dosyalar salt okunur olarak `data/raw/` içine kopyalanır.
- **direnv (isteğe bağlı, Linux/macOS):** `direnv allow` çalıştırırsan klasöre girdiğinde ortam kendiliğinden etkinleşir.

## Klasör yapısı

```
odevNN-ad/
├── README.md          görev, teslim tarihi, puanlama listesi
├── assignment/        hocanın verdiği ödev metni
├── data/
│   ├── raw/           orijinal veri (salt okunur, asla değiştirilmez)
│   └── processed/     notebook'ların ürettiği temiz veri
├── notebooks/         analizler, çalışma sırasına göre numaralı (01_, 02_, …)
├── figures/           rapora eklenecek grafikler
├── report/            yazılı rapor
└── submission/        teslim edilecek son dosyalar
```

## Lisans

Kodlar [MIT lisansı](LICENSE) ile paylaşılmıştır. Ödev metinleri ve veri setleri ders hocasına ve
kendi kaynaklarına aittir, bu lisansa dahil değildir.
