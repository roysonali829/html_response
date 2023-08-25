
let number=[1,2,3,4,5,6,7,8,9,10]
console.log(number);
let even=[];
console.log(number)
for (let n of number)
{
    if (n%2===0)
    {
        even.push();
    }
}
console.log(even);
// number=[1,2,3,4,5,6,7,8,9,10]
number.filter((n,index,array)=>
{
    console.log(n);
    console.log(index);
    console.log(array);
})
//number=[1,2,3,4,5,6,7,8,9,10]
let odd=number.filter((n)=>
{
    return(n%2!=0);
})
console.log(odd)
