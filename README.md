# groupmeData
This program has several functions useful for getting data from GroupMe.

## To start:
You'll need an access token from GroupMe to use the api. You can get one by logging in to https://dev.groupme.com/ and clicking 'access token' at the top. Put that (as a string) as the variable accessToken. Here's a link to the docs...I've found a few typos and what the exact format of what's returned isn't always what they say, but for the most part they're pretty good. https://dev.groupme.com/docs/v3

## getGroups()
Prints an unformatted json object...kind of a hassle to read but it's doable. You can get group names, IDs (needed for getBreakdown), etc.

## getBreakdown()
Prints a breakdown of how much each user has contributed to the chat. You can get the groupID by calling getGroups. For each user, you'll get name, percent of messages that are by them, and number of messages by them, plus the total number of users and messages. The user GroupMe itself is what posts stuff like "person just joined the chat".
