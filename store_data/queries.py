namespaces_str = """
@prefix : <https://tac.nist.gov/tracks/SM-KBP/2018/ontologies/AidaDomainOntologiesCommon#> .
@prefix aida: <https://tac.nist.gov/tracks/SM-KBP/2018/ontologies/InterchangeOntology#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix domainOntology: <https://tac.nist.gov/tracks/SM-KBP/2018/ontologies/SeedlingOntology> .
@prefix ldc: <https://tac.nist.gov/tracks/SM-KBP/2018/ontologies/LdcAnnotations#> .
@prefix ldcOnt: <https://tac.nist.gov/tracks/SM-KBP/2018/ontologies/SeedlingOntology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""


query_entities_with_justification = """
SELECT ?e ?type ?label ?target ?source ?start ?end ?justificationType {
    ?e a aida:Entity ;
       aida:system <http://www.rpi.edu> .
    ?statement a rdf:Statement ;
               rdf:subject ?e ;
               rdf:predicate rdf:type ;
               rdf:object ?type ;
               aida:justifiedBy ?justification .
    OPTIONAL { ?e aida:link/aida:linkTarget ?target }
    OPTIONAL { ?justification skos:prefLabel ?label }
    OPTIONAL { ?justification aida:source ?source }
    OPTIONAL { ?justification aida:startOffset ?start }
    OPTIONAL { ?justification aida:endOffsetInclusive ?end }
    OPTIONAL { ?justification aida:privateData ?typePrivate .
               ?typePrivate aida:system <http://www.rpi.edu> ;
                            aida:jsonContent ?justificationType }
}
"""


query_events_with_justification = """
SELECT DISTINCT ?e ?type ?label ?source ?start ?end ?justificationType {
    ?e a aida:Event ;
       aida:system <http://www.rpi.edu> .
    ?statement a rdf:Statement ;
               rdf:subject ?e ;
               rdf:predicate rdf:type ;
               rdf:object ?type ;
               aida:justifiedBy ?justification .
    OPTIONAL { ?justification skos:prefLabel ?label }
    OPTIONAL { ?justification aida:source ?source }
    OPTIONAL { ?justification aida:startOffset ?start }
    OPTIONAL { ?justification aida:endOffsetInclusive ?end }
    OPTIONAL { ?justification aida:privateData ?typePrivate .
               ?typePrivate aida:system <http://www.rpi.edu> ;
                            aida:jsonContent ?justificationType }
}
"""


query_event_roles = """
SELECT DISTINCT ?e ?p ?o {
    ?e a aida:Event ;
       aida:system <http://www.rpi.edu> .
    ?statement a rdf:Statement ;
               rdf:subject ?e ;
               rdf:predicate ?p ;
               rdf:object ?o ;
               aida:system <http://www.rpi.edu> .
    FILTER (?p != rdf:type)
}
"""


query_relations_with_justification = """
SELECT DISTINCT ?e ?type ?source ?start ?end {
    ?e a aida:Relation ;
       aida:system <http://www.rpi.edu> .
    ?statement a rdf:Statement ;
               rdf:subject ?e ;
               rdf:predicate rdf:type ;
               rdf:object ?type ;
               aida:justifiedBy ?justification 
    OPTIONAL { ?justification aida:source ?source }
    OPTIONAL { ?justification aida:startOffset ?start }
    OPTIONAL { ?justification aida:endOffsetInclusive ?end }
}
"""


query_document_types = """
SELECT DISTINCT ?source ?fileType {
    ?justification a aida:TextJustification ;
                   aida:system <http://www.rpi.edu> ;
                   aida:source ?source ;
                   aida:privateData ?filePrivate .
    ?filePrivate aida:system <http://www.rpi.edu/fileType> ;
                 aida:jsonContent ?fileType
}
"""


query_relations = """
SELECT DISTINCT ?e ?p ?o {
    ?e a aida:Relation ;
       aida:system <http://www.rpi.edu> .
    ?statement a rdf:Statement ;
               rdf:subject ?e ;
               rdf:predicate ?p ;
               rdf:object ?o 
    FILTER (?p != rdf:type)
}
"""
