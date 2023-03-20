from PIL import Image

n = input()
im = Image.open('./resources/icons/' + n)
size = im.size
if size[0] > size[1]:
    im = im.crop(((size[0] - size[1]) // 2, 0, (size[0] - size[1]) // 2 + size[1], size[1]))
elif size[1] > size[0]:
    im = im.crop((0, (size[1] - size[0]) // 2, size[0], (size[1] - size[0]) // 2 + size[0]))
im = im.resize((600, 600))
im.save('./resources/icons/' + n[1:])