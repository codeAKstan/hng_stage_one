# HNG12 Stage 1 Task - Number Classification API (Django)

This is a simple public API built with Django that classifies a number and returns its mathematical properties along with a fun fact.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/codeAKstan/hng_stage_one.git
2. Install dependencies
    ```bash
    pip install -r requirements.txt
3. Run the development server:
    ```bash
    python manage.py runserver


## API Documentation
- **Endpoint**: `GET /api/classify-number?number=<number>`
- **Response (200 OK)**:
    ```json
    {
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }


- **Response (400 Bad Request)**:
    ```json
    {
  "number": "alphabet",
  "error": true
  }

## Example Usage
    ```bash
    curl -X GET https://your-deployed-endpoint/api/classify-number?number=371