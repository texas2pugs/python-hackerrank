# HackerRank problem "Validating phone numbers"
# Python > Regex and parsing

import re

def validate_ph_num(ph):
    """
    Validates a phone number by checking:
    - If length is 10 digits
    - If first digits are 7, 8 or 9
    - No alpha chars are present
    """

    if re.search("^[7-9]\d{9}$",ph):
        print("YES")
    else:
        print("NO")

# Test data
validate_ph_num("71234567898")
validate_ph_num("4123456789")
validate_ph_num("7123456789")
validate_ph_num("8A23456789")
