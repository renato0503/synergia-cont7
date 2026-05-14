# Contexto do Projeto Synergia Cont7 - UNIFACC Cuiabá

Este documento resume as solicitações do Prof. Renato Rosa e as implementações realizadas para a plataforma de perícia e auditoria contábil.

## 📋 Nova Configuração (Maio 2026)

### 1. Pivotagem do Projeto
- **Pedido**: Alterar o foco total do projeto para a disciplina de Contabilidade (Perícia, Auditoria e Agronegócio). Remover todos os mapas e grupos antigos.
- **Caso Problemático**: "O Labirinto da Terra Solidária: Entre o Teto e a Terra".
- **Ações**: 
    - Remoção de todos os arquivos de mapas e grupos anteriores.
    - Redesenho da `index.html` com estética investigativa e foco no conflito fundiário/contábil de Várzea Grande (Pai André).

### 2. Estrutura das Disciplinas Integradas
- **Legislação do Agronegócio**: Foco em Parceria vs. Comodato e Imóvel Rural vs. Expansão Urbana.
- **Contabilidade Pública**: Auditoria de convênios (R$ 5M), desvio de finalidade (LRF) e registro de Ativo Social (MCASP).
- **Perícia Contábil**: Investigação de fluxo de caixa, separação de recursos públicos/privados ("Joio do Trigo") e elaboração de laudo pericial.

### 3. Implementação dos Grupos (Novos Acadêmicos)
- **Grupo 1**: Bruna Saggin, Yorgelis Rojas, Simone Terena. (Foco: Comodato / Imóvel Rural).
- **Grupo 2**: Sarah Ikegami, Vinicius, Alysson Dias, Edson Junior. (Foco: Comodato / Expansão Urbana).
- **Grupo 3**: Paulo Henrique, Leison Silva, Lucas Silva, Leandro Arruda. (Foco: Parceria / Imóvel Rural).

### 4. Destaque Visual: Plano de Contas
- **Pedido**: Dar destaque especial ao Plano de Contas.
- **Ação**: Implementação de um visualizador de Plano de Contas de Regularização em cada página de grupo, mostrando a segregação de ativos e o rastreamento de desvios.

### 5. Melhorias de Apresentação e Interatividade (Última Atualização)
- **Expansão de Conteúdo**: Refatoração das páginas HTML de cada grupo para comportarem **12 slides interativos**, divididos estruturalmente para abordar de forma isolada os requisitos de Legislação, Contabilidade Pública e Perícia.
- **Design "Split-Screen"**: Implementação de leiaute responsivo que divide a tela, garantindo que o conteúdo textual denso esteja perfeitamente legível em contraste com imagens HD contextuais do agronegócio e do judiciário.
- **Imagens Contextualizadas em IA (Pollinations)**: Substituição de placeholders quebrados por 27 imagens exclusivas geradas por Inteligência Artificial via prompts otimizados em inglês (com seeds fixos). As imagens são persistidas localmente (`assets/`) para garantir funcionamento offline em defesas de banca e maior velocidade no GitHub Pages.
- **Integração PPTX (PptxGenJS)**: Adição da funcionalidade de "Exportar PPTX". A plataforma converte programaticamente os elementos em tela (textos, listas, layouts e fundos) diretamente para um arquivo `.pptx` (PowerPoint) editável no lado do cliente. Essa ferramenta atende à exigência da turma, permitindo que os acadêmicos editem seus slides localmente com as imagens processadas.

---

## 🛠️ Tecnologias Utilizadas
- **Frontend**: HTML5, CSS3 (Modern Grid/Flexbox), JavaScript (Vanilla).
- **Geração de Apresentações**: `PptxGenJS` (Exportação client-side para PowerPoint).
- **Geração de Imagens**: API Pollinations IA (com processamento via scripts locais automatizados em Python).
- **Ícones**: Phosphor Icons.
- **Tipografia**: Outfit & Playfair Display (Executive/Investigative style).
- **Infraestrutura**: Git, GitHub (synergia-cont7), GitHub Pages.

## 🔗 Links Úteis
- **Repositório**: [github.com/renato0503/synergia-cont7](https://github.com/renato0503/synergia-cont7)
- **Site ao Vivo**: [renato0503.github.io/synergia-cont7](https://renato0503.github.io/synergia-cont7/)
