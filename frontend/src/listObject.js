import firebase from "./firebase_config";
import { ChakraProvider, List, ListItem, Modal, ModalOverlay, ModalContent, ModalHeader, ModalBody, ModalCloseButton, ModalFooter, Button, useDisclosure, Divider } from "@chakra-ui/react";
import React from "react";

const data = require("./test_data.json").newsitems;
const keys = Object.keys(data);

function ListObject(titleSearch) {
	const articleList = [];
	if (arguments.length === 0) {
		for (var i = 0; i < keys.length; i++) {
			articleList.push(SetListItem(data[keys[i]]));
		}
	} else {
		for (var j = 0; j < keys.length; j++) {
			if (data[keys[i]].headline.includes(titleSearch)) {
				articleList.push(SetListItem(data[keys[j]]));
			}
		}
	}
	console.log(articleList);
	return(
		<List>
			{articleList}
		</List>
	);
}

// export const setList = function(titleSearch) {
// 	const articleList = [];
// 	for (var i = 0; i < keys.length; i++) {
// 		if (data[keys[i]].headline.contains(titleSearch)) {
// 			articleList.push(setListItem(data[keys[i]]));
// 		}
// 	}
// 	return(
// 		<List>
// 			{articleList}
// 		</List>
// 	);
// }

function SetListItem(article) {

	const { isOpen, onOpen, onClose } = useDisclosure()

	return(
		<>
			<ListItem key={article.url} bg="#80ccff" w="75%" onClick={onOpen} rounded="md">
				<div> <b>{article.headline}</b> </div>
				<div> {article.publish_date} </div>
				<div> {article.snippet} </div>
				<div> {article.source} </div>
				<div> <a href = {article.url}> Link </a> </div>
			</ListItem>
			<Divider variant="solid"/>
			<Modal isOpen={isOpen} onClose={onClose}>
				<ModalOverlay />
				<ModalContent>
					<ModalHeader>{article.headline}</ModalHeader>
					<ModalCloseButton />
					<ModalBody>{article.snippet}</ModalBody>
					<ModalFooter>
						<Button onClick={onClose}>Close</Button>
						<Button onClick={article.url}>Link</Button>
					</ModalFooter>
				</ModalContent>
			</Modal>

			
		</>
	);
}

export default ListObject;