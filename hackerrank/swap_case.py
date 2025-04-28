'''
Exercice: convert all lowercase letters to uppercase letters and vice versa.

Method: convert the string in a list do the swaping thing and then reconvert 
the list in a string with the join method
'''



def swap_case(s):

    s_1 = list(s)
    
    for x in range(len(s)):
        if s_1[x] == s_1[x].upper():
            s_1[x] = s_1[x].lower()
        elif s_1[x] == s_1[x].lower():
            s_1[x] = s_1[x].upper()

    final = ''.join(s_1)

    return final


m_string_1 = "Www.HackerRank.com"
m_string_2 = "Pythonist 2"

res_1 = swap_case(m_string_1)  
res_2 = swap_case(m_string_2)  

print(res_1)
print(res_2)

m_string = input("Give a string: ")
result = swap_case(m_string)
print(result)

