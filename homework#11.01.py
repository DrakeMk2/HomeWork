import requests
import pandas as pd
from PIL import Image

# Библиотека requests.

# image = requests.get(
#     'https://static.wikia.nocookie.net/warhammer40k/images/0/04/Adeptus_mechanicus_by_cribs-d4b4afs.jpg/revision/latest?cb=20111026165711')
# with open('test_image.jpg', 'wb') as img:
#     img.write(image.content)
# image = requests.options('https://warhammer40k.fandom.com/wiki/Adeptus_Mechanicus')
# print(image.headers)

# Библиотека pandas.

# fam = pd.read_csv('test_pandas.txt')
# print(fam)

# Библиотека pillow.

# test_img = 'test_image.jpg'
# with Image.open(test_img) as img:
#     img.load()
# print(img.size)
# mirror_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# mirror_img.save('test_img_fliped.jpg')
# resize_img = img.resize((600, 960))
# resize_img.save('test_img_resized.jpg')
