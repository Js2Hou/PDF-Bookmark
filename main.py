# -*- coding: utf-8 -*-

# 添加PDF书签
import configparser
from pdf_utils import MyPDFHandler, PDFHandleMode as mode


def main():
    cf = configparser.ConfigParser()
    cf.read('info.ini', encoding='utf-8')

    pdf_path = cf.get('info', 'pdf_path')
    bookmark_path = cf.get('info','bookmark_path')
    page_offset = int(cf.get('info', 'page_offset'))
    new_pdf_path = cf.get('info','new_pdf_path')

    pdf_handler = MyPDFHandler(pdf_path, mode=mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt(bookmark_path, page_offset=page_offset)
    pdf_handler.save2file(new_pdf_path)


if __name__ == '__main__':
    main()
