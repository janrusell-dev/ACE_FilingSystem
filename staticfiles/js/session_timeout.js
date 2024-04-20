// session_timeout.js

document.addEventListener("DOMContentLoaded", function () {
    // Function to show a session timeout prompt
    function showSessionTimeoutPrompt() {
        alert("Your session has expired due to inactivity. Please log in again.");
        window.location.href = "/login/";  // Replace "/login/" with your actual login URL
    }

    // Set a timeout to show the prompt after 15 minutes (adjust as needed)
    const sessionTimeout = 15 * 60 * 1000; // 15 minutes in milliseconds
    setTimeout(showSessionTimeoutPrompt, sessionTimeout);
});
