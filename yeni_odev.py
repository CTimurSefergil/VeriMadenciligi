"""_template/ klasöründen yeni bir ödev klasörü oluşturur.

Kullanım:  uv run yeni_odev.py <numara> <kisa-ad> [hocadan gelen dosyaların klasörü]
Örnek:     uv run yeni_odev.py 2 kumeleme ~/Downloads/Assignment2
"""

import shutil
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Bu uzantılar ödev metni sayılır; geri kalan her dosya ham veridir
DOC_SUFFIXES = {".doc", ".docx", ".pdf", ".pptx", ".md"}


def main() -> None:
    if len(sys.argv) not in (3, 4) or not sys.argv[1].isdigit():
        sys.exit(__doc__)
    number, name = int(sys.argv[1]), sys.argv[2]
    source = Path(sys.argv[3]).expanduser() if len(sys.argv) == 4 else None

    dest = ROOT / f"odev{number:02d}-{name}"
    if dest.exists():
        sys.exit(f"Zaten var: {dest}")
    if source and not source.is_dir():
        sys.exit(f"Klasör bulunamadı: {source}")

    shutil.copytree(ROOT / "_template", dest)
    readme = dest / "README.md"
    text = readme.read_text(encoding="utf-8")
    readme.write_text(text.replace("{{N}}", str(number)).replace("{{NAME}}", name), encoding="utf-8")

    for f in sorted(source.iterdir()) if source else []:
        # Gizli dosyalar ve Office/LibreOffice kilit dosyaları (.~lock.*, ~$*) atlanır
        if not f.is_file() or f.name.startswith((".", "~$")):
            continue
        if f.suffix.lower() in DOC_SUFFIXES:
            shutil.copy2(f, dest / "assignment")
        else:
            target = dest / "data" / "raw" / f.name
            shutil.copy2(f, target)
            # Ham veri salt okunur yapılır, böylece yanlışlıkla üzerine yazılamaz
            target.chmod(stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)

    print(f"Oluşturuldu: {dest}")


if __name__ == "__main__":
    main()
