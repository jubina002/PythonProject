# pip install pikepdf
from pikepdf import Pdf
from glob import glob

new_pdf = Pdf.new()

for files in glob("*.pdf"):
    old_pdf = Pdf.open(files)
    new_pdf.pages.extend(old_pdf.pages)
new_pdf.save("Final.pdf")
