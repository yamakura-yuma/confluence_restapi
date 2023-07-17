#!/usr/bin/python
# coding: utf-8

import sys
from pprint import pprint
import logging
from atlassian import Confluence

from env_reader import EnvReader
from report import Report
from text_type import TEXT_TYPE

ENV_CONFLUENCE_DOMAIN = "CONFLUENCE_DOMAIN"
ENV_CONFLUENCE_USER_NAME = "CONFLUENCE_USER_NAME"
ENV_CONFLUENCE_API_TOKEN = "CONFLUENCE_API_TOKEN"

log = logging.getLogger(__name__)

if __name__ == '__main__':
    env_reader: EnvReader = EnvReader()
    domain: str|None = env_reader.get(ENV_CONFLUENCE_DOMAIN)
    username: str|None = env_reader.get(ENV_CONFLUENCE_USER_NAME)
    api_token: str|None = env_reader.get(ENV_CONFLUENCE_API_TOKEN)
    
    if domain is None:
        log.debug(f"環境変数 {ENV_CONFLUENCE_DOMAIN} が設定されていません。設定してください。")
        sys.exit(1)

    if username is None:
        log.debug(f"環境変数 {ENV_CONFLUENCE_USER_NAME} が設定されていません。設定してください。")
        sys.exit(1)

    if api_token is None:
        log.debug(f"環境変数 {ENV_CONFLUENCE_API_TOKEN} が設定されていません。設定してください。")
        sys.exit(1)

    confluence: Confluence = Confluence(
        url=domain,
        username=username,
        password=api_token,
        cloud=True
        )

    confluence.allow_redirects = False

    # res_spaces: dict|None = confluence.get_all_spaces()
    # for __res_space in res_spaces["results"]:
    #     # pprint(__res_space.keys())
    #     res_space = confluence.get_space(__res_space["key"], expand="permissions,settings")
    #     # pprint(res_space.keys())

    res_all_page = confluence.get_all_pages_from_space("test")
    for __res_all_page in res_all_page:
        # pprint(__res_all_page["id"])
        expand = ""
        expand += "restrictions.read.restrictions.group,"
        expand += "restrictions.read.restrictions.user,"
        res_page = confluence.get_page_by_id(page_id=__res_all_page["id"], expand=expand)
        # pprint(res_page.keys())
        # pprint(res_page["restrictions"])

    report = Report()
    html_report = report.make(text_type=TEXT_TYPE.HTML)

    # Create the page
    space = "test"
    title = "markdown→html→confluence変換"
    body = html_report
    status = confluence.update_or_create(
        parent_id = "33303",
        title = title,
        body = body,
    )

