% rebase("osnova.tpl")

<div class="row">
    <div class="cell image">
        <slika_html />
    </div>
    <div class="cell color">
        <div class="box" style="background-color:{{RGB_str}}"></div>
        <ul>
            <li class="RGB">{{RGB_str}}</li>
            <li class="HEX">{{HEX_str}}</li>
        </ul>
    </div>
</div>