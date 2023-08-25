from PIL import Image

slika = Image.open("C:/Users/uporabnik/Desktop/3bovka.png")
piksle = slika.load()

RGB_povprecne_piksle = []
for k in range(3):
    sumacija = 0
    for j in range(slika.size[1]):
        for i in range(slika.size[0]):
            sumacija += piksle[i,j][k]
        povprecje = round(sumacija / (slika.size[0] * slika.size[1]))
    RGB_povprecne_piksle.append(povprecje)

print(RGB_povprecne_piksle)

def RGB_v_HEX(RGB):
    return '#{:02x}{:02x}{:02x}'.format(RGB[0], RGB[1], RGB[2])

print(RGB_v_HEX(RGB_povprecne_piksle))