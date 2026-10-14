import sys, io, pikepdf
from PIL import Image
pdf = pikepdf.open(sys.argv[1])
n=0
for page in pdf.pages:
    for name, raw in list(page.images.items()):
        try:
            pim = pikepdf.PdfImage(raw)
            if raw.get('/SMask') is not None or pim.width*pim.height < 400*400: continue
            img = pim.as_pil_image().convert('RGB')
            img.thumbnail((1400,1400))
            b = io.BytesIO(); img.save(b,'JPEG',quality=72,optimize=True)
            raw.write(b.getvalue(), filter=pikepdf.Name.DCTDecode)
            raw.Width, raw.Height = img.size
            raw.ColorSpace = pikepdf.Name.DeviceRGB; raw.BitsPerComponent = 8
            for k in ('/DecodeParms','/Decode'):
                if k in raw: del raw[k]
            n+=1
        except Exception as e: print('skip',e)
pdf.remove_unreferenced_resources()
pdf.save(sys.argv[2], compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate, linearize=True)
print('recompressed',n)
