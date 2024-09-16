# Just-Another-CRUD-REST-API
To-do lists CRUD app but also using REST API principles.

This is a simple Flask-based Todo application that allows users to manage tasks (todos). The app supports both web and API interactions.

Features
-View Todos: Display all todos on the homepage.
-Add Todo: Add a new task via form or JSON API.
-Edit Todo: Modify existing tasks.
-Delete Todo: Remove tasks from the list.
-API Endpoints: Perform CRUD operations using JSON requests.

Routes
Web Routes

-GET / - Displays all todos.
-GET /add - Shows the form to add a new todo.
-POST /add - Submits the new todo form.
-GET /edit/<int:id> - Shows the form to edit an existing todo.
-POST /edit/<int:id> - Submits the updated todo.
-POST /delete/<int:id> - Deletes a specific todo.

API Routes

-GET /todos - Retrieves all todos in JSON format.
-POST /todos - Adds a new todo via JSON.
-PUT /todos/<int:id> - Updates a todo via JSON.
-DELETE /deletejson/<int:id> - Deletes a todo via JSON

Dependencies
-Flask
-MySQL
