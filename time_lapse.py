import cv2

#time_lapse
time_var = 0
time_lapse = int(input('x speed:')) #------x speed------

#video cap
capture = cv2.VideoCapture("video/video.mov")
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#width & height
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

#output video
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('video/output_video.avi', fourcc, 30.0, (int(width), int(height)))

while True:
    ret, frame = capture.read()
    time_var += 1
    print(time_var)
    if time_var > time_lapse:
        time_var = 0
        cv2.imshow("VideoFrame", frame)
        out.write(frame)

    if cv2.waitKey(1) > 0: break

capture.release()
out.release()
cv2.destroyAllWindows()