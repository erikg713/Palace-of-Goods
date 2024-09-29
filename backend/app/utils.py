import requests

PI_API_URL = "https://api.minepi.com/v2/payments"

def process_pi_payment(user, amount):
    # Prepare headers with Pi Network API key
    headers = {
        'Authorization': f'Bearer {user.pi_api_key}',
        'Content-Type': 'application/json',
    }

    # Prepare the payload
    payload = {
        "user_uid": user.pi_user_uid,
        "amount": amount,
        "memo": "Purchase on Palace of Goods",
        "metadata": {
            "product_id": "12345",  # Example product ID
        }
    }

    try:
        response = requests.post(PI_API_URL, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and response_data['status'] == 'success':
            # Payment was successful
            return True
        else:
            # Handle failure scenarios
            return False
    except Exception as e:
        print(f"Error processing Pi payment: {str(e)}")
        return False
