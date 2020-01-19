import cv2
import numpy as np

path_kamo = r'C:\iida\unrelated\img\kamo\1.jpg'
path_backgroun = r'C:\iida\unrelated\img\background\01.jpg'
output_path = r'C:\iida\unrelated\img\test'

def main():
    im_kamo = cv2.imread(path_kamo)
    im_back = cv2.imread(path_backgroun)

    height = im_kamo.shape[0]
    width = im_kamo.shape[1]

    for y in range(height):
        for x in range(width):
            pi = im_kamo[y,x]
            if np.average(pi) >= 200:
                b,g,r = im_back[y,x]
                im_kamo[y,x] = [b,g,r]

    outpath = output_path + "\\" + "255.jpg"

    cv2.imwrite(outpath,im_kamo)

if __name__ == "__main__":
    main()