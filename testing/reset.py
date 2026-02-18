import os
import random
import string

def generate_random_name(length=5):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def rename_files(directory):
    existing_names = set()

    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        # Skip directories
        if not os.path.isfile(old_path):
            continue

        name, ext = os.path.splitext(filename)

        # Generate a unique random name
        while True:
            new_name = generate_random_name()
            if new_name not in existing_names:
                existing_names.add(new_name)
                break

        new_filename = new_name + ext
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f"{filename} -> {new_filename}")

if __name__ == "__main__":
    target_directory = "testing/unlabeled"  # Change this
    rename_files(target_directory)
