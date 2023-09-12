const { dict } = require('./101-data');
const res = {};

for (const key in dict) {
  if (res[dict[key]]) {
    res[dict[key]].push(key);
  } else {
    res[dict[key]] = [key];
  }
}
console.log(res);
