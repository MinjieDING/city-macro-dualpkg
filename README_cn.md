# city-macro-data

`city-macro-data` 是一个用于分发中国城市宏观经济数据的 Python package。  
安装后可直接读取内置数据集、查看元数据，并进行基础数据校验，适合教学、课程作业和实证分析的快速起步。

## 包含内容

- 标准化后的城市面板数据（CSV）
- 对应元数据（JSON），包含数据版本、构建时间、字段信息等
- 简洁稳定的 Python 调用接口

## 安装方式

从 PyPI 安装（发布后可用）

```bash
pip install city-macro-data
```

## 快速使用

```python
from city_macro_data import load_data, get_metadata, data_version, validate_data

df = load_data()
meta = get_metadata()

print(df.shape)
print(data_version())
print(meta.keys())

# 基础校验（非空、必需列等）
validate_data()
```

## 主要 API

- `load_data()`：读取数据并返回 `pandas.DataFrame`
- `get_metadata()`：读取并返回元数据字典
- `data_version()`：返回当前数据版本号
- `validate_data(required_columns=None)`：执行基础数据质量检查

## 数据字段示例

数据集中包含年份、城市、地区生产总值、常住人口、产业结构、财政收支等指标。  
具体字段请以 `load_data()` 返回结果中的列名为准。


