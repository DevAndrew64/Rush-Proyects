from pathlib import Path

""""
Autor: Jhon Ponton
Inspiracion: Codigo Espinoza
Proyecto numero 1 de 50

Este programa organiza tus PDFs en base a la ruta de una carpeta que le proporciones,
por ejemplo la carpeta de descargas
"""

descargas = Path.home() / "Descargas"
archivos_pdf = list(descargas.glob("*.pdf"))

# Aqui se crea una carpeta para documentos en caso tal que no exista aun
carpeta_docs = Path.home() / "Documentos" / "PDFs"
carpeta_docs.mkdir(parents=True, exist_ok=True)

# Mover todos los PDFs a la carpeta nueva
for pdf in archivos_pdf:
    destino = carpeta_docs / pdf.name
    pdf.rename(destino)
    print(f"Movido: {pdf.name}")