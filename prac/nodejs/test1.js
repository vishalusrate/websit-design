console.log("Custom module files")

// yaha par maine function likhkar usko get kiya hai dusre isme
function sumoftheelement(arr){
    let sum = 0;
    arr.forEach(element => {
        sum += element;
    });
    return sum;
}

// agar apko ye function ko dusre file ko accessible banana hai to aap exports karke likh sakte hai 
// aabhi aap usko dusre file me access kar sakte hai 
// module.exports = sumoftheelement;
// aap ikso object banakar bhi bhej sakte hai 

module.exports = {
    sumoftheelement : sumoftheelement,
    name:"Vishal",
    age:23
}

// aap particulat key me bhi bhej sakte hai 
// module.exports.name = "Test";