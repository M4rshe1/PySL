# check if two strings are anagrams
def check_if_is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True


input(check_if_is_anagram(input("Word 1"), input("Word 2")))