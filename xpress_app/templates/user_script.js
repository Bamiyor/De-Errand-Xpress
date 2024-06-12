// Function to handle user registration
function registerUser(event) {
    event.preventDefault(); // Prevent form submission
  
    const formData = new FormData(event.target);
    const userData = Object.fromEntries(formData.entries());
  
    fetch('/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Registration successful:', data);
      // Redirect to login page or handle success as needed
    })
    .catch(error => console.error('Error:', error));
  }
  
  // Function to handle user login
  function loginUser(event) {
    event.preventDefault(); // Prevent form submission
  
    const formData = new FormData(event.target);
    const userData = Object.fromEntries(formData.entries());
  
    // Implement login logic here
    // You can make a POST request to the appropriate API endpoint for authentication
    // and handle the response accordingly (e.g., setting a session cookie, redirecting to a dashboard, etc.)
    console.log('Login data:', userData);
  }