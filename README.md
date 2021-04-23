# Release Notes

## Current Features

- Version number 1.0
- Collects articles from NIH, CDC, NY Times, LA Times, WHO, NEJM, and HealthyUNH.
- Maintains a custom Firebase database to store medical publications.
- Front end newsfeed displays articles from database.
- Articles can be filtered by tags to show articles relevant to the user.

There are currently no known bugs or defects in the project.

# Install Guide

## Python Scraper

Pre-requisites:

- Python 3.6 installation
- Set up Firebase project with initialized Realtime Database

Dependent libraries that must be installed:

- Feedparser >= 6.0.2 (from pip)
- Firebase-admin >= 4.5.1 (from pip)

Download instructions:

- Clone repository from <http://github.com/wjacobc/jie0333>

Build instructions (if needed):

- None

Installation of actual application:

- Valid API keys for the firebase_admin SDK must be placed in scraper/creds/credentials.json.
- Follow the instructions from Firebase on this [documentation page](https://firebase.google.com/docs/admin/setup#python), up to and including the section titled “To generate a private key file for your service account”. Then store that key in the file listed above.
- If all dependent libtaries listed above have been installed, the application is ready to be run.

Run instructions:

- Run python scraper.py from the command line, or set up a cronjob or cloud function to run the scraper periodically.

## React Frontend

Pre-requisites:

- Functional server environment, existing React project to integrate Newsfeed into

Dependent libraries that must be installed:

- Node.js and npm for package management
- All Node packages listed in frontend/package.json, generally what is required for a single-page React application and Chakra-UI

Download instructions:

- Clone repository from [http://github.com/wjacobc/jie0333](http://gllyithub.com/wjacobc/jie0333)

Build instructions (if needed):

- None

Installation of actual application:

- Run npm install to install all dependecies listed in package.json
- Valid API keys for client access to the Firebase Realtime Database must be placed in src/firebase_config.js
- Follow the instructions from Firebase on [this documentation page](https://firebase.google.com/docs/web/setup#with-npm_1), up to and including the section titled “Learn about the Firebase config object”. Then store that key in the file listed above.
- If all dependent libtaries listed above have been installed, the application is ready to be run.

Run instructions:

- Either use npm start to run the project as a single-page React app, or import the package into a different React project to use it as a component named Newsfeed.
