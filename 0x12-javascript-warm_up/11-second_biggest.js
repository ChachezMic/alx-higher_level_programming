#!/usr/bin/node

const process = require('process');
const number = process.argv.slice(2);
let secondlargest = 0;
if (number.length > 1) {
  number.sort();
  secondlargest = number[number.length - 2];
}
console.log(secondlargest);
