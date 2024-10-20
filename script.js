// Toggle the navigation menu on mobile
document.querySelector('.nav-toggle').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('active');
});


// Example pseudocode for your backend (Node.js or similar)
app.get('/auth/telegram/callback', (req, res) => {
    const { id, first_name, last_name, username, photo_url } = req.query;

    // Validate the data here
    // Check the signature, ensuring it comes from Telegram

    // If valid, log the user in
    // Create a session or token for the user
    
    // You can also store user info in your database if needed

    // Redirect to a success page
    res.redirect('/success');
});