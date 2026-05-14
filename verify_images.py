#!/usr/bin/env python3
import re
from pathlib import Path

def check_html_for_external_urls(filepath: str) -> list:
    """Retorna lista de URLs externas ainda presentes no HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    external_patterns = [
        r'https://picsum\.photos',
        r'https://image\.pollinations\.ai',
        r'https://source\.unsplash\.com',
        r'https://images\.pexels\.com',
    ]
    
    found = []
    for pattern in external_patterns:
        matches = re.findall(pattern, content)
        found.extend(matches)
    
    return found

def check_local_images_exist(grupo: str) -> dict:
    """Verifica se todas as imagens locais esperadas existem"""
    results = {}
    for i in range(1, 13):
        slide = f"slide{str(i).zfill(2)}"
        jpg_path = Path(f"assets/{grupo}/{slide}.jpg")
        png_path = Path(f"assets/{grupo}/{slide}.png")
        results[slide] = jpg_path.exists() or png_path.exists()
    return results

def main():
    print("🔍 Verificando integridade das alterações...")
    
    # 1. Checar HTMLs por URLs externas residuais
    print("\n📄 Verificando HTMLs por URLs externas:")
    for html_file in ["grupo1.html", "grupo2.html", "grupo3.html"]:
        externals = check_html_for_external_urls(html_file)
        if externals:
            print(f"✗ {html_file}: {len(externals)} URLs externas encontradas")
        else:
            print(f"✓ {html_file}: sem URLs externas")
    
    # 2. Checar se imagens locais existem
    print("\n🖼️ Verificando existência de imagens locais:")
    for grupo in ["grupo1", "grupo2", "grupo3"]:
        results = check_local_images_exist(grupo)
        missing = [s for s, exists in results.items() if not exists]
        if missing:
            print(f"✗ {grupo}: faltam {len(missing)} imagens: {missing}")
        else:
            print(f"✓ {grupo}: todas as 12 imagens presentes")
    
    print("\n✅ Verificação concluída!")

if __name__ == "__main__":
    main()
