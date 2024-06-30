"""
Helper functions to clean up dates in data
"""
def get_dates(data_frame):
    """
      function that gets dates
      """
    as_of_date = data_frame['asOfDate'].astype(str)
    check_for_duplicates(as_of_date)
    # print(dataframe.columns)
    return as_of_date


def check_for_duplicates(as_of_date):
    """
    function that checks for duplicate of training twelve months
    :param as_of_date
    """
    # pylint: disable=line-too-long
    rename_duplicate_date_to_trailing_twelve_months = as_of_date.loc[as_of_date.duplicated()] = 'TTM'

    return rename_duplicate_date_to_trailing_twelve_months


def renaming_duplicates(dates):
    """
      function that renames duplicate of training twelve months
      :param dates:
      :return:
      """
    dups = {}

    for i, val in enumerate(dates):
        if val not in dups:
            # Store index of first occurrence and occurrence value
            dups[val] = [i, 1]
        else:
            # Special case for first occurrence
            if dups[val][1] == 1:
                dates[dups[val][0]] += str("TTM")
