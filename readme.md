# Thiết bị kính thông minh cho người khiếm thị

## https://youtu.be/0Zp1Fkr2rBw

## Lưu ý

Đây chỉ là bản demo. Sử dụng trong mạng nội bộ.
Folder Client chạy trên Raspberry pi.

## Yêu cầu

Model Tiếng Việt dùng để tóm tắt: [link ](https://www.dropbox.com/s/7de79czdc85pe8u/vi.tar.gz?dl=0)

Thay "them_key_o_day" bằng key cho Vision API của Microsoft ở [/face/facedes.py]() và [/sdes/imagecaption.py]()

```bash
_key = "them_key_o_day"
```
Tải key cho Vision API của Google lưu "key.json" đặt ở [./]()

Gắn nút cho Raspberry pi ở chân số 17
## Khởi chạy

Khởi chạy Server

```bash
python3 main.py
```
Khởi chạy Client

```bash
python3 clientpi.py
```
## Thêm data và train cho nhận diện guơng mặt
Chạy lênh ở [./face]()

Thu thập dữ liệu

```bash
python3 data_collection.py
```
Nếu đã có dữ liệu ảnh về guơng mặt sẵn

```bash
python3 get_data.py
```
Train dữ liệu 

```bash
python3 encode_faces.py
```
 

