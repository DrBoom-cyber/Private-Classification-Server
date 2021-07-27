# Private-Classification-Server
Allows users to log into the server, after which they will be presented with data items, and may sort them into user defined categories.

# Testing
There is one test user already registered to the database. The username is 'admin' and the password is empty.

# Deployment
It is recommended to change the pepper to a random value of your choosing. This can be found in the database/config.json file. Note that any users created before changing the pepper will become unusable, since their passwords will not authenticate correctly.