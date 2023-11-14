import os

def rename_files_with_sequential_prefix(directory):
    try:

        if not os.path.exists(directory):
            raise FileNotFoundError(f"directorul '{directory}' nu exista.")

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        for index, filename in enumerate(files, start=1):
            new_filename = f"file{index}.{filename.split('.')[-1]}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"redenumit {filename} to {new_filename}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":

    directory_path = "test"

    rename_files_with_sequential_prefix(directory_path)