import xml.dom.minidom
import datetime
import matplotlib.pyplot as plt

ONTOLOGIES = {
    'molecular_function': 0,
    'biological_process': 0,
    'cellular_component': 0
}

def parse_go_terms_dom(xml_file):
    start_time = datetime.datetime.now()
    dom = xml.dom.minidom.parse(xml_file)
    for term in dom.getElementsByTagName('term'):
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        ONTOLOGIES[namespace] += 1
    
    end_time = datetime.datetime.now()
    print("Time taken using DOM API:", end_time - start_time)
    
    return ONTOLOGIES

def plot_results(ontologies):
    labels = list(ONTOLOGIES.keys())
    values = list(ONTOLOGIES.values())
    plt.bar(labels, values)
    plt.xlabel('Ontology')
    plt.ylabel('Number of GO Terms')
    plt.title('Frequency of GO Terms in Ontologies')
    plt.show()

def main():
    go_terms = parse_go_terms_dom('go_obo.xml')
    plot_results(go_terms)

if __name__ == "__main__":
    main()