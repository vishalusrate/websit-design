var http = require('http')
var fs = require('fs')

var hostname = '127.0.0.1';
var post = 3000;
var index = fs.readFileSync('index.html');
var about = fs.readFileSync('./about.html');
var services = fs.readFileSync('./services.html');
var contact =  fs.readFileSync('./contact.html');

var server = http.createServer((req,res)=>{
    url = req.url;
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    console.log(req.url)
    if(url == '/'){
        res.end(index)
    }else if(url == '/about'){
        res.end(about)
    }else if(url == '/services'){
        res.end(services)
    
    }else if(url == '/contact'){
        res.end(contact)
    }else{
        res.end('404 not found')
    }
});


server.listen(post,hostname,(error,resp)=>{
    console.log("The server is started")
})