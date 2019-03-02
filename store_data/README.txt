-*- mode: org; -*-
* Data lists
- ~rpi_entity_list.h5~
- ~rpi_event_list.h5~
- ~rpi_event_roles.h5~
- ~rpi_relation_list.h5~
- ~rpi_relations.h5~
- ~rpi_document_types.h5~

Serialized by Pandas HDF5. To read them, using ~pd.read_hdf~, which requires library [[https://www.pytables.org/][~PyTables~]].

* Entity list
Recorded in ~rpi_entity_list.h5~.

| column            | type | desc.                                       |
|-------------------+------+---------------------------------------------|
| e                 | str  | Entity URI                                  |
| type              | str  | LDC type starting with ~ldcOnt:~            |
| label             | str  | PrefLabel                                   |
| source            | str  | Original document ID                        |
| start             | int  | Start offset                                |
| end               | int  | End offset inclusive                        |
| justificationType | str  | Can be ~mention~, ~nominal_~, ~pronominal_~ |

* Event list
Recorded in ~rpi_event_list.h5~.

| column            | type | desc. |
|-------------------+------+-------|
| e                 | str  |       |
| type              | str  |       |
| label             | str  |       |
| source            | str  |       |
| start             | int  |       |
| end               | int  |       |
| justificationType | str  |       |
