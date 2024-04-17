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
      data.characters.forEach(charaterUrl => {
        request(charaterUrl, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            console.log(error);
          }

          const characterData = JSON.parse(body);
          console.log(characterData.name);
        });
      });
    } catch (error) {
      console.log(error);
    }
  });
}

StarWarsApi();
