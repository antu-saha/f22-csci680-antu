import pandas as pd


def get_common_elements(a, b):
    a_set = set(a)
    b_set = set(b)
    c_set = a_set & b_set
    return c_set


def show_co_changed_files(df, no_of_file):
    for i in range(len(df["List of changed files"])):
        counter = 0
        first_changed_file_list = df["List of changed files"][i]
        if len(first_changed_file_list) == no_of_file:
            for j in range(len(df["List of changed files"])):
                if i == j:
                    continue
                second_changed_file_list = df["List of changed files"][j]
                common_files = get_common_elements(first_changed_file_list, second_changed_file_list)
                if len(common_files) == no_of_file:
                    print(
                        f'Commit ID: {df["Commit-ID"][i]}, Commit ID: {df["Commit-ID"][j]}, Common Files: {common_files}')
                    counter = counter + 1
                if counter > 3:
                    break
            print("New Commit...")


if __name__ == "__main__":
    input_file_path = 'modified_commits_11-1-2019.csv'

    df = pd.read_csv(input_file_path,
                     converters={"List of changed files": lambda x: x.strip("[]").replace("'", "").split(", ")})

    # Find commits with 4 co_changed files
    # show_co_changed_files(df, 4)

    # Find commits with 3 co_changed files
    # show_co_changed_files(df, 3)

    # Find commits with 2 co_changed files
    show_co_changed_files(df, 2)
