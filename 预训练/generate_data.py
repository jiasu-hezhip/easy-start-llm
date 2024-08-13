import os
from unicodedata import normalize

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import ujson
from rich import progress


def split_txt_cropus_to_chunk_data(
    texts: list, batch_size: int = 512**2, max_len: int = 512, window_size: int = 2
) -> list:

    buffer, buffer_len = [], 0
    chunk_data = []

    for i, line in enumerate(texts):
        buffer_len += len(line)
        buffer.append(line)

        if buffer_len >= batch_size or i == len(texts) - 1:
            buffer_txt = "".join(buffer)

            # - window_size为滑动窗口，这样每个窗口都包含有window_size个上文
            for i in range(0, len(buffer_txt), max_len - window_size):

                chunk_data.append("".join(buffer_txt[i : i + max_len]))

            buffer, buffer_len = [], 0

    return chunk_data


def gen_wiki(origin_file, output_file):
    liness = []
    with open(origin_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    items, content = [], []
    key_word, kw_line_idx = "", 0
    content_start = False  # 词条内容开始标记

    eos_token = "<|im_end|>"
    for i, line in enumerate(lines):

        line_strip = line.strip()

        # 词条以冒号`：`结尾
        if len(line_strip) > 0 and line_strip[-1] in (":", "："):
            key_word = "".join(line_strip[:-1])
            kw_line_idx = i
            continue

        # 词条key_word在下一行，则合并上个词条并保存
        if i == kw_line_idx + 1 and key_word in line_strip or i == len(lines) - 1:
            txt = "".join(content)

            if len(txt) > 0:
                items.append(f"{txt}{eos_token}")

            content = []
            content.append(f"{key_word}：")

        content.append(line)
    chunk_data = split_txt_cropus_to_chunk_data(items)
    tb = pa.Table.from_arrays([pa.array(chunk_data)], names=["text"])
    pq.write_table(
        table=tb,
        where=output_file,
        row_group_size=50000,
        data_page_size=50000,
    )


def process_none(s: str) -> str:
    if s:
        return s
    return ""

def gen_wiki_filter(origin_file, output_file="../datasets/wiki_fi.parquet"):
    lines = []
    with open(origin_file, "r", encoding="utf-8") as f:
        items = ujson.load(f)
        for item in items:
            lines.append(item["completion"] + "<|im_end|>")
    chunk_data = split_txt_cropus_to_chunk_data(lines)
    tb = pa.Table.from_arrays([pa.array(chunk_data)], names=["text"])
    pq.write_table(
        table=tb,
        where=output_file,
        row_group_size=50000,
        data_page_size=50000,
    )

def gen_bell():
    train_data = []
    eval_data = []
    eval_size = 10000
    max_len = 512
    root = "/data/MINI_LLM_data"
    with open(root + "/train_3.5M_CN/train_3.5M_CN.json", "r", encoding="utf-8") as f:
        for line in f:
            item = ujson.loads(line)

            if len(item["conversations"]) != 2:
                continue

            conversation = item["conversations"]
            txt = ""
            if conversation[0]["from"] == "human":
                txt = f"{conversation[0]['value']}\n{conversation[1]['value']}"
            else:
                txt = f"{conversation[1]['value']}\n{conversation[0]['value']}"

            # 收集测试数据
            if (
                len(txt) >= max_len
                and len(txt) < max_len + 8
                and len(eval_data) < eval_size
                and np.random.rand() <= 0.12
            ):
                eval_data.append(txt)
                continue

            if len(txt) >= max_len:
                continue
            train_data.append(txt)
    for file in [
        root + "/train_2M_CN/train_2M_CN.json",
        root + "/train_1M_CN/Belle_open_source_1M.json",
    ]:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                item = ujson.loads(line)

                if item["input"].strip() != "":
                    txt = f"{item['instruction']}\n{item['input']}\n{item['output']}"
                else:
                    txt = f"{item['instruction']}\n{item['output']}"

                # 收集测试数据
                if (
                    len(txt) >= max_len
                    and len(txt) < max_len + 8
                    and len(eval_data) < eval_size
                    and np.random.rand() > 0.75
                ):
                    eval_data.append(txt)
                    continue

                if len(txt) == 0 or len(txt) >= max_len:
                    continue
                train_data.append(txt)
    tb = pa.Table.from_arrays([train_data], names=["text"])
    # compression='GZIP'
    pq.write_table(
        table=tb,
        where=f"../datasets/bell_pretrain_{max_len}_3M.parquet",
        row_group_size=20480,
        data_page_size=20480,
    )

    tb = pa.Table.from_arrays([eval_data], names=["text"])
    # compression='GZIP'
    pq.write_table(
        table=tb,
        where=f"../datasets/pretrain_eval_{max_len}_1w.parquet",
        row_group_size=20480,
        data_page_size=20480,
    )


gen_wiki_filter(
    "/data/MINI_LLM_data/wikipedia-cn-20230720-filtered/wikipedia-cn-20230720-filtered.json"
)

gen_bell()

