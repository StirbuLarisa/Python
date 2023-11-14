import os
import sys


def read_and_print_files(directory, extension):
    try:

        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directorul '{directory}' nu exista.")

        files_found = False


        for filename in os.listdir(directory):
            if filename.endswith(extension):
                file_path = os.path.join(directory, filename)

                try:

                    with open(file_path, 'r') as file:
                        file_contents = file.read()
                        print(f"\ncontinut {filename}:\n{file_contents}")

                    files_found = True

                except Exception as e:
                    print(f"eroare la citirea din fisier {filename}: {str(e)}")
                    return

        if not files_found:
            print(f"nu sunt fisiere cu extensia '{extension}' in director.")
            return


    except Exception as e:
        print(f"eroare: {str(e)}")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(" <director> <extensie>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)
