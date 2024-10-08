def run(z: float) -> float:
    PI = 3.14
    area1 = PI * ((z + (z / 2)) ** 2)
    area2 = PI * ((z / 2) ** 2)
    gray_area = area1 - area2
    gray_area = round(gray_area, 2)
    return gray_area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
