# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2024/3/17 11:19
# description: XXX

import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.baidu.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("百度一下，你就知道"))
