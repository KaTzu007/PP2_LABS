# def spy_game(nums):
#     sequence = []
#     for num in nums:
#         if num == 7 or num == 0:
#             sequence.append(num)

#     seq = [0, 0, 7]
#     if seq == sequence:
#         print("True")
#     else:
#         print("False")
    
# spy_game([1,2,4,0,0,7,5]) #True
# spy_game([1,0,2,4,0,5,7]) #True
# spy_game([1,7,2,0,4,5,0]) #False

def spy_game(nums):
    zeros = 0  

    for num in nums:
        if num == 0:
            zeros += 1

        elif num == 7 and zeros >= 2:
            print("True")
            return 0

        elif num == 7 and zeros == 1:
            zeros = 0
    
    print("False")

spy_game([1,2,4,0,0,7,5]) #True
spy_game([1,0,2,4,0,5,7]) #True
spy_game([1,7,2,0,4,5,0]) #False