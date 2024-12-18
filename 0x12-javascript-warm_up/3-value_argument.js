#!/usr/bin/node
const noarg = process.argv.slice(2);
if (noarg[0] === undefined) {
  console.log('No argument');
} else { console.log(process.argv[2]); }
