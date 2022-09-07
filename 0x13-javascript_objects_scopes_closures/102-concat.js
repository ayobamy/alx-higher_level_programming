#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const fileOne = fs.readFileSync(args[2], 'utf8').toString;
const fileTwo = fs.readFileSync(args[3], 'utf8').toString;

fs.writeFileSync(args[4], fileOne + fileTwo);
