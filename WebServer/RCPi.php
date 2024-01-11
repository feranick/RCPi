<?php
$status = $_POST['status'];
$command = "./RCPi.py $status 2>&1";
$output = shell_exec($command);
include('index.html');
print "<txt><pre>" .$output. "</pre></txt>";
?>

