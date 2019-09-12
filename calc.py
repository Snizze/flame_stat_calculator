from math import floor

# Stat Equivalents
# one_as = 1.08              # 1 All Stat = x STR
# one_percent_as = 8.31      # 1% All Stat = x STR
# dex_to_str = 12.04         # x DEX = 1 STR
# one_atk = 4.06             # 1 ATK = x STR

# Input Stat Equivalents
input_one_as = float(input("How much is one all stat equivalent to in main stat: "))
input_one_percent_as = float(input("How much is one all stat% equivalent to in main stat: "))
input_main_to_secondary = float(input("How much secondary stat is equivalent to one main stat: "))
input_one_atk = float(input("How much main stat is one attack equivalent to: "))

# Input Flame Stats
input_main_amt = float(input("How much main stat is the flame worth: "))
input_secondary_amt = float(input("How much secondary stat is the flame worth: "))
input_atk_amt = float(input("How much attack is the flame worth: "))
input_as_amt = float(input("How much all stat% is the flame worth: "))


total_strength = input_main_amt + floor(input_as_amt * input_one_percent_as)
if input_secondary_amt > 0:
    secondary_equivalent = floor(input_secondary_amt / input_main_to_secondary)
    total_strength += secondary_equivalent
if input_atk_amt > 0:
    atk_equivalent = floor(input_atk_amt * input_one_atk)
    total_strength += atk_equivalent

print(f"Your flame is equivalent to {floor(total_strength)} main stat")
