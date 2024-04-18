#!/usr/bin/node
const request = require('request');

const path = process.argv[2];
const filmEndpoint = `https://swapi.dev/api/films/${path}`;
function person (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (response.statusCode === 200) {
        const person = JSON.parse(body);
        const name = person.name;
        resolve(name);
      } else {
        reject(error);
      }
    }
    );
  }
  );
}

function getCharacters (filmEndpoint) {
  return new Promise((resolve, reject) => {
    request(filmEndpoint, (error, response, body) => {
      if (response.statusCode === 200) {
        const result = JSON.parse(body);
        const characters = result.characters;
        resolve(characters);
      } else {
        reject(error);
      }
    });
  }
  );
}
getCharacters(filmEndpoint).then((characters) => {
  const listPromises = characters.map(person);
  return Promise.all(listPromises);
}
).then((names) => {
  names.forEach((name) => {
    console.log(name);
  });
}).catch((error) => {
  console.error('An error occured', error);
});
