var express = require("express");
var app = express();
var path = require("path");
var http = require('http').Server(app);
var io = require('socket.io')(http);

var SERVER_PORT = 3000;

process.stdin.resume();

app.get('/', function(req, res){
	res.sendFile(path.join(__dirname+'/client.html'));
});

io.on('connection', function(socket) {
	console.log('client started session');
	socket.on('disconnect', function(){
		console.log('client terminated session');
	});
});

process.on('SIGTERM', function(update) {
	console.log("engine signal received, send update");
	io.emit('update',update);
});

app.use(express.static(__dirname+'/images'));

http.listen(SERVER_PORT, function() {
	console.log('Server running at port %d',SERVER_PORT);
});



