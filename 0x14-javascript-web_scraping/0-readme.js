#!/usr/bin/node

const fs = require("fs")
const filepath = process.argv[2];

if (!filepath) {
  console.error("Provide the path of the file")
  process.exit(1);
}

fs.readFile(filepath, "utf-8", (err, data) => {
  if (err) {
  console.error(err);
  process.exit(1);
  } 
  console.log(data);
});

