import { Input, InputGroup, InputRightAddon, Button } from "@chakra-ui/react";
import React from "react";
import ListObject from "./listObject.js"

function SearchObject() {
    const [value, setValue] = React.useState("")
    const handleClick = (event) => {
        ListObject(value)
        console.log(value)
    }

    return (
        <InputGroup size="lg">
            <Input
                w="70%"
                value={value}
                placeholder="Search for Headline"
                onChange={event => setValue(event.target.value)} />

            <InputRightAddon>
                <Button size="sm" onClick={handleClick}>Search</Button>
            </InputRightAddon>
        </InputGroup>
    )
}

export default SearchObject
