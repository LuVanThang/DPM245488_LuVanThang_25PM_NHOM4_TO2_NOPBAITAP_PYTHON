import re

def  NegativeNumberInStrings(str): 
    pattern = r"-\d+"
    numbers = re.findall(pattern, str)
    if not numbers:
        print(f"Không tìm thấy số nguyên âm nào trong chuỗi: \"{str}\"")
    else:
     
        print(f"Các số nguyên âm tìm thấy trong \"{str}\":")
        
        for num in numbers:
            print(num)

chuoi_dau_vao = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(chuoi_dau_vao)
chuoi_khac = "12,5,6,-2,-77,-888"
NegativeNumberInStrings(chuoi_khac)