#!/usr/bin/node
exports.esrever = function (list) {
  const revarr = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    revarr[j] = list[i];
    j++;
  }
  return revarr;
};
