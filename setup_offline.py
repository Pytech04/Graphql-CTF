#!/usr/bin/env python3
"""
Setup script to make the CTF challenge completely offline
Downloads Bootstrap and FontAwesome assets locally
"""

import os
import urllib.request
import shutil

def download_file(url, filepath):
    """Download a file from URL to local filepath"""
    print(f"Downloading {url}...")
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"✅ Saved to {filepath}")
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")

def setup_offline_assets():
    """Download all external assets for offline use"""
    
    # Create directories
    os.makedirs("static/css", exist_ok=True)
    os.makedirs("static/js", exist_ok=True)
    os.makedirs("static/fonts", exist_ok=True)
    
    # Bootstrap CSS (Dark Theme)
    download_file(
        "https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css",
        "static/css/bootstrap.min.css"
    )
    
    # Bootstrap JS
    download_file(
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
        "static/js/bootstrap.bundle.min.js"
    )
    
    # FontAwesome CSS
    download_file(
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
        "static/css/fontawesome.min.css"
    )
    
    # FontAwesome Fonts
    font_urls = [
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/fa-solid-900.woff2",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/fa-regular-400.woff2",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/fa-brands-400.woff2"
    ]
    
    for url in font_urls:
        filename = url.split("/")[-1]
        download_file(url, f"static/fonts/{filename}")
    
    print("\n🎉 Offline setup complete!")
    print("Your CTF challenge is now completely self-contained.")

if __name__ == "__main__":
    setup_offline_assets()