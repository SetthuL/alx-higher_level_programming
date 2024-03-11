#!/usr/bin/node

function factorial (sl) {
  if (sl < 0) {
    return (-1);
  }
  if (sl === 0 || isNaN(sl)) {
    return (1);
  }
  return (sl * factorial(sl - 1));
}

console.log(factorial(Number(process.argv[2])));
