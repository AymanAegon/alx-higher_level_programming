#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = response.body;
    fs.writeFile(filename, data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
