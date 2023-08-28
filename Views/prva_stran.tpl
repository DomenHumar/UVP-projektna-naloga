<!DOCTYPE html>
<html>
    <head>
        <title>Povprečna barva slike</title>
        <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700" rel="stylesheet" type="text/css">
        <link type="text/css" href="/static/style.css" rel="stylesheet"> 
        <meta name="viewport" content="width=device-width,initial-scale=1" />
    </head>
    <body>
        <h1>Povprečna barva slike</h1>
        <div id="target">
        <form method="POST" action="/nalozi_sliko">
           <input type="file" id="slika">
           <button id="select">Naložite sliko</button>
           <span class="name"></span>
        </form>
        </div>
    </body>
</html>
