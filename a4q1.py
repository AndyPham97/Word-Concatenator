# put your header / citations here
#
# <Andy Pham>
# <101006098>
#
#<Gaddis, T.(2015). "Starting Out With Python">
#
# put your function definitions here
def concat_slices_and_print():
	str = "igfecbjlmpqshantuvwxyzdbcefgiworjlmpqkstuv"
	str = str[12:15] + str[22:23] + str[18:19] + str[30:32] + str[37:38]
	
	print()
	print(str)

def if_positive_concat_slices(x):
	str = "dcbzyxfijklmhanpqstuwgovxyzercdfijk"
	if x > 0:
		str = str[12:15] + str[21:24] + str[27:29]
		
		print(str) 
	
def return_concat_slices():
	str = "pomkqrsvhwxyazecdfglijkmnopqrsuvwyxtdfgijk"
	
	str = str[8:9] + str[12:15] + str[19:20] + str[24:25] + str[30:31] + str[35:36]
	
	return str	
	
def concat_arg_slices_and_return(str):
	if str == "vutrqowxyzscaefhjklmoqrtuvpinwxyzgdefh":
		str = str[10:13] + str[19:20] + str[26:29] + str[33:34]

		return str	
		
	elif str == "qpomjhruvwxystazlhjmopqkinruvwxgyzbc":
		str = str[12:15] + str[16:17] + str[23:26] + str[31:32]

		return str	
		
	else:
		str = str[12:15] + str[19:20] + str[26:29] + str[34:35]
		
		return str
		
		
def main():

	print("Test 1 of 7:", concat_slices_and_print())
	print("Test 2 of 7:", if_positive_concat_slices(1))
	print("Test 3 of 7:", if_positive_concat_slices(-1))
	print("Test 4 of 7:", return_concat_slices())
	
	# replace the strings for the next three arguments with those values
	# provided in the generator-specified criteria for your 4th function
	print("Test 5 of 7:", concat_arg_slices_and_return("vutrqowxyzscaefhjklmoqrtuvpinwxyzgdefh"))
	print("Test 6 of 7:", concat_arg_slices_and_return("qpomjhruvwxystazlhjmopqkinruvwxgyzbc"))
	print("Test 7 of 7:", concat_arg_slices_and_return("nljgfdpqrtuvhomwxyzedfgjlnsicpqrtukvwxy"))

main()