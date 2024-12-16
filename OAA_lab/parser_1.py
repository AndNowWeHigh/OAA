import re
from handlers_1 import handle_create, handle_insert, handle_print_index, handle_search

def parse_command(command):
    command = re.sub(r"[ \t\r\n]+", " ", command.strip())  # Замінюємо зайві пробіли
    command = command.strip(";").strip()
    if command.upper().startswith("CREATE"):
        match = re.match(r"CREATE\s+([a-zA-Z][a-zA-Z0-9_]*);?$", command, re.IGNORECASE)
        if match:
            return handle_create(match.group(1))
    elif command.upper().startswith("INSERT"):
        match = re.match(r"INSERT\s+([a-zA-Z][a-zA-Z0-9_]*)\s+\"(.+)\";?$", command, re.IGNORECASE)
        if match:
            return handle_insert(match.group(1), match.group(2))
    elif command.upper().startswith("PRINT_INDEX"):
        match = re.match(r"PRINT_INDEX\s+([a-zA-Z][a-zA-Z0-9_]*);?$", command, re.IGNORECASE)
        if match:
            return handle_print_index(match.group(1))
    if command.upper().startswith("SEARCH"):
        match = re.match(r"SEARCH\s+([a-zA-Z][a-zA-Z0-9_]*)(\s+WHERE\s+(.+))?;?$", command, re.IGNORECASE)
        if match:
            collection_name = match.group(1)
            query = match.group(3)
            return handle_search(collection_name, query)
    return "Error: Invalid command syntax"

