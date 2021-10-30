from pyzbar import pyzbar
import cv2 as cv

class Video(object):
    def __init__(self):
        # Capturing video
        self.cap = cv.VideoCapture(0)
        
    # exit the program to release the camera
    def __del__(self):
        self.cap.release()
        
    def gen_frames(self):
        while True:
            ret, frame = self.cap.read()  # read the camera frame
            decode_qr = pyzbar.decode(frame, symbols=[64])

            for qrcode in decode_qr:
                (x, y, w) = qrcode.rect  # definisi perintah membuat kotak
                barcode_info = qrcode.data.decode("utf-8")
                # Info frame kotak warna hijau dan tebal 2 pixel
                cv.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 2)
                cv.putText(frame, barcode_info, (x + 6, y - 6), cv.FONT_HERSHEY_PLAIN,2, (0, 255, 0), 3)  # Teks hasil deteksi otomatis mengikuti

                # if not success:
                #     break
                # else:
                if ret:
                    ret, jpeg = cv.imencode('.jpg', frame)
                    return jpeg.tobytes()
                
            # # Display the resulting frame
            # cv.imshow('frame', frame)
            # keyPress = cv.waitKey(1)
            # if keyPress == ord('q'):
            #     break
            # # end if

        # # end while
        # # When everything done, release the capture
        # cap.release()
        # cv.destroyAllWindows()
    # end function
