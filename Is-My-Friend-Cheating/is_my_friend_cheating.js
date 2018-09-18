function removeNb(n) {
  let sum = n * (1 + n) / 2;
  let products = [];
  for (let a = 1; a < n; a++) {
    let b = (sum - a) / (a + 1);
    if (b > n) continue;
    if (b % 1 != 0) continue;
    products.push([a, b]);
  }
  return products;
}
