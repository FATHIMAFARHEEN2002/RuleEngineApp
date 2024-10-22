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

    def to_dict(self):
        """Convert the Node object into a nested dictionary for JSON serialization."""
        return {
            "node_type": self.node_type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }

# Home route to verify server is running
@app.route('/')
def home():
    return "Rule Engine API is running!"

# Route for creating a single rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule_string')
    if not rule_string:
        return jsonify({"error": "Rule string is required."}), 400

    # Creating an AST node
    ast = Node("operator", "AND", Node("operand", rule_string), None)
    return jsonify({"ast": ast.to_dict()})

# Route for combining multiple rules into an AST
@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json.get('rules')  # List of rule strings
    if not rules or not isinstance(rules, list):
        return jsonify({"error": "Rules should be a non-empty list."}), 400

    combined_ast = None

    for rule in rules:
        new_ast = Node("operand", rule)
        if combined_ast:
            combined_ast = Node("operator", "AND", combined_ast, new_ast)
        else:
            combined_ast = new_ast

    return jsonify({"combined_ast": combined_ast.to_dict()})

# Route for evaluating a rule based on given data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast = request.json.get('ast')
    data = request.json.get('data')

    if not ast or not data:
        return jsonify({"error": "Both 'ast' and 'data' are required."}), 400

    # Placeholder logic for evaluation
    if ast.get("node_type") == "operator" and data.get("age", 0) > 30:
        return jsonify({"result": True})
    return jsonify({"result": False})

if __name__ == '__main__':
    app.run(debug=True)
