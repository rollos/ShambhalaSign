from PIL import Image


file_path = "/home/pi/ShambhalaSign/images/gifs/eye.gif"

im = Image.open(file_path)
size = (64, 16)

if im.is_animated():



bg = Image.new('RGB', size, color='black')

bg.paste(
    im, (int((size[0] - im.size[0]) / 2), int((size[1] - im.size[1]) / 2))
)

bg.save(file_path)
