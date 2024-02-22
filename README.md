# click-template

[`click`](https://click.palletsprojects.com/) 是用于创建命令行工具的 Python 包。

`click-template` 是一个 `click` 的模板项目，用于快速创建命令行工具。另外，`click-template` 模板支持了命令缩写特性，即如果命令有唯一的前缀，那么可以使用缩写来代替命令，例如 `click-template h` 代替 `click-template hello`。

## 目录结构

```
.
├── click_template
│   ├── cli.py
│   ├── commands  # 存放命令的目录
│   │   ├── hello.py  # hello 命令
│   │   ├── __init__.py
│   ├── __init__.py
│   └── utils
│       ├── __init__.py
├── requirements.txt  # 依赖的第三方库
└── setup.py
```

## 体验 click-template

### 安装

```bash
git clone git@github.com:zhouzaida/click-template.git
cd click-template
pip install -e . -v
```

### 使用

- 查看提供的命令

  ```
  click-template --help
  ```

- 执行 hello 命令

  ```
  click-template hello tom
  ```

- 执行 hello 命令的缩写

  ```
  click-template h tom
  ```

## 实现自己的命令行工具

- 将 `click-template` clone 到本地

  ```bash
  git clone git@github.com:zhouzaida/click-template.git
  cd click-template
  ```

- 将项目中的 `click-template` 和 `click_template` 替换为自己的命令行工具名称

- 在 `commands` 目录下添加自己的命令并在 `commands` 的 `__init__.py` 中导入

- 安装

  ```bash
  pip install -e .v
  ```

即可体验自己的命令行工具。
