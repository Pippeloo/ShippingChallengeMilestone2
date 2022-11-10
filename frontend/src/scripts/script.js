// Get Server ip
const serverIp = location.host;

// fetch user from API
fetch(`http://${serverIp}/api`)
    .then((res) => res.json())
    .then((data) => {
        // display user name
        document.getElementById("user").innerText = data.user;
    });