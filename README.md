# Introduction
Utilize the [FinnHub](https://finnhub.io/) API to gather data parsed out of 10K financial statements, then reformat that data into usable analysis. With a list of ticker symbols as input, the script queries FinnHub and receives a list of 10K documents. Each document is represented by a series of key-value paris. The script records basic information, such as year, and the user chooses what quantitative metric to store and then analyze (by default net income). The script then uses the company profile endpoint of the FinnHub api to add information such as 'Industry' and 'MarketCap'.

Before the analysis stage each row represents a 10K document. So each row can be thought of as a unique company-year pair. During the analysis stage, the script creates one row per company that shows the change of the company over the years (in the quantitative metric). This allows for easy horizontal analysis on the company for that quantitative metric.

# Installation
Download the package from GitHub, and get a [FinnHub](https://finnhub.io/) API key. Create a file named "api.txt" and store it in the same folder as the rest of the package. In this text file should be the API key and no other text, formatting, etc.

# Usage

Run the script through the main.py file. Edit the default settings if it sutis your needs.
```
python main.py
```
Type 'y' to start the script, 'l' to see the current settings, and 'n' to cancel the script.
# Example