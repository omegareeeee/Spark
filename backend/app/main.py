from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.features.ideas.router import router as IdeaRouter
from app.features.cluster.router import router as ClusterRouter
# from app.features.map.router import router as MapRouter
from app.features.comments.router import router as CommentsRoute

app = FastAPI()

app.include_router(IdeaRouter)
app.include_router(ClusterRouter)
# app.include_router(MapRouter)
app.include_router(CommentsRoute)

@app.get("/health", status_code=200)
def health_check():
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "service": "spark-health"}
    )