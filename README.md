# Kick.com Python Client

Client to use the Kick.com API and the Chat.
This repo is under development and not ready to use. 

## Packages Used

To develop i used Python 3.9.13 the packages used are:

 - requests to handle the api calls
 - websocket-client to interact with the Kick.com chat websockets


## Installation
To install and use the code you have to install the requiremeints.txt via pip


## Usage

In the firtst commit you have to change the chatroom you want to connect. You do this in the *src/client/baseclient.py*. 
In this file is the Chatroom ID hardcoded in line 29. Just change it to whatever you need. 

To get the ID of the chatroom you have to call the Kick API URL:

> https://kick.com/api/v1/channels/USERNAME

In the json response you can find the chatroom ID.


To use the client you have to create a BaseClient:

> from  src.client.baseclient  import  BaseClient
> 
> bc = BaseClient().get_client()

After creating an client you can start the client with

> bc.run_forever(dispatcher=rel, reconnect=5)

If the client is connected and an message is send in the websocket, the client creat an Message Class. See on Message Class below.

You can now call a class you want Like in this repo the *src/messagehandler/commands.py* Commands Class.


# Classes

Description the Classes

## Message

|Name| Descriptoion |
|--|--|
| message | message send |
| messageID | ID of the message |
| messagecontent | the message of the user |
| role | role of the sender |
| isMod | bool sender is mod or not |
| chatroom_id | id of the chatroom |
| created_at | date send the message |

Unused

|Name| Descriptoion |
|--|--|
|type|message type|
|replied_to|replay to message|
|link_preview|preview of a link|
|optional_message|Unknow|
