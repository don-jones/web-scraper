import os
import time
import requests
from requests.auth import HTTPBasicAuth

# -------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------
CONSUMER_KEY = "hyMsuO8qKG8kDrf6rxKmmIygJbEZICGM"
CONSUMER_SECRET = "o4vBdR7nQc4WUV9L"

SEARCH_QUERY = "white paper texture"
TOTAL_IMAGES_TO_DOWNLOAD = 500
DOWNLOAD_FOLDER = "shutterstock_api_images"
# -------------------------------------------------------------

def download_via_shutterstock_api():
    if "YOUR_" in CONSUMER_KEY or "YOUR_" in CONSUMER_SECRET:
        print("Error: Please replace the placeholder API keys with your real credentials.")
        return

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    url = "https://shutterstock.com"
    url = "https://api.shutterstock.com/v2/images/search"
    auth = HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
    
    images_downloaded = 0
    page = 1
    per_page = 100  # Max results per API request allowed by Shutterstock
    
    print(f"Starting API download for query: '{SEARCH_QUERY}'")

    while images_downloaded < TOTAL_IMAGES_TO_DOWNLOAD:
        # Calculate how many images are left to request
        remaining = TOTAL_IMAGES_TO_DOWNLOAD - images_downloaded
        current_per_page = min(per_page, remaining)
        
        params = {
            "query": SEARCH_QUERY,
            "page": page,
            "per_page": current_per_page,
            "view": "minimal"  # Efficient, returns basic metadata and preview links
        }
        
        try:
            response = requests.get(url, auth=auth, params=params)
            
            if response.status_code == 401:
                print("Error 401: Unauthorized. Please check your Consumer Key and Secret.")
               
                break
            elif response.status_code == 202:
                print("API Status 202: Server is provisioning your app keys. Waiting 30 seconds before retry...")
                time.sleep(30)
                continue  # Retries the exact same page iteration

            elif response.status_code != 200:
                print(f"API Error {response.status_code}: {response.text}")
                break
                
            data = response.json()
            results = data.get("data", [])
            
            if not results:
                print("No more images found for this query.")
                break
                
            print(f"Fetched page {page} metadata. Processing {len(results)} images...")
            
            for item in results:
                image_id = item.get("id")
                # Extract image asset sizes. Options usually include: 'huge_thumb', 'large_thumb', 'preview'
                assets = item.get("assets", {})
                preview_data = assets.get("preview") or assets.get("large_thumb")
                
                if not preview_data or "url" not in preview_data:
                    continue
                    
                img_url = preview_data["url"]
                
                # Determine file extension from URL or fallback to jpg
                ext = "jpg"
                if ".png" in img_url.lower():
                    ext = "png"
                    
                filename = f"shutterstock_{image_id}.{ext}"
                filepath = os.path.join(DOWNLOAD_FOLDER, filename)
                
                try:
                    # Download the image file directly
                    img_response = requests.get(img_url, timeout=15)
                    if img_response.status_code == 200:
                        with open(filepath, "wb") as f:
                            f.write(img_response.content)
                        images_downloaded += 1
                        print(f"[{images_downloaded}/{TOTAL_IMAGES_TO_DOWNLOAD}] Downloaded: {filename}")
                    else:
                        print(f"Failed to download image asset {image_id}: Status {img_response.status_code}")
                except Exception as e:
                    print(f"Error downloading asset {image_id}: {e}")
                    
                # Small polite delay between file downloads (unlikely to trigger API caps)
                time.sleep(0.2)
                
                if images_downloaded >= TOTAL_IMAGES_TO_DOWNLOAD:
                    break
                    
            # Increment page for the next batch loop
            page += 1
            # Brief delay between API search page updates
            time.sleep(1.0)
            
        except Exception as e:
            print(f"Network error during API lookup: {e}")
            break

    print(f"\nProcess finished! Saved {images_downloaded} images to '{DOWNLOAD_FOLDER}'.")

if __name__ == "__main__":
    download_via_shutterstock_api()

