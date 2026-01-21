from langdetect import detect


text_1 ="This is sample"


text_2 ="цей текст містить українські літери. він також досить довгий"

text_3 ="Artykuł naukowy"

print(detect(text_1))
print(detect(text_2))
print(detect(text_3))



