#!/usr/bin/node

const { request } = require('http');

request = require('request')

const id = parseInt(process.argv[2]);
const url = `https://swapi.dev/api/films/${id}/`;

request(url, (error, response, body) => {
    if (response.statusCode === 200) {
        console.log(body);
    }

})