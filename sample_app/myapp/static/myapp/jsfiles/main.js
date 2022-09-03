
let score;
const scoreLabel = document.getElementById('score');

fetch('https://sample-groi.el.r.appspot.com/trs/')
    .then(response => {
        if (response.status === 200){
            return response.json();
        }
    })
    .then(data => {
        console.log(data['risk score']);
        score = data['risk score'];
        scoreLabel.textContent = score;
    })
    .catch(err => console.log(err));

console.log('Hello Change');

