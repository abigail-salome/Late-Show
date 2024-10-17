## Late Show
This project is a RESTful API built with Flask-restful that manages a database of Episodes, Guests, and Appearances. It allows users to perform operations such as listing all episodes, retrieving specific episode details, adding new guest appearances, and more.

#### Features
1. Episodes: Retrieve all episodes or details of a specific episode.
2. Guests: List all available guests.
3. Appearances: Create new guest appearances for specific episodes.

#### Prerequisites
To run this project locally, ensure you have the following installed:
* Python 3.x
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-Migrate


#### Installation
1. Clone the Repository
First, clone this repository to your local machine:
git clone <repository_url>
cd <project_directory>

2. Set Up the Database
Before running the application, initialize the database:
* Make sure the database URI in config.py is set correctly for your environment:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

* Run database migrations to create tables:
flask db init
flask db migrate
flask db upgrade

3. Seed the Database (Optional)
If you have sample data in a CSV file and would like to seed it into the database, use the following command:python seed_data.py <path_to_your_csv_file>
Make sure your CSV follows the correct format with columns for guest names, occupations, and episode details.

4. Running the Server
To start the server on port 5555, use the following command:
python app.py
The server will be available at http://localhost:5555.

#### API Endpoints
1. List All Episodes
GET /episodes
Returns a list of all episodes with their details.
Example Response:
[
  {
    "id": 1,
    "date": "2023-10-01",
    "number": 1,
    "appearances": [
      {
        "id": 1,
        "rating": 5,
        "guest": {
          "id": 1,
          "name": "Guest Name",
          "occupation": "Actor"
        }
      }
    ]
  }
]

2. Get Episode by ID
GET /episodes/<int:id>
Retrieve details of a specific episode by its ID.

Example Response:
{
  "id": 1,
  "date": "2023-10-01",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 5,
      "guest": {
        "id": 1,
        "name": "Guest Name",
        "occupation": "Actor"
      }
    }
  ]
}

3. List All Guests
GET /guests
Returns a list of all guests with their details.

Example Response:
[
  {
    "id": 1,
    "name": "Guest Name",
    "occupation": "Actor"
  }
]

4. Create New Appearance
POST /appearances
Creates a new appearance for a guest in an episode. You must send the guest ID, episode ID, and rating in the request body.
Example Request:
{
  "rating": 4,
  "episode_id": 1,
  "guest_id": 1
}

#### Example Usage
To get started with the API, you can use tools like Postman or curl to interact with the endpoints.
For example, to list all episodes, use:
curl -X GET http://localhost:5555/episodes

To add a new appearance:
curl -X POST http://localhost:5555/appearances -H "Content-Type: application/json" -d '{"rating": 5, "episode_id": 1, "guest_id": 2}'

#### Troubleshooting
Database Errors: If you encounter any issues with database migrations, ensure your database is set up correctly and the migrations were applied successfully.
Data Validation: The rating for an appearance must be between 1 and 5. If it's outside this range, an error will be raised.
