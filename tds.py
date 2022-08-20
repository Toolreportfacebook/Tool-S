import requests
token_tds = input(' Nhập Access_Token TDS: ')
token_fb = input(' Nhập Token Facebook: ')
# ĐĂNG NHẬP TK TDS
logintds = requests.get(url=f'https://traodoisub.com/api/?fields=profile&access_token={token_tds}')
if 'data' in logintds.text:
 ten_tk = logintds.json()['data']['user']
 xu_tk = logintds.json()['data']['xu']
 print(' Đăng Nhập Thành Công')
else:
 prinr(' Đăng Nhập Thất Bại')
# LẤY IN4 FACEBOOK
infofb = requests.get(url=f'https://graph.facebook.com/me/?access_token={token_fb}')
if 'id' in infofb.text:
 id_fb = infofb.json()['id']
 ten_fb = infofb.json()['name']
# Cấu Hình TDS
cau_hinh = requests.get(url=f'https://traodoisub.com/api/?fields=run&id={id_fb}&access_token={token_tds}')
if 'data' in  cau_hinh.text:
 print(f' Chạy Facebook {ten_fb} | ID Facebook {id_fb}')
 print(f' Tài Khoảng TDS: {ten_tk}')
 print(f' Xu Hiện Tại: {xu_tk}')
 
