# Kaizntree Dashboard

Kaizntree Dashboard is a Django-based web application designed to manage inventory and sales data.

## Features

- **Dashboard:** View a summary of inventory items including finished products, raw materials and packaging.
- **Filtering:** Filter inventory items based on stock status.
- **Authentication:** Secure login and logout functionality.

## Technologies Used

- Django Rest Framework: For building RESTful APIs.
- DRF Yasg: Generates Swagger/OpenAPI documentation for APIs.
- Bootstrap: Frontend framework for responsive design.
- Memcached: Caching backend for performance optimization.

## Installation

1. Clone the repository:

```
git clone https://github.com/phs-sakshi/Kaizntree_App.git
cd Kaizntree_App
```
Install dependencies:
```
pip install -r requirements.txt 
```

Set up database:
```
python manage.py migrate
```
Run the development server:
```
python manage.py runserver
```
The application will be accessible at http://localhost:8000/.

Usage
Access the dashboard at http://localhost:8000/dashboard/.
Use the search, filtering and sorting options to customize the dashboard view.
APIs are documented using Swagger UI at http://localhost:8000/api-docs/.
Sign out when done.

Database Selection (SQLite3)

Approach:
- Reasoning: SQLite3 was chosen as the database backend due to its simplicity, ease of setup, and suitability for small to medium-sized projects.
- Alignment with Project Requirements:
  - For this project, SQLite3 meets the requirements adequately as it provides the necessary functionality for storing and querying data without the need for complex database management.
  - Given the scope of the project, SQLite3 offers a lightweight solution that doesn't require additional server setup or maintenance, making it ideal for development and testing.

Front-end Technologies
Approach:
- Reasoning: Bootstrap was chosen as the front-end framework due to its ease of use, extensive documentation, and rich set of UI components.
- Alignment with Project Requirements:
   - Bootstrap allows for rapid development of responsive and mobile-first websites, which is crucial for ensuring a consistent user experience across devices.
   - It provides ready-to-use CSS and JavaScript components that streamline the development process, saving time and effort.
   - Additionally, Bootstrap's popularity means that there is a wealth of community resources and third-party plugins available, making it easy to extend and customize as needed.

Open-source Technologies Used
Advantages:
- SQLite3:
  - Advantages: Lightweight, serverless, easy to set up, suitable for small to medium-sized projects.
- Bootstrap:
   - Advantages: Rapid development, extensive documentation, mobile-first approach, rich UI components, large community support.
- Django Rest Framework (DRF):
  - Advantages: Powerful toolkit for building Web APIs, built-in support for serialization, authentication, and pagination, extensive documentation, active community.
