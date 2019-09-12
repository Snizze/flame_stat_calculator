from math import floor

# Stat Equivalents
one_as = 1.08              # 1 All Stat = x STR
one_percent_as = 8.31      # 1% All Stat = x STR
dex_to_str = 12.04         # x DEX = 1 STR
dex_to_str_percent = 8.06  # x DEX% = 1% STR
one_atk = 4.06             # 1 ATK = x STR

# Flame Stats
str_amt = 60  # Amount of STR
dex_amt = 20  # Amount of DEX
atk_amt = 3   # Amount of ATK
as_amt = 5    # Amount of All Stat %


total_strength = str_amt + floor(as_amt * one_percent_as)
if dex_amt > 0:
    dex_equivalent = floor(dex_amt / dex_to_str)
    total_strength += dex_equivalent
if atk_amt > 0:
    atk_equivalent = floor(atk_amt * one_atk)
    total_strength += atk_equivalent

print(floor(total_strength))
