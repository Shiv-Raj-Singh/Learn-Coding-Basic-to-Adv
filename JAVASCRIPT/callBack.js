function abc(a , b , sum ){
    console.log(sum(a,b))
   const ab =  sum(a , b)
   console.log(ab)
}

abc(4 , 7 , (x , y)=> x + y )
