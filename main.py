from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import math

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect (sum of proper divisors equals the number)."""
    if n <= 1:
        return False
    divisors = [1]
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    digits = list(str(n))
    length = len(digits)
    total = sum(int(d) ** length for d in digits)
    return total == n

def digit_sum(n: int) -> int:
    """Calculate the sum of the digits of the number."""
    return sum(int(d) for d in str(abs(n)))

@app.get("/api/classify-number")
async def classify_number(number: str = Query(...)):
    # Validate input is an integer
    if not number.lstrip('-').isdigit():
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True}
        )
    n = int(number)
    
    # Determine properties
    armstrong = is_armstrong(n)
    parity = "even" if n % 2 == 0 else "odd"
    
    is_prime_result = is_prime(abs(n)) if n != 0 else False
    is_perfect_result = is_perfect(n) if n > 0 else False
    
    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append(parity)
    
    digit_sum_result = digit_sum(n)
    
    # Fetch fun fact from Numbers API
    fun_fact = "No fun fact available."
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"http://numbersapi.com/{n}/math?json")
            if response.status_code == 200:
                data = response.json()
                fun_fact = data.get("text", fun_fact)
    except Exception as e:
        pass  # Keep default fun fact message
    
    return {
        "number": n,
        "is_prime": is_prime_result,
        "is_perfect": is_perfect_result,
        "properties": properties,
        "digit_sum": digit_sum_result,
        "fun_fact": fun_fact
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)