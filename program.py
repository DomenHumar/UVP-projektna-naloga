from PIL import Image

def dodaj_sliko(file):
    element = '<div class="row">' \
              '<div class="cell image">' \
              '  <slika />' \
              '</div>' \
              '<div class="cell color">' \
              '  <div class="box"></div>' \
              '  <ul>' \
              '    <li class="rgb"></li>' \
              '    <li class="hex"></li>' \
              '  </ul>' \
              '</div>' \
              '</div>'
    slika = PIL.Image.open(file)
    RGB = najdi_povprecno_barvo(slika)
    RGB_str = 'rgb({}, {}, {})'.format(RGB[0], RGB[1], RGB[2])
    HEX_str = '#{0:02x}{1:02x}{2:02x}'.format(RGB[0], RGB[1], RGB[2])
    box = '<div class="box" style="background-color: {}"></div>'.format(RGB_str)
    RGB_li = '<li class="rgb">{}</li>'.format(RGB_str)
    HEX_li = '<li class="hex">{}</li>'.format(HEX_str)
    element = element.replace('<div class="box"></div>', box)
    element = element.replace('<li class="rgb"></li>', RGB_li)
    element = element.replace('<li class="hex"></li>', HEX_li)
    return element

def najdi_povprecno_barvo(slika):
    RGB_povprecne_piksle = []
    for k in range(3):
        sumacija = 0
        for j in range(slika.size[1]):
            for i in range(slika.size[0]):
                sumacija += piksle[i,j][k]
            povprecje = round(sumacija / (slika.size[0] * slika.size[1]))
        RGB_povprecne_piksle.append(povprecje)
    return RGB_povprecne_piksle
