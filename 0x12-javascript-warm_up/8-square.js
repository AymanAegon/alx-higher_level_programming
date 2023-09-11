#!/usr/bin/node
const x = process.argv[2];
let n = x;
let m = x;
if (x === undefined) {
  console.log('Missing size');
} else if (isNaN(parseInt(x))) {
  console.log('Missing size');
} else {
  while (n > 0) {
    while (m > 0) {
      process.stdout.write('X');
      m -= 1;
    }
    console.log();
    n -= 1;
    m = x;
  }
}
