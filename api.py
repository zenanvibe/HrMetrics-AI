from ai import generate_text
from fastapi import FastAPI, UploadFile, File, HTTPException,Query
from pydantic import BaseModel
from typing import Optional
from Audios.process import extract_text
from Audios.langs import detect_and_translate

app = FastAPI()

class TextRequest(BaseModel):
    querry: str

@app.post("/leave")
async def leave(querry: str = Query(..., description="Query string to generate text")):
    response = generate_text(f"Context: {querry}|")
    return {"response": response}

@app.post("/leave/common")
async def leave(querry: str = Query(..., description="Query string to generate text")):
    try:
        try:
            querry = detect_and_translate(querry)
        except:
            HTTPException(status_code=400, detail="Invalid text input!.")
        response = generate_text(f"Context: {querry}|")
        return {"response": response}
    except:
       HTTPException(status_code=400, detail="Unable to communicate with Ai Server!.")

@app.post("/audio")
async def leave_audio(file: UploadFile = File(...)):
    if file.content_type != "audio/mpeg":
        raise HTTPException(status_code=400, detail="Invalid file type. Only MP3 files are accepted.")
    # Save the uploaded file to a temporary location
    temp_file_path = "temp_audio.mp3"
    with open(temp_file_path, "wb") as f:
        f.write(file.file.read())    
    text = extract_text(temp_file_path)
    return {"text": text}
