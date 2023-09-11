#!/usr/bin/node
function fact (x) {
  if (isNaN(x) || x <= 1) {
    return 1;
  }
  return fact(x - 1) * x;
}
const x = parseInt(process.argv[2]);
console.log(fact(x));
