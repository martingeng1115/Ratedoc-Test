Before running the tests, ensure you have the following installed on your machine:
*   [Node.js](https://nodejs.org/) (LTS Version)
*   [Python 3.8+](https://www.python.org/)
*   [Git](https://git-scm.com/)

 1. API Testing Setup (Newman)
Install Newman globally via npm to run the Postman collections from the command line:
```bash
npm install -g newman
2. UI Testing Setup (Playwright/Python)
It is highly recommended to use a virtual environment for the Python dependencies.

Bash
# Clone the repository
git clone [https://github.com/ishti-du/ratedoc-tests.git](https://github.com/ishti-du/ratedoc-tests.git)
cd ratedoc-tests

# Create and activate a virtual environment
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

# Install dependencies and Playwright browsers
pip install pytest-playwright requests
playwright installRunning the Tests
Running the API Tests
Execute the Newman CLI command against the JSON collection. The tests rely on a baseUrl environment variable.

Bash
newman run ratedoctor_collection.json --env-var "baseUrl=[http://159.89.231.16:3000](http://159.89.231.16:3000)"
Running the UI Tests
Ensure your Python virtual environment is activated, then use Pytest to execute the Playwright script.

To run headless (in the background):

Bash
pytest test_ui_features.py
To run visually (opens a browser window so you can watch):

Bash
pytest test_ui_features.py --headed
