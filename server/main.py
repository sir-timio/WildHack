from typing import Optional
import json
import numpy as np

from fastapi import FastAPI
import uvicorn

app = FastAPI()

# example = http://127.0.0.1:8000/stats/1
# example with optional param http://127.0.0.1:8000/stats/1?q=1

@app.get("/stats/{id}")
def get_stats(id, q=None):
    days = [i for i in range(1, 100)]
    values = [d * np.log(d) for d in days]
    d = dict({
        'optional': q,
        'stats for ': id,
        'days': days,
        'values': values
    })
    return d

if __name__ == '__main__':
    uvicorn.run(app)