import bottle
import os
import io
from program import najdi_RGB

@bottle.get("/")
def stran():
    return bottle.template("prva_stran.tpl")

@bottle.get("/ni_slika")
def napacen_input():
    return bottle.template("ni_slika.tpl")

@bottle.post('/je_slika')
def nalozi_sliko():
    datoteka = bottle.request.files["slika"]
    # Preverimo če je podana datoteka slika (tako da pogledamo njen format)
    ime, form = os.path.splitext(datoteka.filename)
    if form not in (".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"):
        return bottle.redirect("/ni_slika")
    else:
        # Pillow ne deluje na FileUpload, ki nam ga poda Bottle zato rabimo io
        slika = io.BytesIO()
        datoteka.save(slika)
        RGB = najdi_RGB(slika)
        RGB_str='rgb({}, {}, {})'.format(RGB[0], RGB[1], RGB[2])
        HEX_str = '#{:02x}{:02x}{:02x}'.format(RGB[0], RGB[1], RGB[2])
        return bottle.template(
            "je_slika.tpl",
            RGB_str=RGB_str,
            HEX_str=HEX_str,
            slika=slika
        )

@bottle.route('/static/<style>')
def css(style):
    return bottle.static_file(style, root='./static/')

bottle.run(reloader=True, debug=True)
