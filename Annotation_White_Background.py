import cv2
import numpy as np
import glob
import random

path_kamo = r'C:\iida\unrelated\img\kamo\*.jpg'
path_back = r'C:\iida\unrelated\img\background\*.jpg'
path_w = r'C:\iida\unrelated\img\test'

def main():

    files_back = glob.glob(path_back)
    files_kamo = glob.glob(path_kamo)
    back_length = len(files_back)
    i = 1
    for f in files_kamo:
        i1 = "{0:02d}".format(i)
        im_kamo = cv2.imread(f)
        height = im_kamo.shape[0]
        width = im_kamo.shape[1]

        back_factor = random.randint(1,back_length-1)
        back_image = files_back[back_factor]
        im_back = cv2.imread(back_image)

        for y in range(height):
            for x in range(width):
                #img[Y座標, X座標]
                pi = im_kamo[y,x]
                if np.average(pi) == 255:
                    #RGBではなくBGRに注意
                    b,g,r = im_back[y,x]
                    im_kamo[y,x] = [b,g,r]

        output_path = path_w + "\\" + str(i1) + ".jpg"
        cv2.imwrite(output_path,im_kamo)

        i += 1


    # im_kamo = cv2.imread(path_kamo)
    # im_back = cv2.imread(path_back)

    # height = im_kamo.shape[0]
    # width = im_kamo.shape[1]

    # for y in range(height):
    #     for x in range(width):
    #         #img[Y座標, X座標]
    #         pi = im_kamo[y,x]
    #         if np.average(pi) == 255:
    #             #RGBではなくBGRに注意
    #             b,g,r = im_back[y,x]
    #             im_kamo[y,x] = [b,g,r]

    #cv2.imwrite(path_w,im_kamo)
                

if __name__ == "__main__":
    main()