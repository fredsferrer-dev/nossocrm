"""Aplica as sobreposições de texto no dossiê, troca a foto da página 7 e monta a proposta final.

Uso: python merge.py <dossie_stripped.pdf> <overlay.pdf> <dossie-proposta.pdf> <foto_p7.jpg> <saida.pdf>
"""
import sys, pikepdf

stripped, overlay, proposta, foto, saida = sys.argv[1:6]
d = pikepdf.open(stripped); ov = pikepdf.open(overlay); pr = pikepdf.open(proposta)
# ordem das páginas em overlay.html: p3, p5, p7, p8, p6, p4 (índices do dossiê: 2, 4, 6, 7, 5, 3)
for idx, oi in zip((2, 4, 6, 7, 5, 3), range(6)):
    d.pages[idx].add_overlay(ov.pages[oi])
xo = d.pages[6].Resources.XObject['/X91']
for k in ('/SMask', '/DecodeParms', '/Decode', '/Intent'):
    if k in xo:
        del xo[k]
from PIL import Image
w, h = Image.open(foto).size
xo.write(open(foto, 'rb').read(), filter=pikepdf.Name.DCTDecode)
xo.Width, xo.Height = w, h
xo.ColorSpace = pikepdf.Name.DeviceRGB; xo.BitsPerComponent = 8
out = pikepdf.new()
out.pages.append(pr.pages[0])                 # capa nova
for i in range(1, 8): out.pages.append(d.pages[i])  # dossiê 2–8
for pg in list(pr.pages)[1:]: out.pages.append(pg)  # páginas da proposta
out.pages.append(d.pages[9])                  # fechamento do dossiê
out.save(saida)
