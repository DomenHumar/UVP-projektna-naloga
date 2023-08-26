<!DOCTYPE html>
<html>
    <head>
        <title>Povprečna barva slike</title>
        <link href="stil.css" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    </head>
    <body>
        <h1>Povprečna barva slike</h1>
        <div id="target">
            Odložite sliko tukaj (ali kliknite in jo izberite)
            <input type="file" id="upload" multiple />
        </div>
        <div id="footer"></div>
        <py-script src="./program.py"></py-script>
    </body>
</html>
