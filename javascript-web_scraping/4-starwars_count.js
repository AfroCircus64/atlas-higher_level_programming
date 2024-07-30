#!/usr/bin/node
const request = require('request');
const characterId = '18/';
const filmApiUrl = process.argv[2];
const characterApiUrl = 'https://swapi-api.hbtn.io/api/people/';

request(filmApiUrl, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let movieCount = 0;

    films.forEach(function (film) {
      const characters = film.characters;
      if (characters.includes(characterApiUrl + characterId)) {
        movieCount++;
      }
    });
    console.log(movieCount);
  }
});
