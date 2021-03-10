import "./App.css";
import firebase from "./firebase_config";
import { ChakraProvider, Heading } from "@chakra-ui/react";

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
        <ChakraProvider>
            <Heading>Testing Chakra elements</Heading>
        </ChakraProvider>
    );
}

export default App;
