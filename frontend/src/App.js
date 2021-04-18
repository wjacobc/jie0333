import "./App.css";
import React, { useState, useEffect } from "react";
import firebase from "./firebase_config";
import { Box, Text, Heading, Flex, Spacer } from "@chakra-ui/react";
import ListObject from "./listObject.js";
import SearchObject from "./searchObject.js";

function App() {
    const [newsitems, setNewsitems] = useState([]);

    useEffect(() => {
        var newsList = [];
        let ref = firebase.database().ref("newsitems");
        ref.on("value", (snapshot) => {
            const data = snapshot.val();
            newsList.push(data);
        });

        console.log(newsList);
        setNewsitems(newsList);
    }, []);

    return (
        <div class = "app">
            <Flex>
                <Heading class = "header">Your <strong>Newsfeed</strong></Heading>
                <Spacer />
                <Box width = "400px">
                    {SearchObject()}
                </Box>
            </Flex>
            <Box>
                <ListObject newsitems = {newsitems} />
            </Box>
        </div>
    );
}

export default App;
