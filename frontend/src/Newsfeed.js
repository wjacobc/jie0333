import "./App.css";
import React, { useState, useEffect } from "react";
import firebase from "./firebase_config";
import { Box, Text, Heading, Flex, Spacer } from "@chakra-ui/react";
import ListObject from "./listObject.js";
import SearchObject from "./searchObject.js";

function Newsfeed(props) {
    // use React state, and keep a list of all the newsitems so that we
    // can filter the ones that are currently shown based on user input
    // in the search bar
    const [newsitems, setNewsitems] = useState([]);
    const [allNewsitems, setAllNewsitems] = useState([]);


    useEffect(() => {
        // To the client: get the user's tags here
        const userTags = ["Asthma", "Ebola"];

        // limit the number of articles per topic, as the scraper continues
        // to store more data we may not always want to get all the articles
        // dating back in perpetuity
        const articleLimit = 25;

        var newsList = [];

        let ref = firebase.database().ref("newsitems");

        for (const tag of userTags) {
            ref.orderByChild("tags/" + tag).equalTo(true)
            .limitToLast(articleLimit).on("value", (snapshot) => {
                const data = snapshot.val();

                // get each article in the returned list, and add it to
                // the front-end storage list if it's not already in there
                for (const key in data) {
                    const article = data[key];
                    if (!newsList.includes(article)) {
                        newsList.push(article);
                    }
                }

            }, function(error) {
                console.error(error)
            });
        }

        // Firebase can only give use the articles in oldest -> newest order
        // if we do server-side filtering for tags, since only one orderByChild
        // call is allowed, so we sort client-side
        newsList = newsList.sort((a, b) => (a.publish_date < b.publish_date) ? 1 : -1);

        setNewsitems(newsList);
        setAllNewsitems(newsList);
    }, []);


    function filterArticles(filterString) {
        var newList = [];

        // check if each newsitem has the searched for string
        // in the headline, the snippet, or the tags
        for (const newsitem of allNewsitems) {
            if (newsitem.headline.includes(filterString) ||
                newsitem.snippet.includes(filterString) ||
                newsitem.tags.includes(filterString)) {
                newList.push(newsitem);
            }
        }

        setNewsitems(newList);
    }


    return (
        <div class = "app">
            <Flex>
                <Heading class = "header">Your <strong>Newsfeed</strong></Heading>
                <Spacer />
                <Box width = "400px">
                    <SearchObject modifyFunction = {filterArticles} />
                </Box>
            </Flex>
            <Box>
                <ListObject newsitems = {newsitems} />
            </Box>
        </div>
    );
}

export default Newsfeed;
