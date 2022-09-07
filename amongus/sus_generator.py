def get_encoded_sus(sussy_susser: str) -> list[int]:
    """
    Returns a list that represents the encoded sus.

    :param sussy_susser: str
    :return: list[int]
    """
    return [ord(i) for i in sussy_susser]


def get_text(sus_text: str, name: str, filename: str) -> str:
    variable_name = name + "_sus"

    return f'''# Path: amongus\\{filename}
{variable_name} = {get_encoded_sus(sus_text)}


def get_decoded_{name}_sus() -> str:
    """
    Returns a decoded {name} sus

    :return: str
    """

    return "".join([chr(i) for i in {variable_name}])


def get_encoded_{name}_sus() -> list[int]:
    """
    Returns an encoded {name} sus

    :return: list[int]
    """

    return {variable_name}
'''


def main():
    sus = """"""
    first_name = ""
    file_name = first_name + "_sus.py"

    # Checks if sus is empty or if first_name is empty
    if sus.strip() == "" or first_name.strip() == "":
        raise Exception("Sus, and first_name cannot be empty.")

    with open(file_name, "w") as f:
        f.write(get_text(sus, first_name, file_name))

    # Reads the __init__.py file and adds the import statement then writes it back with correct spacing at the end
    with open("__init__.py", "r") as f:
        lines = f.readlines()
        lines.append(f"from amongus.{file_name[:-3]} import get_encoded_{first_name}_sus, get_decoded_{first_name}_sus\n")
        lines = [i for i in lines if i.strip() != ""]

    with open("__init__.py", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()