#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atualiza os arquivos HTML para usar imagens locais em vez de URLs externas
"""

import re
from pathlib import Path

def update_html_file(filepath: str, grupo: str):
    """Substitui URLs de imagens externas por caminhos locais"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar URLs externas em background-image
    patterns_to_replace = [
        r"url\(['\"]?https://picsum\.photos/[^)]+['\"]?\)",
        r"url\(['\"]?https://image\.pollinations\.ai/prompt/[^)]+['\"]?\)",
        r"url\(['\"]?https://source\.unsplash\.com/[^)]+['\"]?\)",
    ]
    
    for pattern in patterns_to_replace:
        # Encontra todos os matches e substitui sequencialmente
        matches = list(re.finditer(pattern, content))
        for i, match in enumerate(matches, 1):
            slide_num = str(i).zfill(2)
            replacement = f"url('assets/{grupo}/slide{slide_num}.jpg')"
            # Tenta também versão .png para slides de infográfico
            content = content.replace(match.group(), replacement)
    
    # Salva o arquivo atualizado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Atualizado: {filepath}")

def main():
    print("🔄 Atualizando arquivos HTML com caminhos de imagens locais...")
    
    files_to_update = [
        ("grupo1.html", "grupo1"),
        ("grupo2.html", "grupo2"),
        ("grupo3.html", "grupo3"),
    ]
    
    for filepath, grupo in files_to_update:
        if Path(filepath).exists():
            update_html_file(filepath, grupo)
        else:
            print(f"✗ Arquivo não encontrado: {filepath}")
    
    print("\n✅ HTMLs atualizados! Faça commit e push para o GitHub Pages.")

if __name__ == "__main__":
    main()
