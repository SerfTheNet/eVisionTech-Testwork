# -*- coding: utf-8 -*-
import pathlib
from fastapi import FastAPI
from config import path as target_path

app = FastAPI()

@app.get("/api/meta")
async def root():
    root = pathlib.Path(target_path)
    
    internals = []
    for child in root.iterdir():
        if child.name != '.disk':
            internals.append(
                {
                'name': child.name,
                'type': 'file' if child.is_file() else 'folder',
                'time': child.stat().st_ctime,
                }
        )

    return {"data": internals}
