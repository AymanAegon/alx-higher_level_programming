#!/usr/bin/node
const arr = process.argv;
let x = arr[2]; let y;
if (arr.length <= 3) {
  console.log(0);
} else {
  for (let i = 3; i < arr.length; i++) {
    if (arr[i] > x) {
      y = x;
      x = arr[i];
    }
  }
  console.log(y);
}
