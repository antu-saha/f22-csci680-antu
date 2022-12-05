import pandas as pd

if __name__ == "__main__":
    input_file_path = './modified_commits_11-1-2019.csv'
    output_file_name = 'group_by_name.csv'
    df = pd.read_csv(input_file_path)
    print(df)
    # Count total # of commits
    print(len(df))
    # Count total # of changed files
    print(df["# of changed files"].sum())

    # Creating group of each author
    group_by_name = df.groupby("Author Name")
    print(group_by_name["Date"])
    group_by_name.to_csv(output_file_name, sep=',', encoding='utf-8')

    # Create a dataframe with the first item from each group for collecting author-email
    first_item_from_each_group = group_by_name.first()
    # first_item_from_each_group.to_csv(output_file_name, sep=',', encoding='utf-8')

    # Counting the total # of commits for each author
    group_by_name = df.groupby("Author Name").count()

    # Counting the total # of changed files for each author
    group_by_name = df.groupby("Author Name").sum()

    # Getting the average of # of changed files for each author
    group_by_name = df.groupby("Author Name").mean()

    # Getting the median on # of changed files for each author
    group_by_name = df.groupby("Author Name").median()

    # Getting the inactive since date for each author
    group_by_name = df.groupby("Author Name")["Date"].max()
    print(group_by_name)
    group_by_name.to_csv(output_file_name, sep=',', encoding='utf-8')