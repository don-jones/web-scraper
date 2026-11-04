import matplotlib.pyplot as plt
import os
import matplotlib.patches as patches

def overlay_images(filepath_bkgd, filepath_pane):
    fig = plt.figure(figsize=(12,9))
    ax_bkgd = fig.add_axes([0,0,1,1])
    img_bkgd = plt.imread(filepath_bkgd)
    ax_bkgd.imshow(img_bkgd)

    img_pane = plt.imread(filepath_pane)[40:360, 130:1000]
    ax_pane = fig.add_axes([0.2,0.2,0.6,0.6])
    ax_pane.imshow(img_pane)
    ax_bkgd.axis('off')
    ax_pane.axis('off')
    xmin = 0
    ymin = 0
    height = 320-1
    width = 870-1
    rect = patches.Rectangle(
        (xmin, ymin), 
        width, 
        height, 
        linewidth=2, 
        edgecolor='red', 
        facecolor='none'  # 'none' ensures the interior remains completely transparent
    )
    
    ax_pane.add_patch(rect)
    plt.show()

def main():
    OVERLAY_IMAGE = "/Users/macuser/freelance_projects/web-scraper/mybot/job_panes/synthesized_data/00010000.png"
    counter = 0
    for img in os.scandir("shutterstock_api_images"):
        overlay_images(img.path, OVERLAY_IMAGE)
        if counter > 5:
            break
        counter += 1

if __name__ == "__main__":
    main()
