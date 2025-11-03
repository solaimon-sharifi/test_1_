"""FastAPI application for the calculator.

Provides simple JSON API endpoints for arithmetic operations and a tiny
HTML UI at `/` so end-to-end tests can interact with the app in a browser.
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .operations import add, subtract, multiply, divide
from .logging_config import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Calculator API")


class Operands(BaseModel):
    left: float
    right: float


@app.get("/", response_class=HTMLResponse)
def homepage():
    html = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Calculator</title>
      </head>
      <body>
        <h1>Calculator</h1>
        <label>Left: <input id="left" value="3"/></label>
        <label>Right: <input id="right" value="2"/></label>
        <div>
          <button id="add">Add</button>
          <button id="sub">Subtract</button>
          <button id="mul">Multiply</button>
          <button id="div">Divide</button>
        </div>
        <h2 id="result">Result: </h2>
        <script>
          async function call(op){
            const left = parseFloat(document.getElementById('left').value);
            const right = parseFloat(document.getElementById('right').value);
            const resp = await fetch('/api/' + op, {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({left, right})
            });
            const data = await resp.json();
            document.getElementById('result').textContent = 'Result: ' + (data.result ?? data.detail ?? JSON.stringify(data));
          }
          document.getElementById('add').onclick = () => call('add');
          document.getElementById('sub').onclick = () => call('subtract');
          document.getElementById('mul').onclick = () => call('multiply');
          document.getElementById('div').onclick = () => call('divide');
        </script>
      </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.post("/api/add")
def api_add(op: Operands):
    logger.info("API add called: %s + %s", op.left, op.right)
    return {"result": add(op.left, op.right)}


@app.post("/api/subtract")
def api_subtract(op: Operands):
    logger.info("API subtract called: %s - %s", op.left, op.right)
    return {"result": subtract(op.left, op.right)}


@app.post("/api/multiply")
def api_multiply(op: Operands):
    logger.info("API multiply called: %s * %s", op.left, op.right)
    return {"result": multiply(op.left, op.right)}


@app.post("/api/divide")
def api_divide(op: Operands):
    logger.info("API divide called: %s / %s", op.left, op.right)
    try:
        return {"result": divide(op.left, op.right)}
    except ZeroDivisionError as exc:
        logger.exception("Division by zero")
        raise HTTPException(status_code=400, detail=str(exc))
