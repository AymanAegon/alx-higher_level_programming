#!/usr/bin/node
const { list } = require('./100-data');
let i = 0;

console.log(list);
const map1 = list.map((x) => x * i++);
console.log(map1);
