const express = require('express')

const app = express()
const path = require('path'); 

const port  = 8080
// express.static("static") .... ye folder hai ..... /static path hai 

app.use("/static",express.static("static"))

// set the pug files
app.set('view engine', 'pug');

// set the directory of pug.... directory
app.set('views',path.join(__dirname,'views'));

// get point initilizse karata tevha ..../demo file name hai 
app.get('/demo', (req, res) => {
    res.status(200).render('demo', { title: 'This is the first demo of the pub', message: 'The demo of the pubg herer' })
  })



// ye wali get method hai 
app.get("/",(req,res)=>{
    res.send("This is my first app");
})
app.get("/about",(req,res)=>{
    res.send("This is my first app about page");
})
// niche wlai post method hai 
app.post("/about",(req,res)=>{
    res.send("This is my first app about page");
})

app.get("/about",(req,res)=>{
    // apko agar status code send karna hai to aap aise bhej sakte hai 
    res.status(200).send("This is my first app about page");
})

app.listen(port,()=>{
    console.log(`The server is run on the port no ${port}`)
})