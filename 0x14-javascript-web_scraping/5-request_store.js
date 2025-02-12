#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file_name = process.argv[3];

if (!url || file_name === undefined) {
  console.error('Usage: ./5-request_store.js <url> <file_name>');
  process.exit(1);
}

request(url, function (error, reponse, body) {
  if (error) {
    console.error(error);
    process, exit(1);
  }

  fs.writeFile(file_name, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
