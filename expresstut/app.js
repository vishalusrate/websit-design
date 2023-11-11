const express = require('express')
var bodyParser = require('body-parser')

const app = express()
const path = require('path'); 
const fs = require('fs'); 

const port  = 8080
// express.static("static") .... ye folder hai ..... /static path hai 
// express ki files hai yaha par
app.use("/static",express.static("static"))
// app.unsubscribe(express.urlencoded())
app.use(bodyParser.urlencoded({ extended: false }))


// iske niche pub ki file hai 
// set the pug files
app.set('view engine', 'pug');
// set the directory of pug.... directory
app.set('views',path.join(__dirname,'views'));

// get point initilizse karata tevha ..../demo file name hai 
app.get('/',(res,req)=>{
    const con = "This is the content of the page here"
    const head = "This is the heading"
    const param = {"title":head,"content":con}
    req.status(200).render('index.pug',param);
});

app.post('/',(req,res)=>{
    let outContetnIs = `The client name is ${req.body.name} and age is ${req.body.age} and address is ${req.body.address} and phone is ${req.body.phone} and more about the client is ${req.body.yourself}`
    const param = {"message":"You data sumitted suucessfully"}
    fs.writeFileSync('Output.txt',outContetnIs)
    res.status(200).render('index.pug',param);
});

app.listen(port,()=>{
    console.log(`The server is run on the port no ${port}`)
})