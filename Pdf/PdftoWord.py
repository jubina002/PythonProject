# pip install pdf2docx
# pip install docx2pdf

from docx2pdf import convert
convert("new.docx", "new_pdf.pdf")

# from pdf2docx import Converter
# old_pdf = "A.pdf"
# new_docx = "new.docx"
# obj = Converter(old_pdf)
# obj.convert(new_docx)
# obj.close()