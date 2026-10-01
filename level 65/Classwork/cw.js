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