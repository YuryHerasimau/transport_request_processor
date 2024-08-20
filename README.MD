# OutVise Interview Task
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Test task for the position of QA Expert with LLM in [OutVise Project on process automation (text recognition) for creating transport orders](https://www.outvise.com/walls/opportunity/358286)

## Description
This script is designed to process customer transport requests. Using natural language processing technologies and OpenAI API (GPT-3), important information is extracted from requests and saved in JSON format.

This script does the following:

1. Extracts transport order data from PDF and images.
2. Splits the data into specific fields in JSON.
3. Validates the extracted data.
4. Contains tests to verify correct operation.

## Getting Started

### Installing 
1. Clone the repository:
```
git clone https://github.com/YuryHerasimau/transport_request_processor.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Сreate a `.env` file in the root directory and pass your API key: `OPENAI_API_KEY=<OPENAI_API_KEY>` 

### Usage
1. `Starting application processing:`
Enter the path to the file (PDF or image) you want to process and run the command in the terminal:
```
python main.py
```

2. `Data format:`
After processing, important information is saved in the `requests.json` file in JSON format.

3. `Testing:`
To run tests, run the following command:
```
python -m unittest discover -s tests
```
To run specific test, run the following command:
```
python -m unittest tests/test_gpt_handler.py
python -m unittest tests/test_data_validator.py
```