const obj1 = {
    name : "Raj Gupta",
    age : 22 ,
    gender:"MAle",
    Phone:9627,
}
const obj3 = {
    name : "Shivam Gupta",
    age : 15 ,
    gender:"MAle",
    Phone:123344,
}


// const obj2 = {
//     name : "Shiv Raj",
//     age : 17 ,                                                                     // Use of this Key Word 
//     gender:"MAle",
//     Phone:9627347143,
//     about : function(){
//         // return `My Name is ${obj2.name} and i'm a ${obj2.gender} My age is ${obj2.age}`
//         return `My Name is ${this.name} and i'm a ${this.gender} My age is ${this.age}`
//     },
//     is18 : function(){
//         console.log(this)
//         return this.age > 18 
//     },
//     abc : ()=>{
//         console.log(this)
//     }
// }

// abc()

// console.log(obj2.about())  // Happy flow for obj2 
// console.log(obj2.is18())
// // // console.log(obj2.abc())

// console.log(obj1.about())  // if we want use about method for obj1 then give an error 
// console.log(obj2.is18())

//  For call a mEthod from An object to Another Object then we have to use Call / Apply / Bind 

// Call Method ------

// console.log(obj2.about.call(obj1))  // Happy flow for obj1 By Call Method
// console.log(obj2.is18.call(obj1))
// console.log(obj2.about.call(obj3))  // Happy flow for obj1 By Call Method
// console.log(obj2.is18.call(obj3))

// // Same Previous Process by Apply Method ------

// console.log(obj2.about.apply(obj1))  // Happy flow for obj1 By Call Method
// console.log(obj2.is18.apply(obj1))


//  Now we will make method out-side the objcect and after that we will use them for diff objects 

// const outMethod = function(hobbi , faveGame){
//     console.log(this)
//     return `age--> ${this.age} and name --> ${this.name} and details --> ${this} hobbis -->  ${hobbi} and Fav Game is ${faveGame} `
// }
// const obj1_Call_method = outMethod.call(obj1 , "plAyibg", 'cricket'  )       // this is by Call Method 

// const obj1_Apply_method = outMethod.apply(obj1, ["plAyibg" , 'cricket'])      // this is by Apply Method  Only Args Inside the Array 

// const obj1_Bind_method = outMethod.bind(obj1 , "plAyibg", 'cricket'  )     // this is by Bind Method 
//                                                                     // bind method bound the function in a variable you can call that any-time
// console.log(obj1_Call_method)
// console.log(obj1_Apply_method)
// console.log(obj1_Bind_method())


// const obj1 = {
//     name : "Yukta",
//     age : 22,
//     gender : "Female",
// }
// const obj2 = { }
// console.log(obj2.name)

