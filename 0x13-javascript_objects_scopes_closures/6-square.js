#!/usr/bin/node

const Square_2 = require('./5-square');

class Square extends Square_2 {
  charPrint (c) {
    if (!c) {
      this.print();
    } 
    else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
