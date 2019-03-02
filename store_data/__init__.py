import pandas as pd
from os.path import join, dirname

dir_ = dirname(__file__)
df_entity = pd.read_hdf(join(dir_, 'rpi_entity_list.h5'))
df_event = pd.read_hdf(join(dir_, 'rpi_event_list.h5'))
df_role = pd.read_hdf(join(dir_, 'rpi_event_roles.h5'))
df_relation = pd.read_hdf(join(dir_, 'rpi_relation_list.h5'))
df_ree = pd.read_hdf(join(dir_, 'rpi_relations.h5'))
df_doc = pd.read_hdf(join(dir_, 'rpi_document_types.h5'))
