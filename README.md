# dro

Dro aims to eventually be a fully featured software to help users manage their personal libraries. It currently falls far short of that particular goal. However, as part of the project I am working on some utilities to work with MARC data, and these utilities do currently offer some amount of *very* basic functionality. At this point the code is capable of decoding and displaying UTF-8 encoded MARC21 bibliographic files. Support for MARC-8 encoded files and editing MARC records is not yet implemented, but support for these features is planned for the semi-near future.

To display MARC records in a terminal, change directories to the directory where the python scripts are stored and:

```
python3 readmarc.py /path/to/marc/records.mrc
```
