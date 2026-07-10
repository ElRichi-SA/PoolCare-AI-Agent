from pydantic import BaseModel


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    
responses={
    500: {
        "model": ErrorResponse
    }
}