def DICH(text):
    if (text == "miêu tả người" or text=="miêu tả guơng mặt" or text=="miêu tả mặt"):
        return "facedes"
    elif (text=="nhận diện" or text=="nhân viên" or text=="nhân duyên"):
        return "facerec"
    elif (text.find("thông tin của")>=0 or text.find("thông tin về")>=0):
        return "prof"+ text[13:]
    elif (text=="miêu tả"):
        return "sdes"
    elif (text=="nhận diện vật" or text=="nhận diện vật thể"):
        return "odes"
    elif (text.find("phát bài hát")>=0 or text.find("các bài hát")>=0 or text.find("hát bài hát")>=0):
        return "music "+text[12:]
    elif (text.find("định nghĩa về")>=0):
        return "wiki"+ text[13:]
    elif (text.find("thời tiết")>=0):
        return "weather"+ text[9:]
    elif (text=="quét mã" or text=="quyết mã"):
        return "scan"
    elif (text=="thoát chế độ đọc báo" or text=="tắt chế độ đọc báo"):
        return "exitnews"
    elif (text.find("đọc báo")>=0):
        return "news"+text[7:]
    elif (text=="trang tiếp theo"):
        return "next"
    elif (text=="trang trước"):
        return "pre"
    elif (text.find("đọc bài số")>=0):
        return "read"+text[10:]
    elif (text.find("tóm tắt bài số")>=0):
        return "rsum"+text[14:]
    elif (text=="đọc chữ"):
        return "ocr"
    elif (text=="dừng nhạc" or text=="zing me" or text=="nhân nhện"):
        return "stop"
    elif (text=="nhận diện quần áo" or text=="quần áo"):
    	return "fash"
    return text

	
