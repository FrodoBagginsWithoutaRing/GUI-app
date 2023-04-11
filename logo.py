from PIL import Image, ImageTk, ImageDraw
image = Image.new("RGB", (200, 200), "black")
draw = ImageDraw.Draw(image)
draw.line([0, 200, 100, 0],fill="red", width=6)
draw.line([200, 200, 100, 0], fill="blue", width=6)
draw.line([0, 200, 200, 200], fill="pink", width=6)
draw.line([200, 200, 50, 100], fill="purple", width=3)
draw.line([100, 200, 100, 0], fill="purple", width=3)
draw.line([0, 200, 150, 100], fill="purple", width=3)


image.save("HAHA.png")