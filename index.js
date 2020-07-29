const {spawn} = require('child_process')
const app = require('express')();
const path = require('path');

app.get('/', (req, res) => {
    res.send('poggers');
});

app.post('/send/:character', (req, res) => {
    spawn('python', ['keypresser.py', req.params.character]);

    console.log('logging ' + req.params.character)
    res.sendStatus(200);
});

app.listen(3000, console.log('Server listening in on 3000'));