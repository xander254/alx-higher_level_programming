#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);

    let count = 0;

    filmData.results.forEach(film => {
      const characterurl = film.characters;
      characterurl.forEach(url => {
        if (url.includes('/people/14444/')) {
          count++;
        }
      });
    });
    console.log(`${count}`);
  }
});
