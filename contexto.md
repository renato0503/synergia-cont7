# Contexto do Projeto Synergia Cont7 - UNIFACC Cuiabá

Este documento oficial detalha a arquitetura, o escopo técnico e as diretrizes pedagógicas aplicadas ao projeto de integração das disciplinas de Contabilidade, Perícia e Agronegócio para a turma de 2026.

## 📋 Escopo e Requisitos do Projeto

### 1. Pivotagem e Foco Temático
- **Objetivo**: Transição total da plataforma para o atendimento das demandas das disciplinas de **Perícia Contábil**, **Auditoria Forense**, **Contabilidade Pública** e **Direito Agrário**.
- **Caso Central**: *"O Labirinto da Terra Solidária"* - Estudo de caso sobre o conflito de terras em Pai André, Várzea Grande/MT.
- **Implementação**: Redesenho completo da interface para uma estética "Investigativa/Auditoria", utilizando paleta de cores sóbrias (Deep Navy e Accent Red).

### 2. Estrutura de Conteúdo por Grupo
Cada equipe de acadêmicos possui uma trilha específica de defesa técnica:
- **Grupo 1**: Enfoque em **Comodato** e **Imóvel Rural** (Bruna, Yorgelis, Simone).
- **Grupo 2**: Enfoque em **Comodato** e **Expansão Urbana/REURB** (Sarah, Vinícius, Alysson, Edson).
- **Grupo 3**: Enfoque em **Parceria Rural** e **Imóvel Rural** (Paulo, Leison, Lucas, Leandro).

### 3. Requisitos Técnicos de Apresentação (Atendidos)
- **Extensão**: 12 slides técnicos por grupo, cobrindo Legislação, LRF, MCASP e Laudo Pericial.
- **Plano de Contas**: Destaque visual centralizado para o Plano de Contas de Regularização, demonstrando a segregação de ativos (Público vs. Privado).
- **Acessibilidade de Dados**: Sistema de navegação rápido entre grupos e Menu Principal centralizado.

### 4. Inovações e Ferramentas de Suporte
- **Estética Visual (Minimalismo)**: Uso de ilustrações exclusivas no estilo **Single Line Art** (traçado de linha única). Esta escolha pedagógica visa reduzir a carga cognitiva, mantendo o foco do espectador no conteúdo normativo e técnico (Artigos da CF, LRF e NBC).
- **Portabilidade (Exportar PPTX)**: Implementação de motor de exportação programática. Os alunos podem gerar arquivos PowerPoint (.pptx) editáveis diretamente do navegador, garantindo autonomia para ajustes de última hora em apresentações presenciais.
- **Persistência Local**: Todas as mídias e ativos são processados e armazenados localmente na estrutura `/assets/`, garantindo que o projeto funcione sem dependência de internet externa durante as bancas de defesa.

---

## 🛠️ Stack Tecnológica
- **Linguagens**: HTML5 Semântico, CSS3 (Modular Layouts), JavaScript ES6+.
- **Bibliotecas**:
    - `PptxGenJS`: Conversão de DOM para Office Open XML (PPTX).
    - `Phosphor Icons`: Sistema de iconografia técnica.
- **Processamento de Imagem**: Pipeline de geração via Pollinations IA com scripts de otimização em Python.
- **Hospedagem**: Versionamento via Git e deploy contínuo via GitHub Pages.

## 🔗 Repositório e Acesso
- **GitHub**: [github.com/renato0503/synergia-cont7](https://github.com/renato0503/synergia-cont7)
- **URL de Produção**: [renato0503.github.io/synergia-cont7](https://renato0503.github.io/synergia-cont7/)

---
*Atualizado em: 13 de Maio de 2026*
*Responsável: Prof. Renato Rosa / Antigravity AI*
