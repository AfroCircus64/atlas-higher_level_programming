#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) throw err;
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed && task.userId) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
