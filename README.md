# es_core_news_sm for PySyft / SyferText

## Context

- PySyft is an open source, privacy-protecting machine learning platform from OpenMined. Examples of privacy concepts include building models on remote data, federated learning, and differential privacy
- SyferText is a library which extends PySyft to NLP / language model tasks
- spaCy is a common NLP library
- es_core_news_sm is a small, GPL-licensed model changed on Spanish news content

## Generating a SyferText version of a model

- Select a model from spaCy's website: https://spacy.io/models/es#es_core_news_sm
- Modify this script from Sachin Kumar: https://github.com/sachin-101/syfertext_lang_models/blob/master/script.py
- Drop the three pickled files from the previous script into the module format used here https://github.com/Nilanshrajput/syfertext_en_core_web_lg/ - including git-lfs (large file storage) if
you use a larger model.

## Testing that the model works

See basic-test.ipynb or follow along below:

```bash
pip install git+git://github.com/mapmeld/syfertext_es_core_news_sm@main

# use latest directions from SyferText for compatibility
pip install syft@git+https://github.com/OpenMined/PySyft@1eb369ae3a1865789f5809bec59f066ac1cbe58d
git clone https://github.com/OpenMined/SyferText.git
cd SyferText && python setup.py install
```

```python
import syft as sy
import torch
import syfertext

hook = sy.TorchHook(torch)
me = hook.local_worker
nlp = syfertext.load('es_core_news_sm', owner=me)

my_str = 'Me llamo Nicolas'
doc = nlp(my_str)
for token in doc:
    print('%10s | %5s | %s'%(token, token.space_after, token.orth))
```

## License

GPLv3+ (as required by es_core_news_sm)
