#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || content === undefined) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filepath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
