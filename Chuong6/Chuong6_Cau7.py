n=int(input("Nhập vào giá trị n: "))
numbers = []
temp=0
print("Bắt đầu nhập dãy số TĂNG DẦN.")
while len(numbers)<n:
    try:
        x=int(input(f"Nhập vào giá trị thứ {len(numbers)+1}: "))
    except ValueError:
        print("Phải nhập vào số nguyên vui lòng nhập lại")
    if x < temp:
        print("Giá trị vừa nhập nhỏ hơn giá trị trước không đúng yêu cầu, nhập lại:")
    else:
        numbers.append(x)
        temp=x
print(numbers)   