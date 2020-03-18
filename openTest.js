//script tag hard code not necessary in codepen, where I tested this
//lodash used, source is https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.15/lodash.min.js

//pitfalls are no error checking or incorrect input testing
//as well as no order of ([)] etc... checking

function openTest(str){
  //convert string into arry
  //within same statement convert it into dictionary like object similar to python collections counter
  //using the lodash countBy
  y = _.countBy(Array.from(str))
  //test whether all types of characters are closed by checking count of each
  if (y["("] == y[")"] && y["["] == y["]"] && y["{"] == y["}"]){
    //return True
    console.log("True")
  }
  //if counts are not equal
  else{
    //return false
    console.log("False")
  }
}

str = "([((({()})))])"
openTest(str)


