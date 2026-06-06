my_dict = {"Nick": {"Phone": "0735558895", "Instagram": "@nick67", "Tiktok": "@nick6767"},
            "Ann": {"Phone": "0995588401", "Instagram": "@ann582", "Tiktok": "@ann_02"},
            "Jane": {"Phone": "0505314589", "Instagram": "@jane_me", "Tiktok": "@janeforme"}}

user = my_dict[input("Enter name: ")][input("Enter contact type: ")]
print(user)
