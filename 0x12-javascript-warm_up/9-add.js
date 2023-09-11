#!/usr/bin/node
function add (a, b) {
  if (a === undefined || b === undefined) {
    console.log(NaN);
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}
const x = process.argv[2];
const y = process.argv[3];
add(x, y);
