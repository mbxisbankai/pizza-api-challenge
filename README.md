# 🍕 Pizza Restaurants API

A Flask-based RESTful API that allows you to manage restaurants, pizzas, and their associations (including price per restaurant).  

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:mbxisbankai/pizza-api-challenge.git
   cd pizza-api-challenge
   ```

2. **Install dependencies using Pipenv**
   ```bash
   pipenv install && pipenv shell
   ```

3. **Export environment variables**
   ```bash
   cd server/
   export FLASK_APP=app.py
   export FLASK_RUN_PORT=5555
   ```

4. **Run the development server**
   ```bash
   flask run
   ```

## Database migration and seeding
1. **Initialize the Database**
   ```bash
   flask db init
   ```

2. **Generate a Migration**
   ```bash
   flask db migrate -m "Initial Migration"
   ```

3. **Apply migrations**
   ```bash
   flask db upgrade head
   ```

4. **Run this from the root of the project to seed the database**
   ```bash
   python -m server.seed
   ```


## Route Summary
### Restaurants
| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| GET    | `/restaurants`          | Get all restaurants          |
| POST   | `/restaurants`          | Create a new restaurant      |
| GET    | `/restaurants/<id>`     | Get restaurant by ID         |
| PATCH  | `/restaurants/<id>`     | Update restaurant by ID      |
| DELETE | `/restaurants/<id>`     | Delete restaurant by ID      |

### Pizzas
| Method | Endpoint                | Description                   |
|--------|-------------------------|-------------------------------|
| GET    | `/pizzas`               | Get all pizzas                |
| POST   | `/pizzas`               | Create a new pizza            |
| GET    | `/pizzas/<id>`          | Get a pizza by ID             |
| PATCH  | `/pizzas/<id>`          | Update a pizza by ID          |
| DELETE | `/pizzas/<id>`          | Delete a pizza by ID          |

### Restaurant Pizzas
| Method | Endpoint                       | Description                   |
|--------|--------------------------------|-------------------------------|
| GET    | `/restaurants_pizzas`          | Get all restaurant pizzas     |
| POST   | `/restaurants_pizzas`          | Create a new restaurant pizza | 
| GET    | `/restaurants_pizzas/<id>`     | Get restaurant pizza by ID    |
| PATCH  | `/restaurants_pizzas/<id>`     | Update restaurant pizza by ID |
| DELETE | `/restaurants_pizzas/<id>`     | Delete restaurant pizza by ID |

## 📬 Example Requests & Responses
### Restaurant
`GET /restaurants`
**Request**
```http
GET /restaurants HTTP/1.1
Host: localhost:5555
```

**Response**
```json
[
  {
    "id": 1,
    "name": "Domino's",
    "address": "123 Pizza Street"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "456 Cheese Avenue"
  }
]
```
`POST /restaurants`
**Request**
```http
POST /restaurants HTTP/1.1
Host: localhost:5555
Content-Type: application/x-www-form-urlencoded

name=New Pizza Place&address=789 Crust Blvd
```

**Response**
```json
{
  "id": 3,
  "name": "New Pizza Place",
  "address": "789 Crust Blvd"
}
```
`GET /restaurants/<id>`
**Request**
```http
GET /restaurants/1 HTTP/1.1
Host: localhost:5555
```

**Response**
```json
{
  "id": 1,
  "name": "Domino's",
  "address": "123 Pizza Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```
`PATCH /restaurants/<id>`
**Request**
```http
PATCH /restaurants/1 HTTP/1.1
Host: localhost:5555
Content-Type: application/x-www-form-urlencoded

name=Updated Pizza Place
```

**Response**
```json
{
  "id": 1,
  "name": "Updated Pizza Place",
  "address": "123 Pizza Street"
}
```
`DELETE /restaurants/<id>`
**Request**
```http
DELETE /restaurants/1 HTTP/1.1
Host: localhost:5555
```

**Response**
```json
{
  "delete_successful": true,
  "message": "No Content."
}
```
### Pizzas
`GET /pizzas`
**Request**
```http
GET /pizzas HTTP/1.1
Host: localhost:5555
```

**Response**
```json
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  },
  {
    "id": 2,
    "name": "Veggie",
    "ingredients": "Dough, Tomato Sauce, Cheese, Vegetables"
  }
]
```
### Restaurant Pizzas
`GET /restaurant_pizzas`
**Request**
```http
GET /restaurant_pizzas HTTP/1.1
Host: localhost:5555
```

**Response**
```json
[
  {
    "id": 1,
    "price": 10,
    "pizza": {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    },
    "restaurant": {
      "id": 1,
      "name": "Domino's",
      "address": "123 Pizza Street"
    }
  }
]
```
`POST /restaurant_pizzas`
**Request**
```http
POST /restaurant_pizzas HTTP/1.1
Host: localhost:5555
Content-Type: application/x-www-form-urlencoded

price=12&pizza_id=1&restaurant_id=2
```

**Response**
```json
{
  "id": 2,
  "price": 12,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Hut",
    "address": "456 Cheese Avenue"
  }
}
```


## ✅ Validation Rules
- price in /restaurant_pizzas must be between 1 and 30.

- If invalid, you will get:
    ```json
    {
       "error": ["Price must be between 1 and 30"]
    }
    ```
- If pizza_id or restaurant_id doesn't exist:
    ```json
    {
       "error": "Invalid restaurant or pizza ID"
    }
    ```

## Postman Usage Instructions
1. Import endpoints manually or paste in the base URL:
   ```
   http:localhost:5555
   ```
2. Set request type (GET, POST, PATCH, etc.).

3. For POST and PATCH, use x-www-form-urlencoded or form-data.

4. View full responses with headers to debug status codes.

