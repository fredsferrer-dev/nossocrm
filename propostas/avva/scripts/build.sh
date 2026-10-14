#!/usr/bin/env bash
# Gera saida/Proposta_Macaix_AVVA.pdf a partir de build/*.html + fonte/Macaix_Dossie_Avva.pdf
# Requisitos: Python 3 com pikepdf e pillow; Chrome/Chromium (defina CHROME se não estiver no PATH).
set -euo pipefail
cd "$(dirname "$0")/.."
CHROME="${CHROME:-$(command -v google-chrome || command -v chromium || command -v chromium-browser || echo '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')}"
mkdir -p tmp
for f in overlay dossie-proposta; do
  "$CHROME" --headless --no-sandbox --disable-gpu --allow-file-access-from-files \
    --virtual-time-budget=10000 --no-pdf-header-footer \
    --print-to-pdf="$PWD/tmp/$f.pdf" "file://$PWD/build/$f.html"
done
python3 scripts/strip.py fonte/Macaix_Dossie_Avva.pdf tmp/dossie_stripped.pdf
python3 scripts/merge.py tmp/dossie_stripped.pdf tmp/overlay.pdf tmp/dossie-proposta.pdf fonte/box_square.jpg tmp/merged.pdf
python3 scripts/shrink.py tmp/merged.pdf saida/Proposta_Macaix_AVVA.pdf
echo "OK: saida/Proposta_Macaix_AVVA.pdf"
