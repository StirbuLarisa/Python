import os
import sys

def count_files_by_extension(directory):
    try:

        if not os.path.exists(directory):
            raise FileNotFoundError(f"directorul '{directory}' nu exista.")


        if not os.listdir(directory):
            print(f"directorul '{directory}' este gol.")
            return

        extension_count = {}


        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            try:

                if os.path.isfile(file_path):
                    _, file_extension = os.path.splitext(filename)

                    extension_count[file_extension] = extension_count.get(file_extension, 0) + 1

            except Exception as e:
                print(f"eroare {file_path}: {str(e)}")


        print("nr de fisiere per extensie:")
        for extension, count in extension_count.items():
            print(f"{extension}: {count} fisiere")

    except Exception as e:
        print(f"eroare: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("<directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
