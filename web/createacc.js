var users = require('./models/users');

var accountData = [
    "1 ck1060516",
    "2 ck1060522",
    "3 ck1060755",
    "4 ck1060282",
    "5 ck1060524",
    "6 ck1060525",
    "7 ck1060166",
    "8 ck1061028",
    "9 ck1060526",
    "10 ck1060168",
    "11 ck1060528",
    "12 ck1060529",
    "13 ck1060530",
    "14 ck1060801",
    "15 ck1060642",
    "16 ck1060844",
    "17 ck1060766",
    "18 ck1060535",
    "19 ck1060058",
    "20 ck1060062",
    "21 ck1060538",
    "22 ck1060894",
    "23 ck1060458",
    "24 ck1060540",
    "25 ck1060026",
    "26 ck1060223",
    "27 ck1060148",
    "28 ck1060544",
    "29 ck1060546",
    "30 ck1060580",
    "31 ck1060425",
    "32 ck1060548",
    "33 ck1060549",
    "34 ck1060187",
    "35 ck1060902",
    "36 ck1060395",
    "37 ck1060553",
    "38 ck1060038"
]

accountData.forEach(element => {
    data = element.split(" ");
    randomPass = Math.random().toString(36).slice(-8);
    var newAccount = new users({
        username: data[1],
        password: randomPass,
        no: data[0],
        direction: "",
        steps: "",
    });
    newAccount.save(function(err,acc){
        if (err) console.log(err);
        console.log(acc.no);
    });
});

console.log("Done!")