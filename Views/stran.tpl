<!DOCTYPE html>
<html>
    <head>
        <title>Povprečna barva slike</title>
        <link rel="stylesheet" type="text/css" href="stil.css"/>
    </head>
    <body>
        <h1>Povprečna barva slike</h1>
        <div id="target">
            Naložite sliko tukaj
        <form method="POST" action="/upload enctype="multipart/form-data">
        <input id="file" name="file" type="file" />
        <button>Upload</button>
        </form>
        </div>
        <div id="images"></div>
    </body>
</html>
