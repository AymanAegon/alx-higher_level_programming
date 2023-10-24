#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    const films = JSON.parse(response.body).results;
    films.forEach(film => {
      film.characters.forEach(c => {
        if (c.includes("18")) {
          count += 1;
        }
      });
    });
    console.log(count);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
