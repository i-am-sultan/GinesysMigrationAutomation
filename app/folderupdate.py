import os
import requests
import shutil
import zipfile
from io import BytesIO

def get_latest_release_info(repo):
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        release_info = response.json()
        return release_info
    else:
        print(f"Failed to fetch release information. Status code: {response.status_code}")
        return None

def checkForUpdates(log_window):
    log_window.append('Checking for updates...')
    try:
        repo = "i-am-sultan/MigrationAutomation"
        latest_release = get_latest_release_info(repo)

        if latest_release:
            latest_version = latest_release['tag_name']
            assets = latest_release['assets']

            if assets:
                update_asset = assets[0]  # Assuming the first asset is the one you want to download
                update_url = update_asset['browser_download_url']

                global version_path

                # Read the current version from a file (version.txt in the app directory)
                with open(version_path, 'r') as f:
                    current_version = f.read().strip()

                log_window.append(f'Current version: {current_version}')
                log_window.append(f'Latest version: {latest_version}')

                # Compare versions
                if latest_version != current_version:
                    log_window.append('New version available. Downloading and applying update...')

                    # Download the update
                    response = requests.get(update_url)
                    if response.status_code == 200:
                        # Define the update directory
                        update_dir_name = f"MigAutomation_{latest_version}"
                        update_dir_path = os.path.join(os.getcwd(), update_dir_name)

                        # Extract the zip file into the new directory
                        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
                            zip_ref.extractall(update_dir_path)

                        log_window.append('Update downloaded and extracted successfully.')

                        # Move the old version to PreviousVersions folder
                        old_version_dir = os.path.join(os.getcwd(), f"MigrationAutomation_{current_version}")
                        previous_versions_dir = os.path.join(os.getcwd(), 'PreviousVersions')
                        if not os.path.exists(previous_versions_dir):
                            os.makedirs(previous_versions_dir)
                        if os.path.exists(old_version_dir):
                            shutil.move(old_version_dir, previous_versions_dir)

                        # Update the current version
                        with open(version_path, 'w') as f:
                            f.write(latest_version)

                        log_window.append('Update applied successfully.')
                    else:
                        log_window.append(f"Failed to download update. Status code: {response.status_code}")
                else:
                    log_window.append('You are already using the latest version.')
            else:
                log_window.append('No assets found in the latest release.')
        else:
            log_window.append('Failed to fetch latest release information.')

    except Exception as e:
        log_window.append(f'Error checking and applying updates: {e}')

# Example usage with a dummy log window (list)
log_window = []
version_path = 'version.txt'  # Ensure this points to the correct version file
checkForUpdates(log_window)
for log in log_window:
    print(log)
