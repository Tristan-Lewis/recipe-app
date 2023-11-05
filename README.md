# recipe-app

Users will be able to create and modify recipes containing ingredients, cooking time, and a
difficulty parameter automatically calculated by the application. Users will also be able to search
for recipes by ingredient.

## Key Features

- Allow for user authentication, login, and logout.
- Let users search for recipes according to ingredients.
- Automatically rate each recipe by difficulty level.
- Receive user input and handle errors appropriately.
- Display more details on each recipe if the user asks for that.
- Add user recipes to an SQLite database.
- Include a Django Admin dashboard for working with database entries.
- Show statistics and visualizations based on trends and data analysis.

## Technical Requirements

- Works on Python 3.6+ installations and Django version 3.
- Handles exceptions or errors that arise during user input, for example, then displays user-friendly
error messages.
- Connects to a PostgreSQL database hosted locally on the same system (an SQLite database is
needed during the development of your application).
- Provides an easy-to-use interface, supported by simple forms of input and concise, easy-to-follow
instructions. Menus containing features like login and logout must be presented neatly—with
concise and easy-to-follow prompts.
- Code with proper documentation and automated tests is uploaded on GitHub. A
“requirements.txt” file is provided, containing the requisite modules for the project.
- Readme file is provided with instructions on downloading and running the app locally on any
machine.
