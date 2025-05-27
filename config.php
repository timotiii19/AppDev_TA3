<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

require_once __DIR__ . '/vendor/autoload.php'; // load Composer autoload

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

// Now you can access your keys safely:
$openaiKey = $_ENV['OPENAI_API_KEY'];
$huggingfaceToken = $_ENV['HUGGINGFACE_TOKEN'];



$host = 'localhost';  
$dbname = 'expense_db'; 
$username = 'root';  // Change this if you have a different MySQL username
$password = '';  // Change this if you have a MySQL password

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

if (!function_exists('checkAuth')) {
    function checkAuth() {
        if (!isset($_SESSION['user_id'])) {
            header("Location: login.php");
            exit();
        }
    }
}

?>
