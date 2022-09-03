
let medianScore;
let averageScore;

const medianScoreLabel = document.getElementById('median-score');
const averageScoreLabel = document.getElementById('average-score');

fetch('https://sample-groi.el.r.appspot.com/trs/')
    .then(response => {
        if (response.status === 200){
            return response.json();
        }
    })
    .then(data => {
        console.log(data['risk_score'], data['average_risk_score']);
        medianScore = data['median_risk_score'];
        averageScore = data['average_risk_score'];
        medianScoreLabel.textContent = medianScore;
        averageScoreLabel.textContent = averageScore;
    })
    .catch(err => console.log(err));

console.log('Hello Change');

