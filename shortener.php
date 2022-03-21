<?php
//Number of characters to be shown when a random file name is generated
$url_length = 5;
//URL which will be displayed after upload (URL will have the file name appended)
$url = "https://luqas.me/";

if(!isset($_POST['url'])) {
    header("HTTP/1.0 400 Bad Request");
    die("HTTP/1.0 400 Bad Request");
}

$name = generateRandomString();

file_put_contents($name, $_POST['url']);

echo $url.$name;

function generateRandomString() {
        global $url_length;
    $characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $randomString = '';
    for ($i = 0; $i < $url_length; $i++) {
        $randomString .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomString;
}
?>