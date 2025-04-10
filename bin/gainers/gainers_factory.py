from .gainer_yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .gainer_wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:
    def __init__(self, choice):
        if choice not in ['yahoo', 'wsj']:
            raise ValueError(f"Unrecognized gainer type: {choice}")
        self.choice = choice

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
