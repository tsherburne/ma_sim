# Build System Model index
def build_index(systemModel: dict):

    # System Model Index
    # <ID> : {"entity_type": <type>, "entity_index": <index>}
    sm_index = {}
    # Call Structure Index
    cs_index = {}
    # <ID> : {"entity_index": <index>}

    for entity_type in systemModel['data']['cpsSystemModel']:
        try:
            for entity_index, entity in enumerate(systemModel['data']['cpsSystemModel'][entity_type]):
                index_item = {
                    "entity_type": entity_type,
                    "entity_index": entity_index
                }
                sm_index[entity['identity']['id']] = index_item

        except TypeError:
            # non iterable object - 'project'
            pass
        except KeyError:
            # call structure 'function' index
            pass
            for entity_index, entity in enumerate(systemModel['data']['cpsSystemModel'][entity_type]):
                cs_index[entity['function']['id']] = entity_index

    systemModel['data']['systemModelIndex'] = sm_index
    systemModel['data']['callStructureIndex'] = cs_index
