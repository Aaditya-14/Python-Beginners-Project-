import qrcode

data= input("Enter what data do you want to add: ")
File_name=input("What should i put the name of the file (must be in PNG): ")
qr= qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)

image=qr.make_image(fill_colour="green" ,back_color="red")

image.save(File_name)