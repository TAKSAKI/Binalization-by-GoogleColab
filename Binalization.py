import cv2

orig = cv2.imread(uploaded_file_name) ##先ほどアップロードした画像を読み込む
src = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB) ##origはBGR空間であり画像処理を施すことができないのでRGB空間に変換する
th, img_th = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY) ##今回はしきい値を128としcv2.THRESH_BINARYよりこの値より小さいものは黒、この値より大きいものは白とする
##thが閾値,img_thが二値化した結果,cv2.threshhold(元々の画像,閾値,maxval,type)
