# 1. Yêu cầu người dùng nhập vào một dãy số nguyên và chuyển đổi thành danh sách các số nguyên
def convert_to_list():
    input_str = input("Nhập dãy số nguyên (cách nhau bằng dấu phẩy): ")
    return list(map(int, input_str.split(',')))

# 2. Tính tổng và trung bình cộng của các số trong danh sách
def sum_and_average(lst):
    total = sum(lst)
    average = total / len(lst) if len(lst) > 0 else 0
    return total, average

# 3. Lọc ra danh sách các số chẵn và lẻ
def filter_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

# 4. Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
def sort_list(lst):
    return sorted(lst), sorted(lst, reverse=True)

# 5. Đảo ngược thứ tự của danh sách
def reverse_list(lst):
    return lst[::-1]

# 6. Kiểm tra xem một số bất kỳ có tồn tại trong danh sách không
def check_exists(lst, num):
    return num in lst

# 7. Tìm vị trí đầu tiên của một phần tử trong danh sách
def find_first_position(lst, num):
    try:
        return lst.index(num)
    except ValueError:
        return -1

# 8. Tìm phần tử lớn nhất và nhỏ nhất trong danh sách
def find_min_max(lst):
    return min(lst), max(lst)

# 9. Đếm số lần một phần tử xuất hiện trong danh sách
def count_occurrences(lst, num):
    return lst.count(num)

# 10. Tìm tất cả các vị trí xuất hiện của một phần tử trong danh sách
def find_all_positions(lst, num):
    return [i for i, x in enumerate(lst) if x == num]

# 11. Tính tổng tất cả các phần tử trong danh sách
def sum_list(lst):
    return sum(lst)

# 12. Tính tích của tất cả các phần tử trong danh sách
def product_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# 13. Tính giá trị trung bình của các số trong danh sách
def average_list(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0

# 14. Xóa toàn bộ các phần tử trong danh sách
def clear_list(lst):
    lst.clear()
    return lst

# 15. Đếm số phần tử khác nhau trong danh sách
def count_unique(lst):
    return len(set(lst))

# 16. Nhập điểm của 5 sinh viên, tính điểm trung bình và in ra sinh viên có điểm trên/dưới trung bình
def student_scores():
    scores = [float(input(f"Nhập điểm sinh viên {i+1}: ")) for i in range(5)]
    avg = sum(scores) / 5
    above_avg = [score for score in scores if score > avg]
    below_avg = [score for score in scores if score < avg]
    return avg, above_avg, below_avg

# 17. Nhập các khoản chi tiêu hàng ngày trong một tuần
def weekly_expenses():
    expenses = [float(input(f"Nhập chi tiêu ngày {i+1}: ")) for i in range(7)]
    total = sum(expenses)
    avg = total / 7
    max_expense = max(expenses)
    min_expense = min(expenses)
    return total, avg, max_expense, min_expense

# 18. Quản lý các sản phẩm trong kho
def manage_inventory():
    inventory = []
    while True:
        choice = input("1. Thêm sản phẩm\n2. Xóa sản phẩm\n3. Tìm sản phẩm\n4. Hiển thị tất cả\n0. Thoát\nChọn: ")
        if choice == '1':
            product = input("Nhập tên sản phẩm: ")
            inventory.append(product)
        elif choice == '2':
            product = input("Nhập tên sản phẩm muốn xóa: ")
            if product in inventory:
                inventory.remove(product)
            else:
                print("Không tìm thấy sản phẩm")
        elif choice == '3':
            product = input("Nhập tên sản phẩm muốn tìm: ")
            if product in inventory:
                print(f"Sản phẩm {product} có trong kho")
            else:
                print(f"Sản phẩm {product} không có trong kho")
        elif choice == '4':
            print("Danh sách sản phẩm:", inventory)
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ")

# 19. Chuyển chuỗi các từ cách nhau bằng dấu phẩy thành danh sách chuỗi
def convert_string_to_list():
    input_str = input("Nhập chuỗi các từ (cách nhau bằng dấu phẩy): ")
    return input_str.split(',')

# 20. Tách một chuỗi thành các từ, mỗi từ là một phần tử trong danh sách
def split_string_to_words():
    input_str = input("Nhập chuỗi: ")
    return input_str.split()

if __name__ == "__main__":
    lst = convert_to_list()
    print("Danh sách số nguyên:", lst)

    # 1. Tính tổng các phần tử
    print("Tổng tất cả các phần tử:", sum_list(lst))

    # 2. Tính tích của các phần tử
    print("Tích của tất cả các phần tử:", product_list(lst))

    # 3. Tính giá trị trung bình
    print("Giá trị trung bình:", average_list(lst))

    # 4. Xóa toàn bộ các phần tử
    print("Xóa toàn bộ danh sách:", clear_list(lst))

    # 5. Đếm số phần tử khác nhau trong danh sách
    lst = convert_to_list()  # Nhập lại danh sách
    print("Số phần tử khác nhau trong danh sách:", count_unique(lst))

    # 6. Nhập điểm của 5 sinh viên và xử lý điểm trung bình
    avg, above_avg, below_avg = student_scores()
    print(f"Điểm trung bình: {avg}, Sinh viên có điểm trên trung bình: {above_avg}, Sinh viên có điểm dưới trung bình: {below_avg}")

    # 7. Nhập các khoản chi tiêu hàng ngày trong một tuần
    total, avg, max_expense, min_expense = weekly_expenses()
    print(f"Tổng chi tiêu: {total}, Chi tiêu trung bình: {avg}, Chi tiêu cao nhất: {max_expense}, Chi tiêu thấp nhất: {min_expense}")

    # 8. Quản lý các sản phẩm trong kho
    manage_inventory()

    # 9. Chuyển chuỗi các từ cách nhau bằng dấu phẩy thành danh sách chuỗi
    words_list = convert_string_to_list()
    print("Danh sách chuỗi:", words_list)

    # 10. Tách một chuỗi thành các từ
    words = split_string_to_words()
    print("Các từ tách từ chuỗi:", words)

    lst = convert_to_list()
    print("Danh sách số nguyên:", lst)

    # 11. Tính tổng tất cả các phần tử
    print("Tổng tất cả các phần tử:", sum_list(lst))

    # 12. Tính tích của tất cả các phần tử
    print("Tích của tất cả các phần tử:", product_list(lst))

    # 13. Tính giá trị trung bình
    print("Giá trị trung bình:", average_list(lst))

    # 14. Xóa toàn bộ các phần tử trong danh sách
    cleared_list = clear_list(lst)
    print("Danh sách sau khi xóa:", cleared_list)

    # Nhập lại danh sách để tiếp tục kiểm tra các hàm khác
    lst = convert_to_list()

    # 15. Đếm số phần tử khác nhau trong danh sách
    print("Số phần tử khác nhau trong danh sách:", count_unique(lst))

    # 16. Nhập điểm của 5 sinh viên, tính điểm trung bình và tìm sinh viên có điểm trên/dưới trung bình
    avg, above_avg, below_avg = student_scores()
    print(
        f"Điểm trung bình: {avg}, Sinh viên có điểm trên trung bình: {above_avg}, Sinh viên có điểm dưới trung bình: {below_avg}")

    # 17. Nhập chi tiêu hàng ngày trong một tuần
    total, avg, max_expense, min_expense = weekly_expenses()
    print(
        f"Tổng chi tiêu: {total}, Chi tiêu trung bình: {avg}, Chi tiêu cao nhất: {max_expense}, Chi tiêu thấp nhất: {min_expense}")

    # 18. Quản lý các sản phẩm trong kho
    manage_inventory()

    # 19. Chuyển chuỗi các từ cách nhau bằng dấu phẩy thành danh sách chuỗi
    words_list = convert_string_to_list()
    print("Danh sách chuỗi:", words_list)

    # 20. Tách một chuỗi thành các từ
    words = split_string_to_words()
    print("Các từ trong chuỗi:", words)
