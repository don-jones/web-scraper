import matplotlib.pyplot as plt
import random
import string

def generate_random_paragraphs(lines=1, width=80):
    # Characters to use for the "words"
    chars = string.ascii_letters + string.digits
    output_lines = []
    
    for _ in range(lines):
        line_chars = []
        current_len = 0
        
        while current_len < width:
            # Randomly determine a realistic word length (2 to 8 characters)
            word_len = random.randint(2, 8)
            
            # Ensure we don't overshoot the maximum line width
            if current_len + word_len > width:
                word_len = width - current_len
                
            # Generate the word fragments
            line_chars.extend(random.choices(chars, k=word_len))
            current_len += word_len
            
            # Add a single trailing space if there is still room left on the line
            if current_len < width:
                line_chars.append(" ")
                current_len += 1
                
        output_lines.append("".join(line_chars))
        
    return "\n".join(output_lines)

def main():
    fig = plt.figure(figsize=(10, 4))

    axis_bkgd = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axis_title = fig.add_axes([0.1, 0.7, 0.4, 0.1])
    axis_title.patch.set_alpha(0.0)
    axis_title.axis('off')
    text_1 = generate_random_paragraphs(lines=1, width=40)
    axis_title.text(x=0, y=0, s=text_1, fontsize=18)




    axis_2 = fig.add_axes([0.1, 0.3, 0.4, 0.2])

    # 3. Make the foreground axes completely transparent so the image shows through
    axis_2.patch.set_alpha(0.0)

    # Optional: Hide the axes spines/ticks so only the text is visible over the image
    axis_2.axis('off')
    axis_bkgd.axis('off')                       # Hide the background axis frame lines

    # Populate your text
    text_2 = generate_random_paragraphs(lines=3, width=80)

    axis_2.text(x=0, y=0, s=text_2, fontsize=12)

    # Populate your background
    bkgd_img = plt.imread('job_pane_generic.png')
    axis_bkgd.imshow(bkgd_img, aspect='auto')  # aspect='auto' matches the image to your 0.8x0.8 box dimensions

    plt.show()

if __name__ == '__main__':
    main()
