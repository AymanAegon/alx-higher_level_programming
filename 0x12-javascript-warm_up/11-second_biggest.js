#!/usr/bin/node
const arr = process.argv;
let x, y;
if (arr.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
  }
  x = arr[2];
  y = arr[3];
  for (let i = 3; i < arr.length; i++) {
    if (arr[i] > x) {
      y = x;
      x = arr[i];
    } else if (arr[i] > y) {
      y = arr[i];
    }
  }
  console.log(y);
}
