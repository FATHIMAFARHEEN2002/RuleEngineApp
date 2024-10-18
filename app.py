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

if __name__ == '__main__':
    app.run(debug=True)

