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

        return(
                <List>
                        {articleList}
                </List>
        );
}

function generateTagString(tags) {
    // remove the list format text
    tags = tags.replace("[", "");
    tags = tags.replace("]", "");
    tags = tags.replaceAll("'", "");
    return tags;
}

function SetListItem(article) {

    let tagString = generateTagString(article.tags);

    return(
        <div class = "newsitem">
            <ListItem key={article.url} rounded="md">
                <div class = "headline">
                    <a href = {article.url}><b>{article.headline}</b></a>
                </div>

                <div class = "source">{article.source}</div>
                <div>{article.publish_date}</div>
                <div>{article.snippet}</div>

                <div class = "tags">Tags: {tagString}</div>
            </ListItem>
        </div>
    );
}

export default ListObject;
