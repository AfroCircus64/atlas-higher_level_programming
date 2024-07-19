#!/usr/bin/node
const x = parseInt(process.argv[2]);

function factorial (x) {
  let product = 1;
  for (let i = 1; i <= x; i++) {
    product *= i;
  }
  console.log(product);
}

factorial(x);
