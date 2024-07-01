def split_count(Var_count):
    # Convert Var_count to string
    Var_count_str = str(Var_count)

    # Check if Var_count contains a dot (indicating a fractional part)
    if '.' in Var_count_str:
        # Split Var_count into integer and fractional parts
        integer_part, fractional_part = Var_count_str.split('.')
        
        # If there are four or more zeros after the decimal point, consider it as an integer
        if len(fractional_part) >= 4 and fractional_part[:4] == '0000':
            return [int(integer_part)]

    # If there are less than four zeros or non-zero digits after the decimal point, return the original Var_count
    return [float(Var_count)]

# Example usage
#Var_count = "0.9999500024998751"
#individual_counts = split_count(Var_count)
#print(individual_counts)
