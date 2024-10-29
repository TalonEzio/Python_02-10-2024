from datetime import datetime

def nhap_danh_sach_xe():
    danh_sach_xe=[]

    while True:
        xe = nhap_xe()
        if xe is None:
            print('đã dừng nhập xe')
            break
        danh_sach_xe.append(xe)

    return danh_sach_xe

def nhap_xe():
    print('********** Thông tin xe mới: **********')
    hang_xe = input("==> Nhập hãng xe (hoặc 'kt' để kết thúc): ")
    if hang_xe.lower() == 'kt':
        return None

    while True:
        try:
            don_gia = float(input("==> Nhập đơn giá (số dương): "))
            if don_gia <= 0:
                raise ValueError("==> Đơn giá phải là số dương.")
            break
        except ValueError as e:
            print(f"==> Lỗi dữ liệu đầu vào đơn giá: {e}. Vui lòng nhập lại.")


    max_year= datetime.now().year
    min_year = max_year - 100
    while True:
        try:
            nam_san_xuat = int(input(f"==> Nhập năm sản xuất ({min_year} tới {max_year}): "))
            if nam_san_xuat < min_year or nam_san_xuat > max_year:
                raise ValueError(f"==> Năm sản xuất phải từ {min_year} tới {max_year}.")
            break
        except ValueError as e:
            print(f"==> Lỗi dữ liệu đầu vào năm sản xuất: {e}. Vui lòng nhập lại.")

    return {
        'hang_xe': hang_xe,
        'don_gia': don_gia,
        'nam_san_xuat': nam_san_xuat,
    }

def xe_gia_cao_nhat(danh_sach_xe,count = 2):
    result = danh_sach_xe.copy()

    result.sort(key=lambda xe: xe['don_gia'],reverse=True)

    return result[:count]

def them_so_nam_bao_hanh(danh_sach_xe):
    for xe in danh_sach_xe:
        while True:
            try:
                so_nam_bh = int(input(f'==> Nhập số năm bảo hành cho xe {xe['hang_xe']}: '))
                if so_nam_bh <= 0:
                    raise ValueError("==> Số năm bảo hành phải là năm dương.")
                break
            except ValueError as e:
                print(f"==> Lỗi dữ liệu đầu vào năm bảo hành: {e}. Vui lòng nhập lại.")
        xe['so_nam_bao_hanh'] = so_nam_bh

def tim_va_cap_nhat(danh_sach_xe,don_gia_min = 850,so_nam_bao_hanh = 3,giam_gia = 0.1):

    condition = lambda xe: xe['don_gia'] < don_gia_min and xe['so_nam_bao_hanh'] == so_nam_bao_hanh

    exist = False
    print(f'xe co don gia < {don_gia_min} va so nam bao hanh = {so_nam_bao_hanh}: ')
    for xe in danh_sach_xe:
        if condition(xe):
            exist = True
            xe['don_gia'] = xe['don_gia'] * (1 - giam_gia)
            print(xe)
    if not exist:
        print('Khong co xe nao thoa man dieu kien de giam gia')

if __name__ == '__main__':
    danh_sach_xe= nhap_danh_sach_xe()

    count = 3
    result_b = xe_gia_cao_nhat(danh_sach_xe,count)

    print(f'{count} xe co gia cao nhat: ')
    for item in result_b:
        print(item)

    them_so_nam_bao_hanh(danh_sach_xe)
    tim_va_cap_nhat(danh_sach_xe,don_gia_min = 850,so_nam_bao_hanh = 3,giam_gia = 0.1)

