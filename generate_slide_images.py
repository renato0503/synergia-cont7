#!/usr/bin/env python3
"""
Script otimizado para gerar imagens - Processa em lotes menores
Execute em partes se necessário
"""

import requests
from pathlib import Path
from urllib.parse import quote
import time

BASE_URL = "https://image.pollinations.ai/prompt/"
OUTPUT_DIR = "assets"
WIDTH, HEIGHT = 1280, 720


def generate_batch(grupo, slides_dict, start_seed=1000):
    """Processa um lote de slides"""
    grupo_dir = Path(OUTPUT_DIR) / grupo
    grupo_dir.mkdir(parents=True, exist_ok=True)

    for slide_name, prompt in slides_dict.items():
        output_file = grupo_dir / f"{slide_name}.jpg"
        print(f"  Gerando {slide_name}...")

        encoded_prompt = quote(prompt)
        url = f"{BASE_URL}{encoded_prompt}?width={WIDTH}&height={HEIGHT}&nologo=true&model=flux"

        try:
            response = requests.get(url, timeout=180)
            response.raise_for_status()

            with open(output_file, "wb") as f:
                f.write(response.content)
            print(f"    ✓ Salvo")
            time.sleep(20)  # Espera razoável
        except Exception as e:
            print(f"    ✗ Erro: {e}")

    print(f"  Lote {grupo} completo!")


# GRUPO 1 - lote 1 (slides 1-4)
batch_g1_p1 = {
    "slide01": "cover image: large rural Brazilian property with 200 families receiving keys to new houses, forensic accountant with magnifying glass, professional documentary style, dramatic lighting, 16:9 aspect ratio",
    "slide02": "aerial view of Brazilian conflict: 500 hectare farm near city with 200 families in simple housing, public money bags with government seal, Ministry of Public workers inspecting, documentary photography style",
    "slide03": "legal illustration: two hands signing contract over rural land, Brazilian Civil Law book open, INCRA stamp, property documents, lawyer in suit, law office with bookshelves, professional legal photography",
    "slide04": "environmental embargo scene: red government embargo sign on fence, forest area with legal reserve, bulldozer stopped near river, environmental police officer writing ticket, legal barriers, Amazon vegetation",
}

# GRUPO 1 - lote 2 (slides 5-8)
batch_g1_p2 = {
    "slide05": "Brazilian agricultural tax: farmer with coffee crop, Funrural tax stamp, productivity chart, federal revenue building, cooperative warehouse, coffee beans, accounting calculator, professional style",
    "slide06": "fiscal responsibility violation: Brazilian city hall, money bags diverted to commercial warehouse, cement bags marked public housing used in commercial building, mayor with LRF book, red alert stamp",
    "slide07": "accounting registry: government accountant at desk with MCASP book, house construction background, balance sheet diagram, public funds flow chart, Brazilian treasury seal, computer with government software",
    "slide08": "forensic investigation: two forensic accountants examining documents with magnifiers, bank statements and invoices, laptop with spreadsheet, crime scene photos, evidence markers, professional forensic photography",
}

# Execute os lotes separadamente conforme necessário
# Exemplo: generate_batch("grupo1", batch_g1_p1)
