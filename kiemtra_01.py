import random


def nhap_xe():
    hang_xe = input("Nhập hãng xe (hoặc 'kt' để kết thúc): ")
    if hang_xe.lower() == 'kt':
        return None

    while True:
        try:
            don_gia = float(input("Nhập đơn giá (số dương): "))
            if don_gia <= 0:
                raise ValueError("Đơn giá phải là số dương.")
            break
        except ValueError as e:
            print(f"Lỗi đơn giá: {e}. Vui lòng nhập lại.")

    while True:
        try:
            nam_san_xuat = int(input("Nhập năm sản xuất (năm dương): "))
            if nam_san_xuat < 2000:
                raise ValueError("Năm sản xuất phải từ 2000 trở lên.")
            break
        except ValueError as e:
            print(f"Lỗi năm sản xuất: {e}. Vui lòng nhập lại.")

    return {
        'hang_xe': hang_xe,
        'don_gia': don_gia,
        'nam_san_xuat': nam_san_xuat,
        # 'so_nam_bh': so_nam_bh
    }


def tao_du_lieu_ngau_nhien(soluong):
    hang_xe_list = ['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes', 'Lamborgini']
    danh_sach_xe = []
    for _ in range(soluong):
        xe = {
            'hang_xe': random.choice(hang_xe_list),
            'don_gia': random.uniform(500, 1000),
            'nam_san_xuat': random.randint(2000, 2024),
            'so_nam_bh': random.randint(1, 5)
        }
        danh_sach_xe.append(xe)
    return danh_sach_xe


def in_xe_gia_cao_nhat(danh_sach_xe):
    xe_gia_cao_nhat = danh_sach_xe[0]

    # for i in range(1, len(danh_sach_xe)):
    #     if danh_sach_xe[i]['don_gia'] > xe_gia_cao_nhat['don_gia']:
    #         xe_gia_cao_nhat = danh_sach_xe[i]

    xe_gia_cao_nhat = max(danh_sach_xe, key=lambda x: x['don_gia'])
    print("\nXe có giá cao nhất:")
    print(xe_gia_cao_nhat)

def them_so_nam_bao_hanh(danh_sach_xe):
    for xe in danh_sach_xe:
        while True:
            try:
                so_nam_bh = int(input(f'Nhập số năm bảo hành cho xe {xe['hang_xe']}: '))
                if so_nam_bh <= 0:
                    raise ValueError("Số năm bảo hành phải là năm dương.")
                break
            except ValueError as e:
                print(f"Lỗi: {e}. Vui lòng nhập lại.")


def in_xe_bao_hanh_3_nam(danh_sach_xe):
    print("\nXe có giá dưới 850 và bảo hành 3 năm:")

    # found = False
    # for xe in danh_sach_xe:
    #     if xe['don_gia'] < 850 and xe['so_nam_bh'] == 3:
    #         print(xe)
    #         found = True
    # if not found:
    #     print("Không có xe nào thỏa mãn điều kiện.")

    condition = lambda x: x['don_gia'] < 850 and x['so_nam_bh'] == 3
    result = [xe for xe in danh_sach_xe if condition(xe)]

    if len(result) != 0:
        for xe in result:
            print(xe)
    else:
        print('không có xe nào thoả mãn yêu cầu')


def giam_gia(danh_sach_xe, ty_le):
    print("\nGiá xe sau khi giảm {:.0f}%:".format(ty_le * 100))
    for xe in danh_sach_xe:
        xe['don_gia'] *= (1 - ty_le)
        print(xe)



if __name__ == '__main__':
    danh_sach_xe = []
    lua_chon = input("Bạn muốn nhập xe thủ công (nhập '1') hay tạo dữ liệu ngẫu nhiên (nhập '2'): ")

    if lua_chon == '1':
        while True:
            xe = nhap_xe()
            if xe is None:
                break
            danh_sach_xe.append(xe)
    elif lua_chon == '2':
        so_luong = int(input("Nhập số lượng xe ngẫu nhiên cần tạo: "))
        danh_sach_xe = tao_du_lieu_ngau_nhien(so_luong)

    if danh_sach_xe:
        in_xe_gia_cao_nhat(danh_sach_xe)

        if(lua_chon == '1'):
            them_so_nam_bao_hanh(danh_sach_xe)

        in_xe_bao_hanh_3_nam(danh_sach_xe)
        giam_gia(danh_sach_xe, 0.1)

