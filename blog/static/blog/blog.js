/*
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

let ii = 10

do {
  console.log(ii)
  ii += 1
} while(ii < 10)

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.forEach((value => {
  console.log(value)
}))

const doubled = numbers.map(value => value * 2)

console.log(doubled)

// class definition in JS
class Greeter {
  constructor (name) {
    this.name = name
  }

  getGreeting () {
    if (this.name === undefined) {
      return 'Hello, no name'
    }

    return 'Hello, ' + this.name
  }

  showGreeting (greetingMessage) {
    console.log(greetingMessage)
  }

  greet () {
    this.showGreeting(this.getGreeting())
  }
}

// class call in JS to create objects
const g = new Greeter('Patchy')
g.greet()

//Inheritance
class DelayedGreeter extends Greeter {
  delay = 2000
  constructor (name, delay) {
    super(name)
    if (delay !== undefined) {
      this.delay = delay
    }
  }
  greet () {
    setTimeout(
      () => {
        this.showGreeting(this.getGreeting())
      }, this.delay
    )
  }
}

const dg2 = new DelayedGreeter('Patchy 2 Seconds')
dg2.greet()

const dg1 = new DelayedGreeter('Patchy 1 Second', 1000)
dg1.greet()
*/
// Promise
/* function resolvedCallback(data) {
  console.log('Resolved with data ' +  data)
}

function rejectedCallback(message) {
  console.log('Rejected with message ' + message)
}

const lazyAdd = function (a, b) {
  const doAdd = (resolve, reject) => {
    if (typeof a !== "number" || typeof b !== "number") {
      reject("a and b must both be numbers")
    } else {
      const sum = a + b
      resolve(sum)
    }
  }

  return new Promise(doAdd)
}

const p = lazyAdd(3, 4)
p.then(resolvedCallback, rejectedCallback)

lazyAdd("nan", "alsonan").then(resolvedCallback, rejectedCallback)*/


//React JS code
class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState(
      {wasClicked: true}
    )
  }

  render () {
    let buttonText

    if(this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: () => {
          this.handleClick()
        }
      },
      buttonText
    )
  }
}
const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(ClickButton),
  domContainer
)