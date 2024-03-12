#!/usr/bin/node

function reverseList(list) {
let len = list.length - 1;
  let sl = 0;
  while ((len - sl) > 0) {
    const aux = list[len];
    list[len] = list[sl];
    list[sl] = aux;
    sl++;
    len--;
  }
  return list;
};
