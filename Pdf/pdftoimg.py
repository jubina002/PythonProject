# pip install pdf2image
# https://github.com/oschwartz10612/poppler-windows/releases/
# download Release-24.02.0-0.zip 

from pdf2image import convert_from_path
old_pdf = convert_from_path("A.pdf",
                            poppler_path=r"C:\Users\OneDrive\Desktop\PP\Pdf\Release-24.02.0-0.zip\poppler-24.02.0\Library\bin")
for i in range(len(old_pdf)):
    old_pdf[i].save("New"+str(i)+".jpg","JPEG")

