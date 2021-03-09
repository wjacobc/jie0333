import logo from "./logo.svg";
import "./App.css";
import firebase from "./firebase_config";
import { useEffect } from "react";

let newsitems = [];

function App() {
  // the hook that retrieves all newsitems from database
  useEffect(() => {
    let ref = firebase.database().ref("newsitems");
    ref.on("value", (snapshot) => {
      newsitems = snapshot.val();
      // test
      console.log(newsitems);
    });
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
