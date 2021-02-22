"""
Proof of concept parser to enter each webpage and check for specific words
"""
import requests
import re
import csv
import sys
from bs4 import BeautifulSoup

source_url = "https://deliveroo.co.uk/sitemap"

########## Functions for crawling, scraping, parsing ############
def restaurant_finder(location):
    """ Function to find each restaurant link on the main sitemap page """
    href_links = []
    
    # use request to retrieve html source code, then BeautifulSoup to parse
    source_code = requests.get(source_url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    
    # restaurants are stored in <a> blocks and include 'menu' string in href
    search_string = 'menu/' + location
    for a in soup.findAll('a'):
        if search_string in a['href']:
            href_links.append(a)
        # if you want to search more locations than just one, repeat the
        # following block of code with the location string you want
#        elif 'menu/london/bexleyheath' in a['href']:
#            href_links.append(a)

    # print statements here are just to show the retrieved urls look right
#    print("href_links are: ")
#    print(href_links[0:6])
#    print("") 

    return href_links

def restaurant_checker(word, href_links):
    """ Function to check if the word is in each restaurant's page """
    # create a dictionary to contain the restaurant and boolean
    restaurant_data = []
    
    # loop over the list of restaurant pages
    for link in href_links[0:10]: # change/remove indices to parse more restaurants
        # need to convert and extract info from links
        restaurant_dictionary = {'Name' : [], 'Sale' : [], 'URL' : [], 'Location' : []}
        restaurant_url = str(link['href'])
        restaurant_name = str(link.string)
        # use regex pattern to get locations out of href string 
        res_pattern = "menu/london/(.*?)/" # change the pattern if not london based
        restaurant_location = re.search(res_pattern, restaurant_url).group(1)

        # parse each restaurants individual url
        total_url = "https://deliveroo.co.uk" + restaurant_url
        # use request to retrieve html source code, then BeautifulSoup to parse
        restaurant_source_code = requests.get(total_url).text
        soup2 = BeautifulSoup(restaurant_source_code, 'html.parser')
        # we want the text from the restaurant's page
        restaurant_text = soup2.get_text()
        print("Text found for " + restaurant_name)
        
        # check if the text of the restaurant's page contains the word we want
        page_check = text_checker(word, restaurant_text) 
        # add the restaurant name and boolean to the dictionary
        restaurant_dictionary['Name'] = restaurant_name
        restaurant_dictionary['Sale'] = page_check
        restaurant_dictionary['URL'] = total_url
        restaurant_dictionary['Location'] = restaurant_location
        restaurant_data.append(restaurant_dictionary)

    return restaurant_data

def text_checker(word, text):
    """ Function to check for a specific word in the text """
    # using regex to find if the word is in the text, do not care about case
    word_list = re.findall(word, text, flags=re.IGNORECASE)
    if len(word_list) >= 1:
        result = True
    else:
        result = False
    return result

################# CSV Stuff ############################

def csv_generator(restaurant_data, csv_name):
    csv_columns = ['Name', 'Sale', 'URL', 'Location']
    csv_file = csv_name
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            res_writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            res_writer.writeheader()
            for data in restaurant_data:
                res_writer.writerow(data)
        print("\nCSV successfully written to " + csv_file)
    except IOError:
        print("I/O error occurred while writing csv")

############### Run Management #####################

def io_printer(test_word, location_choice, csv_name):
    """ Function to neatly print io statements """
    print("Searching for \"" + test_word + "\"...")
    print("Searching in \"" + location_choice + "\"...")
    print("Output will be stored in " + csv_name + "...\n")
    return



def main():
    
    # IO Stuff
    # default values for test_word and csv_name
    test_word = "T&Cs apply"
    location_choice = "london/bexleyheath"
    csv_name = "restaurant_test.csv"


    if len(sys.argv) == 1:
        print("Default option selected...")
        io_printer(test_word, location_choice, csv_name)
    elif len(sys.argv) == 2:
        try:
            location_choice = str(sys.argv[1])
            print("Custom option selected...")
            io_printer(test_word, location_choice, csv_name)
        except:
            print("Something was wrong with your input, proceeding with default...")
            print("Default option selected...")
            io_printer(test_word, location_choice, csv_name) 
    elif len(sys.argv) == 3:
        try:
            location_choice = str(sys.argv[1])
            csv_name = str(sys.argv[2]) + ".csv"
            io_printer(test_word, location_choice, csv_name)
        except:
            print("Something was wrong with your input, proceeding with default")
            print("Default option selected...")
            io_printer(test_word, location_choice, csv_name)
    else:
        print("Something is wrong with your input, proceeding with default")
        print("Default option selected...")
        io_printer(test_word, location_choice, csv_name)

    # Running the Functions
    restaurant_html = restaurant_finder(location_choice)
    restaurant_data = restaurant_checker(test_word, restaurant_html)
    csv_generator(restaurant_data, csv_name)
 
    # loop over resulting dictionary and print values to check output
#    print("\nResults of search for " + test_word.lower() + ": ")
#    for item in restaurant_data:
#        print(item)


main()
