# Rule Engine API

## Overview
The Rule Engine API is a simple application designed to create, combine, and evaluate conditional rules using an Abstract Syntax Tree (AST). It allows users to define rules based on attributes such as age and department, providing an interface for evaluating user eligibility based on those rules.

## Features
- Create individual rules and receive their AST representation.
- Combine multiple rules into a single AST.
- Evaluate rules against provided user data.

## API Endpoints

 1. Home
- Endpoint: `/`
- Method: `GET`
- Description: Returns a message indicating that the API is running.
- Response:
  plaintext
  Rule Engine API is running!

2. Create Rule
- Endpoint: /create_rule
- Method: POST
- Request Body:
- {
    "rule_string": "(age > 30 AND department = 'Sales')"
}

- Response:
{
    "ast": "Node(type=operator, value=AND)"
}
- Description: Creates a new rule and returns its AST representation.

4. Combine Rules
- Endpoint: /combine_rules
- Method: POST
- Request Body:
- {
    "rules":["(age > 30 AND department = 'Sales')",
        "(salary > 50000 OR experience > 5)"
       
}

- Response:
{
    "combined_ast": "<__main__.Node object at 0x0000019A3B1510D0>"
}
- Description: Combines multiple rules into a single AST.

4. Evaluate Rule
- Endpoint: /evaluate_rule
- Method: POST
- Request Body:
- {
    "ast": {
        "node_type": "operator",
        "value": "AND",
        "left": {
            "node_type": "operand",
            "value": "(age > 30 AND department = 'Sales')"
        }
    },
    "data": {
        "age": 35,
        "department": "Sales"
    }
}

- Response:
- {
    "result": true
}
- Description: Evaluates the given AST against the provided user data.

- Requirements
. Python 3.x
. Flask

- Installation
1.Clone the repository:
  - git clone https://github.com/FATHIMAFARHEEN2002/RuleEngineApp.git
  
2.Change into the project directory
  - cd RuleEngineApp
  
3.Install the required packages:
 -  pip install Flask

4.Run the application:
- python app.py
  - The API will be accessible at http://127.0.0.1:5000.

- Testing
- You can test the API endpoints using Postman or any other API client.

- Example Tests
1.Create Rule: Send a POST request to /create_rule with a valid JSON body containing rule_string.
2.Combine Rules: Send a POST request to /combine_rules with a list of rules.
3.Evaluate Rule: Send a POST request to /evaluate_rule with an AST and user data.
