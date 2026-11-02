import os
import matplotlib.pyplot as plt
import random

def main():
    img = plt.imread('icons/-1_pv_50_usa.png')
    height_px, width_px = 31,746
    my_dpi = 100
    scale = 1
    fig = plt.figure(figsize=(width_px / my_dpi * scale, height_px / my_dpi * scale), dpi=my_dpi)

    for i in range(40,50):
        text_1 = i/10
        #plt.imshow(img, extent=[0, width_px, 0, height_px], origin='upper')
        plt.imshow(img, aspect='auto',origin='upper')
        plt.axis('off')
        plt.text(x=175, y=20, s=text_1, fontsize=6, 
                 bbox=dict(fc="white", ec="none"))
        filename = f"-1_pv_{''.join(str(text_1).split('.'))}_usa.png"
        #plt.set_xlim(0, width_px)
        #plt.set_ylim(height_px, 0)
        print(filename)
        plt.savefig(f"icons/{filename}",bbox_inches='tight')

if __name__ == '__main__':
    main()

