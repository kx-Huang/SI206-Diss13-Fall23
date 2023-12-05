import csv
import matplotlib.pyplot as plt


def load_github_data():
    with open('issues.csv') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        issues = list(csv_reader)
    with open('repos.csv') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        repos = list(csv_reader)
    return repos, issues

######################### TASK 1 #########################
def plot_top_10_languages_repo_stat(repos):
    """
    Generate one plot with two subplots side by side
    Left subplot: a horizontal bar chart. The y axis is the coding languages, and the x axis is total repository number which coded in this lanaguage.
    Right subplot: a bar chart. Each portion is a coding lanaguage.

    Args:
        repos (List[List]): a list of lists. Each item contains: coding lanaguage, total repo number
        Example: [['Python', 548870], ['Java', 369282], ['C++', 278066], ...]
    """
    # TODO: implement this function
    ...

######################### TASK 2 #########################
def plot_issue_trend_by_language(issues, languages=['Python', 'C', 'C++', 'Java', 'JavaScript', 'HTML']):
    """
    Generate a multi-line chart. The x axis is the year, and the y axis is the number of issues. Each line represents a coding language.

    Args:
        issues (List[List]): a list of lists, each list item contains: coding language name, year, quarter, count
        Example: [['Python', '2012', '1', '6774'], ['Java', '2012', '1', '4429'], ['C++', '2012', '1', '3421']...]
        Here ['Python', '2012', '1', '6774'] means 6774 issues are found in Python repos in the first quarter of year 2012

        languages (List[Str]): a list of coding language names

    Tips:
        1. create a nested dictionay with following data structure would be helpful:
            {
                "Python": {
                    "2012": 78383, # this is the sum of 4 quarters
                    "2013": 176586,
                    ...
                },
                "Java": {
                    "2012": 49331,
                    "2013": 146833,
                    ...
                },
                ...
            }
        2. the total count of a year is the sum of each quarter
    """
    # TODO: implement this function
    ...


def main():
    repos, issues = load_github_data()
    repos = [[repo[0], int(repo[1])] for repo in repos]
    plot_top_10_languages_repo_stat(repos)
    plot_issue_trend_by_language(issues)


if __name__ == '__main__':
    main()
