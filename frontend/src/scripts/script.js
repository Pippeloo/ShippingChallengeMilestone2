// Get Server ip
const serverIp = location.host;
const nginx_hostname = window.location.hostname;

document.getElementById("nginx_hostname").innerText = nginx_hostname;

// fetch user from API
fetch(`http://${serverIp}/api/user`)
    .then((res) => res.json())
    .then((data) => {
        // display user name
        document.getElementById("user").innerText = data.name;
    });

// fetch hostname from API
fetch(`http://${serverIp}/api/hostname`)
    .then((res) => res.json())
    .then((data) => {
        // display hostname
        document.getElementById("api_hostname").innerText = data.hostname;
    }
    );