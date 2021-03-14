import "./App.css";
import firebase from "./firebase_config";
import { ChakraProvider, Heading, List, ListItem, Box } from "@chakra-ui/react";
import setList from "./listObject.js"

let newsitems = [];

function getFirebaseNewsItems() {
    let ref = firebase.database().ref("newsitems");
    ref.on("value", (snapshot) => {
        newsitems = snapshot.val();
        // test
        return newsitems;
    });
}

function App() {
    return (
        <div>{setList()}</div>
    );
}

export default App;
