import cv2
import time
# image = cv2.imread("1.jpg")

# gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def get_faces(video):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    cap = cv2.VideoCapture(video)
    faces=[]
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]
    compare_method = cv2.HISTCMP_CORREL
    distinct_hist=[]


    count=0
    
    while True:
        
        ret, frame = cap.read()

        if not ret:
            break  
        
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_face = face_cascade.detectMultiScale(gray)
        if( len(detected_face) != 0):
            
            for (x1, y1, X2, Y2) in detected_face:
                if(X2>100 and Y2>100):
                    
                    count+=1
                    x2=x1+X2
                    y2=y1+Y2
                    face=frame[y1:y2,x1:x2]
                    base=cv2.cvtColor(face, cv2.COLOR_BGR2HSV)
                    hist_base = cv2.calcHist([base], channels, None, histSize, ranges, accumulate=False)
                    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
                    if(len(distinct_hist)==0):
                        distinct_hist.append([hist_base,count])
                        cv2.imwrite(f"face-{count}.jpg", face)
                        faces.append(f"face-{count}.jpg")
                    else:
                        write=0
                        for hist,c in distinct_hist:
                            comp=cv2.compareHist(hist_base, hist, compare_method)
                            
                            if(comp<=.52):
                                write+=1
                            else:
                                write=0
                        if(write%len(distinct_hist)==0 and write!=0):
                            distinct_hist.append([hist_base,count])
                            cv2.imwrite(f"face-{count}.jpg", face)
                            faces.append(f"face-{count}.jpg")
                                
                    
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )
        # cv2.imshow("Face Detection", frame)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    cap.release()
    return(faces)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# detected_faces = face_cascade.detectMultiScale(gray)
# print(detected_faces)
# for (column, row, width, height) in detected_faces:
#     cv2.rectangle(
#         image,
#         (column, row),
#         (column + width, row + height),
#         (0, 255, 0),
#         2
#     )

# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

