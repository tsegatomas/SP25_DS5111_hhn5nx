from bin.gainers.gainers_factory import GainerFactory
import sys

# Template/Runner Class
class ProcessGainer:
    def __init__(self, downloader, processor):
        self.downloader = downloader
        self.processor = processor

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.processor.normalize()

    def _save_to_file(self):
        self.processor.save_with_timestamp()

    def process(self):
        self._download()
        self._normalize()
        self._save_to_file()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main_script.py <yahoo|wsj>")
        sys.exit(1)
    
    choice = sys.argv[1]
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    runner = ProcessGainer(downloader, processor)
    runner.process()
