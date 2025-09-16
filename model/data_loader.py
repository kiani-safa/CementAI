# create a load_data function for importing
def load_data():
    df=pd.read_csv("../data/synthetic_cement_thickening_dataset_10000.csv")
    return df