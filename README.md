# To-Do List App with Angular and Django

## Overview

This project is a simple To-Do List application built using the Angular framework for the frontend and the Django framework for the backend. It provides a user-friendly interface for managing tasks, allowing users to create, update, delete, and mark tasks as completed.

## Features

- **User Authentication:** Users can create accounts, log in, and log out to manage their own to-do lists securely.
  
- **Task Management:** Create, edit, delete, and mark tasks as completed or incomplete.

- **Responsive Design:** The application is designed to be responsive, ensuring a seamless experience across various devices.

## Technologies Used

- **Frontend:**
  - Angular (Version X.X)
  - Angular Material for UI components
  
- **Backend:**
  - Django (Version X.X)
  - Django REST Framework for building APIs
  
- **Database:**
  - SQLite (for development)
  - Consider using a more robust database (e.g., PostgreSQL) for production

## Setup Instructions

1. **Frontend:**
   - Navigate to the `frontend` directory.
   - Run `npm install` to install dependencies.
   - Run `ng serve` to start the development server.

2. **Backend:**
   - Navigate to the `backend` directory.
   - Create a virtual environment: `python -m venv venv`.
   - Activate the virtual environment: `source venv/bin/activate` (Linux) or `venv\Scripts\activate` (Windows).
   - Install dependencies: `pip install -r requirements.txt`.
   - Run migrations: `python manage.py migrate`.
   - Start the Django development server: `python manage.py runserver`.

3. **Access the App:**
   - Open your browser and go to `http://localhost:4200` to access the Angular frontend.
   - The Django backend can be accessed at `http://localhost:8000`.

## Folder Structure

/to-do-list
|-- frontend
| |-- src
| |-- angular.json
| |-- ...
|-- backend
| |-- manage.py
| |-- todo
| |-- settings.py
| |-- ...
|-- README.md
|-- requirements.txt


## Contributions

Contributions are welcome! If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md).
