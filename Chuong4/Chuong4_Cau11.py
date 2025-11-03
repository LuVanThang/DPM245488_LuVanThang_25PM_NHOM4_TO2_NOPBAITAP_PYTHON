def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s
'''
def main():
    global val
    val = 5
    print(sum1(5))
    print(sum2())
    print(sum3())
main()
'''
# Kết quả trả về của lệnh trên là 5,5,0
# Giải thích:
# Hàm sum1 nhận tham số n với giá trị 5, vòng lặp while chạy 5 lần, trả về 5
# Hàm sum2 sử dụng biến toàn cục val với giá trị 5, vòng lặp while chạy 5 lần, trả về 5 và biến val được gán lại giá trị 0
# Hàm sum3 sử dụng biến toàn cục val với giá trị 0 (do hàm sum2 đã gán lại), vòng lặp for không chạy lần nào, trả về 0

'''
def main():
    global val
    val = 5
    print(sum1(5))
    print(sum3())
    print(sum2())
main()
'''
# Kết quả trả về của lệnh trên là 5,5,5
# Giải thích:
# Hàm sum1 nhận tham số n với giá trị 5, vòng lặp while chạy 5 lần, trả về 5
# Hàm sum3 sử dụng biến toàn cục val với giá trị 5, vòng lặp for chạy 5 lần, trả về 5
# Hàm sum2 sử dụng biến toàn cục val với giá trị 5 (do hàm sum3 không thay đổi giá trị val), vòng lặp while chạy 5 lần, trả về 5

'''
def main():
    global val
    val = 5
    print(sum2())
    print(sum1(5))
    print(sum3())
main()
'''
# Kết quả trả về của lệnh trên là 5,5,0
# Giải thích:
# Hàm sum2 sử dụng biến toàn cục val với giá trị 5, vòng lặp while chạy 5 lần, trả về 5 và biến val được gán lại giá trị 0
# Hàm sum1 nhận tham số n với giá trị 5, vòng lặp while chạy 5 lần, trả về 5
# Hàm sum3 sử dụng biến toàn cục val với giá trị 0 (do hàm sum2 đã gán lại), vòng lặp for không chạy lần nào, trả về 0