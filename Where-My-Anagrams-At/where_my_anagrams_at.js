const lower = "abcdefghijklmnopqrstuvwxyz".split("");

function alphabetize(string) {
  return string.split("").sort().join("");
}

function anagrams(word, words) {
  let alpha = alphabetize(word);
  let alphas = words.map(alphabetize);

  let list = [];
  for (let [key, value] of alphas.entries()) {
    if (value == alpha) {
      list.push(words[key]);
    }
  }
  return list;
}
