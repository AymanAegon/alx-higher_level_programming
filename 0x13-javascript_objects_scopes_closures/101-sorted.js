const { dict } = require("./101-data");
let res = {}, i = 0;

for (let key in dict) {
  if (res[dict[key]]) {
    res[dict[key]].push(key);
  } else {
    res[dict[key]] = [key];
  }
}
console.log(res);
