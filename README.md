## Google Search Console Automation Tools

![GSC-Automation-Tools Jenderal92](https://github.com/user-attachments/assets/ffef1158-4590-49bf-862a-eaed954b3a9f)

This tool automates the retrieval of performance data from Google Search Console using the API, allowing for efficient website performance analysis. The data is saved as a JSON file, making it easy to review and process further. It is designed for compatibility with **Python 2.7**.

---

## **Features**

- **Secure Authentication:** Uses Google API credentials with a Service Account for secure access.  
- **Automated Data Retrieval:** Fetches performance data (clicks, impressions, CTR, position) based on customizable dimensions.  
- **Json Export:** Saves the retrieved data directly to a Json file.  
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
   - **`OUTPUT_FILE`**: The name of the JSON output file.  
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
