const {spawn} = require('child_process')
const app = require('express')();
const path = require('path');

app.get('/', (req, res) => {
    res.send('poggers');
});

app.post('/send/:character', (req, res) => {
     const childProcess = spawn('python', ['keypresser.py', req.params.character]);

     childProcess.on('data', function(data){
        process.stdout.write("python script output",data);
    });
    childProcess.on('close', function(code) {
            if ( code === 1 ){
                process.stderr.write("error occured",code);
                process.exit(1);
            }
            else{
                process.stdout.write('python script exist with code: ' + code + '\n');
            }
        });
    res.sendStatus(200);
});

app.listen(3000, console.log('Server listening in on 3000'));