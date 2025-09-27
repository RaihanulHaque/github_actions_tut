from fastapi import FastAPI

app = FastAPI()

# Simple function to add two numbers
def add_numbers(a: int, b: int) -> int:
    return a + b

# API 1: Hello World
@app.get("/")
def read_root():
    return {"message": "Hello, World! This is Rahi."}

# API 2: Add two numbers
@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    result = add_numbers(a, b)
    return {"result": result}

# API 3: Just for fun, multiply two numbers
@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}