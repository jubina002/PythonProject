# pip install pikepdf

import pikepdf
pdf = pikepdf.Pdf.open("pm.pdf")
for i in pdf.pages:
    i.Rotate = 180
    pdf.save("Rotatedpdf.pdf")
# To know the total pages of pdf
# print(pdf.pages) 