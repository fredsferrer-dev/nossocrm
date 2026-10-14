# Proposta Maçaix × AVVA: continuação no computador local

Este pacote tem tudo para continuar a proposta em uma sessão do Claude Code rodando no seu computador, com acesso às pastas do Google Drive para computador.

## Como abrir no computador

1. Instale o **Google Drive para computador** e deixe o Drive sincronizado.
2. Instale o **Claude Code** (app desktop ou `npm i -g @anthropic-ai/claude-code`).
3. Clone o repositório e entre no branch:
   ```bash
   git clone https://github.com/fredsferrer-dev/nossocrm.git
   cd nossocrm
   git checkout claude/avva-move-proposal-uxclkk
   cd propostas/avva
   ```
4. Instale as dependências do build: `pip install pikepdf pillow` (Chrome já instalado basta).
5. Abra o Claude Code nessa pasta e cole o prompt da seção "Prompt para a próxima sessão".

## O que está aqui

| Pasta | Conteúdo |
|---|---|
| `build/overlay.html` | Textos corrigidos que vão por cima das páginas 3 a 8 do dossiê (claims, certificações, selos provisórios) |
| `build/dossie-proposta.html` | Capa nova e páginas da proposta (ponto de partida, caminhos, produtos, freezer, benefícios, números, próximo passo) |
| `build/img/` | Fotos usadas hoje (resolução web) |
| `font/` | Montserrat (300, 400, 500, 700, 800) |
| `fonte/Macaix_Dossie_Avva.pdf` | Dossiê original, base das páginas 2 a 8 e da página final |
| `fonte/box_square.jpg` | Foto que substitui a imagem da página 7 do dossiê |
| `scripts/build.sh` | Gera `saida/Proposta_Macaix_AVVA.pdf` (16 páginas) |
| `saida/` | Última versão gerada (v6) |

Para regerar: `./scripts/build.sh` (defina `CHROME=/caminho/do/chrome` se precisar).

## Decisões já fechadas com o Fred

- **Três caminhos:** (1) freezer na casa com açaí incluído na mensalidade, sem meta; (2) degustação no encontro mensal com **um** representante Maçaix, usando a caixa de 5 L do enxoval (se precisar de mais, a Maçaix banca); top 3 do Move por trimestre ganham caixa de 2 L; (3) Jornada Maçaix dentro do Move (gamificação), sem pressa.
- **Primeira compra** (enxoval + 1 freezer pré-pago, preço de volume): 96 potes 240 ml × R$ 20,50; 36 potes 500 ml × R$ 36; 16 caixas 2 L × R$ 95; 1 caixa 5 L × R$ 249 = **R$ 5.033** (3x de R$ 1.677,67) ou **R$ 4.529,70** à vista (10%).
- **Benefícios AVVA:** preço de volume travado 12 meses em toda reposição; exclusividade de wellness house no Centro de Florianópolis; alunos com 10% na primeira compra e 5% nas seguintes (lojas e e-commerce); freezer em comodato; ficha para nutricionista; relatório de impacto.
- **Troca de vitrines:** vídeo-manifesto Maçaix nas TVs da AVVA; AVVA nos canais Maçaix.
- **Formatos B2C:** só 240 ml, 500 ml e 2 L. A caixa de 5 L é food service e aparece só na degustação.

## Regras de comunicação (não errar)

- Nunca "orgânico" solto como atributo: usar **"Feito com polpa orgânica de Colheita Especial"**. Nomes de certificações e lista de ingredientes ficam como estão.
- Impacto ambiental: **"florestas do Brasil"**, não só Amazônia (Amazônia/Óbidos pode aparecer como origem).
- **Sem ORAC**, sem "performance comprovada", sem alegação de saúde ("protege células", "envelhecimento"). Usar: polifenóis e antocianinas naturais do açaí, despolpa em até 12 h, patente INPI do extrato da semente.
- Vitamina C: **13 mg · 13% VD** (referência Anvisa IN 75/2020). Confirmar no rótulo.
- Certificações: USDA Organic · IBD Orgânico · Halal · Kosher BKA Parve.

## Pendências (pedido do Fred em 14/10)

1. **Selos originais** na página 3 (hoje são círculos provisórios em `build/overlay.html`). No Drive: `usda-organic-hd.png`, `ibd-organic-hd.png`, `kosher-bka-hd.png`, `halal-fambras-hd.png` (pasta de selos criada em 28/09). Tirar fundo se precisar.
2. **Confirmar nome do Halal:** o arquivo é da FAMBRAS; no texto está "Sul Halal".
3. **Fotos em alta** da pasta do Drive **"10 ENSAYO FER · alta (set-oct 2026)"** (DSC_6045, DSC_6047, DSC_6054, DSC_6129, DSC_6162, DSC_6174, DSC_6222, DSC_6266, DSC_6276, DSC_6302, DSC04800, DSC04872, DSC04909, DSC04917, DSC04974, DSC04978, DSC05017, DSC05024).
4. **Nenhuma foto repetida.** Manter a foto da capa (cacho). Trocar a foto da página 3 do dossiê, que repete a capa.
5. **Foto do freezer** em que apareçam bem as caixas e os potes de dentro.
6. Seguir o padrão visual da **apresentação do Café Cultura** (não encontrada no Drive pela busca; pedir o caminho ao Fred).
7. Depois de aprovado, salvar o PDF final na pasta **AVVA** do Drive.

## Prompt para a próxima sessão

> Leia `HANDOFF.md` nesta pasta. Continue a proposta Maçaix × AVVA resolvendo as pendências 1 a 7, usando os arquivos originais do meu Google Drive (pasta sincronizada no computador). Mantenha as regras de comunicação. Regere o PDF com `./scripts/build.sh`, confira cada página renderizada e salve o resultado na pasta AVVA do Drive.
