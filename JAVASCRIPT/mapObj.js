const person = {
    "name":"shiv raj ",
    "college":"rjit",
    "rollNo":21
}

// console.log(Object.entries(person))
const obj = new Map(Object.entries(person))                 // for Convert Normal obj to  Map Obj   
 console.log(obj)
 const mapObj =  new Map()                                     // for Create Normal Map Obj   
 
obj.set(null , 'don')
obj.set([1234 , 1223] , 'don')
obj.set('m' , 'don')
obj.set(123 , 'qwerr')
obj.abc = true

console.log(obj)

// // console.log(obj)
for( let [i,j] of obj){
    console.log(i,'-->' , j)
}
console.log(typeof obj)
