import requests
import os

def download_files(base_url, save_dir, max_attempts=1000):
    """
    Sequentially download files from a base URL until a file doesn't exist.

    Parameters:
    - base_url: The base URL with a placeholder for the file part (e.g., 'https://example.com/part-{i:03d}-00000.npy').
    - save_dir: The directory to save the downloaded files.
    - max_attempts: Maximum number of parts to attempt before stopping.
    """
    os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist
    part_number = 0

    while part_number < max_attempts:
        file_url = base_url.format(i=part_number)
        file_name = f"train_preprocessed_c4_part_{part_number:03d}.npy"
        file_path = os.path.join(save_dir, file_name)

        print(f"File {file_name}")
        
        if os.path.isfile(file_path):
            print(f"    {file_path} already exists. Skipping.")
            continue

        try:
            response = requests.get(file_url, timeout=10)
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"    Downloaded: {file_name}")
            else:
                print(f"    File not found: {file_url}. Stopping.")
                break
        except requests.RequestException as e:
            print(f"    Error downloading {file_url}: {e}")
            break

        part_number += 1

# Example usage:
download_files("https://olmo-data.org/preprocessed/c4/v1_7-dd_ngram_dp_030-qc_cc_en_bin_001-fix/gpt-neox-olmo-dolma-v1_5/part-{i:03d}-00000.npy", "largefiles")