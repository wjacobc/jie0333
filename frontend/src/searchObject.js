import { Input, InputGroup, InputRightAddon, Button } from "@chakra-ui/react";
import React from "react";
import ListObject from "./listObject.js"

function SearchObject(props) {
    const [value, setValue] = React.useState("");
    const handleClick = function() {
        const textFieldValue = value;
        props.modifyFunction(textFieldValue);
    };

    const handleChange = (event) => {
        const newValue = event.target.value;
        setValue(newValue);
    };

    return (
        <InputGroup size="lg">
            <Input
                w="70%"
                placeholder="Search for Headline"
                onChange={handleChange} />

            <InputRightAddon>
                <Button size="sm" onClick={handleClick}>Filter</Button>
            </InputRightAddon>
        </InputGroup>
    )
}

export default SearchObject
