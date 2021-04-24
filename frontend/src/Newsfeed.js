import "./App.css";
import React, { useState, useEffect } from "react";
import firebase from "./firebase_config";
import { Box, Text, Heading, Flex, Spacer } from "@chakra-ui/react";
import ListObject from "./listObject.js";
import SearchObject from "./searchObject.js";

function Newsfeed(props) {
    const [newsitems, setNewsitems] = useState([]);
    const [allNewsitems, setAllNewsitems] = useState([]);

    const userTags = ["COVID-19"];

    useEffect(() => {
        var newsList = [];
        let ref = firebase.database().ref("newsitems");
        ref.on("value", (snapshot) => {
            const data = snapshot.val();
            for (const key in data) {
                const article = data[key];
                const formattedTagString =
                    article.tags.replaceAll("'", "\"").replaceAll("True", "true")
                        .replaceAll("False", "false");
                const tags = JSON.parse(formattedTagString);
                if (Object.keys(tags).some(tag => userTags.includes(tag))) {
                    newsList.push(article);
                }
            }
        }, function(error) {
            console.error(error)
        });

        setNewsitems(newsList);
        setAllNewsitems(newsList);
    }, []);


    function filterArticles(filterString) {
        var newList = [];
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
