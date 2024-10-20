// Toggle the navigation menu on mobile
document.querySelector('.nav-toggle').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('active');
});


const crypto = require('crypto');

// Telegram sends an object with user data
function checkTelegramAuth(data, botToken) {
    const secret = crypto.createHash('sha256').update(botToken).digest();
    const checkString = Object.keys(data)
        .filter(key => key !== 'hash')
        .sort()
        .map(key => `${key}=${data[key]}`)
        .join('\n');
    
    const hmac = crypto.createHmac('sha256', secret).update(checkString).digest('hex');
    return hmac === data.hash;
}

// Example usage
const userData = { /* User data from Telegram */ };
const botToken = 'YOUR_BOT_TOKEN'; // 7642252782:AAGUVwNlrJIUK1-aoz0Sq3ElACpyTjGzSPE 

if (checkTelegramAuth(userData, botToken)) {
    console.log('User is authenticated!');
} else {
    console.log('Authentication failed.');
}
