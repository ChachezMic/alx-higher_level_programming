#!/usr/bin/node

const farg = process.argv[2];
if (farg === undefined) {
  console.log('No argument');
} else {
  console.log(farg);
}
