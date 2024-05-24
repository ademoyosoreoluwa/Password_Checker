# Watermark PDF

import PyPDF2

template_path = '/Users/eagleseyes/Desktop/ML/Project/super.pdf'
watermark_path = '/Users/eagleseyes/Desktop/ML/Project/wtr.pdf'
output_path = '/Users/eagleseyes/Desktop/ML/Project/watermarked_output.pdf'

def water_mark():
    with open(template_path, 'rb') as template_file, open(watermark_path, 'rb') as watermark_file:
        template = PyPDF2.PdfReader(template_file)
        watermark = PyPDF2.PdfReader(watermark_file)
        output = PyPDF2.PdfWriter()

        watermark_page = watermark.pages[0]

        for i in range(len(template.pages)):
            page = template.pages[i]
            page.merge_page(watermark_page)
            output.add_page(page)

        with open(output_path, 'wb') as output_file:
            output.write(output_file)

            print(f"Watermarked PDF saved as: watermarked_output.pdf")

water_mark()