// class Laptop{
//     constructor(name , brand , ram , price ){
//         this.name = name,
//         this.brand = brand , 
//         this.ram = ram ,
//         this.price = price
//     } 

//     about(){
//         return `the Lapi Price is just ${this.price} and you got the brand ${this.brand}`
//     }
// }

// const lap1 = new Laptop('ShivRaj' , "H-P" , 16 , 45000)
// console.log(lap1.about())



// **********     ***********************   Inheritance   (( ********************************************************888))

class Laptop{
    constructor(name , brand , ram , price ){
        this.name = name,
        this.brand = brand , 
        this.ram = ram ,
        this.price = price
    } 

    about(){
        return `the Lapi Price is just ${this.price} and you got the brand ${this.brand}`
    }
}
class Laptop1 extends Laptop{
    constructor(name , brand , ram , price , color ){
        super(name , brand , ram , price , color)
            this.color = color 
    } 
    about(){
        return `the Lapi Price is just ${this.price} and you got the brand ${this.brand} color is ${this.color}`
    }

}

const lap1 = new Laptop('ShivRaj' , "H-P" , 16 , 45000)
console.log(lap1.about())
