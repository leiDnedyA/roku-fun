#!/bin/bash

response=$(curl https://www.roku.com/api/v1/sow/content/v1/roku/b54e4af702bf5e6fa63fed39742aecd4-1)
playId=$(echo "$response" | jq -r '.view.viewOptions[] | select(.channelName == "Disney Plus") | .playId')
