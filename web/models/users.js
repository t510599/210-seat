var mongoose = require('mongoose');
mongoose.Promise = require('bluebird');

mongoose.connect('mongodb://localhost/210-seats');
var Schema = mongoose.Schema;

var user = new Schema({
    username: String,
    password: String,
    no: Number,
    direction: String,
    steps: String
});
var users = mongoose.model('users', user);

module.exports = users;