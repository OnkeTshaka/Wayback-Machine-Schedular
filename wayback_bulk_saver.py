#!/usr/bin/env python3
"""
Wayback Machine Bulk URL Saver
Automatically saves a list of URLs to the Internet Archive's Wayback Machine
"""

import time
import logging
from datetime import datetime
from typing import List, Dict, Optional
import requests
from waybackpy import WaybackMachineSaveAPI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('wayback_saver.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WaybackBulkSaver:
    def __init__(self, delay_between_requests: float = 5.0):
        """
        Initialize the bulk saver
        
        Args:
            delay_between_requests: Delay in seconds between archive requests (be respectful to the service)
        """
        self.delay = delay_between_requests
        self.results = []
        
    def save_url(self, url: str) -> Dict[str, any]:
        """
        Save a single URL to Wayback Machine
        
        Args:
            url: The URL to archive
            
        Returns:
            Dictionary with result information
        """
        result = {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'success': False,
            'archive_url': None,
            'error': None
        }
        
        try:
            logger.info(f"Attempting to save: {url}")
            
            # Create save API instance
            save_api = WaybackMachineSaveAPI(url)
            
            # Save the URL
            archive_url = save_api.save()
            
            result['success'] = True
            result['archive_url'] = archive_url
            logger.info(f"✅ Successfully archived: {url} -> {archive_url}")
            
        except Exception as e:
            result['error'] = str(e)
            logger.error(f"❌ Failed to archive {url}: {e}")
            
        return result
    
    def save_urls_from_list(self, urls: List[str]) -> List[Dict[str, any]]:
        """
        Save multiple URLs with delay between requests
        
        Args:
            urls: List of URLs to archive
            
        Returns:
            List of result dictionaries
        """
        logger.info(f"Starting bulk save of {len(urls)} URLs")
        
        for i, url in enumerate(urls, 1):
            logger.info(f"Processing {i}/{len(urls)}: {url}")
            
            result = self.save_url(url)
            self.results.append(result)
            
            # Add delay between requests (except for the last one)
            if i < len(urls):
                logger.info(f"Waiting {self.delay} seconds before next request...")
                time.sleep(self.delay)
        
        return self.results
    
    def save_urls_from_file(self, filename: str) -> List[Dict[str, any]]:
        """
        Save URLs from a text file (one URL per line)
        
        Args:
            filename: Path to file containing URLs
            
        Returns:
            List of result dictionaries
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            logger.info(f"Loaded {len(urls)} URLs from {filename}")
            return self.save_urls_from_list(urls)
            
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            return []
        except Exception as e:
            logger.error(f"Error reading file {filename}: {e}")
            return []
    
    def generate_report(self, output_file: str = "wayback_report.txt"):
        """
        Generate a summary report of the archiving results
        
        Args:
            output_file: Path to save the report
        """
        if not self.results:
            logger.warning("No results to report")
            return
        
        successful = [r for r in self.results if r['success']]
        failed = [r for r in self.results if not r['success']]
        
        report = f"""
WAYBACK MACHINE BULK SAVE REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY:
Total URLs processed: {len(self.results)}
Successfully archived: {len(successful)}
Failed to archive: {len(failed)}
Success rate: {len(successful)/len(self.results)*100:.1f}%

SUCCESSFUL ARCHIVES:
"""
        
        for result in successful:
            report += f"✅ {result['url']} -> {result['archive_url']}\n"
        
        if failed:
            report += "\nFAILED ARCHIVES:\n"
            for result in failed:
                report += f"❌ {result['url']} - Error: {result['error']}\n"
        
        # Save report to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Report saved to {output_file}")
        print(report)

def main():
    """
    Main function - demonstrates usage
    """
    # Example URLs to archive
    example_urls = [
        "https://www.python.org",
        "https://github.com",
        "https://stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    
    # Create saver instance with 3-second delay between requests
    saver = WaybackBulkSaver(delay_between_requests=3.0)
    
    print("=== Wayback Machine Bulk URL Saver ===\n")
    
    choice = input("Choose input method:\n1. Use example URLs\n2. Load from file\n3. Enter URLs manually\nChoice (1-3): ").strip()
    
    if choice == "1":
        # Use example URLs
        results = saver.save_urls_from_list(example_urls)
        
    elif choice == "2":
        # Load from file
        filename = input("Enter filename (e.g., urls.txt): ").strip()
        if not filename:
            filename = "urls.txt"
            
        # Create example file if it doesn't exist
        try:
            with open(filename, 'r'):
                pass
        except FileNotFoundError:
            print(f"Creating example file: {filename}")
            with open(filename, 'w') as f:
                f.write("# Add your URLs here, one per line\n")
                f.write("# Lines starting with # are ignored\n")
                for url in example_urls:
                    f.write(f"{url}\n")
            print(f"Example URLs added to {filename}. Edit the file and run again.")
            return
            
        results = saver.save_urls_from_file(filename)
        
    elif choice == "3":
        # Manual entry
        urls = []
        print("Enter URLs (one per line, empty line to finish):")
        while True:
            url = input("> ").strip()
            if not url:
                break
            urls.append(url)
        
        if urls:
            results = saver.save_urls_from_list(urls)
        else:
            print("No URLs entered.")
            return
    else:
        print("Invalid choice.")
        return
    
    # Generate and display report
    print("\n" + "="*50)
    saver.generate_report()

if __name__ == "__main__":
    main()