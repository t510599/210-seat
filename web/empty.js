var users = require('./models/users');

users.find({}).sort({ no: 1 }).exec(function(err,data){
    for (set of data) {
        if (set.direction == "") {
            console.log(set.no)
        }
    }
});

