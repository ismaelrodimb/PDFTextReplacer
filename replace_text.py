import fitz  # PyMuPDF
import os

input_dir = r"C:\Users\UX425\Desktop\scriptClase\input"
output_dir = r"C:\Users\UX425\Desktop\scriptClase\output"

font_path = r"C:\Users\UX425\Desktop\scriptClase\font\Figtree-Light.ttf"  # Asegúrate de que esta ruta es correcta y que la fuente existe

os.makedirs(output_dir, exist_ok=True)

def replace_text_in_pdf(input_path, output_path, search_text, replace_text, font_path):
    doc = fitz.open(input_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text_instances = page.search_for(search_text)

        for inst in text_instances:
            spans = page.get_text("dict", clip=inst).get('blocks', [])[0].get('lines', [])[0].get('spans', [])
            if spans:
                span = spans[0]

                page.add_redact_annot(inst)
                page.apply_redactions()

                vertical_adjustment = 7  
                horizontal_adjustment = 3 


                page.insert_text(
                    (inst.x0 + horizontal_adjustment, inst.y0 + vertical_adjustment), 
                    replace_text,
                    fontname="Figtree-Light",
                    fontfile=font_path,
                    fontsize=span['size'], 
                    color=span['color'], 
                    render_mode=0
                )


    doc.save(output_path)
    doc.close()

for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        replace_text_in_pdf(input_path, output_path, "Class 2", "Class 1", font_path)

print("Modificación completada y guardada en la carpeta de salida.")
