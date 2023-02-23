def flatten_dict(d: dict, sep='_', pr='') -> dict:
    """Принимает вложенный словарь и возвращает плоский"""
    return {pr + sep + k if pr else k: v
            for kk, vv in d.items()
            for k, v in flatten_dict(vv, sep, kk).items()
            } if isinstance(d, dict) else {pr: d}

# def flatten_dict(d: dict) -> dict:
#     import pandas as pd
#     df = pd.json_normalize(d, sep='_')
#     return df.to_dict(orient='records')[0]


print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))
print(flatten_dict({'Germany_berlin': 7,
                    'Europe_italy_Rome': 3,
                    'USA_washington': 1,
                    'USA_New York': 4}))
print(flatten_dict({'a': [100, 200, 300], 'b': [200, 400, 600, 800]}))

assert flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}) == {'Q_w_E_r_T_y': 123}
assert flatten_dict({'Germany_berlin': 7,
                     'Europe_italy_Rome': 3,
                     'USA_washington': 1,
                     'USA_New York': 4}) == {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1,
                                             'USA_New York': 4}
assert flatten_dict({'a': 100, 'b': 200}) == {'a': 100, 'b': 200}
