

let request = new XMLHttpRequest();
let scoreboard = []
request.open("GET", "Replace this string with a static Ngrok URL from PyNgrok dashboard.")
request.send();
request.onload = () => {
    scoreboard = request.responseText;
    let result = JSON.parse(scoreboard)
    console.log(result)
    console.log("The score is: ", scoreboard);
    document.getElementById("scores").innerHTML = result;
}





