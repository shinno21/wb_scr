# coding: utf-8
# import os
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


# プロキシ設定
# os.environ["http_proxy"] = os.environ["pip_proxy"]
# os.environ["https_proxy"] = os.environ["pip_proxy"]

# TODO 画像とCSV保存ディレクトリを作成

URL = "https://www.veterinary-adoption.com/search/view.php?id=4223"


@dataclass
class PageData:
    """URIから取得した情報を入れるクラス
    """

    uri: str
    name: str
    kind: str
    sex: str
    age_at_reg: int
    weight: float
    color: str
    is_breedable: bool  # 避妊・去勢
    has_microchip: bool  # マイクロチップ
    is_vaccinated: bool  # ワクチン接種
    pict_path: str


def get_pagedata(uri):
    """
        Args:
            param1(str): データ取得先URI
        Returns:
            PageData
    """
    # リクエスト
    r = requests.get(uri)
    html = r.content

    # htmlパース
    soup = BeautifulSoup(html, "html.parser")

    # プロフィール取得
    table_tags = soup.find_all("table")

    img_tags = soup.find_all("img")

    # 犬猫の写真を取得
    picts = [t["src"] for t in img_tags if "UPLOAD" in str(t["src"])]
    for p in picts:
        img_src = p.split(r"/")[-1]
        IMG_URL = f"https://www.veterinary-adoption.com/UPLOAD/animal/{img_src}"
        r = requests.get(IMG_URL)
        with open(img_src, "wb") as file:
            file.write(r.content)
        print(IMG_URL)


if __name__ == "__main__":
    # htmlリクエスト
    r = requests.get(URL)
    html = r.content

    # htmlパース
    soup = BeautifulSoup(html, "html.parser")
    img_tags = soup.find_all("img")

    # 犬猫の写真を取得
    picts = [t["src"] for t in img_tags if "UPLOAD" in str(t["src"])]
    for p in picts:
        img_src = p.split(r"/")[-1]
        IMG_URL = f"https://www.veterinary-adoption.com/UPLOAD/animal/{img_src}"
        r = requests.get(IMG_URL)
        with open(img_src, "wb") as file:
            file.write(r.content)
        print(IMG_URL)
    exit(0)
