import random
from generate_data import generate_top_badge_text

def main():
    for i in range(3):
        top_badge_text_1, top_badge_text_2 = generate_top_badge_text()

        print(f"{top_badge_text_1} • {top_badge_text_2}")

if __name__ == '__main__':
    main()

