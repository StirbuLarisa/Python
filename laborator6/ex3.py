import os
import sys

def calculate_total_file_size(directory):
    try:

        if not os.path.exists(directory):
            raise FileNotFoundError(f"directorul '{directory}' nu exista")

        total_size = 0

        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                try:
                    total_size += os.path.getsize(file_path)

                except Exception as e:
                    print(f"eroare {file_path}: {str(e)}")

        print(f"total size '{directory}': {total_size} bytes")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(" <director>")
        sys.exit(1)

    directory_path = sys.argv[1]

    calculate_total_file_size(directory_path)
