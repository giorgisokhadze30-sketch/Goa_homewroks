// 1) დაწერეთ map, რომელიც სიტყვების მასივიდან ახალ მასივში დაამატებს თითოეული სიტყვის ბოლო ასოს.

const Fruits = ["Apple", "Pear", "Melon", "Banana", "Watermelon"]

const Words = Fruits.map(fruit => {return fruit.length - 1})

console.log(Words)

// 2) დაწერეთ filter, რომელიც [1, 3.14, 'javaScript', true, 'Hello World', 82] მასივს გაფილტრავს და ახალ სიაში დატოვებს 
// მხოლოდ სტრინგ მონაცემებს.
const RandomWords = [1, 3.14, 'javaScript', true, 'Hello World', 82]

const OnlyString = RandomWords.filter(word => {return word[0] === ""})

console.log(OnlyString)

// 3) forEach მეთოდით სიტყვების მასივიდან დააბრუნეთ იმ ელემენტის ინდექსი, რომელიც ასო 'L' ზე იწყება.#

const name = ["Luka", "Lika", "Giorgi", "Nika"]


const startswithL = name.findIndex(letter => {return letter[0] === L})