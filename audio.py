
import argparse
from audio_function import audio_analyser


if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Arguments for audio transcribing")
    parser.add_argument('--url',type=str,help="give the url of the audio")
    args=parser.parse_args()
    result=audio_analyser(args.url)
    print(result.text)
