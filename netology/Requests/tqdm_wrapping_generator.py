# import numpy as np
# from tqdm.contrib import tenumerate, tmap, tzip
#
# for _ in tenumerate(range(int(1e6)), desc="builtin enumerate", color='green'):
#     pass
#
# for _ in tenumerate(np.random.random((999, 999)), desc="numpy.ndenumerate"):
#     pass
#
# for _ in tzip(np.arange(1e6), np.arange(1e6) + 1, desc="builtin zip"):
#     pass
#
# mapped = tmap(lambda x: x + 1, np.arange(1e6), desc="builtin map")
# assert (np.arange(1e6) + 1 == list(mapped)).all()


"""
Asynchronous examples using `asyncio`, `async` and `await` on `python>=3.7`.
"""
import numpy as np
import pandas as pd

from tqdm.auto import tqdm

df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))

# Register `pandas.progress_apply` and `pandas.Series.map_apply` with `tqdm`
# (can use `tqdm.gui.tqdm`, `tqdm.notebook.tqdm`, optional kwargs, etc.)
tqdm.pandas(desc="Прогресс ")

# Now you can use `progress_apply` instead of `apply`
# and `progress_map` instead of `map`
df.progress_apply(lambda x: x**2)
# can also groupby:
# df.groupby(0).progress_apply(lambda x: x**2)

# -- Source code for `tqdm_pandas` (really simple!)
# def tqdm_pandas(t):
#   from pandas.core.frame import DataFrame
#   def inner(df, func, *args, **kwargs):
#       t.total = groups.size // len(groups)
#       def wrapper(*args, **kwargs):
#           t.update(1)
#           return func(*args, **kwargs)
#       result = df.apply(wrapper, *args, **kwargs)
#       t.close()
#       return result
#   DataFrame.progress_apply = inner
