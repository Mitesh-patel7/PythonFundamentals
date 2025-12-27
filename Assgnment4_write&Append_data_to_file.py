
userinput = input('Enter text to write to the file: ')

with open('output.txt','wt') as file:
    add_data = file.write(str(userinput))
    print('Data Successfully written to output.txt\n')

additional_input = input('Enter additional text to append to the file: ')

with open('output.txt','at') as file:
    append_data = file.write(f'\n{str(additional_input)}')
    print('Data Successfully appended to output.txt\n')

print('Final content of output.txt: ')

with open('output.txt','rt') as file:
    read = file.read()
    print(read)
