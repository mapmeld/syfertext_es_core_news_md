from pathlib import Path
import pickle
import os
import numpy as np

# Get the path to the data folder
DATA_PATH = os.path.join(Path(__file__).parent, "vocab")


def _load_vectors():
    """Loads the embedding vectors of the vocabulary strings from disk.

    Returns:
        vectors (array): a numpy array which as much rows as words in the vocabulary.
            the number of columns is equal to the vector's dimensions (300 in this case).

        default_vector (array): a numpy array of size as `vectors`.
            this vector is used for out-of-vocabulary tokens.
    """

    # Get the path to the file where vectors are stored
    vectors_path = os.path.join(DATA_PATH, "vectors")

    # Unpickle the vectors
    with open(vectors_path, "rb") as vectors_file:
        vectors = pickle.load(vectors_file)

    # Create a default vector that is returned
    # when an out-of-vocabulary token is encountered
    default_vector = np.zeros(vectors.shape[1], dtype=vectors.dtype)

    return vectors, default_vector


def _load_key2row():
    """Loads the pickled `key2row` dictionary from disk.

    Returns:
        key2row (dict): a dictionary that maps a word hash to an index.
            This index points to the row corresponding to the word
            in the `vectors` array.
    """

    # Create the path to the file where the `key2row` dict
    # is stored as a pickled object.
    key2row_path = os.path.join(DATA_PATH, "key2row")

    # Unpickle the file
    with open(key2row_path, "rb") as key2row_file:
        key2row = pickle.load(key2row_file)

    return key2row


# Create a dictionary of loaders.
LOADERS = dict(vectors=_load_vectors, key2row=_load_key2row)
