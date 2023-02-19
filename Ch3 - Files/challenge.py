
import os
from os import path

def main():
    dir, this_file = path.split(path.realpath("challenge.py"))

    # get file names & stats
    file_names = []
    total_bytes = 0
    for item in os.listdir(dir):
        if path.isfile(item):
            total_bytes += path.getsize(item)
            file_names.append(str(item + "\n"))
    file_names.sort()

    # create results folder
    if not os.listdir(dir).__contains__("results"):
        os.mkdir("results")
    results_path = path.join(dir, "results", "results.txt")

    # create results file & populate
    try:
        results_file = open(results_path, "w+")
        results_file.write(f"Total byte count: {total_bytes}\n")
        results_file.write("Files list:\n--------------\n")
        results_file.writelines(file_names)
        results_file.close()
    finally:
        if not results_file.closed:
            results_file.close()


# only run if primary application
if __name__ == "__main__":
    main()