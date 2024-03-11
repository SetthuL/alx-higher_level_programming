#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let sl = 0; sl < x; sl++) {
    theFunction();
  }
};
