# i want to create a webscraper that scrapes data into a csv file for further examination
# this webscraper assumes that the websites provided by the user permits webscraping
import requests
import validators
import bs4
import csv

def main():
    # intro
    print("Hi, welcome to scraper 1.0, this web_scraper will take a URL of your choosing, please ensure to provide a valid URL including 'https://' and a CSV will be provided with the HTML you requested!\n")
    print("(we're leaving acquiring the permission to web_scrape upto you for now!)\n")

    # check get input and check validity
    while True:
        url = input("Please provide the URL of the site you wish to scrape!: ")
        if validators.url(url) == True:
            break


    # generate the request of the full HTML from the URL
    request = requests.get(url)
    request.encoding = 'utf-8'

    # use beautiful soup to create the soup using the html.parser
    soup = bs4.BeautifulSoup(request.text, "html.parser")

    print("\n")

    # find number of tags that user wants to use to scrape by
    while True:
        try:
            numb_tag = int(input("How many tags would you like to scrape by? "))
            if numb_tag > 0:
                break
        except ValueError:
            print("Please provide a number greater than 0")

    # append inputs to the tag list
    tag_list = []

    print("\n")

    for tag in range(numb_tag):
        temp_input = input("Please provide a tag to scrape by: ")
        tag_list.append(temp_input)

    # ask for user input of any classes they want to search by
    class_list = []

    print("\n")

    print("Please provide any classes you wish to search using, if none or less than the number of tags required, please input 'none' to end input (note: please insert classes in a corresponding order to the tags you provided)\n")
    for tag in range(numb_tag):
        temp_class = input(f"Class {tag + 1}: ")
        if temp_class == "none":
            break
        class_list.append(temp_class)


    
    print("\n")

    # create a new list where we will append the findalls   
    parsed_soups = []
    # if no classes are provided by the user
    if len(class_list) < 1:

        temp = soup.find_all(tag_list[tag])
        parsed_soups.append(temp)


    # else if any classes are provided by the user
    else:

        # populate the class_list with 'none'
        if len(class_list) != numb_tag:
            for i in range(numb_tag - len(class_list)):
                space = "none"
                class_list.append(space)


        # either find_all with a class or without based on none presence
        for tag in range(numb_tag):
            if class_list[tag] != "none":
                temp_fa = soup.find_all(tag_list[tag], class_= class_list[tag])
                parsed_soups.append(temp_fa)
            elif class_list[tag] == "none":
                temp_fa = sound.find_all(tag_list[tag])
                parsed_soups.append(temp_fa)

    print(parsed_soups)
    print("\n")

    # write to csv
    with open("output.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        for parse in range(len(parsed_soups)):
            for soup in parsed_soups[parse]:
                writer.writerow(soup)

if __name__ == "__main__":
    main()
