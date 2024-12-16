from data_structures import InvertedIndex

collections = {}

def handle_create(collection_name):
    global collections  # fix
    if collection_name in collections:
        return f"Error: Collection {collection_name} already exists."
    collections[collection_name] = InvertedIndex()
    return f"Collection {collection_name} has been created."

def handle_insert(collection_name, document):
    if collection_name not in collections:
        return f"Error: Collection {collection_name} does not exist."
    collections[collection_name].add_document(document)
    return f"Document has been added to {collection_name}."

def handle_print_index(collection_name):
    if collection_name not in collections:
        return f"Error: Collection {collection_name} does not exist."
    return collections[collection_name].print_index()

def handle_search(collection_name, query):
    if collection_name not in collections:
        return f"Error: Collection {collection_name} does not exist."
    return collections[collection_name].search(query)
