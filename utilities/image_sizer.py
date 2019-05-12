from PIL import Image


file_path = "/home/pi/ShambhalaSign/images/owl.png"

im = Image.open(file_path)

size = (64, 16)

bg = Image.new('RGB', size, color='black')

bg.paste(
    im, (int((size[0] - im.size[0]) / 2), int((size[1] - im.size[1]) / 2))
)

bg.save(file_path)
