function getUserProfile() {
    const username = document.getElementById('username').value;
    fetch(`http://127.0.0.1:5001/api/user/${username}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('userProfile').innerText = JSON.stringify(data, null, 2);
        });
}

function getRecommendations() {
    const username = document.getElementById('username').value;
    fetch(`http://127.0.0.1:5001/api/recommend/${username}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('recommendations').innerText = JSON.stringify(data, null, 2);
        });
}
