import pikepdf
old_pdf = pikepdf.Pdf.open("pm.pdf")

# reverse Pdf
# old_pdf.pages.reverse()
# old_pdf.save("reverse.pdf")

#Replace Pdf
old_pdf.pages[3] = old_pdf.pages[0]
old_pdf.save("Replace.pdf")

#Del pdf
#index starts from 0
del old_pdf.pages[1:3] 
old_pdf.save("delete.pdf")