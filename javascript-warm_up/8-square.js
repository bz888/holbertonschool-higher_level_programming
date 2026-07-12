#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
}

for (let index = 0; index < size; index++) {
  let row = '';

  for (let width = 0; width < size; width++) {
    row += 'X';
  }

  console.log(row);
}
