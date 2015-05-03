var express = require("express");
var app = express();
var path = require("path");

app.get('/', function(req, res){
	res.sendFile(path.join(__dirname+'/client.html'));
});
app.use(express.static(__dirname+'/images'));
app.listen(3000);

console.log("Server running at port 3000");
