from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the Node class for the AST representation
class Node:
    def __init__(self, node_type, value, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node(type={self.node_type}, value={self.value})"

# Home route
@app.route('/')
def home():
    return "Rule Engine API is running!"

# New API route for rule creation
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule_string')
    if not rule_string:
        return jsonify({"error": "Rule string is required."}), 400
    
    # Creating a simple AST (Abstract Syntax Tree) node
    ast = Node("operator", "AND", Node("operand", rule_string), None)
    return jsonify({"ast": str(ast)})





# Combine Rules route
@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json.get('rules')  # List of rule strings
    combined_ast = None

    for rule in rules:
        new_ast = Node("operand", rule)
        if combined_ast:
            combined_ast = Node("operator", "AND", combined_ast, new_ast)
        else:
            combined_ast = new_ast

    return jsonify({"combined_ast": repr(combined_ast)})

# Evaluate Rule route
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast = request.json.get('ast')  # Example: {"type": "operator", "value": "AND", ...}
    data = request.json.get('data')  # Example: {"age": 35, "department": "Sales"}

    # Placeholder logic for evaluation (expand this based on your AST design)
    if ast["type"] == "operator" and data.get("age", 0) > 30:
        return jsonify({"result": True})
    return jsonify({"result": False})

if __name__ == '__main__':
    app.run(debug=True)
