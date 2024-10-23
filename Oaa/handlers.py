""" file contains command handlers for the parser """

class Handles():
    def create(self, collection_name):
        if not collection_name.isidentifier():
            print(f"Error: Invalid collection name '{collection_name}'.")
        else:

            print(f"Collection '{collection_name}' has been created.")

    def insert(self, collection_name, document):
        # Знімаємо лапки з початку та кінця документа
        document = document.strip('"')
        print(f"Document '{document}' inserted into collection '{collection_name}'.")

    def print_index(self, collection_name):
        print(f"Printing index for collection '{collection_name}'.")

    def search(self, collection_name, query=None):
        if query:
            print(f"Performing search in '{collection_name}' with query '{query}'.")
        else:
            print(f"Performing search in '{collection_name}'.")
