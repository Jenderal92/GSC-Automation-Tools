# **Google Search Console Automation Tools**

This tool automates the retrieval of performance data from Google Search Console using the API, allowing for efficient website performance analysis. The data is saved as a CSV file, making it easy to review and process further. It is designed for compatibility with **Python 2.7**.
---

## **Features**
- **Secure Authentication:** Uses Google API credentials with a Service Account for secure access.  
- **Automated Data Retrieval:** Fetches performance data (clicks, impressions, CTR, position) based on customizable dimensions.  
- **CSV Export:** Saves the retrieved data directly to a CSV file.  
---

## **Requirements**
1. **Google Search Console API enabled** in a Google Cloud project.  
2. **Python 2.7** installed on your system.  
3. Dependencies:  
   - `google-api-python-client`  
   - `oauth2client`

Install the dependencies with:  
```bash
pip install google-api-python-client oauth2client
```

---

## **How to Obtain the Credentials JSON**
1. Log in to [Google Cloud Console](https://console.cloud.google.com/).  
2. Enable the **Google Search Console API**.  
3. Create a **Service Account** and download the JSON credentials file.  
4. Add the Service Account's email (found in the JSON file under `client_email`) as a **user** in Google Search Console with **Full access** to your property.

For a detailed guide, see [Google's API documentation](https://developers.google.com/search/apis).

---

## **How to Use**
1. Save the credentials JSON file in the same directory as this tool.  
2. Update the configuration in `gsc_automation.py`:  
   - **`CREDENTIALS_FILE`**: Path to your JSON credentials file.  
   - **`SITE_URL`**: The URL of the Google Search Console property you want to retrieve data from.  
   - **`OUTPUT_FILE`**: The name of the CSV output file.  
3. Run the script with:  
   ```bash
   python gsc_automation.py
   ```

---

## **Default Configuration**
- **Date Range**: Automatically retrieves data for the last 30 days.  
- **Dimensions**: By default, the tool uses the `'query'` dimension. You can change it to:
  - `'page'`
  - `'country'`
  - `'device'`
  - Or any combination of dimensions supported by the API.

---

## **Output**
- The tool generates a CSV file with the following structure:  
  - Columns: `query`, `clicks`, `impressions`, `ctr`, `position`  
- Example output:  
  ```
  query,clicks,impressions,ctr,position
  example query 1,10,100,0.1,1.5
  example query 2,20,150,0.13,2.0
  ```

---

### **Keywords**
- Google Search Console  
- GSC Automation  
- Python 2.7 Tools  
- CSV Data Export  
- API Integration  