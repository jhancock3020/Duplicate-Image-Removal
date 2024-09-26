import os
from PIL import Image
import imagehash

def delete_similar_images(folder_path, hash_size=8, threshold=5):
    # Store image hashes and file paths
    hashes = {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Ensure we are working with files, not directories
        if os.path.isfile(file_path):
            try:
                # Open the image file
                with Image.open(file_path) as img:
                    # Compute the image hash
                    img_hash = imagehash.average_hash(img, hash_size=hash_size)

                    # Compare this hash with the hashes we've seen so far
                    found_duplicate = False
                    for existing_hash, existing_file_path in hashes.items():
                        if img_hash - existing_hash <= threshold:
                            print(f"Deleting similar image: {file_path}")
                            os.remove(file_path)
                            found_duplicate = True
                            break

                    # If no similar image was found, store the hash
                    if not found_duplicate:
                        hashes[img_hash] = file_path

            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # Set the folder path where the images are stored
    folder_path = r"C:\path\to\folder"
    
    # Run the function
    delete_similar_images(folder_path)
