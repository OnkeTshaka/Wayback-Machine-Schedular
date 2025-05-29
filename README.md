# Wayback Machine Bulk Saver

## Python program that saves lists of webpages to the Internet Archive's Wayback machine. Perfect for preserving web content systematically.

## Key Features

- The program includes a **3-5 second delay** between requests to be respectful to the Internet Archive servers,
- **Comprehensive logging** to file and console (e.g. wayback_saver.log)
- **Error Handling** for failed archives
- **Progress tracking** with timestampes
- **Detailed reports** showing success/failure rates (e.g. wayback_report.txt)
- **Flexible input methods** (Use example URLs, Load from a text file or Enter URLs manually)

## Running the Program (windows):

**Create a virtual environment**

```bash
py -m venv .venv
```

**Activate virtual environment**

```
.venv/scripts/activate
```

**Install request packages**

```
pip install -r requirements.txt
```

**Run program**

```
py wayback_saver.py
```

## Usage Options

1. **Use example URLs** - Great for testing
2. **Load from a text file**

   a. Create a text file (**urls.txt**)

   b. Add **one url per line**

3. **Enter URLs manually** - Good file
