# A script for poking at API endpoints ig. Work on this sometimes when im bored. It's not much rn but will be someday
import argparse, requests, sys, urllib
import re as regex
from colorama import *

# TODO add alot more features. this is just a basic project for now

def parseArgs():
    parser = argparse.ArgumentParser(description='A script to poke and prod API endpoints.', usage='endpointPoker.py -e [link] [OPTIONAL-ARGS]')
    parser.add_argument('-e', required=True, help='Link for API endpoint.')
    parser.add_argument('-us', required=False, help='Optional auth username.')
    parser.add_argument('-pa', required=False, help='Optional auth password.')
    parser.add_argument('-k', required=False, help='Optional argument for the API key for JSON stuff.')
    parser.add_argument('-dr', required=False, action='store_true', help='Display the responses from requests in addition to their detected responses.')
    # TODO implement full authentication support

    args = parser.parse_args()
    return args

def checkResponse(requestOutput, regexInput): # Check result against regex function
    text = regex.search(regexInput, requestOutput)
    if text == None:
        return False
    else:
        return True

def main():
    args = parseArgs() # Parse args
    endpoint = args.e # Endpoint

    # Test GET
    print(Fore.YELLOW + "\nAttempting test GET..." + Fore.CYAN)
    req = requests.get(endpoint)
    if args.dr == True:
        print("Response: " + req.text)
    if req.status_code==200:
        if checkResponse(req.text, r".*") == True:
            print("GET did return text of some kind. Request success!")
    elif req.status_code == 405:
            print("Response returned status code 405, indicating GET requests are not allowed.")
    else:
        print("Unexpected status code received: " + str(req.status_code))

    # Test GET with simple auth
    if args.pa and args.us:
        auth=(args.us, args.pa)
        print(Fore.YELLOW + "\nAttempting simple test GET with provided auth credentials..." + Fore.CYAN)
        req = requests.get(endpoint, auth)
        if args.dr == True:
            print("Response" + req.text)
        if req.status_code==200:
            if checkResponse(req.text, r".*") == True:
                print("GET w simple auth did return text of some kind. Request success!")
            if checkResponse(req.text, r"/.*(denied).*|.*(access).*|.*(incorrect).*/gmi") == True:
                print("GET w simple auth returned a string that might be an indicator of an incorrect password.")
        elif req.status_code == 405:
            print("Response returned status code 405, indicating GET requests are not allowed.")
        else:
            print("Unexpected status code received: " + str(req.status_code))

    # Test POST boilerplate JSON
    payload={
            "test":"test"
        }
    print(Fore.YELLOW + "\nAttepting POST with boilerplate test JSON..." + Fore.CYAN)
    req = requests.post(endpoint, data=payload)
    if args.dr == True:
        print("Response:" + req.text)
    if req.status_code==200:
        if checkResponse(req.text, r".*(JSON).*") == True:
            print("Response string contains word \"JSON\".")
        if checkResponse(req.text, r"(^\{(?:\n*|.*)*\})") == True:
            print("Response string appears to contain curly brackets, perhaps indicating JSON.")
        if checkResponse(req.text, r"/(error)/gmi"):
            print("Response string appears to contain a form of the string \"Error\". The server might be able to accept JSON, but for obvious reasons does not like the boilerplate data.")
    elif req.status_code == 405:
            print("Response returned status code 405, indicating POST requests are not allowed.")
    else:
        print("Something went wrong attempting to POST with boilerplate test JSON. Status code:" + str(req.status_code))

    # Test POST boilerplate JSON with key
    if args.k:
        payload={
            "key":args.k,
            "test":"test"
        }
        print(Fore.YELLOW + "\nAttepting POST with boilerplate test JSON & Key in index 1..." + Fore.CYAN)
        req = requests.post(endpoint, data=payload)
        if args.dr == True:
            print(req.text)
        if req.status_code==200:
            if checkResponse(req.text, r".*(JSON).*") == True:
                print("Response string contains word \"JSON\".")
            if checkResponse(req.text, r"(^\{(?:\n*|.*)*\})") == True:
                print("Response string appears to contain curly brackets, perhaps indicating JSON.")
            if checkResponse(req.text, r"/(error)/gmi"):
                print("Response string appears to contain a form of the string \"Error\". The server might be able to accept JSON, but for obvious reasons does not like the boilerplate data.")
        elif req.status_code == 405:
            print("Response returned status code 405, indicating POST requests are not allowed.")
        else:
            print("Something went wrong attempting to POST with boilerplate test JSON & Key in index 1. Status code:" + str(req.status_code))
        
    # TODO add alot more stuff

    # TODO add stupid shit to do stuff, umm
        # add URL-parsed data testing and other things
        # add alot more tests
    

main()