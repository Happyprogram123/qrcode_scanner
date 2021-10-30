from pyzbar import pyzbar
import cv2 as cv

cap = cv.VideoCapture(0) # inisiasi webcam

while True:
    ret, frame = cap.read()
    decode_qr = pyzbar.decode(frame,symbols=[64])
    for qrcode in decode_qr:
        (x,y,w,h) = qrcode.rect # definisi perintah membuat kotak 
        
        barcode_info = qrcode.data.decode("utf-8")
        cv.rectangle(frame, (x,y), (x + w, y + w), (0, 255, 0), 2) # Info frame kotak warna hijau dan tebal 2 pixel
        cv.putText(frame, barcode_info, (x + 6, y - 6), cv.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3) # Teks hasil deteksi otomatis mengikuti 
        
        #Ekspor hasil deteksi ke dalam bentuk teks
        with open("qrcode-result.txt", 'w') as file:
            file.write("Recognize code : " + barcode_info)
    cv.imshow("QR Scanner Result",frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() # Tampilkan webcam
cv.destroyAllWindows()

