import os.path
import json
import logging
from typing import Callable, Dict, Optional
import pandas as pd
from gastrodon import RemoteEndpoint, inline
from store_data.queries import *
from settings import triplestore_url


endpoint = RemoteEndpoint(url=triplestore_url,
                          prefixes=inline(namespaces_str).graph)


# define paths
dir_ = os.path.dirname(__file__)
df_entity_path = os.path.join(dir_, 'rpi_entity_list.h5')
df_event_path = os.path.join(dir_, 'rpi_event_list.h5')
df_role_path =os.path.join(dir_, 'rpi_event_roles.h5')
df_relation_path = os.path.join(dir_, 'rpi_relation_list.h5')
df_ree_path = os.path.join(dir_, 'rpi_relations.h5')
df_doc_path = os.path.join(dir_, 'rpi_document_types.h5')


to_int = lambda s: int(s) if isinstance(s, str) or isinstance(s, int) else -1
get_justification = lambda s: json.loads(s).get('justificationType')


def retrieve_dataframe(endpoint: RemoteEndpoint, query: str, path: str,
                       types: Optional[Dict[str, Callable]]=None,
                       process: Optional[Dict[str, Callable]]=None):
    logging.log(logging.INFO, "Querying data to {}".format(path))
    df = endpoint.select(query)
    if process:
        for key, func in process:
            df[key] = df[key].apply(func)

    to_types = {column: str for column in df.columns}
    if types:
        to_types.update(types)
    df.astype(to_types).to_hdf(path, 'data', mode='w', format='fixed')


def load_dataframe(path: str, fallback: Optional[Callable]=None):
    if not os.path.exists(path):
        if not fallback:
            logging.log(logging.WARN, "Dataframe {} doesn't exist, and no back plan.".format(path))
        logging.log(logging.INFO, "Dataframe {} doesn't exist, try to query it from source".format(path))
        fallback(path)
    logging.log(logging.INFO, "Loading data from {}".format(path))
    df = pd.read_hdf(path)
    return df


df_entity = load_dataframe(
    df_entity_path,
    lambda path: retrieve_dataframe(endpoint, query_entities_with_justification, path, {'start': int, 'end': int},
                                    {'start': to_int, 'end': to_int, 'justificationType': get_justification}))
df_event = load_dataframe(
    df_event_path,
    lambda path: retrieve_dataframe(endpoint, query_events_with_justification, path, {'start': int, 'end': int},
                                    {'start': to_int, 'end': to_int, 'justificationType': get_justification}))
df_role = load_dataframe(df_role_path, lambda path: retrieve_dataframe(endpoint, query_event_roles, path))
df_relation = load_dataframe(
    df_relation_path,
    lambda path: retrieve_dataframe(endpoint, query_relations_with_justification, path,
                                    {'start': int, 'end': int}, {'start': to_int, 'end': to_int}))
df_ree = load_dataframe(df_ree_path, lambda path: retrieve_dataframe(endpoint, query_relations, path))
df_doc = load_dataframe(
    df_doc_path,
    lambda path: retrieve_dataframe(endpoint, query_document_types, df_doc_path,
                                    process={'fileType': lambda s: json.loads(s).get('fileType')}))
