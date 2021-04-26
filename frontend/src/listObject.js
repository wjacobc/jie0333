import { List, Text, ListItem } from "@chakra-ui/react";

function ListObject(props) {
    if (props.newsitems === [] || props.newsitems == undefined) {
        // this means no articles for that filter or tag were found
        return(
            <Text>Sorry, no articles could be found!</Text>
        );
    } else {
        return(
            <List>
                {props.newsitems.map((item) => <NewsListItem article = {item} />)}
            </List>
        );
    }
}

function generateTagString(tags) {
    var tagString = "";
    for (const tag in tags) {
        tagString += tag + ", ";
    }
    return tagString.slice(0, tagString.length - 2);
}

function NewsListItem(props) {

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
