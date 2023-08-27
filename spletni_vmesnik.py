import bottle
from program import dodaj_sliko

@bottle.get("/")
def stran():
    return bottle.template("stran.tpl")

@bottle.post("/")
def nalozi_sliko():

bottle.run(debug=True, reloader=True)