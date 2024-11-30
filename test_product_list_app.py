from product_list_app import app  # Adjust import if necessary

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_products():
    tester = app.test_client()
    response = tester.get('/products')  # Replace with actual routes
    assert response.status_code == 200
