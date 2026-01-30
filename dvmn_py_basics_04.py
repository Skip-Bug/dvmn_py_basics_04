from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()

coordinates_red_1 = (50, 0, red.width, red.height)
coordinates_red_2 = (25, 0, red.width-25, red.height)
cropped_red_1 = red.crop(coordinates_red_1)
cropped_red_2 = red.crop(coordinates_red_2)

red_b = Image.blend(cropped_red_1, cropped_red_2, 0.5)

coordinates_blue_1 = (25, 0, blue.width-25, blue.height)
coordinates_blue_2 = (0, 0, blue.width-50, blue.height)
cropped_blue_1 = blue.crop(coordinates_blue_1)
cropped_blue_2 = blue.crop(coordinates_blue_2)

blue_b = Image.blend(cropped_blue_1, cropped_blue_2, 0.6)
coordinates_green = (25, 0, green.width-25, green.height)
cropped_green = green.crop(coordinates_green)

channels = (red_b, cropped_green, blue_b)
image_mod = Image.merge("RGB", channels)
image_mod.save("modific.jpg")

image_mod.thumbnail((80, 80))
image_mod.save("ava.jpg")
print("Аватарка готова")