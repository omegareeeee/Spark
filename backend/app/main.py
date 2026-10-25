from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.features.ideas.router import router as IdeaRouter
from app.features.cluster.router import router as ClusterRouter
from app.features.map.router import router as MapRouter
from app.features.comments.router import router as CommentsRouter
from app.features.intersect.router import router as IntersectRouter

from app.core.config import FRONTEND_ORIGIN

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_ORIGIN,
        " http://localhost:3000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(IdeaRouter)
app.include_router(ClusterRouter)
app.include_router(MapRouter)
app.include_router(CommentsRouter)
app.include_router(IntersectRouter)

@app.get("/health", status_code=200)
def health_check():
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "service": "spark-health"}
    )