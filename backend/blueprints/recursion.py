@app.route('/api/levels/recursion', methods=['POST'])
def recursion_level():
    data = request.get_json()
    code = data['code']

    # Simulate running the code securely
    result = run_recursion_code_sandboxed(code)  # Function to securely run player code

    if result == "Expected Output":
        return jsonify({
            "success": True,
            "message": "Well done! You solved the recursion challenge."
        })
    else:
        return jsonify({
            "success": False,
            "message": "Try again! Your recursion logic is incorrect."
        })
