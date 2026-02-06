from fpdf import FPDF

pdf = FPDF(unit="mm", format=(120, 140))

page_width = pdf.w  # Page width
image_width = 100   # Width
x_position = (page_width - image_width) / 2

user_name = input("Input your name: ")

pdf.add_page()
pdf.set_font("helvetica", style="B", size=20)
pdf.cell(text="CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", x=x_position, y=30, w=image_width)

pdf.set_text_color(255, 255, 255)  # white text
pdf.set_font("helvetica", size=14)
pdf.cell(text=f"{user_name} Harvard took CS50", h=110, center=True)

pdf.output("tuto1.pdf")