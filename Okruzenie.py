from pprint import pprint
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import Image, ImageFilter

# Используем библиотеку numpy
c = np.random.randint(1, 10, size=(4,4))
d = np.random.randint(1, 10, size=(4,4))
print(c)
print(d)
print(c**d)

#Используем библиотеку request

print(f"{'requests':*^30}")
response = requests.get('https://api.spoonacular.com/food/products/22347',
                         params={'apiKey': '92ff0441402543658ecf622434a7e5ef'})
ingredient_list = response.json()['ingredientList']
print('requests: Состав Сникерса >>>')
pprint(ingredient_list)
print()

print(f"{'pandas':*^30}")
students = pd.read_csv("StudentsPerformance.csv")
# print(students.head())
# print(students.tail(3))
print(students.groupby(["gender", "test preparation course"])["writing score"].count())
#students.to_excel("students.xlsx")
print()

print(f"{'matplotlib':*^30}")
plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()

print(f"{'Pillow':*^30}")
filename = "House.jpg"
with Image.open(filename) as img:
    img.load()


try:
    original = Image.open("House.jpg")
except FileNotFoundError:
    print("Файл не найден")

print("Размер изображения:")
print(original.format, original.size, original.mode)

blurred = original.filter(ImageFilter.BLUR)
original.show()
blurred.show()
blurred.save("blurred.png")

image_path = Image.open("blurred.png")
new_image = image_path.resize((1000, 600))
new_image.show()
new_image.save('Size.png')
new_size = Image.open("Size.png")
print(new_size.format, new_size.size, new_size.mode)