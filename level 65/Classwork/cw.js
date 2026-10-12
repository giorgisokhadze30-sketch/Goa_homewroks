// შექმენით ორი მასივი: languageA, languageB. სადაც 5-5 ელემენტს მოათავსებთ. თქვენი დავალებაა გამოიყენოთ forLoop-ი, 
// რომ დაადგინოთ ამ ორ მასივს შორის არის თუ არა საერთო 
// ელემენტები. თუ აღმოაჩენთ - კონსოლში დალოგეთ 'found mutual language: {...}'

const languageA = ["Spanish" , "Georgian" , "English" , "Russian"]
const languageB = ["French" , "Georgian" , "Latin"]



for(i = 0; i < languageA.length ; i++ ){
    for(x = 0; x < languageB.length ; x++){
        if (languageA[i] === languageB[x]){
            console.log(`found mutual language: ${languageA[i]}`)


        }

    }
}


// 2) შექმენით fruits მასივი: ['apple', 'cherry', 'melon']
// დაწერეთ while loop-ის პროგრამა, math.random-ის საშუალებით currentFruit-ში ყოველ ჯერზე რენდომული მნიშვნელობა ჩაიწერება, 
// სანამ 'cherry' მნიშვნელობა არ ჩაჯდება currentFruit-ში, იქამდე გააგრძელეთ ძებნა.


const fruits = ['apple', 'cherry', 'melon']

let currentFruit = "";

while(currentFruit !== "cherry"){
    const index = Math.floor(Math.random() * fruits.length -1);
    currentFruit = fruits[index];
    console.log(`Current fruit: ${currentFruit}`);
}