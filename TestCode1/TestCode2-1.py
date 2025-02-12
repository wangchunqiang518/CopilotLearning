from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class TextModel(BaseModel):
    text: str

@app.post("/checksum")
def get_checksum(item: TextModel):
    if not item.text:
        raise HTTPException(status_code=400, detail="Text field cannot be empty")
    checksum = hashlib.md5(item.text.encode()).hexdigest()
    return {"checksum": checksum}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
