var express = require('express');
var router = express.Router();
var users = require('../models/users');
var path = require('path');
var fs = require('fs');

router.get('/', function(req, res, next) {
    if (!req.session.stdno) {
        return res.redirect('login');
    }
    var seats = JSON.parse(fs.readFileSync(path.resolve(__dirname, "../../cli/seats.txt"), 'utf8'));
    var directions = {
        "f": "向前",
        "b": "向後",
        "r": "向右",
        "l": "向左",
        "fr": "向右前",
        "fl": "向左前",
        "br": "向右後",
        "bl": "向左後"
    }
    users.findOne({ username: req.session.stdno }).exec(function(err,user){
        res.render('index', { title: '自己選自己的', msg: req.flash().msg, errMsg: req.flash().errMsg, directions: directions, seats: seats, user:user });
    });
});

router.post('/', function(req, res, next){
    if (!req.session.stdno) {
        return res.redirect('login');
    }
    if (!req.body.direction || !req.body.steps || req.body.direction == "" || req.body.steps == "" || !(/^[0-9]+$/g.exec(req.body.steps))) {
        req.flash('errMsg','請填寫正確格式!');
        return res.redirect('.');
    }
    users.updateOne({ username: req.session.stdno }, {
        direction: req.body.direction,
        steps: req.body.steps
    }).exec(function(err) {
        if (err) {
            res.status(500).send('Error');
        } else {
            req.flash('msg','提交成功');
            res.redirect('.');
        }
    });
});

router.get('/show', function(req, res, next) {
    var seats = JSON.parse(fs.readFileSync(path.resolve(__dirname, "../../cli/seats.txt"), 'utf8'));
    res.render('show', { title: '自己選自己的', seats: seats});
});

router.get('/login', function(req, res, next) {
    if (req.session.stdno) {
        return res.redirect('.');
    }
    res.render('login', { title: 'Login', errMsg: req.flash().error });
});

router.post('/login', function(req, res, next){
    users.findOne({username: req.body.username, password: req.body.password}).exec(function(err,user){
        if (err) {
            req.flash('error', '帳號或密碼錯誤');
            res.redirect('login');
        }
        if (!user) {
            req.flash('error', '帳號或密碼錯誤');
            res.redirect('login');
        } else {
            req.session.stdno = user.username;
            res.redirect('.');
        }
    });
});

router.get('/logout', function(req, res, next){
    req.session.stdno = null;
    res.redirect('login');
});

module.exports = router;
