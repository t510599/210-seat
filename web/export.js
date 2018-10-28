var fs = require('fs');
var path = require('path');
var users = require('./models/users');

fs.writeFileSync(path.resolve(__dirname,"../cli/requirements.txt"),""); // empty the file

users.find({}).sort({ no: 1 }).exec(function(err,data){
    for (set of data) {
        console.log(set.no)
        if (set.direction != "" && set.steps != "") {
            console.log('yes')
            fs.appendFileSync(path.resolve(__dirname,"../cli/requirements.txt"),`${set.no} ${set.direction} ${set.steps}\n`);
	    }
    }
});

