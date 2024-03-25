document.addEventListener('DOMContentLoaded', function () {
  const emailInput = document.getElementById('username');
  const emailError = document.getElementById('email-error');

  // Event listener to check email existence on input change
  emailInput.addEventListener('input', function () {
    const email = emailInput.value.trim();
    // Ajax request to check if email already exists (replace this with your backend logic)
    // Example: You can send a request to your Flask backend to check if the email exists
    // If email exists, display error message
    const emailExists = false; // Replace with your logic
    if (emailExists) {
      emailError.textContent = 'Email already exists';
    } else {
      emailError.textContent = ''; // Clear error message if email doesn't exist
    }
  });
});


