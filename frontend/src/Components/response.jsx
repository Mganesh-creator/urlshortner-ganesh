import React from "react";
import Service from "../utils/http";
import { Anchor, Button, Card,Container , Group, Title, Space } from "@mantine/core";

const service = new Service();

export default function Response(props) {
  const baseUrl = service.getBaseURL();
  const redirectUrl = `${baseUrl}/api/s/${props?.response?.shortCode}`;

  return (
     <Container>
      <Stack
      h={300}
      bg="var(--mantine-color-body)"
      align="center"
      justify="center"
      gap="md"
    >
       <Anchor href={redirectUrl}target="_blank">
      Short url
    </Anchor>
      <Button
          onClick={() => props.setResponse(null)}
        >
          {" "}
          Clear Response{" "}
        </Button>
      </Stack>
     </Container>
  )
}
