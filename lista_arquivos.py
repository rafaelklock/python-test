import os


def extract_name():
    return name.split(".")[0]


def read_lines(filename):
    _file = open(os.path.join("data", "meta-data", filename), "rt")
    data = _file.read().split("\n")  # split create a list with lines from file open
    _file.close()
    return data


def read_metadata(filename):
    metadata = []  # created a tuple
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split('\t'[:3])))
    return metadata


def prompt():
    print("\nO que deseja ver?")
    print("(l) Listas entidades")
    print("(d) Exibir atributos")
    print("(r) Exibir referencias de uma entidade")
    print("(s) Sair do programa")
    return input('')


def main():
    meta = {}
    keys = {}
    relationships = {}

    for meta_data_file in os.listdir(os.path.join("data", "meta-data")):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = read_metadata(meta_data_file)
        keys[identifier] = table_name

    for key, value in meta.items():
        for col in value:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationships[key] = keys[col[0]]

    option_prompt = prompt()
    while option_prompt != 's':
        if option_prompt == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif option_prompt == 'd':
            entity_name = input('Nome da entidade: ')
            for col in meta[entity_name]:
                print(col)
        elif option_prompt == 'r':
            entity_name = input('Nome entidade: ')
            other_entity = relationships[entity_name]
            print(other_entity)
        else:
            print("Inexistente\n")
        option_prompt = prompt()


if __name__ == "__main__":
    main()
