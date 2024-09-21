import itertools
import requests
import time
import sys

# Mojang API URL for checking username profiles
mojang_api_url = "https://api.mojang.com/users/profiles/minecraft/"

# Characters allowed in the usernames
characters = 'abcdefghijklmnopqrstuvwxyz0123456789_'

# Generate all 3-character combinations
combinations = [''.join(comb) for comb in itertools.product(characters, repeat=3)]
total_usernames = len(combinations)

# Function to check username availability using Mojang API
def is_username_available(username):
    try:
        response = requests.get(f"{mojang_api_url}{username}", timeout=5)
        
        # Handle different status codes
        if response.status_code == 204 or "Couldn't find any profile with name" in response.text:
            return username, "Available"
        elif response.status_code == 200:
            return username, "Taken"
        elif response.status_code == 429:  # Rate limit exceeded
            return username, "Rate Limited"
        else:
            return username, f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return username, f"Error: {e}"

# Check usernames and save results
available_usernames = []
taken_usernames = []

print("Checking username availability. This may take some time...")

start_time = time.time()

# Open files for live writing
with open('available_usernames.txt', 'a') as available_file, open('taken_usernames.txt', 'a') as taken_file:
    for index, username in enumerate(combinations):
        while True:
            username, status = is_username_available(username)
            
            if status == "Available":
                available_usernames.append(username)
                available_file.write(username + '\n')  # Write to available file immediately
                available_file.flush()  # Flush to ensure the write is saved immediately
                print(f"Available: {username}")
                break  # Exit the retry loop
            elif status == "Taken":
                taken_usernames.append(username)
                taken_file.write(username + '\n')  # Write to taken file immediately
                taken_file.flush()  # Flush to ensure the write is saved immediately
                print(f"Taken: {username}")
                break  # Exit the retry loop
            elif status == "Rate Limited":
                print(f"{username}: Rate limit exceeded. Retrying in 10 seconds...")
                time.sleep(10)  # Wait 10 seconds before retrying
            else:
                print(f"{username}: {status}")
                break  # Exit the retry loop for other errors

        # Update ETA
        elapsed_time = time.time() - start_time
        remaining_time = (total_usernames - index - 1) * (elapsed_time / (index + 1))  # Average time per check
        eta = time.strftime("%H:%M:%S", time.gmtime(remaining_time))  # Format remaining time

        # Clear the previous line before printing progress
        sys.stdout.write(f"\rProgress: {index + 1}/{total_usernames} | ETA: {eta}      ")
        sys.stdout.flush()

        time.sleep(0.5)  # Adjust as necessary for your network and API limits

print(f"\n\nTotal Available Usernames: {len(available_usernames)}")
print(f"Total Taken Usernames: {len(taken_usernames)}")
print("Results saved live to 'available_usernames.txt' and 'taken_usernames.txt'")
