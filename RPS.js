let wins = 0;
let losses = 0;
let d = false

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log("Welcome to rock paper scissors. For now, it's just random,\nbut " +
    "I may add an algorithm later. Type 'd' when done.\n" +
    "Rock(0), Paper(1), Scissors(2)")

let move_list = ['R', 'P', 'S']

while (d === false) {

    let cpu = move_list[Math.floor(Math.random() * move_list.length)];

    let usr = 2

    if (usr === 1) {
        console.log("It's a tie!")
    }
}