import pikepdf

old_pdf = pikepdf.Pdf.open("pm.pdf")
for n, page_content in enumerate(old_pdf.pages):
    new_pdf = pikepdf.Pdf.new()
    new_pdf.pages.append(page_content)
    name = "test"+str(n)+".pdf"
    new_pdf.save(name)
