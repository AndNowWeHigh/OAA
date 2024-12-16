import re

class InvertedIndex:
    def __init__(self):
        self.documents = []  # Список документів
        self.index = {}      # Інверсний індекс

    def add_document(self, document):
        doc_id = len(self.documents)
        self.documents.append(document)
        words = re.findall(r"[a-zA-Z0-9_]+", document.lower())
        for position, word in enumerate(words):
            if word not in self.index:
                self.index[word] = {}
            if doc_id not in self.index[word]:
                self.index[word][doc_id] = []
            self.index[word][doc_id].append(position)

    def print_index(self):
        result = []
        for word, postings in sorted(self.index.items()):
            result.append(f'"{word}":')
            for doc_id, positions in postings.items():
                result.append(f"  d{doc_id} -> {positions}")
        return "\n".join(result)

    def search(self, query):
        if not query:
            # Якщо немає запиту, повертаємо всі документи
            return "\n".join(self.documents)

        query = query.lower().strip()
        print(query)
        # Точний пошук за ключовим словом
        if query.startswith('"') and query.endswith('"'):
            keyword = query.strip('"')
            if keyword in self.index:
                doc_ids = self.index[keyword].keys()
                return "\n".join(self.documents[doc_id] for doc_id in doc_ids)
            return "No matching documents found."

        # Префіксний пошук
        if query.endswith("*"):
            print('1')
            prefix = query[:-1]
            matching_words = [word for word in self.index if word.startswith(prefix)]
            matching_docs = set()
            for word in matching_words:
                matching_docs.update(self.index[word].keys())
            return "\n".join(
                self.documents[doc_id] for doc_id in matching_docs) if matching_docs else "No matching documents found."

        # Пошук на відстані <N>
        match = re.match(r'"(.+)"\s+<(\d+)>\s+"(.+)"', query)
        if match:
            word1, distance, word2 = match.groups()
            distance = int(distance)
            word1, word2 = word1.lower(), word2.lower()
            if word1 in self.index and word2 in self.index:
                matching_docs = set(self.index[word1].keys()).intersection(self.index[word2].keys())
                result_docs = []
                for doc_id in matching_docs:
                    positions1 = self.index[word1][doc_id]
                    positions2 = self.index[word2][doc_id]
                    for p1 in positions1:
                        if any(abs(p1 - p2) <= distance for p2 in positions2):
                            result_docs.append(doc_id)
                            break
                return "\n".join(
                    self.documents[doc_id] for doc_id in result_docs) if result_docs else "No matching documents found."
        return "Error: Invalid query."