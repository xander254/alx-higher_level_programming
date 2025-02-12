#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);

  const userCompletedTasks = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (userCompletedTasks[task.userId]) {
        userCompletedTasks[task.userId]++;
      } else {
        userCompletedTasks[task.userId] = 1;
      }
    }
  });

  Object.entries(userCompletedTasks).forEach(([userId, count]) => {
    console.log(`User ${userId} completed ${count} tasks`);
  });
});

