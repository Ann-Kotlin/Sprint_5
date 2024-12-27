# 130828463	
def decode_string(instruction: str) -> str:
    stack = []
    current_string = ''
    current_num = 0
    
    for element in instruction:
        # Если элемент это цифра
        if element.isdigit():
            # Для чисел из нескольких цифр
            current_num = current_num * 10 + int(element)
        elif element == '[':
            stack.append(current_string)
            stack.append(current_num)
            current_string = ''
            current_num = 0
        elif element == ']':
            repeat_nums = stack.pop()
            string_befor = stack.pop()
            current_string = string_befor + current_string * repeat_nums
        else: 
            # Элемент буква или символ         
            current_string += element
    
    return current_string

if __name__ == '__main__':
    encoded_string = input()
    decoded_string = decode_string(encoded_string)
    print(decoded_string)
