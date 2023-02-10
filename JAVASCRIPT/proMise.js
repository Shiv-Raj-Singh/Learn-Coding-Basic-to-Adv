// const bucket = ['matar' , 'paneer', 'masal' , 'gobi']
// // if(bucket.includes("matar")){
// //     console.log("yeah i have done your Matar Paneer")
// // }

// //  Promise for make matar - paneer let's make the ,atar-paneer ********************************************8

// const matarPaneerPromise = new Promise( (resolve , reject)=>{
//     if(bucket.includes("matar") && bucket.includes("paneer") && bucket.includes("masale")){
//         return resolve("yeah i have done your Matar Paneer")
//     }else{
//         return reject("i m not able to make your matar paneer !")
//     }
// })
// matarPaneerPromise.then((v)=>{
//     console.log(v)
// })
// .catch((err)=> console.log(err))


// #################################################  2nd example ###################################

// function abc(a){
//   return  new Promise((rs ,rj)=>{
//         if(a) rs(a)
//         else rj('you did not pass any argument !')
//     })
// }

// abc(0).then(v =>{
//     console.log(v)
//     v++
//     abc(v).then(v=>{
//         console.log(v)
//         v++
//         abc(v).then(v=>{
//             console.log(v)
//         })
//     })
// })
// .catch( err =>{
//     console.log('oof your number is a odd number')
// })


function abc(a){
    let sum = 0
    for(let i = 0 ; i < (2*a)+1 ; i=i+2){
        // console.log(i)
        let x = i**2
        sum+=x
    }
    return sum
}

console.log(abc(4))
console.log(abc(1))

// console.log(abc(3))
// console.log(abc(10))
