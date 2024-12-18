#!/usr/bin/node
const number = process.argv[2];
const string = 'C is fun\n';
if (number === undefined) {
  console.log('Missing number of occurrences');
} else if (number < 0) {
  // doing nothing
} else { console.log(string.repeat(number)); }
