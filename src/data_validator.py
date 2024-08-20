# Data validation function
def validate_data(data):
    if not data.get("client_name"):
        return False, "Client name must not be empty."
    if not data.get("delivery_date"):
        return False, "Date must not be empty."
    if not data.get("transport_type"):
        return False, "Transport type must not be empty."
    if not data.get("address"):
        return False, "Address must not be empty."
    return True, ""
