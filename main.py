import functions_framework

@functions_framework.http
def my_test_function(request):
    """
    Standard HTTP Cloud Function.
    """
    # Logic to handle JSON or URL parameters
    request_json = request.get_json(silent=True)
    name = "Stranger"

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request.args and 'name' in request.args:
        name = request.args.get('name')

    return f"Success! Cloud Build deployed this. Hello, {name}!"