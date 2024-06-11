# SimpleDjangoCMS

## Description
SimpleDjangoCMS is a simple web application built with Django that allows users to create, edit, and delete articles. The site also includes several static pages such as "About Us", "News", "Contact", and more.

## Main Features
- **Admin Panel**: Fully functional admin panel for managing content and users.
- **Article Management**: Users can create, edit, and delete their own articles.
- **Static Pages**: The site includes predefined pages such as "About Us", "News", "Contact", etc.
- **Authentication and Authorization**: User registration and login system.

## Installation and Setup
To install and run the project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/DjangoBlog.git
    cd DjangoBlog
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

4. Create a superuser for accessing the admin panel:
    ```sh
    python manage.py createsuperuser
    ```

5. Start the server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the running site.

## Requirements
- Python 3.x
- Django 3.x or higher

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

