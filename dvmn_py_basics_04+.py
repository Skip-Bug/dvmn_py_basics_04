from PIL import Image
import os
name_image = input("Название картинки: ") 
image = Image.open(name_image+".jpg")
image = image.convert('RGB')
image_rgb = image 
image_rgb.save("image_rgb.jpg")
image = Image.open ("image_rgb.jpg")
red, green, blue = image.split()
red.save("red.jpg")
green.save("geen.jpg")
blue.save("blue.jpg")
coordinates_red_1 = (50, 0, red.width, red.height)
coordinates_red_2 = (25, 0, red.width-25, red.height)
cropped_red_1 = red.crop(coordinates_red_1)
cropped_red_2 = red.crop(coordinates_red_2)
cropped_red_1.save("red_1.jpg")
cropped_red_2.save("red_2.jpg")
red_b = Image.blend(cropped_red_1, cropped_red_2, 0.5)
red_b.save("red_b.jpg")
coordinates_blue_1 = (25, 0, blue.width-25, blue.height)
coordinates_blue_2 = (0, 0, blue.width-50, blue.height)
cropped_blue_1 = blue.crop(coordinates_blue_1)
cropped_blue_2 = blue.crop(coordinates_blue_2)
cropped_blue_1.save("blue_1.jpg")
cropped_blue_2.save("blue_2.jpg")
blue_b = Image.blend(cropped_blue_1, cropped_blue_2, 0.6)
blue_b.save("blue_b.jpg")
coordinates_green = (25, 0, red.width-25, red.height)
cropped_green = green.crop(coordinates_green)
cropped_green.save("green.jpg")
image_m = Image.merge("RGB", (red_b, cropped_green, blue_b))
image_m.thumbnail((80,80))
image_m.save ("ava.jpg")
files_to_delete = ["image_rgb.jpg", "red.jpg", "geen.jpg",
"blue.jpg","red_1.jpg","red_2.jpg", "red_b.jpg","blue_1.jpg",
"blue_2.jpg", "blue_b.jpg","green.jpg"]
for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"Удален файл: {file}")
    else:
        print(f"Файл не найден: {file}")