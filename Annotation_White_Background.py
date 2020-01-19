import cv2
import numpy as np
import glob
import random

#パス
path_kamo = r'C:\iida\unrelated\img\kamo\*.jpg'
path_back = r'C:\iida\unrelated\img\background\*.jpg'
path_w = r'C:\iida\unrelated\img\test'

def main():
    #ディレクトリ内の背景と画像のパスを取得
    files_back = glob.glob(path_back)
    files_kamo = glob.glob(path_kamo)
    #背景の画像数を取得
    back_length = len(files_back)
    i = 1
    #対象物の画像に背景をつける
    for f in files_kamo:
        i1 = "{0:02d}".format(i)
        #対象物画像読み込み
        im_kamo = cv2.imread(f)
        #対象物の高さ，幅取得
        height = im_kamo.shape[0]
        width = im_kamo.shape[1]

        #乱数を用いて背景を表示したい．
        back_factor = random.randint(1,back_length-1)
        back_image = files_back[back_factor]
        #乱数により設定した背景画像を取得
        im_back = cv2.imread(back_image)

        for y in range(height):
            for x in range(width):
                #img[Y座標, X座標]
                pi = im_kamo[y,x]
                #対象物によって「255」の数値を変更する．
                if np.average(pi) >= 200:
                    #RGBではなくBGRに注意
                    b,g,r = im_back[y,x]
                    im_kamo[y,x] = [b,g,r]

        output_path = path_w + "\\" + str(i1) + ".jpg"
        #生成した画像を書き出す．
        cv2.imwrite(output_path,im_kamo)

        i += 1




if __name__ == "__main__":
    main()