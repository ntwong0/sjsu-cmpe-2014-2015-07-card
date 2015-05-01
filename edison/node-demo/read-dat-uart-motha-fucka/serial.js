var SerialPort = require("serialport").SerialPort
var serialPort = new SerialPort("/dev/ttyMFD1", {
  baudrate: 921600
});

var fs = require('fs');
var buff = "";

serialPort.open(function (error) {
  if ( error ) {
    console.log('failed to open: '+error);
  } else {
    console.log('open');
    serialPort.on('data', function(data) {
	buff += data.toString('hex');
      console.log(data);
    });
    serialPort.write("ls\n", function(err, results) {
      console.log('err ' + err);
      console.log('results ' + results);
    });
  }
});

setInterval(function() {
	fs.appendFile("output.dat", buff, function(err) {
	    if(err) {
	        return console.log(err);
	    }
		buff = "";
	    console.log("The file was saved!");
	}); 
}, 2000);
