# my-first-app


## Setup - Environment

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```


## Setup

Install Packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from AlphaVantage](https://www.alphavantage.co/support/#api-key) or from the professor (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"

SENDGRID_API_KEY="_________"
SENDER_ADDRESS="_________"
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the Unemployment Report:

```sh
python app/unemployment_report.py
```

Run the Email Service:

```sh
python app/email_service.py
```