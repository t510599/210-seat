var nodemailer = require('nodemailer');
var users = require('./models/users');
var sleep = require('sleep')

var transporter = nodemailer.createTransport({
    host: '',
    port: 465,
    secure: true,
    auth: {
        user: "", // generated ethereal user
        pass: "" // generated ethereal password
    }
});

var options = {
    from: '',
    subject: '210選座位登入系統 帳號密碼通知信', // Subject line
};

var mailContent = `這是210選座位登入系統 帳號密碼通知信
帳號：####
密碼：$$$$

請到<a href="https://ck72nd210.tw/seats/login">這裡</a>登入
`;

users.find({}).sort({ no: 1 }).exec(function(err,data){
    for (set of data) {
        var content = options;
        email = set.username + "@gl.ck.tp.edu.tw";
        content.to = email;
        content.html = mailContent.replace("####",set.username).replace("$$$$",set.password);
        console.log("To: " + email + ", For: " + set.username);
        transporter.sendMail(content, function(error, info){
            if(error){
                console.log(error);
            }else{
                console.log('Response: ' + info.response);
            }
        });
        sleep.sleep(1)
    }
});

