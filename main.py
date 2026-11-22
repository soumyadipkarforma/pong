# main file for pong game we start with defining variables
def main():
    vx = 10

    def draw_box():
        print("Drawing box...")
        n = 0
        k = 0
        while n < 3:
            def draw_line():
                while k < 3:
                    print("#", end="")
                    k += 1
                print()
            draw_line()
            n += 1
    draw_box()

if __name__ == "__main__":
    main()