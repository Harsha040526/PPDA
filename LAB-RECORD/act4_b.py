import os
import shutil

# Define file and folder paths
source_file = "example.txt" # Replace with your actual file
destination_folder = "backup_folder"
renamed_file = "renamed_example.txt"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Copy file to destination folder
shutil.copy(source_file, destination_folder)
print(f"File '{source_file}' copied to '{destination_folder}'.")

# Rename the copied file
source_path = os.path.join(destination_folder, source_file)
destination_path = os.path.join(destination_folder, renamed_file)
os.rename(source_path, destination_path)
print(f"File renamed to '{renamed_file}'.")

# Move the renamed file back to the original directory
final_destination = os.path.join(os.getcwd(), renamed_file)
shutil.move(destination_path, final_destination)
print(f"File moved back to '{final_destination}'.")
