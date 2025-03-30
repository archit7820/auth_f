# app/main.py
from fastapi import FastAPI
# from app.api.v1.endpoints import auth, users, items
# from app.middlewares.security_middleware import SecurityMiddleware
# from app.core.config import settings

app = FastAPI(title="Secure FastAPI Project", version="1.0")

# Add security middleware
# app.add_middleware(SecurityMiddleware)

# Include API routers
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(items.router, prefix="/api/v1/items", tags=["items"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
