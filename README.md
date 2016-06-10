"# ParseSortCreate" 

Step 1 - 
Either download the project or just download the main.py put in a folder and
create a folder in that folder called File1Here

Step 2 - 
start a query  to the item_template table on the world server that will return the results with
all of the items you want to be in the vendors. Make sure the query only includes the cols
name,entry,Requiredlevel in that order.

Step 3 - 
save the rows that are returned from the query as a delimitted text file with ; as the seperator
put the .csv file it creates in to the File1Here folder

Step 4 -
Run main.py as a python file

Step 5 - 
When the script asks for your vendor id's, enter them in order of lowest level items to highest

Step 6 - 
with your sql server running open the .sql file the script creates

Step 7 - 
Run the query it brings up


Notes - 
The items you have cannot have the same name as another item or it will create issues with the script
