from abc import ABC, abstractmethod

# Downloader Abstract Base Class
class GainerDownload(ABC):
    def __init__(self, url=None):
        self.url = url

    @abstractmethod
    def download(self):
        """
        Abstract method to download data.
        Subclasses must implement this.
        """
        pass

# Processor Abstract Base Class
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        """
        Abstract method to normalize the downloaded data.
        Subclasses must implement this.
        """
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """
        Abstract method to save processed data with a timestamp.
        Subclasses must implement this.
        """
        pass
