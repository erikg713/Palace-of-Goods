from flask import jsonify

def handle_error(e):
    response = {
        "success": False,
        "error": str(e),
    }
    return jsonify(response), 500
