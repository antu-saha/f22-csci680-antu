import os
import csv


def download_git_log():
    os.system("cd pdfbox && git log --stat-width=300 --pretty=format:%h,%an,%ae,%s,%ai,%as > ../commit.csv")


def preprocess_git_log(input_file_path, output_file_path):
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Commit-ID', 'Author Name', 'Author Email', '# of changed files', 'List of changed files', 'Date'])

    with open(input_file_path, 'r', encoding='latin-1') as f:
        lines = f.readlines()
        reader = csv.reader(lines, delimiter=',')
        changed_file_name_list = []
        counter = 0
        for row in reader:
            if len(row) == 6:
                commit_id, name, email, date = row[0], row[1], row[2], row[4].split(" ")[0]
            elif len(row) == 1:
                changed_file_name = row[0].split(" ")[1]
                changed_file_name_list.append(changed_file_name)
            elif len(row) == 0 or counter == len(lines)-1:
                with open(output_file_path, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow([commit_id, name, email, len(changed_file_name_list), changed_file_name_list, date])
                # print(commit_id, name, changed_file_name_list)
                changed_file_name_list = []
            counter = counter + 1


if __name__ == "__main__":
    # download_git_log()
    input_file_path = 'commit.csv'
    output_file_path = './modified_commits.csv'
    preprocess_git_log(input_file_path, output_file_path)


