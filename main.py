# imports
from os import listdir # used in order to see all files in the folder


__author__ = "Drdread"  # just cuz i guess


##################### Functions #######################################################################

def sql_generator(data,vendors):
    # will be created once I know for sure how you want it separated ...
    write_file = open("ItemEnter.sql","w+")  # this is the sql file that will be written in to
    write_file.write("INSERT INTO npc_vendor(entry,item,slot)")
    write_file.write("\n")

    counter_1 = 0
    write_file.write("VALUES")
    for vendor in data:

        vendor_id = vendors[counter_1]
        counter_2 = 1
        for item in vendor:
            adder = ","

            if counter_2 == len(vendor) and counter_1 == len(data) - 1:

                adder = " "

            write_file.write("(" + vendor_id + "," + item[1] + "," + str(counter_2) + ")" + adder + "\n")

            counter_2 += 1
        counter_1 += 1


    write_file.close()

    print("Your sql file has been created, enjoy. Press anything to close the script.")
    input()



def alphabet_sorter(data,vendors):
    # this will sort the data based alphabetically

    alphabetized_list = []  # will hold the final alphabetized list

    for vendor in data:  # parses through each vendor list in the data passed variable
        new_list = []  # used to hold the alphabetized names for proper sorting
        all_names = []  # this will be appended to the alphabetized list for each vendor

        for item in vendor:

            all_names.append(item[0])  # basically extracts the names from the list and appends them to
            #  all_names list for sorting

        all_names.sort()  # this call the sort function is python to sort it alphabetically

        # this loop is used to place the items in the correct order in the list
        # it looks to see if an item has the same name as the name in the all_names list then appends it to new_list
        for name in all_names:

            for item in vendor:

                if name == item[0]:

                    new_list.append(item)

        alphabetized_list.append(new_list)  # appends the final vendor list to the alphabetized_list

    sql_generator(alphabetized_list,vendors)  # sends the list to the sql generator


def level_sorter(data, vendors):
    # this splits the data based on levels
    # first part to sort is the levels. I will be splitting levels up to vendors based on how many vendors
    largest_level = 1
    for item in data:
        # this changes the largest_level variable to the actual largest level req in the item list
        if int(item[2]) > largest_level:

            largest_level = int(item[2])


    per_v_deci = largest_level / len(vendors)  # this will create the average amount of levels per vendor

    per_v_whole = per_v_deci - (per_v_deci % 1)  # this will make it round down to a whole number

    extra_levels = largest_level % per_v_whole  # this states how many extra levels after the final division
    #                                          #  will go to the last vendor

    vendor_indi_lists = []
    for x in range(0,len(vendors)):
        # this is used to create an empty list for every vendor
        vendor_indi_lists.append([])

    for item in data:
        # this will sort each item based on level
        # which vendors gets which levels is decided based on the max level req of the items,
        #  then divided to each vendor
        use_vendor = len(vendors) - 1

        for num in range(0,len(vendors)):

            check = int(item[2]) - (per_v_whole * (num + 1))
            neg_max = -per_v_whole

            if 0 > check > neg_max:

                use_vendor = num - 1

        vendor_indi_lists[use_vendor].append(item) # adds the item to the appropriate list

    alphabet_sorter(vendor_indi_lists,vendors)


def splitter(data, vendors):
    """ this will split the file into a list from the \n. Then split each one of those from the ; and pass it to the
     sorting function """
    final_list = []
    split_list = data.split("\n")

    del split_list[len(split_list) - 1]

    for item in split_list:

        final_list.append(item.split(";"))

    level_sorter(final_list, vendors)


def read_file(file, vendors):
    # this function will read the file then pass that variable to the splitter function
    # the file should have the columns in the order of [Name, ID, level(if it is sorted by level too)]
    file_read = open(file,"r+") # opens the file for reading capability

    data = file_read.read() # reads the whole file and sets the information in it to the variable data

    file_read.close() # closes the file ... duh ...

    splitter(data, vendors)


#######################################################################################################

##################### Speaking with the terminal ######################################################
print("Please enter your vendor ID's. Enter one at a time, and enter 'Done' when you are done.")
vendor_list = [] # used to hold the vendor id's
open_file = "" # this will hold the actual file to parse and stuff
enter = input() # holds a vendor id

while enter != "Done":
    # this loop will take input as long as it does not equal 'Done', in which case it will close. If it is not "Done"
    # then it will add the vendor id to the vendor_list variable.
    vendor_list.append(enter) # appends the vendor id to the vendor_list vari

    enter = input() # takes an input for the vendor id

print("You entered " + str(len(vendor_list)) + " vendor ID's") # prints how many vendor id's the user entered

if len(vendor_list) > 0:

    print("Okay, reading and separating the delimited text data file. Hopefully the field separator is ';' !")
    # this is where the reading process starts
    file_to_read = [] # this is used to check if there are more than one file in the folder

    for file in listdir("File1Here/"):
        # this will add file names to the file_to_read list as long as the end with .csv
        if file.endswith(".csv") is True:
            file = "File1Here/" + file
            file_to_read.append(file)

    if len(file_to_read) > 1:
        # this is triggered when there is more than 1 file in the directory, and will ask which file to use
        print("You have more than 1 file in the directory!")
        print("These are your files that you have in the folder")
        counter = 1
        for x in file_to_read:

            print(str(counter) + "-" + x)
            counter += 1

        print("Please enter the corresponding number for the file that you want to actually use.")
        chooser = input()
        open_file = file_to_read[int(chooser) - 1] # sets the variable to the correct file name

    elif len(file_to_read) == 1:
        # if there is only one file in the dir then this will set the variable to that file
        open_file = file_to_read[0]

    elif len(file_to_read) == 0:
        # this checks if there is no files that end in .csv in the dir then will not change the open_file variable
        print("You forgot to put a file in to the folder! Or they do not end in .csv ...")
        print("Please restart this script after you have put a file in the folder.")
        input("Enter anything to exit...")

    if open_file != "":

        read_file(open_file, vendor_list)

else:

    print("Please rerun the script and enter the vendor ID's")