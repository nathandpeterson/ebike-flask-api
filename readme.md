## REST API for an e-bike e-commerce website.

Built with Flask, Flask-RESTful, and SQLAlchemy

Routes:
### ebike routes
* GET '/ebikes' : returns all ebikes in db
* GET '/ebike/<name>' : returns an ebike with name
* POST '/ebike/<name>' : adds an ebike with name
* DELETE '/ebike/<name>' : deletes an ebike from db
* PUT '/ebike/<name>' : updates info about an ebike
### user routes
* GET '/user/<email>' : returns the account information for the user
* POST '/user/<email>' : adds a new user to the db
* GET '/users' : returns all users
