#!/usr/bin/node
const number = Number(process.argv[2]);
const string = 'C is fun';
if (isNaN(number) || number === undefined) {
  console.log('Missing number of occurrences');
} else if (number < 0) {
  // Doing nothing
}
for (let i = 0; i < number; i++) {
  console.log(string);
}
