import cv2
import glob

path_r = r'C:\iida\unrelated\img\Resources\*.jpg'
path_w = r'C:\iida\unrelated\img\background'

def main():
    i = 1
    files = glob.glob(path_r)
    for f in files:
        im = cv2.imread(f)
        # print(im)
        # print(f)
        dst = cv2.resize(im, (416, 416))
        i1 = "{0:02d}".format(i)
        path_out = path_w + "\\" + str(i1) + ".jpg"
        
        cv2.imwrite(path_out, dst)

        i += 1
    

if __name__ == "__main__":
    main()