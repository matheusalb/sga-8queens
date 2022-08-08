from SGA_8queens import SGA_8queens

def main():
    eight_queens = SGA_8queens(100, 10000, 0.9, 0.4)
    
    eight_queens.fit()

if __name__ == '__main__':
    main()