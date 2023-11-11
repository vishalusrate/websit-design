var http = require('http')
var fs = require('fs')

var content1 = fs.readFileSync('test.txt')

var server = http.createServer((req,content)=>{
    content.writeHead(200,{'Content-type':'text/html'});
    content.end(content1)
});

server.listen(80,'127.0.0.1',()=>{
  console.log("This is the test site");
})