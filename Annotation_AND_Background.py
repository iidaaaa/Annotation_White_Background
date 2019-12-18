import cv2
import numpy as np
import random
import sys
import glob,os


path_kamo = r'C:\iida\unrelated\img\kamo\*.jpg'
path_back = r'C:\iida\unrelated\img\background\*.jpg'
path_w = r'C:\iida\unrelated\img\test'

#どのくらい離すか
mergine=0.00
group="1"



#pathには画像が入っている
def make_label(path,back,i):
    img = cv2.imread(path)
    #im_back = cv2.imread(path)
    im_back = cv2.imread(back)
	#print("len:{}".format(len(img[0])))

	#画像の座標の0,0は左上
    left=800
    right=0
    upper=600
    lower=0
    #高さループ　y軸　len(img)は縦、len(img[0])は横、[]は一次元外すという意味。二次元配列ではなく縦の中に横が入っているイメージ。
    for y in range(len(img)):
        #横ループ　x軸
        for x in range(len(img[y])):

            # 画素値が255以外 白は255らしい
            #pxにy,x座標の画素値を代入
            px=img[y,x]
            #print("px:{} sum(px):{}".format(px,sum(px)))
            if np.average(px) != 255:

                #左の一番小さい座標を取得
                if left>x:
                    left=x
                #右の一番大きい値を取得
                if right<x:
                    right=x
                #上の一番小さい座標を取得　画像の座標0,0は左上
                if upper>y:
                    upper=y
                #下の一番大きい座標を取得
                if lower<y:
                    lower=y
                
            #
            else:
                #RGBではなくBGRに注意
                b,g,r = im_back[y,x]
                img[y,x] = [b,g,r]

        #
    #
    #print("left:{} right:{} upper:{} lower:{}".format(left,right,upper, lower))

    #少し囲む範囲を大きくした
    left=int(max(left-len(img[0])*mergine,0))
    upper=int(max(upper-len(img)*mergine,0))
    right=int(min(right+len(img[0])*mergine,len(img[0])))
    lower=int(min(lower+len(img)*mergine,len(img)))

    #----------------　#カモの周りを描画してくれる　---------------------------------
    # #左上と、右下に点を打つ
    # img = cv2.circle(img,(left,upper),20,(255,0,0), -1)
    # img = cv2.circle(img,(right, lower),20,(0.255,0), -1)
    # #四角形の線を引く
    # img = cv2.line(img, (left, upper),(right,upper),(0,0,255),1)
    # img = cv2.line(img, (left, upper),(left, lower),(0,0,255),1)
    # img = cv2.line(img, (right,lower),(right, upper),(0,0,255),1)
    # img = cv2.line(img, (right, lower),(left, lower),(0,0,255),1)
    # #↓描画してくれる
    # #cv2.imwrite(path_w+"\\"+path.split("\\")[-1].replace(".jpg","")+".png",img)
    #---------------------------------------------------------------------------------------
    i2 = "{0:08d}".format(i)
    output_path = path_w + "\\" + str(i2) + ".jpg"
    cv2.imwrite(output_path,img)
    return left,upper,right,lower
    #

#テキストファイルに書く
def file_write():
    i=0
    #C:\Iida\kawau\images\001\*.jpg　のjpgが存在するまでjpgをfilesに代入
    files=glob.glob(path_kamo)
    files_back = glob.glob(path_back)
    back_length = len(files_back)
    
    for f in files: 
        i=i+1
        i1 = "{0:08d}".format(i)
        back_factor = random.randint(1,back_length-1)
        back_image = files_back[back_factor]
        #make_label関数からleft,upper,right,lowerを取得
        left,upper,right,lower=make_label(f,back_image,i) 
        print(str(i)+":   "+str(left)+"  "+ str(upper)+"  "+ str(right)+"  "+ str(lower))
        #f = c:\Iida\kawau\images\001\001.jpg
        #f.split("\\") = c:, Iida, kawau, images, 001, 001.jpg
        #f.split("\\")[-1] = 001.jpg
        #f.split("\\")[-1].replace(".jpg","") = 001
        #split-1は配列の一番後ろにいく
        #.jpgを空行に置き換える＝削除する
        neme=f.split("\\")[-1].replace(".jpg","")
        
        text=open(path_w + "\\" + str(i1) + ".txt", "w")
        #commit
        text.write(group + "\r")
        text.write(str(left) + " " +str(upper)+" "+str(right)+" "+str(lower))
        #push
        #text.flush()



#イラナイ
def main():
	make_label("a.jpg")

#メイン
if __name__ == "__main__":
	file_write()
