# --- HÀM 1: NHẬP MA TRẬN (ĐƠN GIẢN) ---
def nhap_matrix(ten_matrix):
    """
    Hàm nhập ma trận đơn giản, giả định người dùng nhập đúng.
    """
    print(f"\n--- Nhập ma trận {ten_matrix} ---")
    R = int(input("Nhập số hàng: "))
    C = int(input("Nhập số cột: "))

    # Tạo một danh sách rỗng để chứa ma trận
    matrix = []
    
    print(f"Nhập các phần tử cho {ten_matrix} ({R} hàng x {C} cột):")
    for i in range(R):
        hang_moi = [] # Tạo một hàng mới cho mỗi lần lặp
        for j in range(C):
            # Giả định người dùng nhập đúng số
            gia_tri = float(input(f"  {ten_matrix}[{i}][{j}]: "))
            hang_moi.append(gia_tri)
        matrix.append(hang_moi) # Thêm hàng vừa nhập vào ma trận
        
    return matrix

# --- HÀM 2: CỘNG MA TRẬN ---
def cong_matrix(A, B):
    """Hàm cộng 2 ma trận."""
    # Kiểm tra kích thước (cần thiết cho logic)
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("LỖI: Hai ma trận không cùng kích thước, không thể cộng.")
        return None

    R = len(A)
    C = len(A[0])

    # Tạo ma trận kết quả bằng List Comprehension (cách 1)
    C_cong = [[A[i][j] + B[i][j] for j in range(C)] for i in range(R)]
    
    # --- Hoặc bạn có thể dùng cách 2 (dùng vòng lặp, dễ hiểu hơn):
    # C_cong = []
    # for i in range(R):
    #     hang_ket_qua = []
    #     for j in range(C):
    #         hang_ket_qua.append(A[i][j] + B[i][j])
    #     C_cong.append(hang_ket_qua)
    # ---
    
    return C_cong

# --- HÀM 3: HOÁN VỊ (CHUYỂN VỊ) MA TRẬN ---
def hoan_vi_matrix(matrix):
    """Hàm tìm ma trận hoán vị (chuyển vị) - phiên bản ngắn."""
    if not matrix:
        return []
    
    # Dùng List Comprehension để hoán vị
    # Giải thích:
    # 1. Duyệt qua TỪNG CỘT (i) của ma trận cũ (range(len(matrix[0])))
    # 2. Với mỗi cột, tạo một hàng mới bằng cách lấy [row[i]]
    #    (tức là lấy phần tử ở cột đó của TẤT CẢ CÁC HÀNG (row))
    matrix_hv = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    return matrix_hv

# --- CHƯƠNG TRÌNH CHÍNH ---

# 1. Nhập
A = nhap_matrix("A")
B = nhap_matrix("B")

print("\n--- MA TRẬN ĐÃ NHẬP ---")
print(f"Ma trận A = {A}")
print(f"Ma trận B = {B}")

# 2. Cộng
print("\n--- 1. TỔNG A + B ---")
C_tong = cong_matrix(A, B)
if C_tong: # Chỉ in nếu C_tong không phải là None
    print(f"Ma trận tổng (A + B) = {C_tong}")

# 3. Hoán vị (Chuyển vị)
print("\n--- 2. MA TRẬN HOÁN VỊ ---")
A_T = hoan_vi_matrix(A)
print(f"Ma trận hoán vị của A (A_T) = {A_T}")

B_T = hoan_vi_matrix(B)
print(f"Ma trận hoán vị của B (B_T) = {B_T}")