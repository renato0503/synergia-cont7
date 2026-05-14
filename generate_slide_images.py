#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar imagens contextuais para os slides dos Grupos 1, 2 e 3
Usa Pollinations AI com seeds fixos para consistência visual
"""

import os
import requests
from pathlib import Path
import time

# Configurações
BASE_URL = "https://image.pollinations.ai/prompt/"
OUTPUT_DIR = "assets"
WIDTH, HEIGHT = 1280, 720
QUALITY = 85

# Prompts organizados por grupo e slide (27 total)
PROMPTS = {
    "grupo1": {
        "slide01": "cinematic documentary photo of a rural housing construction site in Brazilian Cerrado at golden hour, workers in safety vests, modest homes under construction, farmland in background, realistic photography style --ar 16:9 --seed 1001",
        "slide02": "aerial drone view of Várzea Grande MT showing urban edge meeting rural farmland, small informal settlements visible, green fields, dirt roads, realistic satellite-style photography --ar 16:9 --seed 1002",
        "slide03": "close-up of legal documents on wooden desk: Brazilian land contract, gavel, calculator, with blurred rural landscape through window, professional documentary style --ar 16:9 --seed 1003",
        "slide04": "Brazilian rural property sign 'Imóvel Rural' with fence, Cerrado vegetation, distant farm buildings, natural lighting, photojournalistic style --ar 16:9 --seed 1004",
        "slide05": "split composition: left side modest rural housing, right side native Cerrado vegetation with environmental protection sign, symbolic tension, realistic photography --ar 16:9 --seed 1005",
        "slide06": "Brazilian tax document 'ITR' and 'Funrural' on desk with calculator, rural property in background through window, professional office lighting --ar 16:9 --seed 1006",
        "slide07": "auditor's hands reviewing financial documents with red highlighter, calculator, blurred government building in background, serious documentary style --ar 16:9 --seed 1007",
        "slide08": "modern accounting spreadsheet on laptop screen showing 'Ativo Social' classification, professional office environment, shallow depth of field --ar 16:9 --seed 1008",
        "slide09": "forensic accountant tracing financial flow on whiteboard with red string connecting documents, investigative journalism style, dramatic lighting --ar 16:9 --seed 1009",
        "slide10": "legal document with numbered questions 'Quesitos Periciais' on desk, gavel nearby, Brazilian court seal visible, professional photography --ar 16:9 --seed 1010",
        "slide11": "clean minimalist visualization of accounting chart of accounts with color-coded branches, modern infographic style, white background, professional presentation aesthetic --ar 16:9 --seed 1011",
        "slide12": "professional team of three diverse Brazilian women in business attire shaking hands with advisor in modern university setting, warm natural lighting, documentary style --ar 16:9 --seed 1012"
    },
    "grupo2": {
        "slide01": "cinematic photo of urban-rural interface in Mato Grosso: paved road dividing city buildings and farmland, sunrise lighting, hopeful atmosphere, documentary photography --ar 16:9 --seed 2001",
        "slide02": "community meeting under simple shelter in rural settlement, diverse families discussing, maps and documents on table, natural daylight, photojournalistic style --ar 16:9 --seed 2002",
        "slide03": "Brazilian legal document highlighting 'função social da propriedade' with green highlight, rural landscape visible through window, professional style --ar 16:9 --seed 2003",
        "slide04": "map of Várzea Grande showing urban expansion zone overlapping rural area, red boundary lines, professional cartographic style with legend --ar 16:9 --seed 2004",
        "slide05": "environmental officer in uniform reviewing documents with community leader near construction site, tense but respectful dialogue, realistic documentary --ar 16:9 --seed 2005",
        "slide06": "signing ceremony of legal document 'Termo de Ajustamento de Conduta' at wooden table, multiple hands, Brazilian official seal, professional photography --ar 16:9 --seed 2006",
        "slide07": "modern accounting software interface showing 'Ativo Social em Regularização' classification, clean UI, professional office environment --ar 16:9 --seed 2007",
        "slide08": "dashboard screen showing public management KPIs: execution rate, transparency index, social counterpart, modern data visualization style --ar 16:9 --seed 2008",
        "slide09": "mediator facilitating discussion between community members and officials around table with documents, collaborative atmosphere, natural lighting --ar 16:9 --seed 2009",
        "slide10": "document titled 'Recomendações Conciliatórias' with bullet points, green checkmarks, professional legal document style, shallow depth of field --ar 16:9 --seed 2010",
        "slide11": "visual flowchart of hybrid accounting structure: public funds + community resources, color-coded branches, clean infographic on white background --ar 16:9 --seed 2011",
        "slide12": "group of four diverse Brazilian students (2M/2F) presenting to professor in modern classroom, confident expressions, natural window lighting --ar 16:9 --seed 2012"
    },
    "grupo3": {
        "slide01": "professional photo of Brazilian rural partnership agreement signing: hands shaking over contract, farm landscape through window, warm natural lighting --ar 16:9 --seed 3001",
        "slide02": "cooperative agricultural activity in Mato Grosso: families harvesting vegetables together, rustic storage shed, Cerrado background, documentary style --ar 16:9 --seed 3002",
        "slide03": "vintage-style Brazilian law book 'Lei 4.504/64' open on desk with rural partnership contract, calculator, natural wood texture, professional photography --ar 16:9 --seed 3003",
        "slide04": "aerial view of farm with color-coded zones: residential area (blue), agricultural area (green), legal reserve (brown), professional cartographic overlay --ar 16:9 --seed 3004",
        "slide05": "split document showing two columns: 'Finalidade Social' and 'Atividade Produtiva', hands pointing to clauses, professional legal photography --ar 16:9 --seed 3005",
        "slide06": "Brazilian tax forms 'ITR' and 'PIS/COFINS Rural' side by side with calculator and rural property photo, professional office lighting --ar 16:9 --seed 3006",
        "slide07": "accounting ledger with color-coded entries: blue for public funds, green for private revenue, clear separation, shallow depth of field --ar 16:9 --seed 3007",
        "slide08": "fresh vegetables harvest (legumes, greens) in wooden crates with price tags, rural market setting, natural daylight, documentary style --ar 16:9 --seed 3008",
        "slide09": "financial analyst reviewing agricultural revenue report with charts, laptop showing cash flow, professional office environment --ar 16:9 --seed 3009",
        "slide10": "before/after visualization: messy handwritten ledger transforming into clean digital accounting chart, symbolic arrow, infographic style --ar 16:9 --seed 3010",
        "slide11": "professional hybrid accounting structure diagram: public + cooperative + tax branches, color-coded, minimalist white background, presentation-ready --ar 16:9 --seed 3011",
        "slide12": "team of four Brazilian male students in business casual attire standing confidently in front of university building, natural afternoon light, documentary style --ar 16:9 --seed 3012"
    }
}

def download_image(prompt: str, output_path: str):
    """Baixa imagem da Pollinations AI com parâmetros otimizados"""
    
    # Se a imagem já existir e tiver tamanho maior que 0, pula
    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        print(f"✓ Já existe: {output_path}")
        return True
        
    # Codifica o prompt para URL
    encoded_prompt = requests.utils.quote(prompt)
    
    # Monta URL com parâmetros de otimização
    url = f"{BASE_URL}{encoded_prompt}?width={WIDTH}&height={HEIGHT}&nologo=true&model=flux"
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            
            # Salva como JPG para fotos, PNG para infográficos
            if "infographic" in prompt.lower() or "chart" in prompt.lower() or "visualization" in prompt.lower():
                output_path = output_path.replace(".jpg", ".png")
                with open(output_path, 'wb') as f:
                    f.write(response.content)
            else:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
            
            print(f"✓ Salvo: {output_path}")
            time.sleep(2) # evita limits de API
            return True
            
        except requests.exceptions.RequestException as e:
            if hasattr(e.response, 'status_code') and e.response.status_code == 429:
                wait_time = 5 * (attempt + 1)
                print(f"⚠ Rate limit atingido. Tentando novamente em {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"✗ Erro ao baixar {output_path}: {e}")
                time.sleep(2)
                if attempt == max_retries - 1:
                    return False
    return False

def main():
    print("🎨 Gerando imagens para slides dos Grupos 1, 2 e 3...")
    print(f"📁 Diretório de saída: {OUTPUT_DIR}/")
    
    for grupo, slides in PROMPTS.items():
        grupo_dir = Path(OUTPUT_DIR) / grupo
        grupo_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n📦 Processando {grupo}...")
        
        for slide_name, prompt in slides.items():
            output_file = grupo_dir / f"{slide_name}.jpg"
            if "infographic" in prompt.lower() or "chart" in prompt.lower() or "visualization" in prompt.lower():
                output_file = grupo_dir / f"{slide_name}.png"
            download_image(prompt, str(output_file))
    
    print("\n✅ Processo concluído! Imagens salvas em assets/grupo{1,2,3}/")
    print("🔧 Próximo passo: atualizar os arquivos HTML com os caminhos locais.")

if __name__ == "__main__":
    main()
