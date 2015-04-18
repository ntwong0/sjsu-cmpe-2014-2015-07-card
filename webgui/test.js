/*
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.
  res.end('Hello World\n');
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');
*/
var express = require("express");
var app = express();
var path = require("path");

app.get('/', function(req, res){
	res.sendFile(path.join(__dirname+'/gui.html'));
});
app.use(express.static(__dirname+'/images'));
app.listen(3000);

console.log("Server running at port 3000");
