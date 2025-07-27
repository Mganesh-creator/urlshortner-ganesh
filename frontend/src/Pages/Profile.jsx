import React, { useState } from "react";

import Service from "../utils/http";
import { Avatar, Container, Stack, Text } from "@mantine/core";
import { useEffect } from "react";
const service = new Service();
export default function Profile() {
  const [profileData, setProfileData] = useState(null);

  async function getProfileData() {
    let data = await service.get("user/me");
    setProfileData(data);
    console.log(data);
  }
  useEffect(() => {
    getProfileData();
  }, []);

  return (
    <Container>
      <Stack
        h={500}
        bg="var(--mantine-color-body)"
        align="center"
        justify="center"
        gap="lg"
      >
        <Avatar
          variant="outline"
          radius="xl"
          size="xl"
          color="pink"
          src={profileData?.avatar}
        />
        <Text tt="">
          {" "}
          <strong>Email: </strong>:{profileData?.email}
        </Text>
        <Text tt="capitalize">
          <strong>Name: </strong>
          {profileData?.name}
        </Text>
      </Stack>
    </Container>
  );
}
