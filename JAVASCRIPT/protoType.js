// **********************************************        ProtoType     *************************************************************

// every function have own constructor object that's called  prototype that is an empty object which exist inside evry Function

// function hello(){
//     return 'hello world '
// }

// console.log(hello.prototype)
// hello.prototype.name = "SHIV RAJ"
// console.log(hello.prototype)


// function CreateUser(x , y , z){
//     const user = Object.create(CreateUser.prototype)
//     user.name = x,
//     user.age = y,
//     user.gender = z 
//     return user 
// }

// const user1 = CreateUser('Mangal' , 22 , "MAle")
// const user2 = CreateUser('Raj' , 19 , "MAle")
// console.log(user1)
// console.log(user2)

// CreateUser.prototype.about = function(){
//     return  ` his Name is ${this.name} and his age is  ${this.age} , he from ${this.gender}`
// }
// CreateUser.prototype.is18 = function(){
//     return  this.age >= 18
// }

// console.log(user1.about())
// console.log(user2.is18())
// console.log(CreateUser.prototype)
// console.log(Object.keys(user1))



// Use OF New KeyWord ----->   NEW    //    Constructor Function 


function CreateUser(name , age , gender){
    this.name = name, 
    this.age = age ,
    this.gender = gender
}

const user1 = new CreateUser('Mangal' , 22 , "MAle")
const user2 = new  CreateUser('Raj' , 19 , "MAle")

// console.log(user1)
// console.log(user2)

CreateUser.prototype.about = function(){
    return  ` his Name is ${this.name} and his age is  ${this.age} , he from ${this.gender}`
}
CreateUser.prototype.is18 = function(){
    return  this.age >= 18
}

// console.log(user1.about())
// console.log(user2.is18())
// console.log(Object.keys(user1))

// for( let i in user1){
//     console.log(i)   //  All keys along with Prototype keys/Methods Keys
// }

// **********************************************************************   Array Function ProtoType  *************************************8

// const num = [1,2,3,4,5]
// const num = new Array(1 , 2 , 3)
// // num.prototype.name = 'mangal'
// console.log(num.prototype)        

// arr[0]//  xxxxxxxxxx not working 



// const obj = {
//     name : "Mangal",
//     age : 22
// }

// // console.log(obj.this.age)

// const isValidName =function(str){
//     const  nameRegex =/^[a-zA-Z( \)]{2,20}$/
//     return nameRegex.test(str)
// }

// function Abc(){
//         if(!valid) return console.log(`this is Valid Name -->${this.name} `)
//         if(valid) return console.log(`this is InValid Name -->${this.name} `)
//     }



// Abc.prototype  = {...obj}
// Abc.prototype.isValidName  = function(str){
//     const  nameRegex =/^[a-zA-Z( \)]{2,20}$/
//     const valid =  nameRegex.test(this.str)}

// console.log(Abc.prototype)
// Abc.isValidName()




// const num = [1,2,3,4,5]
// const PrintAll = obj => console.log(Object.getOwnPropertyNames(obj));

// PrintAll(num.prototype[0]);




