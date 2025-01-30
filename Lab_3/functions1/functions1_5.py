from itertools import permutations

def next_permutation(user_input):
    for perm in permutations(user_input):
        print(''.join(perm)) #метод join берёт каждый элемент в последовательности perm и соединяет их в одну строку

user_input = input("Enter a string: ")

print("All permutations:")
next_permutation(user_input)