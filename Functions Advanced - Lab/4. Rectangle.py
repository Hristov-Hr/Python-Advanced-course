def rectangle(length, width):

    if not type(length) == int or not type(width) == int:
        return "Enter valid values!"

    return f'Rectangle area: {length * width}\nRectangle perimeter: {(length + width) * 2}'