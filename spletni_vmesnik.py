import bottle

@bottle.get("/")
def stran():
    return bottle.template("prva_stran.tpl")

@bottle.post("/")
def nalozi_sliko():
    pass

@bottle.route('/static/<style>')
def css(style):
    return bottle.static_file(style, root='./static/')

bottle.run(reloader=True)
