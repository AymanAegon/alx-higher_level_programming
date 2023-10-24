#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const d = {};
    const data = JSON.parse(response.body);
    data.forEach(todo => {
      if (d[todo.userId] === undefined) {
        d[todo.userId] = 0;
      }
      if (todo.completed === true) {
        d[todo.userId] += 1;
      }
    });
    console.log(d);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
