# messanger-api
Messenger API with ability to create, retrieve, delete messages

<h2>Overview</h2>
Project stored on Heroku: https://messenger-api-nb.herokuapp.com/
You can test API with Postman: https://www.getpostman.com/collections/ee33061c4d4d9d6ff113

<h2>Using this API user can</h2>
<ul>
  <li>Retrieve all messages</li>
  <li>Write a new message</li>
  <li>Get all messages of a specific user</li>
  <li>Get all undread messages for a specific user</li>
  <li>Read message (will return the text of a single message)</li>
  <li>Delete message (as sender or as a receiver)</li>
</ul>

<h2>How to use</h2>
Follow the Postman link to see the collection of saved requests.

<h4>Retrieve all messages</h4>
To get all the message you just need to follow https://messenger-api-nb.herokuapp.com/

<h4>Write a new message</h4>
<ul>
<li>Add a name of the Sender to the URL after the '/' (e.g. https://messenger-api-nb.herokuapp.com/Avi)</li>
<li>The body of the request should contain the following keys: "receiver", "subject", "message"</li>
Note: method POST
</ul>

<h4>Get all messages of a specific user</h4>
<ul>
<li>Add a name of the Sender to the URL after the '/' (e.g. https://messenger-api-nb.herokuapp.com/Avi)</li>
for now simple logic was implemented - it is possible add another argument that will check if the provided user name should be Sender or Reciever. The same logic I used for Retrieving specific message. You can choose the role of the user there.
Note: method GET
</ul>

<h4>Get all undread messages for a specific user</h4>
<ul>
<li>Follow the link https://messenger-api-nb.herokuapp.com/unread-messages)</li>
<li>The body of the request should contain the following keys: "status", "sender"</li>
Also possible to add the logic from Retrieving specific message to have a choice of the role (sender, receiver)
</ul>

<h4>Read message (will return the text of a single message)<h4>
 <ul>
<li>Follow the link (e.g. https://messenger-api-nb.herokuapp.com/single-message)</li>
<li>The body of the request should contain the following key: "subject"</li>
</ul>
  
<h4>Delete message (as sender or as a receiver)</h4>
<li>Add a name of the Sender to the URL after the '/' https://messenger-api-nb.herokuapp.com/Gabi</li>
<li>The body of the request should contain the following keys: "subject", "role"
