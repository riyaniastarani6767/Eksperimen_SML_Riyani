import pandas as pd

def preprocess_data(input_path, output_path):
    # load dataset
    df = pd.read_csv(input_path)

    # hapus data duplikat
    df = df.drop_duplicates()

    # encoding target variable
    df['deposit'] = df['deposit'].map({'yes': 1, 'no': 0})

    # encoding fitur kategorikal
    df = pd.get_dummies(df, drop_first=True)

    # menyimpan dataset hasil preprocessing
    df.to_csv(output_path, index=False)

    print("Preprocessing selesai. Dataset disimpan di:", output_path)


if __name__ == "__main__":
    input_file = "dataset_raw/bank_marketing.csv"
    output_file = "bank_marketing_processed/bank_marketing_clean.csv"

    preprocess_data(input_file, output_file)