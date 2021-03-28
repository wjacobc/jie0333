import "./App.css";
import firebase from "./firebase_config";
import { ChakraProvider, Box } from "@chakra-ui/react";
import ListObject from "./listObject.js";
import SearchObject from "./searchObject.js";
import theme from "./theme.js"

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
    	<div>
	    	<Box>{SearchObject()}</Box>
	        <Box>{ListObject()}</Box>
	    </div>
    );
}

export default App;
