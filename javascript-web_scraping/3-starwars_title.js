#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(apiUrl, function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
