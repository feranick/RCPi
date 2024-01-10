<?php
$status = $_POST['status'];

//$command = "sudo python3 piRC_manual.cpython-34.pyc $status 2>&1";y
$command = "./RCPi.py $status 2>&1";
$output = shell_exec($command);

print "
<html>
<title> RCPico - no file version</title>
<body>
<h2>Requesting: $status</h2>
<h3>Result: $output</h3>
<script>
console.log('PHP-input:" .$status. "');
console.log('PHP-output:" .$output. "');
</script>
</body>
</html>
";

include('buttons.html');
?>
