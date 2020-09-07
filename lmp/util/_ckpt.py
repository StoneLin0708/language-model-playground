import os
from lmp.util._io import sort_by_integer_pattern


class ckpt_patterns:
    model_write = 'model-{}.pt'
    model_extract = r'model-(\d+)\.pt'
    optimizer_write = 'optimizer-{}.pt'
    optimizer_extract = r'optimizer-(\d+)\.pt'


def _limited_by_pattern(folder, limit, patterns, commit):
    if not os.path.exists(folder):
        return []
    fs = os.listdir(folder)
    rm_list = []
    for pattern in patterns:
        m = sort_by_integer_pattern(fs, pattern)
        if limit > 0:
            m = m[:-limit]
        rm_list += m
    if commit:
        for _, i in rm_list:
            os.remove(os.path.join(folder, i))
    return [i for _, i in rm_list]


def limited_ckpt(folder, limit, commit=True):
    """
    remove old checkpoint
    set limit < 0 to disable
    """
    if limit >= 0:
        return _limited_by_pattern(
            folder, limit, [ckpt_patterns.model_extract, ckpt_patterns.optimizer_extract], commit)


def get_model_ckpt_name(folder, step):
    return os.path.join(folder, ckpt_patterns.model_write.format(step))


def get_optimizer_ckpt_name(folder, step):
    return os.path.join(folder, ckpt_patterns.optimizer_write.format(step))


def get_latest_valid_ckpt_count(folder):
    if not os.path.exists(folder):
        return 0
    fs = os.listdir(folder)
    m_ckpt = sort_by_integer_pattern(fs, ckpt_patterns.model_extract)
    o_ckpt = sort_by_integer_pattern(fs, ckpt_patterns.optimizer_extract)
    if (len(m_ckpt) == 0) or (len(o_ckpt) == 0):
        return 0
    if m_ckpt[-1][0] != o_ckpt[-1][0]:
        raise Exception(
            f'latest checkpoint model-{m_ckpt[1]} != optimizer-{o_ckpt[1]}')
    return m_ckpt[-1][0]
