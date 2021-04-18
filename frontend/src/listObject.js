import { List, Text, ListItem } from "@chakra-ui/react";
import React, { useState, useEffect } from "react";

function ListObject(props) {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        for (const item in props.newsitems[0]) {
            var articleList = [];
            articleList.push(props.newsitems[0][item]);
        }
        setArticles(articleList);
    }, []);

    console.log(articles);
    return(
        <List>
            {articles}
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

function NewsListItem(props) {

    console.log(props.article);
    let tagString = generateTagString(props.article.tags);

    return(
        <div class = "newsitem">
            <ListItem key={props.article.url} rounded="md">
                <div class = "headline">
                    <a href = {props.article.url} target = "blank"><b>{props.article.headline}</b></a>
                </div>

                <div class = "source">{props.article.source}</div>
                <div>{props.article.publish_date}</div>
                <div>{props.article.snippet}</div>

                <div class = "tags">Tags: {tagString}</div>
            </ListItem>
        </div>
    );
}

export default ListObject;
