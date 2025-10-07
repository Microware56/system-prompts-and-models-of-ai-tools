from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.fernet import Fernet

app = FastAPI()

# Generate a key for encryption (use a secure storage in production)
key = Fernet.generate_key()
cipher = Fernet(key)

# Data model for input
class Command(BaseModel):
    user_id: str
    command_text: str

# Local processing endpoint
@app.post("/process-command")
async def process_command(command: Command):
    try:
        # Encrypt command text
        encrypted_command = cipher.encrypt(command.command_text.encode())

        # Simulate local processing
        response = {
            "user_id": command.user_id,
            "encrypted_command": encrypted_command.decode(),
            "status": "processed locally"
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))