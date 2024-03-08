import pikepdf
old_pdf = pikepdf.Pdf.open("pm.pdf")
no_extr = pikepdf.Permissions(extract=False)
old_pdf.save("EncryptedPdf.pdf", 
             encryption= pikepdf.Encryption(user="noneofyobusiness",
                                            owner="me",
                                            allow=no_extr))

