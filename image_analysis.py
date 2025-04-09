
import argparse
from image_function import image_analyser_function




if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Arguments for image classification")
    parser.add_argument('--url',type=str,help="give the url of the image")
    parser.add_argument('--url_2',type=str,help="give the url of the image 2")
    parser.add_argument('--question',type=str,help='What do you want to ask about the image')
    args=parser.parse_args()
    result=image_analyser_function(args.url,args.url_2,args.question)
    print(result)