from .base_gainers import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self):
        print("Downloading Yahoo gainers...")
        return "Data from Yahoo"

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self):
        print("Normalizing Yahoo gainers data...")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers data with timestamp...")
