def calculate_rectangle_area(base, height):
    """
    Calculate the area of a rectangle given its base and height.
    
    :param base: The base of the rectangle 
    :param height: The height of the rectangle 
    :return: The area of the rectangle 
    """
    area = base * height
    return area


def main():
    """
    Main function to demonstrate the usage of calculate_rectangle_area function.
    """
    base = 5
    height = 10
    area = calculate_rectangle _area(base, height)
    print(f"The area of the rectangle with base {base} and height {height} is {area}.")


if __name__ == "__main__":
    main()
