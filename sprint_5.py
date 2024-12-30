# 130891619
import string	
def decode_string(instruction: str) -> str:
    stack = []
    current_string = ''
    current_num = 0
    
    for element in instruction:
        # Если элемент это цифра
        if element in string.octdigits: 
            current_num += str(element)
        elif element == '[':
            stack.append((current_string, current_num))
            current_string = ''
            current_num = ''
        elif element == ']':
            string_befor, repeat_nums = stack.pop()
            current_string = string_befor + current_string * int(repeat_nums)
        else: 
            # Элемент буква или символ         
            current_string += element
    
    return current_string

if __name__ == '__main__':
    encoded_string = input()
    decoded_string = decode_string(encoded_string)
    print(decoded_string)
