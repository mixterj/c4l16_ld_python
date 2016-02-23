from __future__ import print_function
import sys
import rdflib
from rdflib import URIRef, Namespace, RDF, Graph, Literal, BNode, plugin, Variable
from optparse import OptionParser

# given a subject uri and a string for a schema.org predicate,
# return a list of any matching objects
# representing the object by its name property if available, 
# otherwise representing the object by its uri
#graph = rdflib.Graph()
def get_labels(graph, uri, predicate_string):
    predicate = rdflib.term.URIRef(u'http://schema.org/'+predicate_string)
    name = rdflib.term.URIRef(u'http://schema.org/name')
    object_list = []
    for obj in graph.objects(uri, predicate):
        label = obj
        if graph.value(obj, name):
            label = graph.value(obj, name)
        object_list.append(label)
    object_labels = ('\n'.join(object_list))
    return(object_labels)

#if __name__ == "__main__":
def main():
    # set default uri and predicates
    uri = rdflib.term.URIRef(u'http://www.worldcat.org/oclc/82671871')
    predicates_delimited = "name,creator,description,about"

    # look for uri and predicates parameters that over-ride the defaults
    parser = OptionParser()
    parser.add_option("-u", dest="uri", help="The URI of the RDF resource", action='store')
    parser.add_option("-p", dest="predicates_delimited", help="A comma-separated list of predicates to list, e.g., name,creator,contributor,about", action='store')
    (options, args) = parser.parse_args(sys.argv)
    if options.uri:
      uri = rdflib.term.URIRef(options.uri)
    if options.predicates_delimited:
      predicates_delimited = options.predicates_delimited
    predicates = predicates_delimited.split(",")

    # create an in-memory RDF graph for the resource named in uri
    graph = rdflib.Graph()
    graph.parse(uri)
    
    # for each of the strings in the predicates list ...
    for predicate_string in predicates:
    
        # get a label(s) for any object(s) in the graph for the predicate
        print(get_labels(graph,uri,predicate_string))

if __name__ == "__main__":
    #graph = rdflib.Graph()
    main()
