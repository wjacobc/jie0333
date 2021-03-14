import firebase from "./firebase_config";
import { ChakraProvider, List, ListItem } from "@chakra-ui/react";
import React from "react";

const data = require("./test_data.json").newsitems;
const keys = Object.keys(data);

export const setList = function() {
	const articleList = [];
	for (var i = 0; i < keys.length; i++) {
		articleList.push(setListItem(data[keys[i]]));
	}
	return(
		<List>
			{articleList}
		</List>
	);
}

function setListItem(article) {
	return(
		<ListItem bg="grey" w="50%">
			<div> <h2>{article.headline}</h2> </div>
			<div> {article.publish_date} </div>
			<div> {article.snippet} </div>
			<div> {article.source} </div>
			<div> <a href = {article.url}> Link </a> </div>
		</ListItem>
	);
}

export default setList;