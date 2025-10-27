# A python script to grab robots.txt from a input website and print the results.

import argparse, requests # Import modules

def parseArgs(): # Parse script arguments from input
    parser = argparse.ArgumentParser(description='A script to grab robots.txt from a website and print it out.', usage='robotsTxtGrabber.py -w [DOMAIN/WEBSITE]')
    parser.add_argument('-w', required=True, help='Input website/domain thingy.')
    parser.add_argument('--http', required=False, action='store_true', help='To use http instead of HTTPS.')
    parser.add_argument('--llms', required=False, action='store_true', help='Search for llms.txt instead of robots.txt.')
    args = parser.parse_args()
    return args

def main():
    args = parseArgs() # Get the user input from arguments

    if args.http != False: # Should the script use HTTP or HTTPS
        hType = "https://"
    else:
        hType = "http://"

    if args.llms != False: # Should the script seach for robots.txt or llms.txt
        lType = "/llms.txt"
    else:
        lType = "/robots.txt"
    
    inputURL = hType + args.w + lType # Combine inputs to make the full URL
    req = requests.get(inputURL) # Send the GET request
    if req.status_code != 200: # If the status code is not 200 then tell the user something is wrong.
        print("ERROR: Request returned status code other than 200.")
        print("Status code:" + str(req.status_code))
        if req.status_code == 404:
            print("Status code was 404. This likely indicates robots.txt or llms.txt does not exist.") # Make sure the user knows that the file might not exist
    else:
        print(req.text) # Print the text of the request
main()

