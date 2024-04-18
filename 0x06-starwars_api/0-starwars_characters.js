#!/usr/bin/node
const request = require('request');

const path = process.argv[2];
const filmEndpoint = `https://swapi.dev/api/films/${path}`;

/* Create a function for making request to each person endpoints
 * in characters array
 */

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

/* A funcion that makes a request to a film endpoint and returns an characters attribute
 * which is an array of person endpoints in a particular file
 */

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
/* calling the getcharacter function to the the character and subsequently
 * make a request to each person endpoint in the character array
 */

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
