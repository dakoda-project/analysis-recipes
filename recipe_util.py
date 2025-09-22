from cassis import Cas, TypeSystem
from dakoda.uima import load_dakoda_typesystem
import re

def dep_to_dict(cas: Cas, span: tuple[int, int], view_name: str):
    view = cas.get_view(view_name)

    # construct dummy annotation to use for covered select (i.e. restrict results to given span (usually a single sentence))
    covered = dummy_anno(_begin=span[0], _end=span[1])

    offset_to_index = {}
    for idx, p in enumerate(view.select('de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS')):
        offset_to_index[p.begin] = idx  
    
    words = [
        {
            'text': p.get_covered_text(), 
            'tag': p.PosValue
        } 
        for p in view.select_covered(
            'de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS',
            covering_annotation=covered
        )
    ]

    # how to restrict arcs to covered span?
    arcs = [
        {
            'start': offset_to_index[d.Governor.begin], 
            'end': offset_to_index[d.Dependent.begin],
            'label': d.DependencyType, 
            'dir': 'left'
        } 
        for d in view.select(
            'org.dakoda.syntax.UDependency'
        )
        if span[0] <= d.Governor.begin <= span[1] and span[0] <= d.Dependent.begin <= span[1]
    ]

    # ensure that start is always smaller than end
    # i.e. direction is only encoded in 'dir' field
    for arc in arcs:
        if arc['start'] > arc['end']:
            arc['start'], arc['end'] = arc['end'], arc['start']

    # remove root (i.e. keep everything except root where start == end)
    arcs = [arc for arc in arcs if arc['start'] != arc['end']]


    return {"words": words, "arcs": arcs}

def dummy_anno(_begin: int, _end: int):
    # should this be cached?
    typesystem = load_dakoda_typesystem()
    T = typesystem.get_type('de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token')
    
    return T(begin=_begin, end=_end)