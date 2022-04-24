<?php

error_reporting(0);

$output = null;

if (isset($_GET['text']) && is_string($_GET['text'])) {
  $text = $_GET['text'];
  $output = shell_exec("echo ${text} | /usr/bin/figlet");
} else {
  highlight_file(__FILE__);
  exit;
}

?>

<!DOCTYPE html>
<html>
  <head>
    <title>FaaS</title>
  </head>
  <body>
    <pre><?= htmlspecialchars($output) ?></pre>
  </body>
</html>
