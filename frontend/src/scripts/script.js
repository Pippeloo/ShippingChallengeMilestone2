// Get Server ip
const serverIp = location.host;
console.log(serverIp);

// fetch user from API
fetch(`http://${serverIp}/api/user`)
    .then((res) => res.json())
    .then((data) => {
        // display user name
        document.getElementById("user").innerText = data.name;
    });