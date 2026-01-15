# Data QA Findings – Web Scraping Project

## QA Scope
Manual validation of scraped book data against the live website.

---

## Issues Identified

### Issue 1: Relative URLs
- Field: url
- Description: Product URLs are stored as relative paths instead of full URLs.
- Impact: Requires additional processing before use.
- Example: ../../../the-grand-design_405/index.html

---

### Issue 2: Availability Formatting
- Field: availability
- Description: Availability values include extra whitespace and newline characters.
- Expected: Clean values (e.g., "In stock")
- Actual: Values include line breaks.

---

### Issue 3: Rating Representation
- Field: rating
- Description: Ratings are stored as text labels (e.g., "Three", "Four") instead of numeric values.
- Impact: Requires transformation for analytics.

---

### Issue 4: Pagination Limitation
- Description: Scraper collects data only from the first 5 pages.
- Impact: Dataset is incomplete.
