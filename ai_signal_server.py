from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from datetime import datetime

app = FastAPI(title="AI Signal Server")

PAIRS = ["EURUSD","USDJPY","GBPUSD","USDCHF","AUDUSD","USDCAD","NZDUSD","EURJPY"]

class BiasResponse(BaseModel):
    pair: str
    bias: float
    timestamp: str

def generate_bias(pair):
    # simple placeholder logic – replace later with your AI rules
    seed = (hash(pair + datetime.utcnow().strftime("%Y%m%d%H")) % 100) / 100
    bias = round(np.sin(seed * np.pi), 2)
    return bias

@app.get("/bias")
def read_bias():
    data = []
    for pair in PAIRS:
        data.append({
            "pair": pair,
            "bias": generate_bias(pair),
            "timestamp": datetime.utcnow().isoformat()
        })
    return {"bias_list": data}

# Run it with:  uvicorn ai_signal_server:app --host 0.0.0.0 --port 5000
