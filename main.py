# imports
from os import listdir # used in order to see all files in the folder


__author__ = "Drdread" # just cuz i guess


##################### Functions #######################################################################

def sql_generator(data):
    # will be created once I know for sure how you want it separated ...
    pass


def alphabet_sorter(data):
    # this will sort the data based alphabetically

    alphabetized_list = []

    for vendor in data:
        new_list = []
        all_names = []

        for item in vendor:

            all_names.append(item[0])

        all_names.sort()

        while all_names < len(vendor):

            for name in all_names:

                for item in vendor:

                    if name == item[0]:

                        new_list.append(item)

        alphabetized_list.append(new_list)




def level_sorter(data, vendors):
    # this splits the data based on levels
    # first part to sort is the levels. I will be splitting levels up to vendors based on how many vendors
    largest_level = 1
    for item in data:
        # this changes the largest_level variable to the actual largest level req in the item list
        if item[2] > largest_level:

            largest_level = item[2]

    per_v_deci = largest_level / len(vendors)  # this will create the average amount of levels per vendor

    per_v_whole = per_v_deci - (per_v_deci % 1)  # this will make it round down to a whole number

    extra_levels = largest_level % per_v_whole  # this states how many extra levels after the final division
    #                                          #  will go to the last vendor

    vendor_indi_lists = []
    for x in range(1,len(vendors)):
        # this is used to create an empty list for every vendor
        vendor_indi_lists.append([])

    for item in data:
        # this will sort each item based on level
        # which vendors gets which levels is decided based on the max level req of the items,
        #  then divided to each vendor
        use_vendor = len(vendors) - 1

        for num in range(0,len(vendors)):

            check = item[2] - (per_v_whole * (num + 1))
            neg_max = -per_v_whole

            if 0 > check < neg_max:

                use_vendor = num

        vendor_indi_lists[use_vendor].append(item) # adds the item to the appropriate list

    alphabet_sorter(vendor_indi_lists)


def splitter(data, vendors):
    """ this will split the file into a list from the \n. Then split each one of those from the ; and pass it to the
     sorting function """
    final_list = []
    split_list = data.split("\n")

    for item in split_list:

        final_list.append([item.split(";")])

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

print("Okay, reading and separating the delimited text data file. Hopefully the field separator is ';' !")
# this is where the reading process starts
file_to_read = [] # this is used to check if there are more than one file in the folder

for file in listdir("/File1Here"):
    # this will add file names to the file_to_read list as long as the end with .csv
    if file.endswith(".csv") is True:

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