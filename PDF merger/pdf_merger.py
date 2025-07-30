from pypdf import PdfWriter

merger = PdfWriter()
all_pdf=[]
no_of_pdf=int(input("Enter the number of PDF's you want to merz:"))


for i in range(0,no_of_pdf):
    list_of_pdf=input(f"Enter the name of {i+1} pdf : ")
    all_pdf.append(list_of_pdf)
    


for pdf in all_pdf:
    merger.append(pdf)

merger.write("Brand_new_PDF.pdf")
merger.close()

