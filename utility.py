# Build System Model index
def build_index(systemModel: dict):
    # <ID> : {"entity_type": <type>, "index_name": <name>, "entity_index": <index>}
    sm_index = {}
    for entity_type in systemModel['data']['cpsSystemModel']:
        try:
            for entity_index, entity in enumerate(systemModel['data']['cpsSystemModel'][entity_type]):
                index_item = {
                    "entity_type": entity_type,
                    "index_name": "identity",
                    "entity_index": entity_index
                }
                sm_index[entity['identity']['id']] = index_item

        except TypeError:
            # non iterable object - 'project'
            pass
        except KeyError:
            for entity_index, entity in enumerate(systemModel['data']['cpsSystemModel'][entity_type]):
                index_item = {
                    "entity_type": entity_type,
                    "index_name": "function",
                    "entity_index": entity_index
                }
                sm_index[entity['function']['id']] = index_item

    systemModel['data']['systemModelIndex'] = sm_index
