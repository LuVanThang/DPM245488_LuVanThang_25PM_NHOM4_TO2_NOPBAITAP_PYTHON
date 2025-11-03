import time


# --- Định nghĩa 4 hình ảnh bằng chuỗi nhiều dòng ---

hinh_1 = """
      * 
      * *
      * * *
* * * * * * *
* * * 
* *  
*
"""

hinh_2 = """
      * 
      * *
      *   *
* * * * * * *
*   * 
* *  
*
"""

hinh_3 = """
      * * * *
      * * *
      * *
      *
    * *
  * * *
* * * *
"""

hinh_4 = """
      * * * *
      *   *
      * *
      *
    * *
  *   *
* * * *
"""
cac_hinh = [hinh_1, hinh_2, hinh_3, hinh_4]
for hinh in cac_hinh:
    print(hinh)
    time.sleep(5)
print("Đã hiển thị xong 4 hình!")