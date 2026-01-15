# Web Scraped Data Validation & Quality Assurance

## Project Overview
This project focuses on validating data collected from a web scraping pipeline. 
The goal was to manually QA scraped outputs, identify data quality issues, and prepare a clean dataset for downstream use.

## Data Source
https://books.toscrape.com

## Data Collected
- Book title
- Price
- Availability
- Rating
- Product URL

## QA Checks Performed
- Accuracy checks against live web pages
- Completeness checks for missing fields
- Consistency checks across records
- Duplicate detection

## Issues Identified
- Relative URLs instead of absolute URLs
- Inconsistent availability formatting
- Ratings stored as text instead of numeric values
- Incomplete data due to pagination limits

## Tools Used
- Python
- BeautifulSoup
- Pandas
