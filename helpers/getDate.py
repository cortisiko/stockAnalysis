
def getDates(dataframe):

    asOfDate = dataframe['asOfDate'].astype(str)
    checkForDuplicates(asOfDate)
    #print(dataframe.columns)
    return asOfDate


def checkForDuplicates(asOfDate):
    renameDuplicateDateToTrailingTwelveMonths = asOfDate.loc[asOfDate.duplicated()] = 'TTM'

    return renameDuplicateDateToTrailingTwelveMonths


def renamingDuplicates(dates):
    dups = {}

    for i, val in enumerate(dates):
        if val not in dups:
            # Store index of first occurrence and occurrence value
            dups[val] = [i, 1]
        else:
            # Special case for first occurrence
            if dups[val][1] == 1:
                dates[dups[val][0]] += str("TTM")