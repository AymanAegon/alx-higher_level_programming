#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const films = JSON.parse(response.body).results;
    films.forEach(film => {
      film.characters.forEach(c => {
        if (character == c) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
