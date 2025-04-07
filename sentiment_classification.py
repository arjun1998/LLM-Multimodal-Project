from dotenv import load_dotenv
import os
from openai import OpenAI
import argparse
from classify import classify_text


if __name__ =="__main__":
    parser = argparse.ArgumentParser(description='Argument parser for my sentiment analyser')
    parser.add_argument('--text',type=str,help="A text to classify")
    args=parser.parse_args()
    classify_text(args.text)