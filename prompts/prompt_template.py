create_order_template = "Create a transport order based on this client request: {text}"

extract_information_template = (
    "Extract all important information from the following text query: {text}"
)

extract_information_by_keys_template = (
    "Please extract (if possible) the following information from the client request:\n"
    "1. document_number\n"
    "2. order_date\n"
    "3. client_name\n"
    "4. address\n"
    "5. phone\n"
    "6. email\n"
    "7. transpot_type\n"
    "8. delivery_date\n"
    "9. packing\n"
    "10. notes (here you need to extract any important information related to the transport order, but not included in the fields above)\n\n"
    "Client request: {text}\n\n"
    "Reply in JSON format containing only keys and values."
)
