const obj1 = {
    a : 1,
    b : 2 , 
    c :3
}
const obj2 = {
    p : 7,
    q : 5
}
// console.log(obj1.a)
// console.log(obj2.a)  // Undefined 

// const obj3 = Object.create(obj1)   //  giving the ref of obj to obj2
// console.log(obj3)      //  empty object now 
// obj3.d = 7
// obj3.e = 5           
// console.log(Object.keys(obj3))      //  empty object now 

// console.log(obj1.a)     //   1 
// console.log(obj3.a)  //     1     bcoz there obj3 have not any key by a name now it's inherting the value of a from obj1 (first object)


// function createUser(name , age , gender , address){
//     const user = {}
//     user.name = name,
//     user.age = age,
//     user.address = address,                             // Create obj with Methods 
//     user.gender = gender
//     user.about = ()=>{
//         return ` his Name is ${user.name} and his age is  ${user.age} , he from ${user.address}`
//     }
//     user.is18 = function(){
//                 return this.age >= 18
//      } 
//     return user 
// }
// const user1 = createUser("Shiv Raj" , 22 , "Uttar-Pradesh" , "Male")
// console.log(user1)
// const user2 = createUser("Raj Gupta" , 22 , "Kanpur" , "Male")
// console.log(user2)
// // console.log(user1)
// console.log(user2.about())

// Method Object 

// const user2 = createUser("Shiv Raj", 22, "Uttar-Pradesh", "Male")
// console.log(user2)
// console.log(user2.about())                               
                                         
// *****************************************    // Create obj for  Methods  ***************************************************************

// const methodObject = {
//     about : function(){
//         return ` his Name is ${this.name} and  , his age is  ${this.age} , he from ${this.address}`
//     },                                                                                   
//     is18 : function(){
//         return this.age >= 18
//     }                                               
// }

// function createUser(name , age ,address , gender ){
//     const user = {}
//     user.name = name,
//     user.age = age,
//     user.address = address,                             
//     user.gender = gender
//     return user 
// }

// const user1 = createUser("Shiv Raj" , 22 , "Uttar-Pradesh" , "Male")
// const user2 = createUser("Raj Gupta" , 12 , "Uttar-Pradesh B.S.R" , "Male")
// const user3 = createUser("Shivam Gupta" , 32 , "Madhya-Pradesh" , "Male")

// console.log(user1)
// console.log(user2)
// // console.log(user3)
// console.log(methodObject.about.call(user1))
// console.log(methodObject.is18.call(user1))

// // console.log(user2)
// console.log(methodObject.about.call(user2))
// console.log(methodObject.is18.apply([user2]))

// *****************************#################  use __proto__ object ******************************************


// const methodObject = {
//     about : function(){
//        return ` his Name is ${this.name} and  , his age is  ${this.age} , he from ${this.address}`
//    },                                                                                   
//    is18 : function(){
//        return this.age >= 18
//    }                                               
// }

// function createUser(name , age , gender , address){
//    const user =Object.create(methodObject)
//    user.name = name,
//    user.age = age,
//    user.address = address,                             
//    user.gender = gender
//    return user 
// }

// const user1 = createUser("Shiv Raj" , 22 , "Uttar-Pradesh" , "Male")
// const user2 = createUser("Shiv" , 12 , "Uttar-Pradesh B.S.R" , "Male")

// console.log(user1 )
// console.log(user1.about())
// // console.log(user1.is18())
                            // console.log(user1.__proto__)
// console.log(user2)
// console.log(user2.about())
// console.log(user2.is18())

// // **********************************************  Proto-Type *************************************************************

// // every function have own constructor object that's called  prototype that is an empty object which exist inside evry Function

function hello(){
    console.log('hello world ')
}
const methodObject = {
    about : function(){
       return ` his Name is ${this.name} and  , his age is  ${this.age} , he from ${this.address}`
   },                                                                                   
   is18 : function(){
       return this.age >= 18
   }                                               
}

// const hello2 =  ()=>{
//     console.log('hello world ')
// }
// hello()
// console.log(hello.prototype)
// // console.log(hello2.prototype)
// hello.prototype = {...methodObject}
// console.log(hello.prototype.about())


// let obj = {a :1 , b : 2} 
// let objA = {p :10 , q : 2 , c:12}
// let objk = Object.create(objA)
// console.log(objk.c)

// function abc(){
//     return "abaav"
// }
// abc.prototype.name = "subho yadav"

// console.log(abc.prototype);