#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(response.body);
    console.log(obj.title);
  }
});
