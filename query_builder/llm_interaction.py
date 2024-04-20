import requests


# ollama config
OLLAMA_PORT = 11434
OLLAMA_BASE_URL = f"http://127.0.0.1:{OLLAMA_PORT}"
OLLAMA_GENERATE_ENDPOINT = f"{OLLAMA_BASE_URL}/api/generate"
SELECTED_MODEL = "sqlcoder"


# this is the prompt template which is sent to the llm
# table_metadata are the DDL statements which define the table schema
PROMPT_TEMPLATE = """
### Task
Generate a MySQL query to answer [QUESTION]{user_question}[/QUESTION]

### Database Schema
The query will run on a database with the following schema:
{table_metadata}

### Answer
Given the database schema, here is the SQL query that [QUESTION]{user_question}[/QUESTION]
[SQL]
[/SQL]
"""


def get_response(question: str, table_metadata: str):
    payload = {
        "model": SELECTED_MODEL,
        "prompt": PROMPT_TEMPLATE.format(
            user_question=question, table_metadata=table_metadata
        ),
        "stream": False,
    }
    resp = requests.post(
        OLLAMA_GENERATE_ENDPOINT,
        json=payload,
    )
    query = resp.json().get("response")
    if not query:
        raise Exception(f"ollama api didnt provide response key:\n{resp.json()}")

    return query


if __name__ == "__main__":
    EXAMPLE_QUESTION = "What are our top 3 products by revenue in the New York region?"
    EXAMPLE_TABLE_METADATA = """
CREATE TABLE products (
  product_id INTEGER PRIMARY KEY, -- Unique ID for each product
  name VARCHAR(50), -- Name of the product
  price DECIMAL(10,2), -- Price of each unit of the product
  quantity INTEGER  -- Current quantity in stock
);

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY, -- Unique ID for each customer
  name VARCHAR(50), -- Name of the customer
  address VARCHAR(100) -- Mailing address of the customer
);

CREATE TABLE salespeople (
  salesperson_id INTEGER PRIMARY KEY, -- Unique ID for each salesperson 
  name VARCHAR(50), -- Name of the salesperson
  region VARCHAR(50) -- Geographic sales region 
);

CREATE TABLE sales (
  sale_id INTEGER PRIMARY KEY, -- Unique ID for each sale
  product_id INTEGER, -- ID of product sold
  customer_id INTEGER,  -- ID of customer who made purchase
  salesperson_id INTEGER, -- ID of salesperson who made the sale
  sale_date DATE, -- Date the sale occurred 
  quantity INTEGER -- Quantity of product sold
);

CREATE TABLE product_suppliers (
  supplier_id INTEGER PRIMARY KEY, -- Unique ID for each supplier
  product_id INTEGER, -- Product ID supplied
  supply_price DECIMAL(10,2) -- Unit price charged by supplier
);

-- sales.product_id can be joined with products.product_id
-- sales.customer_id can be joined with customers.customer_id 
-- sales.salesperson_id can be joined with salespeople.salesperson_id
-- product_suppliers.product_id can be joined with products.product_id
"""
    print(get_response(EXAMPLE_QUESTION, EXAMPLE_TABLE_METADATA))
