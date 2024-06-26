#!/usr/bin/node

const process = require('process');
const request = require('request');

async function StarWarsApi () {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

  request(url, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.log(error);
    }

    try {
      const data = JSON.parse(body);
      // console.log(data);
      const characters = data.characters;
      printCharacterNames(characters, 0);
    } catch (error) {
      console.log(error);
    }
  });
}

function printCharacterNames (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error(error);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);

    printCharacterNames(characters, index + 1);
  });
}

StarWarsApi();
