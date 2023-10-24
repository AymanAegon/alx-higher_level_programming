#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const chars = JSON.parse(response.body).characters;
    const d = {};
    chars.forEach(char => {
      request(char, (err, resp) => {
        if (err) {
          console.log(err);
        } else {
          const data = JSON.parse(resp.body);
          if (data.url.length === 45) {
            d[parseInt(data.url[43])] = data.name;
          } else {
            d[parseInt(data.url[43] + data.url[44])] = data.name;
          }
        }
      });
    });
    setTimeout(() => {
      let i = 0;
      while (Object.keys(d).length > 0) {
        if (d[i]) {
          console.log(d[i]);
          delete d[i];
        }
        i++;
      }
    }, 3000);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
