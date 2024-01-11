<?php
$status = $_POST['status'];
$command = "./RCPi.py $status 2>&1";
$output = shell_exec($command);
?>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=0" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta names="apple-mobile-web-app-status-bar-style" content="black-translucent" />
        <link rel="stylesheet" type="text/css" href="rcpi.css" media="screen" />
        <!-- Choose a 57x57 image for the icon -->
        <link rel="apple-touch-icon" href="rcpi_icon.png" />
    </head>
<body>

<title>RCPi</title>
<form action = "index.php" method = "POST">
<input type = "submit" name ="status" id="Submit" value = "OPEN/CLOSE">
</form>
<txt><pre><?php echo $output; ?></pre></txt>
</body>
</html>

