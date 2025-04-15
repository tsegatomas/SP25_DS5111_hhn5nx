# my_script.py
import datetime

def get_yahoo_gainers():
    """
    Simulates downloading Yahoo gainer data.
    Replace this function with the actual download code if available.
    """
    print("Downloading Yahoo gainers...")
    # For now, we just return a simple string.
    return "Yahoo data"

def get_wsj_gainers():
    """
    Simulates downloading WSJ gainer data.
    Replace this function with the actual download code if available.
    """
    print("Downloading WSJ gainers...")
    return "WSJ data"

def save_to_csv(data, filename):
    """
    Saves the provided data to a CSV file.
    """
    with open(filename, "w") as f:
        f.write(data)
    print(f"Saved file: {filename}")

def main():
    # Get the current timestamp formatted as YYYYMMDD_HHMMSS
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Call the functions to download data
    yahoo_data = get_yahoo_gainers()
    wsj_data = get_wsj_gainers()

    # Create filenames with timestamps
    yahoo_filename = f"yahoo_gainers_{now}.csv"
    wsj_filename = f"wsj_gainers_{now}.csv"

    # Save the data to CSV files
    save_to_csv(yahoo_data, yahoo_filename)
    save_to_csv(wsj_data, wsj_filename)

if __name__ == "__main__":
    main()
