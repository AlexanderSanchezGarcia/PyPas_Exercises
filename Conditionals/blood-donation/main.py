def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    suitable_for_donation = False
    if (18 <= age <= 65) and (50 <= weight) and (50 <= heartbeat <= 110) and (150000 <= platelets):
        suitable_for_donation = True
    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
