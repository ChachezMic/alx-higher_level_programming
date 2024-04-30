#!/usr/bin/node

const { argv } = require('process');
const number = parseInt(argv[2]);
if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let row = ' ';
    for (let j = 0; j < number; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
