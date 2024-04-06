def validate_ip_or_mask_octet_with_message(octet, is_mask=False):
    if octet.isdigit() and 0 <= int(octet) <= 255:
        binary_octet = format(int(octet), '08b')
        if is_mask:
            if '01' in binary_octet:
                return "INVALID", False
        return binary_octet, True
    else:
        return "INVALID", False

def validate_and_format_input(input_str, is_mask=False):
    octets = input_str.split(".")
    binary_representation = []
    validity = True
    
    for octet in octets:
        binary_octet, is_valid = validate_ip_or_mask_octet_with_message(octet, is_mask)
        binary_representation.append(binary_octet)
        if not is_valid:
            validity = False
    
    binary_str = ".".join(binary_representation)
    if validity and not is_mask:
        return f"{binary_str}.   VALID"
    elif validity and is_mask:
        combined_binary = ''.join(binary_representation)
        if '01' in combined_binary:
            return f"{binary_str}.   INVALID"
        return f"{binary_str}.   VALID"
    else:
        return f"{binary_str}."

def process_batch_custom_format():
    input_file_path = input("Enter the path to the input file: ")
    is_mask_input = input("Is this file for subnet masks? (yes/no): ").lower() == "yes"
    output_file_path = input("Enter the path to the output file: ")
    
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            line = line.strip()
            if line: 
                validation_result = validate_and_format_input(line, is_mask_input)
                output_file.write(f" {line}\n   {validation_result}\n")

def interactive_mode():
    input_type = input("Enter 'IP' for IP address or 'MASK' for subnet mask: ").lower()
    input_str = input("Enter the value: ")
    is_mask = input_type == 'mask'
    result = validate_and_format_input(input_str, is_mask)
    print(f"{input_str}\n   {result}")

if __name__ == "__main__":
    mode = input("Choose mode (interactive/batch): ").lower()
    if mode == "interactive":
        interactive_mode()
    elif mode == "batch":
        process_batch_custom_format()
    else:
        print("Invalid mode selected.")
