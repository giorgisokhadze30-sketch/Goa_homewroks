// 2) შექმენი მასივი fruits რამდენიმე ხილის დასახელებით. დაბეჭდე კონსოლში ტექსტი: "მასივში არის X ელემენტი", 
// სადაც X არის მასივის სიგრძე.

const fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი"];

console.log();





// 3) შექმენი ცარიელი მასივი todoList. .push() მეთოდის გამოყენებით თანმიმდევრობით დაამატე 3 აქტივობა 
// (მაგ. "learn", "workout", "rest"). დაბეჭდე საბოლოო მასივი.

const todoList = [];
todoList.push("learn");
todoList.push("workout");
todoList.push("rest");

console.log(todoList);




// 4) გაქვს მასივი numbers = [10, 20, 30, 40, 50]. წაშალე მასივიდან ბოლო ელემენტი .pop()-ით, ხოლო წაშლილი
//  მნიშვნელობა შეინახე ცალკე ცვლადში removedNumber და დაბეჭდე კონსოლში.

const numbers = [10, 20, 30, 40, 50];

const removedNumber = numbers.pop();

console.log(removedNumber);





// 5) შექმენი მასივი colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]. .at() მეთოდის გამოყენებით
//  დაბეჭდე:
// პირველი ელემენტი და ბოლო ელემენტი 


const colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"];

console.log(colors.at(0));
console.log(colors.at(4));

// 6) გაქვს რიგის მასივი queue = ["გიორგი", "ანა", "ნიკა", "მარიამი"]. რადგან პირველი მომხმარებელი მოემსახურა, ამოიღე 
// ის მასივიდან .shift()-ით და დაბეჭდე განახლებული რიგი.

const queue = ["გიორგი", "ანა", "ნიკა", "მარიამი"];

queue.shift();

console.log(queue);

// 7) შექმენი ორი მასივი: frontEnd = ["HTML", "CSS", "JS"] და backEnd = ["Node.js", "Python"]. შეაერთე ეს ორი მასივი
//  .concat()-ის გამოყენებით ახალ fullStack მასივში და დაბეჭდე.

const frontEnd = ["HTML", "CSS", "JS"];

const backEnd = ["Node.js", "Python"];

const fullStack = frontEnd.concat(backEnd);

console.log(fullStack);

// 8) გაქვს მასივი animals = ["Dog", "Cat", "Bear", "Wolf"].
// იპოვე და დაბეჭდე "Cat"-ის ინდექსი .indexOf()-ის საშუალებით.
// შეამოწმე, რას დააბრუნებს .indexOf("lion") და ახსენი რატომ მივიღეთ მსგავსი შედეგი.

const animals = ["Dog", "Cat", "Bear", "Wolf"];

console.log(animals.indexOf("Cat"));
console.log(animals.indexOf("lion")); 

// 9) გაქვს კვირის დღეების მასივი days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", 
// "პარასკევი", "შაბათი", "კვირა"]. .slice()-ის გამოყენებით ამოჭერი მხოლოდ სამუშაო დღეები
//  (ორშაბათიდან პარასკევის ჩათვლით) ახალ მასივში workDays.

const days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"];
const workDays = days.slice(0, 5);
console.log(workDays);





// 10) შექმენი მასივი randomMovies = ["Inception", "Interstellar"]. .unshift() მეთოდით სიის საწყისში (პირველ ადგილას)
//  დაამატე ფილმი "The Dark Knight".

const randomMovies = ["abduction", "Interstellar"];

randomMovies.unshift("supernaturla");

console.log(randomMovies);


// 11) გაქვს მასივი scores = [50, 65, 78, 92, 45, 88, 99]. .slice() მეთოდის გამოყენებით ამოჭერი და ცალკე მასივში შეინახე 
// ბოლო 3 ქულა.


const scores = [50, 65, 78, 92, 45, 88, 99];

const lastThreeScores = scores.slice(4, -1)

console.log(lastThreeScores);

// 12) შექმენი ცარიელი მასივი searchHistory.
// 1. დაამატე მასში 3 ლინკი .push()-ით: "google.com", "github.com", "youtube.com".
// 2. წაშალე ბოლო ეწვიეული საიტი .pop()-ით.
// 3. დაამატე ახალი საიტი "stackoverflow.com".
// 4. დაბეჭდე მასივის მიმდინარე სიგრძე (.length) და ბოლო ელემენტი (.at(-1)).


const searchHistory = [];

searchHistory.push("google.com", "github.com", "youtube.com");

searchHistory.pop();

searchHistory.push("stackoverflow.com");

console.log(searchHistory.length);

console.log(searchHistory.at(-1));



// 13) შექმენი მასივი shoppingList = ["bread", "milk", "cheese", "eg"].
// .indexOf()-ით იპოვე "cheese"-ის ინდექსი.

const shoppingList = ["bread", "milk", "cheese", "eg"];

const cheeseIndex = shoppingList.indexOf("cheese");

console.log("cheeseIndex");



// 14) არ დაგეზაროთ და აუცილებლად უყურეთ თავიდან ჩანაწერს.