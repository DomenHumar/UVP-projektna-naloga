from PIL import Image

def najdi_RGB(file):
    slika = Image.open(file)
    RGB = []
    piksle = slika.load()
    for k in range(3):
        sumacija = 0
        for j in range(slika.size[1]):
            for i in range(slika.size[0]):
                sumacija += piksle[i,j][k]
            povprecje = round(sumacija / (slika.size[0] * slika.size[1]))
        RGB.append(povprecje)
    return RGB
