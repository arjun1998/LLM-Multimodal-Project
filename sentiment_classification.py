import argparse
from classify import classify_text
import pandas as pd


if __name__ =="__main__":
    parser = argparse.ArgumentParser(description='Argument parser for my sentiment analyser')
    parser.add_argument('--path',type=str,help="give path to file containing text to classify")
    args=parser.parse_args()
    df=pd.read_csv(args.path)
    df['emotion']=df['text'].apply(classify_text)
    print(df)