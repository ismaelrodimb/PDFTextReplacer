# PDFTextReplacer

PDFTextReplacer es una herramienta en Python para buscar y reemplazar texto en archivos PDF, permitiendo ajustes en la posición y tipografía del texto reemplazado. Es especialmente útil para modificaciones rápidas y específicas de documentos PDF.

## Contexto

El script nace de la necesidad de cambiar de forma masiva una gran cantidad de fichas técnicas en las cuales había un campo erróneo. De esta manera, se reduce el tiempo del proceso de regeneración de las fichas de varias horas a escasos segundos.

## Características

- Reemplaza texto específico en archivos PDF.
- Ajusta la posición vertical y horizontal del texto reemplazado.
- Utiliza una fuente personalizada para mantener la consistencia en la tipografía.

## Requisitos

- Python 3.x
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) - Biblioteca para manipulación de PDFs.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/ismaelrodimb/PDFTextReplacer.git
   cd PDFTextReplacer
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```
   python -m venv venv
   source venv/bin/activate   # En Windows usa: venv\Scripts\activate
   ```

3. Instala las dependencias listadas en requirements.txt:

   ```
   pip install -r requirements.txt
   ```

4. Configura las rutas:

- Asegúrate de que tus archivos PDF de entrada estén en la carpeta input.
- Coloca la fuente Figtree-Light.ttf o la que necesites en formato ttf en la carpeta font y actualiza la ruta en el script si es necesario.

5. Ejecuta el script para reemplazar texto en los PDFs:

   ```
   python replace_text.py

   ```

## Configuración

Los archivos de input son una demo utilizada en un entorno real de producción, son completamente modificables por aquellos documentos que necesites modificar.
Puedes ajustar las siguientes variables en replace_text.py para personalizar la ejecución:

- `vertical_adjustment` Ajuste vertical en puntos.
- `horizontal_adjustment` Ajuste horizontal en puntos.
- `font_path` Ruta al archivo de la fuente personalizada.
- `Class 2` Modifica el texto 'Class 2' por el texto que quieras que rastree y modifique
- `Class 1` Modifica el texto 'Class 1' por el texto que quieres que sustituya a 'Class 2'

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## Sígueme en redes sociales

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ismael--Rodriguez-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ismael-rodriguez-imbernon/)
