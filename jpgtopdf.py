from fpdf import FPDF
import os

# creating pdf
pdf = FPDF(orientation="P", unit="mm", format="letter")
images = []
for filename in os.listdir(img_path):
    images.append(filename)
for jpg in images:
    if jpg.endswith(".jpg"):
        steven = images.index(jpg)
        pdf.add_page()
        pdf.image("/Users/nelsonparra/Desktop/05232022_FE_A_RGI_2/"+jpg,h=50,w=150)
    else:
        print("did not work")
pdf.output("convertedImages.pdf")






# for filename in os.listdir(img_path):
#         pdf.add_page()
#         print(filename)
#         pdf.image(filename)
        # pdf.image(filename)
        # pdf.output(filename+".pdf")
        # print("we made it")
        # print("Successfully made pdf file")
        # put file in folder
        # file = open(pdf_path, "wb")
        # file.write(pdf)
        # file.close()
        # print("Successfully store pdf")
