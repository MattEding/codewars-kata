function gcd(a, b) {
  if (!b) {return a}
  return gcd(b, a % b);
}

function lcm(a, b) {
  return a * b / gcd(a, b)
}

function convertFrac(fractions) {
  let result = "";
  if (!fractions.length) {return result}

  let numerators = fractions.map(f => f[0]);
  let denominators = fractions.map(f => f[1]);
  let lcd = denominators.reduce(lcm);

  for (let [i, n] of numerators.entries()) {
    let num = n * lcd / denominators[i];
    result += `(${num},${lcd})`
  }
  return result;
}
