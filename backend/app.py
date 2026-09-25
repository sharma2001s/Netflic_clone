from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/api/movies")
def get_movies():
    movies=[
        
        {
            "id": 1,
            "title": "Movie 1",
            "category": "Action",
            "image_url": "https://placehold.co/200x300"
        },
                {
            "id": 2,
            "title": "Movie 2",
            "category": "Comedy",
            "image_url": "https://placehold.co/200x300"
        },
                {
            "id": 3,
            "title": "Movie 3",
            "category": "Drama",
            "image_url": "https://placehold.co/200x300"
        },
                {
            "id": 4,
            "title": "Movie 4",
            "category": "Thriller",
            "image_url": "https://placehold.co/200x300"
        },
                {
            "id": 5,
            "title": "Movie 5",
            "category": "Horror",
            "image_url": "https://placehold.co/200x300"
        },
        
    ]
    return movies
print("MY APP FILE IS RUNNING")