🗂️ Event Management API System
This project is a FastAPI-based Event Management System developed as part of the AltSchool of Engineering's Tinyuka Second Semester Python Project. It enables users to:
- Register for events
- Manage speakers
- Track attendance
- Simulate CRUD operations for users, events, and registrations using in-memory data structures


🚀 Features

**User Management**

-Create and list users

-Update and Delete users

-Deactivate users 

**Event Management**

-Create, list, and close events

-Mark events as closed rather than deleting

**Speaker Management**

-View all event speakers

**Registration & Attendance**

-Register users for events

-Prevent duplicate registrations

-Mark attendance for registered users


🧾 Technologies Used

-Python 3.10+

-FastAPI

-Uvicorn (ASGI server)

-Pydantic

Note: This project uses in-memory data (lists) and is not connected to a database.


🛠️ How to Run the Project

✅ Prerequisites

-Make sure you have:

-Python 3.10+ installed

-Git installed


📦 Setup Instructions

1. Clone the repository

https://github.com/Raheem2010/event-management-api.git
cd event-management-api

2.Create and activate a virtual environment

python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the FastAPI app

uvicorn app.main:app --reload

5. Open your browser and visit:

http://127.0.0.1:8000/docs

This will load the FastAPI Swagger documentation where you can test all endpoints interactively.


🧪 Sample API Endpoints
Here are a few example endpoints:

Action	                Method	Endpoint

Create a User	          POST     /users/
Deactivate a User       PATCH	   /users/{user_id}/deactivate
Create an Event	        POST	   /events/
Close an Event	        PATCH	   /events/{event_id}/close
Register User to Event	POST	   /registrations/
Mark Attendance 	      PATCH	   /registrations/{reg_id}/attend
Get All Speakers	      GET	     /speakers/


📂 Project Structure
.
├── main.py              # Entry point of the FastAPI application
├── database.py          # In-memory storage (lists) simulating a database
├── routes/              # All API route definitions (user, event, registration, speaker)
├── services/            # Business logic and helper functions
├── schemas/             # Pydantic schemas
├── requirements.txt
└── README.md


🧠 Tech Stack
FastAPI

Python 3.10+

Pydantic (Data validation)

Uvicorn (ASGI Server)


🙋‍♂️ Author
Adeniyi Adeyemi
AltSchool of Engineering – Backend Track
Email: [adeyemiadeniyi97@gmail.com]
GitHub: https://github.com/Raheem2010
LinkedIn:


📎 License
This project is for educational purposes and personal portfolio building under the guidelines of AltSchool Africa. Feel free to fork and expand.
