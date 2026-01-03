from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi

from app.core.database import Base, engine
from app.models.user import User
from app.routes import auth, trips, itineraries

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create app FIRST
app = FastAPI(title="GlobeTrotter API")

# Attach routers
app.include_router(auth.router)
app.include_router(trips.router)
app.include_router(itineraries.router)

# ---------------- Swagger JWT Support ----------------

security = HTTPBearer()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="GlobeTrotter API",
        version="1.0",
        description="API documentation",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# ---------------- Root ----------------

@app.get("/")
def root():
    return {"message": "GlobeTrotter backend running"}
