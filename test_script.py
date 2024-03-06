from script import *

conn = create_server_connection()

# In All test Cases the write_to_table function is not called and test because in all cases it attempts to write if nothing
# is provided or even after succcessful writing it does not return anythin but prints the amount of records inserted
# So no test case for it as this is mainly focused upon the input data

def test_csv_to_list_proper():
	element, count = csv_to_list("hindalco.csv")
	assert [type(x) for x in element[0]] == [type(datetime(2024,3,1)), float,float,float,float,int,str]
	
def test_csv_to_list_empty():
	element, count = csv_to_list("empty.csv")
	assert element == []

def test_csv_to_list_no_param():
	element,count = csv_to_list("")
	assert element == None

def test_csv_to_file_missing_vals():
	element,count = csv_to_list("hindalco_miss.csv")
	assert type(element) == list

def test_csv_to_file_mixed_vals():
	element, count = csv_to_list("hindalco_mixed.csv")
	assert type(element) == list

def test_csv_to_file_full_with_mixed():
	element, count = csv_to_list("hindalco_copy.csv")
	assert type(element) == list
	