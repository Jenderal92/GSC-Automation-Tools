#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import json
import codecs
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

def print_banner():
    banner = """
    ===============================================
    GOOGLE SEARCH CONSOLE AUTOMATION TOOLS      
    Automate GSC Data Retrieval Effortlessly
    ===============================================
    """
    print(banner)

def authenticate_gsc(credentials_file):
    try:
        scopes = ['https://www.googleapis.com/auth/webmasters.readonly']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scopes)
        service = build('searchconsole', 'v1', credentials=credentials)
        print("[INFO] Authentication successful.")
        return service
    except Exception as e:
        print("[ERROR] Authentication failed: {}".format(e))
        raise

def get_gsc_data(service, site_url, start_date, end_date, dimensions):
    try:
        request = {
            'startDate': start_date,
            'endDate': end_date,
            'dimensions': dimensions
        }
        response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        print("[INFO] Data retrieval successful.")
        return response.get('rows', [])
    except Exception as e:
        print("[ERROR] Failed to fetch data: {}".format(e))
        return []

def save_to_json(data, output_file):
    if not data:
        print("[INFO] No data retrieved.")
        return
    
    with codecs.open(output_file, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        
    print("[INFO] Data saved to {}".format(output_file))

def get_valid_url():
    while True:
        site_url = raw_input("Enter url (e.g., https://site.com):  ").strip()
        if site_url:
            return site_url
        else:
            print("[ERROR] URL cannot be empty. Please enter a valid URL.")
            
            
if __name__ == "__main__":
    print_banner()

    CREDENTIALS_FILE = "credentials.json" #Replace with your credentials
    SITE_URL = get_valid_url()
    OUTPUT_FILE = "gsc_data.json" 
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

    # Dimensions (change as needed: ['query', 'page', 'country', 'device'])
    DIMENSIONS = ['query']

    service = authenticate_gsc(CREDENTIALS_FILE)
    gsc_data = get_gsc_data(service, SITE_URL, start_date, end_date, DIMENSIONS)

    save_to_json(gsc_data, OUTPUT_FILE)
