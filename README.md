# Minecraft Username Availability Checker

This Python script checks the availability of 3-character Minecraft usernames using the Mojang API and saves the results to files in real-time.

## Features

- **3-Character Username Check**: Generates and checks all possible 3-character Minecraft usernames.
- **Real-Time File Updates**: Writes available and taken usernames to separate files (`available_usernames.txt` and `taken_usernames.txt`) as they are found.
- **Rate Limit Handling**: Pauses and retries after encountering rate limits from the API.
- **Progress and ETA Display**: Shows progress and estimated time remaining (ETA) for checking all usernames.

## Requirements

- **Python 3.x**
- **`requests`** library (install using `pip install requests`)

## Setup

### 1. Clone or Download the Repository

Clone this repository using Git:

```bash
git clone https://github.com/AriasADev/3-char-username-checker.git
```

Or download the ZIP file and extract it to your preferred directory.

### 2. Install Required Libraries

Ensure that the `requests` library is installed. You can install it using:

```bash
pip install requests
```

## Usage

### 1. Running the Script

Navigate to the directory containing the script:

```bash
cd /path/to/directory
```

Run the script:

```bash
python namemc.py
```

### 2. Monitoring Output

The script will display real-time progress in the terminal, indicating which usernames are available or taken. It will also show the progress and estimated time of completion.

**Output Files**:
- `available_usernames.txt`: Contains all available usernames found during the check.
- `taken_usernames.txt`: Contains all taken usernames found during the check.

These files are updated live as the program runs.

## Customization

### Modify Username Length

To check usernames of a different length (e.g., 4 characters), modify the `itertools.product` call:

1. Open `namemc.py`.
2. Change this line:

```python
combinations = [''.join(comb) for comb in itertools.product(characters, repeat=3)]
```

To:

```python
combinations = [''.join(comb) for comb in itertools.product(characters, repeat=4)]
```

This will check 4-character usernames instead of 3.

### Adjust Rate Limits

If you encounter frequent rate limits:

1. Open `namemc.py`.
2. Adjust the sleep time after hitting a rate limit:

```python
time.sleep(10)  # Wait 10 seconds before retrying
```

Increase this value if needed to avoid excessive rate limiting.

## Troubleshooting

### Common Errors

- **Rate Limit (429)**: If you encounter a rate limit too frequently, increase the delay between requests.
- **Request Timeout**: Ensure your internet connection is stable. You can increase the request timeout if necessary by modifying this part of the script:

```python
response = requests.get(f"{mojang_api_url}{username}", timeout=5)
```

Increase the `timeout` value as needed.

### Debugging

To add more detailed logging for debugging purposes, insert print statements to show additional details about the script's execution, such as the exact error messages or response codes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
