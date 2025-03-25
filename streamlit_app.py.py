# import streamlit as st

# from camera_input_live import camera_input_live

# image = camera_input_live()

# if image:
#   st.image(image)
import streamlit as st

from streamlit_webrtc import webrtc_streamer, VideoHTMLAttributes

import av

import cv2
import time

qrcode = cv2.QRCodeDetector()             # QRCode 偵測器
qr_code_text = ''


class VideoProcessor:

  def __init__(self) -> None:
    # self.threshold1 = 100
    # self.threshold2 = 100
    self.text = 'This is test'
  def run(self):
     return self.text
  def recv(self, frame):

    img = frame.to_ndarray(format="bgr24")

    # print('shape', img.shape)

    # img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)
    data, bbox, rectified = qrcode.detectAndDecode(img)  # 辨識 QRCode
    if bbox is not None and len(data) == 15:
      self.text= data
      print(self.text)
    # if ok:
    #     for i in range(len(data)):
    #         self.text = data[i]            # QRCode 內容
    #         # box = boxSize(bbox[i])    # QRCode 座標
    #         # cv2.rectangle(overlay,(x1 + box[0], y1 + box[1]),(x1 + box[2],y1 + box[3]),(0,0,255),5)  # 繪製外框
    #         print(len(self.text),self.text)                   # 顯示文字
    # #         # if len(text) == 15:
    # #         #     st.subheader(text)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

ctx = webrtc_streamer(key="example", video_processor_factory=VideoProcessor)#,video_html_attrs=VideoHTMLAttributes(autoPlay=True, controls=True, style={"width": "100%"}, muted=True)
def continuously_update(placeholder):
    while 1:
        # 模擬計算或資料變化
        # result = f"Current count: {counter}"
        # 更新佔位符的內容
        if ctx.video_processor:
          if len(ctx.video_processor.text) == 15:
            # placeholder.subheader(ctx.video_processor.text)
            break
        time.sleep(0.5)  # 控制更新頻率
# result = ctx.VideoProcessor.run()
# st.subheader(result)
if ctx.video_processor:
  placeholder = st.empty()
  continuously_update(placeholder)
  # st.subheader(ctx.video_processor)
  st.subheader(ctx.video_processor.text)
  # ctx.video_processor.threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)

  # ctx.video_processor.threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)