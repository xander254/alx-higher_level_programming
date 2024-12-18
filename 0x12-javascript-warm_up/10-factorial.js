#!/usr/bin/node
const number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log('1');
}
function factorize (num) {
  let result = number;
  if (num === 0 || num === 1) { return 1; }
  while (num > 1) {
    num--;
    result *= num;
  }
  return result;
}
console.log(factorize(number));
