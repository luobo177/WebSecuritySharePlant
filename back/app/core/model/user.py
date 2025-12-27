from pydantic import BaseModel

class RegisterRequest(BaseModel):
    public_key: str
    invite_code: str
    timestamp: int
    signature: str
