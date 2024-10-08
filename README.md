# spartamarket
 # 🪷 SpartaMarket_DRF 🪷

# ⏰ Development Period
- 2024.08.14 ~ 2024.08.28
----
# 👩🏻‍💻 Project Introduction
This project is a conversion of code developed during the Sparta Coding Club Bootcamp into Django Rest Framework. 
It includes features for product registration, product listing, product updating, product deletion, user registration, login, and profile viewing.
----
# 💻 Development Environment

| Programming Language |            python 3.10             |
|:--------------------:|:----------------------------------:|
|    Web Framework     |  Django 4.2, Djangorestframework   |
|       Database       |               SQLite               |
|         IDE          |              PyCharm               |
|   Version Control    |            Git, Github             |
|       Backend        | Python, Django, Djangorestframwork |
|       Database       |         Django ORM, SQLite         |
|       POSTMAN        |              POSTMAN               |


----

#### 👑팀원 Cho Jun-ho



# 🧬 Directory Structure
| Structure        | Function|
|------------------|----------------|
| accounts         | User authentication and account management capabilities |
| articles         | Create, modify, delete, and search posts (objects) |
| spartamarket_DRF | Project Settings and Initialization Files |


----
# 📌 Project Features

## 1. Account [membership function]

### Registration (CREATE)
- URL: /api/register/
- Method: POST
- Data Format: JSON
- Required Fields: username, password, email, first_name, last_name
- Response: 201 Created (success), 400 Bad Request (failure)

### Login (LOGIN)
- URL: /api/login/
- Method: POST
- Data Format: JSON
- Required Fields: username, password
- Response: 200 OK (success, includes JWT tokens), 401 Unauthorized (failure)

### Profile Viewing (LIST)
- URL: /api/users/<username>/
- Method: GET
- Required Permission: Authenticated User
- Response: 200 OK (success), 404 Not Found (user not found)

## 2.Article [publishing function]

### Product Registration (CREATE)
- URL: /api/products/
- Method: POST
- Data Format: JSON
- Required Fields: title, content, image
- Required Permission: Authenticated User
- Response: 201 Created (success), 400 Bad Request (failure)

### Product Listing (LIST)
- URL: /api/products/
- Method: GET
- Response: 200 OK (success, includes product list)

### Product Update (UPDATE)
- URL: /api/products/<pk>/
- Method: PUT
- Data Format: JSON
- Required Permission: Authenticated User, Product Author
- Response: 200 OK (success), 403 Forbidden (permission denied), 404 Not Found (product not found)

### Product Deletion (DELETE)
- URL: /api/products/<pk>/
- Method: DELETE
- Required Permission: Authenticated User, Product Author
- Response: 204 No Content (success), 403 Forbidden (permission denied), 404 Not Found (product not found)

----

# ERD Diagram
![image](./image/spartamarket_DRF.png)

# POST MAN
## - ACCOUNT_CREATE
![image](./image/accounts_create.PNG)
## - ACCOUNT_LOGIN
![image](./image/accounts_login.PNG)
## - ACCOUNT_LIST
![image](./image/accounts_list.PNG)
## - PRODUCTS_CREATE
![image](./image/products_create.PNG)
## - PRODUCTS_LIST
![image](./image/products_list.PNG)
## - PRODUCTS_update
![image](./image/products_update.PNG)
## - PRODUCTS_CREATE
![image](./image/products_delete.PNG)

# 개발 및 기여

## Code Changes
- Please commit your changes, push them, and then create a Pull Request.

## Contribution
- To contribute to this project, please raise issues or leave suggestions in the Issues tab.

