import sys
import binary_search
input_numbers = []

for i in range(1,len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))
print(f'user given element are',input_numbers)
search_element = float(input('enter the element to be searched: '))
search_index = binary_search.binary_search(search_element,input_numbers)
if search_index == -1:
    print(f'the search element {search_element} was not found')
else:
    print(f'the search element { search_element} was found in postion {search_index}')