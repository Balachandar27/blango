alert('Hello, world!')
// let scope
const theNumber = 1
let yourName = 'Ben'

if (theNumber === 1) {
  let yourName = 'Leo'
  alert(yourName)
}

alert(yourName)

// different types of console logging
console.time('myTimer')
console.count('counter1')
console.log('A normal log message')
console.warn('Warning: something bad might happen')
console.error('Something bad did happen!')
console.count('counter1')
console.log('All the things above took this long to happen:')
console.timeEnd('myTimer')

// standard function definition and call
function addNumbers(a, b) {
    return a + b
}

const result = addNumbers(3, 4)
console.log(result)

// variation of function definition and call
const doubler = (x) => { return x * 2 }
console.log(doubler(2))  // outputs 4

// to illustrate timeout
function showAnAlert() {
  alert('Timeout finished.')
}

setTimeout(showAnAlert, 2000)

// another usage
function sayHello(yourName1) {
  if (yourName === undefined) {
      console.log('Hello, no name')
  } else {
       console.log('Hello, ' + yourName)
  }
}

const yourName1 = 'Your Name'  // Put your name here

console.log('Before setTimeout')

setTimeout(() => {
    sayHello(yourName)
  }, 2000
)

console.log('After setTimeout')

// control flow statements

for(let i = 0; i < 10; i += 1) {
  console.log(i)
}

let i = 0

while(i < 10) {
  console.log(i)
  i += 1
}

let i = 10

do {
  console.log(i)
  i += 1
} while(i < 10)

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.forEach((value => {
  console.log(value)
}))

const doubled = numbers.map(value => value * 2)

console.log(doubled)