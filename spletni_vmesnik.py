import bottle

@bottle.get("/")
def stran():
    return bottle.template("stran.tpl")

bottle.run(debug=True, reloader=True)