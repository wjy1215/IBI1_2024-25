import xml.sax
from xml.dom import minidom
from datetime import datetime
import os

os.chdir('practical 14')
FILENAME = "go_obo.xml"

# DOM 
def process_with_dom(filename):
    start_time = datetime.now()
    doc = minidom.parse(filename)
    terms = doc.getElementsByTagName("term")

    result = {
        'molecular_function': [],
        'biological_process': [],
        'cellular_component': []
    }

    max_counts = {
        'molecular_function': 0,
        'biological_process': 0,
        'cellular_component': 0
    }

    for term in terms:
        ns = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
        term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
        term_name = term.getElementsByTagName("name")[0].firstChild.nodeValue
        is_a_list = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_list)

        if ns in result:
            if is_a_count > max_counts[ns]:
                max_counts[ns] = is_a_count
                result[ns] = [(term_id, term_name, is_a_count)]
            elif is_a_count == max_counts[ns]:
                result[ns].append((term_id, term_name, is_a_count))

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    return result, duration

# SAX 
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.in_term = False
        self.current_id = ""
        self.current_name = ""
        self.current_ns = ""
        self.is_a_count = 0
        self.current_element = ""

        self.result = {
            'molecular_function': [],
            'biological_process': [],
            'cellular_component': []
        }

        self.max_counts = {
            'molecular_function': 0,
            'biological_process': 0,
            'cellular_component': 0
        }

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "term":
            self.in_term = True
            self.current_id = ""
            self.current_name = ""
            self.current_ns = ""
            self.is_a_count = 0

    def endElement(self, name):
        if name == "term":
            if self.current_ns in self.result:
                max_count = self.max_counts[self.current_ns]
                entry = (self.current_id, self.current_name, self.is_a_count)
                if self.is_a_count > max_count:
                    self.max_counts[self.current_ns] = self.is_a_count
                    self.result[self.current_ns] = [entry]
                elif self.is_a_count == max_count:
                    self.result[self.current_ns].append(entry)
            self.in_term = False
        self.current_element = ""

    def characters(self, content):
        if not self.in_term:
            return
        content = content.strip()
        if self.current_element == "id":
            self.current_id += content
        elif self.current_element == "name":
            self.current_name += content
        elif self.current_element == "namespace":
            self.current_ns += content
        elif self.current_element == "is_a":
            self.is_a_count += 1

def process_with_sax(filename):
    start_time = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(filename)
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    return handler.result, duration

# output
def print_result(method, result_dict, duration):
    print(f"{method} completed in {duration:.4f} seconds")
    print()

    for ns, terms in result_dict.items():
        if terms:
            max_count = terms[0][2]
            print(f"[{method}] {ns} (max is_a: {max_count}):")
            for term_id, name, count in terms:
                print(f"  - {term_id} ({name}) with {count} is_a relations")
            print()


if __name__ == "__main__":
    print("Processing with DOM")
    dom_result, dom_time = process_with_dom(FILENAME)
    print_result("DOM", dom_result, dom_time)

    print("Processing with SAX")
    sax_result, sax_time = process_with_sax(FILENAME)
    print_result("SAX", sax_result, sax_time)

    # compare the time taken by both methods
    if dom_time < sax_time:
        print(f">>> DOM was faster by {sax_time - dom_time:.4f} seconds.")
    elif sax_time < dom_time:
        print(f">>> SAX was faster by {dom_time - sax_time:.4f} seconds.")
    else:
        print(">>> Both methods took the same amount of time.")
    # # SAX was faster / DOM was faster in this case