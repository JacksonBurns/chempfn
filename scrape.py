import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# List of benchmarks
polaris_benchmarks = [
    "polaris/pkis2-ret-wt-cls-v2", "polaris/pkis2-ret-wt-reg-v2",
    "polaris/pkis2-kit-wt-cls-v2", "polaris/pkis2-kit-wt-reg-v2",
    "polaris/pkis2-egfr-wt-reg-v2", "polaris/adme-fang-solu-1",
    "polaris/adme-fang-rppb-1", "polaris/adme-fang-hppb-1",
    "polaris/adme-fang-perm-1", "polaris/adme-fang-rclint-1",
    "polaris/adme-fang-hclint-1", "tdcommons/lipophilicity-astrazeneca",
    "tdcommons/ppbr-az", "tdcommons/clearance-hepatocyte-az",
    "tdcommons/cyp2d6-substrate-carbonmangels", "tdcommons/half-life-obach",
    "tdcommons/cyp2c9-substrate-carbonmangels", "tdcommons/clearance-microsome-az",
    "tdcommons/dili", "tdcommons/bioavailability-ma",
    "tdcommons/vdss-lombardo", "tdcommons/cyp3a4-substrate-carbonmangels",
    "tdcommons/pgp-broccatelli", "tdcommons/caco2-wang",
    "tdcommons/herg", "tdcommons/bbb-martins",
    "tdcommons/ames", "tdcommons/ld50-zhu"
]

base_url = "https://polarishub.io/benchmarks/"
all_rows = []

for path in polaris_benchmarks:
    url = f"{base_url}{path}"
    print(f"Fetching: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table')
            if table:
                # FIX: Do not filter out empty headers. Keep them to preserve indexing.
                headers = [th.text.strip() for th in table.find_all('th')]
                
                for tr in table.find_all('tr')[1:]:
                    cells = [td.text.strip() for td in tr.find_all('td')]
                    if cells:
                        row_data = {"Benchmark_ID": path}
                        for i, val in enumerate(cells):
                            # FIX: If the header is empty, assign it a generic name or ignore the column
                            if i < len(headers) and headers[i]:
                                header_name = headers[i]
                            else:
                                header_name = f"col_{i}"
                            
                            # Only add the data if it actually belongs to a named column
                            if header_name.startswith("col_") and val == "":
                                continue # Skip empty structural cells
                                
                            row_data[header_name] = val
                        all_rows.append(row_data)
        time.sleep(1) 
    except Exception as e:
        print(f"Failed to fetch {path}: {e}")

if all_rows:
    df = pd.DataFrame(all_rows)
    # Optional: Drop the unnamed structural columns entirely to clean up the DataFrame
    cols_to_drop = [c for c in df.columns if c.startswith('col_')]
    df = df.drop(columns=cols_to_drop)
    
    outname = f"polaris_benchmarks_leaderboard_{time.strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(outname, index=False)
    print(f"Success! Data saved to '{outname}'")
else:
    print("No data collected.")
    