<?php
if(!isset($_GET['jam'])) {
    header("HTTP/1.0 400 Bad Request");
    die("HTTP/1.0 400 Bad Request");
}
if (!file_exists($_GET['jam'])) {
    header("HTTP/1.0 400 Bad Request");
    die("HTTP/1.0 400 Bad Request");
}
header("Location: ".file_get_contents($_GET['jam']));
die();
?>