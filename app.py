import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk, ImageDraw
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#LOGO
logo = Image.open('HAHA.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo  #nešešeri
logo_label.grid(column=1, row=0)

#intstructions
instructions = tk.Label(root, text="Ta šak si vyber PDF súbor", font='Raleway')
instructions.grid(columnspan=3,column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Výber suboru", filetype=[("Pdf file","*.pdf")])
    if file == True:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1,row=3)

        browse_text.set("Prehľadavac")


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Prehľadavac")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)




root.mainloop()