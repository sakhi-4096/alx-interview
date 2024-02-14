#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');
const API_URL = 'https://swapi.dev/api';


if (process.argv.length > 2) {
    // Make an HTTP request to fetch information about the specified film
    request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
        if (err) {
            console.error('Error fetching film information:', err);
            return;
        }
        // Parse the response body to extract character URLs
        const charactersURL = JSON.parse(body).characters;

        // Map each character URL to a Promise that fetches the character's name
        const charactersNamePromises = charactersURL.map(url => {
            return new Promise((resolve, reject) => {
                request(url, (promiseErr, __, charactersReqBody) => {
                    if (promiseErr) {
                        // Reject the Promise if an error occurs during the request
                        reject(promiseErr);
                        return;
                    }
                    // Resolve the Promise with the character's name parsed from the response body
                    resolve(JSON.parse(charactersReqBody).name);
                });
            });
        });

        // Wait for all character name Promises to resolve
        Promise.all(charactersNamePromises)
            .then(names => {
                console.log(names.join('\n'));
            })
            .catch(allErr => {
                console.error('Error fetching character names:', allErr);
            });
    });
} else {
    console.error('Please provide a film ID as a command-line argument.');
}
