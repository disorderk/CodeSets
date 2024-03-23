import asyncio
import os


async def fileClassify():
    # picEX = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".webp", ".avif"]
    # zipEX = [".zip", ".rar", ".7z", ".tar.gz"]
    # logEX = [".log"]
    # appEX = [".exe"]
    # shellEX = [".bat", ".sh", ".ps1"]
    EX_Dir = {
        "picEX": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".webp", ".avif"],
        "zipEX": [".zip", ".rar", ".7z", ".tar.gz"],
        "logEX": [".log"],
        "appEX": [".exe"],
        "shellEX": [".bat", ".sh", ".ps1"],
        "docuEX": [".txt", ".docx", ".xlsx", "pptx", ".doc", "xls", ".ppt", ".pdf"]
    }
    """
    好吧，昨天整了bat的三版整累了，今天感觉这边简单就发现，好像更复杂(指当前文件夹遍历文件的复杂和效率问题),
    我歇逼了，不干力！
    2024-03-23/21:24:34
    """
