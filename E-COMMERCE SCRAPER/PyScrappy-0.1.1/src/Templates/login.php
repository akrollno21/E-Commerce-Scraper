<?php
// Start session
session_start();

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate username and password (replace this with your validation logic)
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Example validation (replace with your actual validation logic)
    if ($username === "admin" && $password === "password") {
        // Set session variables (replace with your actual session data)
        $_SESSION["username"] = $username;

        // Redirect to home page or dashboard
        header("Location: home.php");
        exit();
    } else {
        // Display error message or redirect to login page with error flag
        echo "Invalid username or password. Please try again.";
    }
}
?>
