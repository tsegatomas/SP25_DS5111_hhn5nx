# Project Setup Guide

This document outlines the basic steps to quickly set up a VM and environment for a web-scraping project using Chrome headless browser and Python.

## VM Setup Steps

### Initial Setup

Run an initial package update:
```bash
sudo apt update
```

Clone your repository:
```bash
git clone <your_repository_url>
cd SP25_DS5111_hhn5nx
```

Run the initialization script:
```bash
./init.sh
```

This installs necessary tools (`make`, Python venv, `tree`).

### Chrome Headless Browser

Install Chrome headless:
```bash
./scripts/install_chrome_headless.sh
```

Quick test installation:
```bash
google-chrome-stable --version
```

### Python Environment

Make sure `requirements.txt` contains:
```
pandas
lxml
```

Set up your Python environment:
```bash
make update
```

### Test Headless Browser

Run this command to test the full pipeline:
```bash
make ygainers.csv
```

Check if data is correctly downloaded:
```bash
head ygainers.csv
```

### Final Directory Structure

Your directory should look like this (excluding the virtual environment `env`):

```bash
tree SP25_DS5111_hhn5nx -I env

SP25_DS5111_hhn5nx/
├── Makefile
├── README.md
├── init.sh
├── requirements.txt
├── sample_data
│   └── ygainers.csv
├── scripts
│   ├── install_chrome_headless.sh
│   ├── setup_git_creds.sh
│   └── setup_ssh_keys.sh
├── ygainers.csv
└── ygainers.html
```

### Sample Data
A sample data file (`ygainers.csv`) is provided in the `sample_data/` directory.

