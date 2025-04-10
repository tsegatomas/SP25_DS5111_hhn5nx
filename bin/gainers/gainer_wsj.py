from .base_gainers import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self):
        print("Downloading WSJ gainers...")
        return "Data from WSJ"

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self):
        print("Normalizing WSJ gainers data...")

    def save_with_timestamp(self):
        print("Saving WSJ gainers data with timestamp...")
