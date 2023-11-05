import random


def complex_mutation(child_permutation):
    # Generate two random indexes
    index1 = random.randint(1, len(child_permutation) // 2 - 5)
    index2 = random.randint(len(child_permutation) // 2 + 5, len(child_permutation) - 1)

    print(f"Index1: {index1}")
    print(f"Index2: {index2}")

    # Reverse the values between the generated indexes
    child_permutation[index1:index2] = child_permutation[index1:index2][::-1]

    print(child_permutation)

if __name__ == '__main__':
    #permutation1_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #permutation2_ = [4, 5, 2, 1, 8, 7, 6, 9, 3, 10, 20, 18, 16, 14, 12, 11, 13, 15, 17, 19]

    permutation1_ = [1, 9, 3, 12, 13, 7, 4, 10, 8, 17, 6, 15, 0, 19, 2, 18, 16, 11, 5, 14]
    permutation2_ = [13, 5, 15, 14, 18, 10, 7, 8, 1, 6, 0, 16, 12, 2, 9, 3, 11, 4, 19, 17]

    # Number from 1 to 20
    permutation3_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    complex_mutation(permutation3_)


