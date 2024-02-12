# Kaizntree Dashboard

Kaizntree Dashboard is a Django-based web application designed to manage inventory and sales data.

## Features

- **Dashboard:** View a summary of inventory items including finished products, raw materials and packaging.
- **Filtering:** Filter inventory items based on stock status.
- **Authentication:** Secure login and logout functionality.
- **Caching:** Local caching is implemented for optimizing performance.

## Technologies Used

- Django Rest Framework: For building RESTful APIs.
- DRF Yasg: Generates Swagger/OpenAPI documentation for APIs.
- Bootstrap: Frontend framework for responsive design.
- AWS EC2: Hosting the application.
- Local caching: Implemented for performance optimization.

## Security
CSRF tokens are used to ensure security against cross-site request forgery (CSRF) attacks.

## Installation

1. Clone the repository:

```
git clone https://github.com/phs-sakshi/Kaizntree_App.git
cd Kaizntree_App
python -m venv .venv
source .venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt 
```

Set up database:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver
```
The application will be accessible at [KZ App](http://50.17.116.22:8000/).

Deployment
The application is deployed on an AWS EC2 instance and can be accessed via the following URLs:

Admin Panel (for adding items and item categories): [admin](http://50.17.116.22:8000/admin/)
Dashboard UI: Use the search, filtering and sorting options to customize the dashboard view - [dashboard](http://50.17.116.22:8000/dashboard/)
Swagger UI for API documentation: [api-docs](http://50.17.116.22:8000/api-docs/)

Database Selection (SQLite3)

Approach:
- Reasoning: SQLite3 was chosen as the database backend due to its simplicity, ease of setup, and suitability for small to medium-sized projects.
- Alignment with Project Requirements:
  - For this project, SQLite3 meets the requirements adequately as it provides the necessary functionality for storing and querying data without the need for complex database management.
  - Given the scope of the project, SQLite3 offers a lightweight solution that doesn't require additional server setup or maintenance, making it ideal for development and testing.
  - The dataset was well structured making SQL databases a pretty good fit

Front-end Technologies
Approach:
- Reasoning: Bootstrap was chosen as the front-end framework due to its ease of use, extensive documentation, and rich set of UI components.
- Alignment with Project Requirements:
   - Bootstrap allows for rapid development of responsive websites.
   - It provides ready-to-use CSS and JavaScript components that streamline the development process, saving time and effort.
   - Additionally, Bootstrap's popularity means that there is a wealth of community resources and third-party plugins available, making it easy to extend and customize as needed.


Code:
The Code is available on [github](https://github.com/phs-sakshi/Kaizntree_App)
Developer: Sakshi Sharma
