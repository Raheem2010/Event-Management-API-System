## Project Created By Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428
from fastapi import FastAPI
from routes import user, event, speaker, registration
from database import speakers
from uuid import uuid4
from schemas.speaker import Speaker

app = FastAPI(title="Event Management API System")



speakers.extend([
    Speaker(id=uuid4(), name="Adeyemi Adeniyi Abdul-Raheem", topic="2nd Semester Backend Development Exam"),
    Speaker(id=uuid4(), name="Hamzah Adedamola", topic="Product Management"),
    Speaker(id=uuid4(), name="Rising Odegua", topic="FullStack"),
])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Event Management API System created by Adeyemi Adeniyi Abdul-Raheem with ID ALT/SOE/024/2428"}

app.include_router(user.router)
app.include_router(event.router)
app.include_router(speaker.router)
app.include_router(registration.router)




