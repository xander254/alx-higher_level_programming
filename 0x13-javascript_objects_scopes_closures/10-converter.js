#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number === 0) return '0';
    const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = '';
    let n = number;

    while (n > 0) {
      result = digits[n % base] + result;
      n = Math.floor(n / base);
    }

    return result;
  };
};
