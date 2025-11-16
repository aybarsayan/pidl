#!/usr/bin/env python3
"""
Tez dosyalarını birleştirip PDF oluştur
"""

import os
from pathlib import Path

# Tüm bölümleri sırayla oku
files = [
    "ON_KISIM_OZET.md",
    "BOLUM_1_GIRIS.md", 
    "BOLUM_2_KURAMSAL_CERCEVE.md",
    "BOLUM_3_YONTEM.md",
    "BOLUM_4_BULGULAR.md",
    "BOLUM_5_TARTISMA_VE_SONUC.md",
    "KAYNAKCA.md",
    "EKLER.md"
]

# Tüm içeriği birleştir
full_content = []

# Başlık sayfası
full_content.append("""
---
title: "İnsan-AI İşbirliği Modellerinde Yetkinlik Transferi ve Performans Optimizasyonu"
subtitle: "Blockchain Tabanlı Eğitim Teknolojilerinde Çok Katmanlı Yetkinlik Modellemesi"
author: "[İsminiz]"
date: "Ekim 2025"
documentclass: report
fontsize: 12pt
geometry: margin=2.5cm
toc: true
toc-depth: 3
lang: tr-TR
---

\\newpage

""")

for filename in files:
    filepath = Path(filename)
    if filepath.exists():
        print(f"✓ Eklendi: {filename}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            full_content.append(content)
            full_content.append("\n\\newpage\n")  # Her bölüm sonrası yeni sayfa
    else:
        print(f"✗ Bulunamadı: {filename}")

# Birleştirilmiş dosyayı yaz
combined_file = "TEZ_BIRLESTIRILMIS.md"
with open(combined_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(full_content))

print(f"\n✅ Birleştirilmiş dosya oluşturuldu: {combined_file}")
print(f"📄 Toplam boyut: {len(''.join(full_content)) / 1000:.1f} KB")

# Şimdi PDF'e çevir (pandoc ile)
print("\n🔄 PDF oluşturuluyor...")

import subprocess

try:
    # HTML üzerinden PDF (daha kolay)
    subprocess.run([
        'pandoc',
        combined_file,
        '-o', 'DOKTORA_TEZI_TAM.pdf',
        '--from=markdown',
        '--toc',
        '--toc-depth=3',
        '-V', 'geometry:margin=2.5cm',
        '-V', 'fontsize=12pt',
        '-V', 'documentclass=report',
        '-V', 'lang=tr-TR',
        '--pdf-engine=wkhtmltopdf'
    ], check=True)
    
    print("✅ PDF başarıyla oluşturuldu: DOKTORA_TEZI_TAM.pdf")
    
except subprocess.CalledProcessError:
    print("⚠️  wkhtmltopdf yok, HTML oluşturuluyor...")
    
    # Fallback: HTML
    subprocess.run([
        'pandoc',
        combined_file,
        '-o', 'DOKTORA_TEZI_TAM.html',
        '--standalone',
        '--toc',
        '--toc-depth=3',
        '-V', 'lang=tr-TR'
    ])
    
    print("✅ HTML oluşturuldu: DOKTORA_TEZI_TAM.html")
    print("💡 HTML'i tarayıcıda açıp 'Print to PDF' yapabilirsiniz")

except Exception as e:
    print(f"❌ Hata: {e}")
    print("\n📝 Birleştirilmiş Markdown dosyası hazır: TEZ_BIRLESTIRILMIS.md")
    print("💡 Bu dosyayı online PDF converter'da kullanabilirsiniz:")
    print("   - https://markdown-pdf.com")
    print("   - https://cloudconvert.com/md-to-pdf")

