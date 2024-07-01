def split_count(Var_count):
    # Convert Var_count to string
    Var_count_str = str(Var_count)

    # Split Var_count into integer and fractional parts
    integer_part, fractional_part = Var_count_str.split('.') if '.' in Var_count_str else (Var_count_str, '')

    # If there are four or more zeros after the decimal point, remove the fractional part entirely
    if len(fractional_part) >= 4 and all(char == '0' for char in fractional_part[:4]):
        return [int(integer_part)]
    else:
        # Convert integer part to individual counts
        individual_counts = [1] * int(integer_part)

        # Add the fractional part as a float if it's not empty
        if fractional_part:
            fractional_float = float('0.' + fractional_part)
            individual_counts.append(fractional_float)

        return individual_counts

