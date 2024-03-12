#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let sl = 0; sl < this.height; sl++) {
      let s = '';
      for (let hn = 0; hn < this.width; hn++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}
module.exports = Rectangle;
