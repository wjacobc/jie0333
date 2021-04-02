import "./App.css";
import firebase from "./firebase_config";
import { ChakraProvider, Box, Heading, Flex, Spacer } from "@chakra-ui/react";
import ListObject from "./listObject.js";
import SearchObject from "./searchObject.js";
import theme from "./theme.js"

let newsitems = [];

function getFirebaseNewsItems() {
    let ref = firebase.database().ref("newsitems");
    ref.on("value", (snapshot) => {
        newsitems = snapshot.val();
        return newsitems;
    });
}

function App() {
    return (
        <div class = "app">
            <Flex>
                <Heading class = "header">Your <strong>Newsfeed</strong></Heading>
                <Spacer />
                <Box width = "400px">{SearchObject()}</Box>
            </Flex>
            <Box>{ListObject()}</Box>
        </div>
    );
}

export default App;
