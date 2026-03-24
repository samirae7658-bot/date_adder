import os
from datetime import datetime

folder = "test_files"
today = datetime.today().strftime('%Y-%m-%d')

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if os.path.isfile(old_path):
        new_name = f"{today}_{filename}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

print("Files renamed successfully!")
