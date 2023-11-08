#!/usr/bin/node

const request = require('request');

/**
 * function to process a characters info
 * @param {string} url : movies character link
 * @returns {Promise}
 */
function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        resolve(character.name);
      } else {
        reject(error);
      }
    });
  });
}

/**
 * function to handle films' responses
 * @param {Error} error: response error
 * @param {Response} response : http response
 * @param {JSON} body : http JSON response body
 */
async function handleRequestData (error, response, body) {
  const charactersNames = [];

  if (!error && response.statusCode === 200) {
    const filmObj = JSON.parse(body);
    const charactersLinkArr = filmObj.characters;

    try {
      for (const url of charactersLinkArr) {
        const characterData = await fetchCharacter(url);
        charactersNames.push(characterData);
      }

      charactersNames.forEach((name) => {
        console.log(name);
      });
    } catch (err) {
      console.error(err);
    }
  } else {
    console.error(error);
  }
}

/**
 * function to query film's data
 * the start point
 */
function getCharactersData () {
  const filmID = process.argv.slice(2)[0];
  request.get(
    'https://swapi-api.alx-tools.com/api/films/' + filmID,
    handleRequestData
  );
}

getCharactersData();
