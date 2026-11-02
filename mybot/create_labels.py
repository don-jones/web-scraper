import os
import matplotlib.pyplot as plt
import random

def get_img_filenames():
    img_filenames = {  "-1_pv_50_foreign" : 175,
                       "-1_pv_50_usa" : 175,
                       "ar_pv_50_foreign" : 330,
                       "ar_pv_50_usa" : 330 }

    return img_filenames

def main():
    img_filenames = get_img_filenames()
    height_px, width_px = 31,746
    my_dpi = 100
    scale = 1
    for img_filename, rating_loc in img_filenames.items():
        fig = plt.figure(figsize=(width_px / my_dpi * scale, height_px / my_dpi * scale), dpi=my_dpi)
        for i in range(40,50):
            text_1 = i/10
            img = plt.imread(f"icons/{img_filename}.png")
            plt.imshow(img, aspect='auto',origin='upper')
            plt.axis('off')
            plt.text(x=rating_loc, y=20, s=text_1, fontsize=6, 
                     bbox=dict(fc="white", ec="none"))
            filename = img_filename.replace("50", ''.join(str(text_1).split('.')))
            plt.savefig(f"icons/{filename}",bbox_inches='tight')

if __name__ == '__main__':
    main()

