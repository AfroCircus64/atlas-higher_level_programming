#!/usr/bin/node
const request = require('request');
const characterId = '18/';
const filmApiUrl = process.argv[2];

request(filmApiUrl, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let movieCount = 0;

    films.forEach(function (film) {
      if (film.characters.includes(characterId)) {
        movieCount++;
      }
    });

    console.log(movieCount);
  } else {
    console.error(err);
  }
});
