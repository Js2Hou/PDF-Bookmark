# PDF-Bookmark

> 网络下载的pdf书籍很多都没有大纲信息，当然可以使用Adobe Acrobat Reader软件添加目录结构，但当书籍章节很多时这样颇为耗时。为解决此痛点，本项目可半自动给pdf书籍添加目录大纲结构。

## 功能

本项目实现了给pdf书籍添加书签的功能。

## 使用步骤

1. 安装依赖库 `pip install -r requirements.txt
`
2. 制作pdf目录页码索引.txt文件

    格式：[缩进]@[章节标题]@[页码]，
    样例如下

    ```python
    #@content@-7
    #@1 Introduction@1
    ##@1.1 A Universal Task: Pursuit of Low-Dimensionality@1
    #@2 Sparse Signal Models@33
    ```

    其中`#`数目表示层级，如`#`表示一级标题，`##`表示二级标题；`@`为分隔符，第一个`@`后为章节名称，第二个`@`后为页码数。

    **注意**：可通过QQ ocr辅助制作该文件，后面会介绍

3. 修改配置文件info.ini

    ```python
    [info]
    pdf_path = C:\Users\ahou\Desktop\book.pdf
    bookmark_path = C:\Users\ahou\Desktop\bookmark.txt
    page_offset = 26
    new_pdf_path = C:\Users\ahou\Desktop\new_book.pdf
    ```

    `bookmark_path` 为步骤1中生成的文件路径；`pdf_path`和`new_pdf_path`分别为待处理pdf文件和处理后新文件保存路径；`page_offset`为显示页码和实际页码差。书籍一般从正文开始记页，但在该页前面可能会有目录、前言、封面等信息，这部分页码数即为`page_offset`。

4. 运行`main.py`文件

## 使用QQ OCR辅助制作书签索引

可以使用qq功能键ctrl+alt+o OCR识别pdf目录，生成对应文本。然后在notepad++中编辑格式，使用正则表达式进行快捷替换，常用替换规则如下：

1. 替换页码前的换行回车为@：`([a-z])\r\n([1-9][0-9])  -->  \1@\2`

    ```python
    # before
    chapter 1 Introduction
    50
    
    # after
    chapter 1 Introduction@50
    ```

2. 替换目录名称前的换行回车为空格：`(\.[1-9])\r\n([A-Z])  -->  \1 \2`

    ```python
    # before
    1.1.1
    Background
    
    # after
    1.1.1 Background
    ```

3. 替换一级标题后面的换行回车为空格：`(\r\n[1-9]+)\r\n([A-Z])  --->  \1 \2`

    ```python
    # before
    1
    Background
    
    # after
    1 Background
    ```

4. 标题添加缩进
   - 一级标题：`\r\n([1-9]+ [A-Z])  --->  \r\n#@\1`
   - 二级标题：`\r\n([0-9]+\.[0-9]+ [A-Z])  --->  \r\n##@\1`
   - 三级标题：`\r\n([0-9]+\.[0-9]+\.[0-9]+ [A-Z])  --->  \r\n###@\1`
   - 剩余无缩进的添加一级缩进
