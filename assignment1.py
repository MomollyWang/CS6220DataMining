import pandas as pd

data_file = 'basket_data.csv'

def cardinality_items(data_file):
    # read csv file
    df = pd.read_csv(data_file, header = None, on_bad_lines='skip')
    # sum up numbers of unique items 
    return df.nunique().sum()


def all_itemsets(data_file):
    # read csv file
    df = pd.read_csv(data_file, header = None, on_bad_lines='skip')
    #find all unique items and merge them into a set
    item_set = set()
    for col in df:
        item_set = item_set.union(df[col].unique())
    #find all subsets 
    sublst = []
    n = len(item_set)
    item_lst = list(item_set)
    for i in range(1<<n):
        sublst.append([item_lst[j] for j in range(n) if (i & (1 << j))])
    return sublst

def prob_S(target_set, data_file):
    # read csv file
    df = pd.read_csv(data_file, header = None, on_bad_lines='skip')
    # extract first 20 lines as dataset
    sub_df = df.values[:20]
    #count total set and target set
    total = 0
    freq = 0
    for row in sub_df:
        total += 1
        row_set = set()
        for item in row:
            row_set.add(item)
        print(row_set)
        if target_set == row_set:
            freq += 1
    #calculate prob
    return freq/total
