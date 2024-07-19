#!/usr/bin/node
const args = process.argv.slice(2);

function secondBiggest (args) {
  if (args.length === 0) {
    console.log(0);
    return;
  }
  if (args.length === 1) {
    console.log(0);
    return;
  }
  args.sort((a, b) => b - a);
  console.log(args[1]);
}

secondBiggest(args);
