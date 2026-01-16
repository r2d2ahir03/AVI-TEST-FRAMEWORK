# Avi Test Framework

## Project Structure
```
.
├── main.py               # Entry point for running tests
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── config/               # Configuration files
│   ├── api.yaml          # API endpoint configurations
│   ├── credentials.yaml   # User credentials for API access
│   └── testcases.yaml     # Test case definitions
├── framework/            # Core framework code
│   ├── __init__.py       # Package initialization
│   ├── api_client.py     # API client for making requests
│   ├── config_loader.py   # YAML configuration loader
│   ├── executor.py       # Parallel task executor
│   ├── mock_connectors.py # Mock functions for testing
│   └── validations.py    # Validation functions for test assertions
└── tests/                # Test cases
    └── test_disable_vs.py # Test case for disabling virtual services
```

## Installation
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage
To execute the tests, run the following command:

```bash
python main.py
```

