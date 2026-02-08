from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

facts = [
    {"id": 1, "fact": "The sun is a star."},
    {"id": 2, "fact": "Water boils at 100°C."},
    {"id": 3, "fact": "Earth has one moon."}
]

@app.get("/api/facts")
def get_facts():
    return facts
