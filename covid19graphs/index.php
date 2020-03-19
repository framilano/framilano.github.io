<?php
ini_set("display_errors", "On");
ini_set("error_reporting", E_ALL);
$statsfile = fopen("assets/stats.txt", "r");
$topdeath = 0;
$topheal = 0;
$topcont = 0;
$totdeath = 0;
$totheal = 0;
$totcont = 0;
$name = "";
$value = 0;
fscanf($statsfile, "%s %d", $name, $topdeath);
fscanf($statsfile, "%s %d", $name, $topheal);
fscanf($statsfile, "%s %d", $name, $topcont);
fscanf($statsfile, "%s %d", $name, $totdeath);
fscanf($statsfile, "%s %d", $name, $totheal);
fscanf($statsfile, "%s %d", $name, $totcont);
fclose($statsfile);
?>


<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="../css/style.css" />
    <div style="width: 100%;text-align: right;">
        <button class="buttondark" id="themebutton" onclick="changetheme(document.getElementById('themebutton').innerHTML)">☀️</button>
    </div>
    <h1 style="font-size:400%">Grafici Covid-19 in Italia</h1>
    <div style="width:100%;text-align: center;font-size: 300%;"><a href="https://github.com/pcm-dpc/COVID-19">Fonte</a></div>
</head>

<body class="darkbody">



    <div style="margin-top:4%; text-align:center"><img class="normal" src="assets/deathconhealperdayline.png"></div>
    <div><?php include "statspage.html" ?></div>

    <div style="margin-top:12%; text-align:center"><img class="normal" border="1px" src="assets/posneglatestpie.png"></div>


    <div><img class="normal" style="margin-top:12%; text-align:center" src="assets/posneglatestbar.png"></div>

    </table>
</body>

</html>

<script>
    function changetheme(icon) {
        switch (icon) {
            case '☀️':
                document.getElementsByTagName('body')[0].className = 'lightbody'
                document.getElementById('themebutton').innerHTML = '🌙'
                document.getElementById('themebutton').className = 'buttonlight'
                collection = document.getElementsByTagName('img')
                for (const item of collection) {
                    item.className = 'inverted'
                }
                break;
            case '🌙':
                document.getElementsByTagName('body')[0].className = 'darkbody'
                document.getElementById('themebutton').innerHTML = '☀️'
                document.getElementById('themebutton').className = 'buttondark'
                collection = document.getElementsByTagName('img')
                for (const item of collection) {
                    item.className = 'normal'
                }
                break;
        }
    }
</script>