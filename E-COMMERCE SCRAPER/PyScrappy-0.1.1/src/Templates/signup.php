<?php
// Start session
session_start();

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate form data
    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    $confirm_password = $_POST["confirm_password"];

    // Validate input (example: check if username and password are not empty)
    if (empty($username) || empty($email) || empty($password) || empty($confirm_password)) {
        echo "All fields are required.";
        exit();
    }

    // Example validation (replace with your actual validation logic)
    if ($password !== $confirm_password) {
        echo "Passwords do not match. Please try again.";
        exit();
    }

    // Hash password (you should use a secure hashing algorithm like bcrypt)
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Save user data to database (replace with your database logic)
    // Example: Insert user data into a users table
    // Note: This is just an example and not secure. Use prepared statements or an ORM to prevent SQL injection
    $servername = "localhost";
    $db_username = "your_db_username";
    $db_password = "your_db_password";
    $dbname = "your_db_name";

    // Create connection
    $conn = new mysqli($servername, $db_username, $db_password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Insert user data into database
    $sql = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$hashed_password')";

    if ($conn->query($sql) === TRUE) {
        echo "User registered successfully.";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Close connection
    $conn->close();
}
?>
