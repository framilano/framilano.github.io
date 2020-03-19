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
    <h1>Grafici Covid-19 in Italia</h1>
    <div style="width:100%;text-align: center;font-size: 300%;"><a href="https://github.com/pcm-dpc/COVID-19">Fonte</a></div>
</head>

<body class="darkbody">

    <div class="container"><img src="assets/deathconhealperdayline.png">

        <div class="text-block"><?php include "statspage.html" ?></div>
    </div>

    <div style="margin-top:12%"><img border="1px" src="assets/posneglatestpie.png"></div>


    <div><img src="assets/posneglatestbar.png"></div>

    </table>
</body>

</html>