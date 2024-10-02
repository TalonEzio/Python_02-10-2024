def tim_ten_xuat_hien_nhieu_nhat(ten_list):
    ten_dict = {}
    for ten in ten_list:
        if ten in ten_dict:
            ten_dict[ten] += 1
        else:
            ten_dict[ten] = 1

    ten_dict = {'Chien': 1, 'Anh': 2, 'Nam': 1, 'Vien': 1}

    ten_pho_bien_nhat = max(ten_dict, key=ten_dict.get)
    so_lan_xuat_hien = ten_dict[ten_pho_bien_nhat]

    print(f"Tên xuất hiện nhiều nhất: {ten_pho_bien_nhat}, số lần xuất hiện: {so_lan_xuat_hien}")


if __name__ == '__main__':
    # A = input("Nhập chuỗi A: ")
    A = "Le Van Chien, Nguyen Le Nam Anh, Hoang Anh, Tran Anh Nam, Nguyen Anh Vien"

    ds_sinh_vien = A.split(", ")

    ho_list = []
    ten_list = []

    for sinh_vien in ds_sinh_vien:
        parts = sinh_vien.split()
        parts = [part.strip() for part in parts]

        ho = ' '.join(parts[:-1])
        ten = parts[-1]

        ho_list.append(ho)
        ten_list.append(ten)


    print(ho_list)
    print(ten_list)

    tim_ten_xuat_hien_nhieu_nhat(ten_list)



