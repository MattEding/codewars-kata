function counter(iterable) {
  let map = new Map();
  for (item of iterable) {
    if (!map.has(item)) {map.set(item, 1);}
    else {map.set(item, map.get(item) + 1);}
  }
  return map;
}

function firstNonRepeatingLetter(string) {
  let counts = counter(string.toLowerCase());
  let first = "";
  for (let [char, count] of counts) {
    if (count == 1) {
      first = char;
      break;
    }
  }
  let regex = new RegExp(first, "i");
  let match = string.match(regex)[0];
  return match;
}
