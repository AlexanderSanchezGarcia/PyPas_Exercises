def run(n: int) -> int:
    if n >= 0 and n <= 9:
        str_n = str(n)
        result = int(str_n ) + int(str_n + str_n) + int(str_n + str_n + str_n)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
