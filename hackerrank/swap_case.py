'''
Exercice: convert all lowercase letters to uppercase letters and vice versa.

Method: convert the string in a list do the swaping thing and then reconvert 
the list in a string with the join method
'''

m_string = input("Give a string: ")


def swap_case(s):

    s_1 = list(s)
    
    for x in range(len(s)):
        if s_1[x] == s_1[x].upper():
            s_1[x] = s_1[x].lower()
        elif s_1[x] == s_1[x].lower():
            s_1[x] = s_1[x].upper()

    final = ''.join(s_1)

    return final

res_1 = swap_case("Www.HackerRank.com")  
res_2 = swap_case("Pythonist 2")  

print(res_1)
print(res_2)

result = swap_case(m_string)
print(result)
