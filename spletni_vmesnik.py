import bottle
import os
from program import dodaj_sliko

@bottle.get("/")
def stran():
    return bottle.template("prva_stran.tpl")

@bottle.get("/ni_slika")
def napacen_input():
    return bottle.template("ni_slika.tpl")

@bottle.post("/nalozi_sliko")
def nalozi_sliko():
    ime, form = os.path.splitext(slika.filename)
    if form not in (".png", ".jpg", ".jpeg"):
        return bottle.redirect("/ni_slika")
    

@bottle.route('/static/<style>')
def css(style):
    return bottle.static_file(style, root='./static/')

bottle.run(reloader=True)
