"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    # Sports related activities
    "Soccer Team": {
        "description": "Join the school soccer team and compete in local leagues",
        "schedule": "Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["alex@mergington.edu", "lucas@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly matches",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["mia@mergington.edu", "liam@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Swim Team": {
        "description": "Train and compete with the school's swim team",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["sarah@mergington.edu", "noah@mergington.edu"]
    },

    # Artistic activities
    "Art Club": {
        "description": "Explore painting, drawing, and sculpture",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["ava@mergington.edu", "ethan@mergington.edu"]
    },
    "Drama Society": {
        "description": "Act, direct, and produce school plays",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["isabella@mergington.edu", "jack@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and participate in photo walks",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["lucy@mergington.edu", "ben@mergington.edu"]
    },
    "Music Band": {
        "description": "Join the school band and perform at events",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["oliver@mergington.edu", "ella@mergington.edu"]
    },

    # Intellectual activities
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["william@mergington.edu", "grace@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": ["harry@mergington.edu", "amelia@mergington.edu"]
    },
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
