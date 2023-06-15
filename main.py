import re

def read_Cheader_file(filename:str) -> str:
    """
    To read the contents of a C header file into Python

    Args:
        filename (str): path of C header file

    Returns:
        str: the content of C header file
    """
    try:
        with open(filename, 'r') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return ""
    except IOError:
        print(f"Error: Unable to read file {filename}")
        return ""
    else:
        return file_contents
    
def parse_struct_definition(struct_definition:str):
    """
    This func uses regular expression to match and parse a struct_definition

    Args:
        struct_definition (str): The structure definition waiting for parsing

    Returns:
        dict: The parsed result meets the requirements mentioned in the readme file, 
        but the length of fields has not been calculated
    """
    struct_pattern = r"struct\s+(\w+)\n\{\n([^}]+)\}"
    field_pattern = r"\s+(\w+)\s+(\w+(\[\d+\])*);"

    match = re.findall(struct_pattern, struct_definition)
    res = {}
    if match:
        for _struct_name, _struct_fields in match:
            res[_struct_name] = [0, []]
            _fields = re.findall(field_pattern, _struct_fields)
            for _field in _fields:
                res[_field[1]] = _field[0]
                res[_struct_name][1].append(_field[1])
                
    else:
        print("No match found.")
    return res

def main():
    struct_definition = read_Cheader_file('BdsDxe.debug.h')
    parse_struct_definition(struct_definition)

if __name__ == '__main__':
    main()