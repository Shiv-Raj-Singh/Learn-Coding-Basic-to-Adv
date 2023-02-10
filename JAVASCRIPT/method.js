// const obj = {
//     name : "Shiv Raj",
//     age : 22 ,
//     gender:"MAle",
//     Phone:9627347143,
//     about : function(){
//         return `My Name is ${obj.name} and i'm a ${obj.gender} My age is ${obj.age}`
//     }
// }
// console.log(obj.about())

const obj = {
    name : "Shiv Raj",
    age : 17 ,                                                                     // Use of this Key Word 
    gender:"MAle",
    Phone:9627347143,
    about : function(){
        return `My Name is ${this.name} and i'm a ${this.gender} My age is ${this.age}`
    },
    is18 : function(){
        return this.age > 18 
    },
   
}
// console.log(obj.this)
// console.log(obj.about())
console.log(obj.is18())

