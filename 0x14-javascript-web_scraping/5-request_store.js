#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

if (!url || fileName === undefined) {
  console.error('Usage: ./5-request_store.js <url> <fileName>');
  process.exit(1);
}

request(url, function (error, reponse, body) {
  if (error) {
    console.error(error);
    process, exit(1);
  }

  fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
