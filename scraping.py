# coding: utf-8
import os
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


# プロキシ設定
# os.environ["http_proxy"] = os.environ["pip_proxy"]
# os.environ["https_proxy"] = os.environ["pip_proxy"]

# TODO 画像とCSV保存ディレクトリを作成

# URL
# 制約前
# BASE_URL = "https://www.veterinary-adoption.com/search/view.php?id="
# 制約済(animalクエリは機能していない？dogでもcatでも両方取得できる)
BASE_URL = "https://www.veterinary-adoption.com/search/view.php?key=&animal=cat&established=1&id="

# CSVファイルパス
# 制約前
# OUT_CSV = "./csv/pet.csv"
# 制約済
OUT_CSV = "./csv/pet_established.csv"

cols = [
    "名前",
    "種類",
    "性別",
    "年齢（登録時)",
    "体重",
    "毛色",
    "避妊・去勢",
    "マイクロチップ",
    "ワクチン接種",
    "ひとこと",
    "健康状態",
    "性格",
    "保護された経緯",
]
IMG_PATH = "./img/"


@dataclass
class PageData:
    """URIから取得した情報を入れるクラス
    """

    petid: str  # id
    name: str
    kind: str
    sex: str
    age_at_reg: str
    weight: str
    color: str
    is_breedable: str  # 避妊・去勢
    has_microchip: str  # マイクロチップ
    is_vaccinated: str  # ワクチン接種
    comment: str  # ひとこと
    heath_cond: str  # 健康状態
    personality: str  # 性格
    how_protected: str  # 保護された経緯
    img_path: str  # 写真のディレクトリ


class WhitePageException(Exception):
    """データのない白いページだった時の例外"""

    pass


def get_pagedata(uri, petid):
    """
        Args:
            param1(str): データ取得先URI
            param2(str): ペットID
        Returns:
            PageData
    """
    print("processing: " + petid)
    # リクエスト
    r = requests.get(uri + petid)
    html = r.content

    # htmlパース
    soup = BeautifulSoup(html, "html.parser")

    # プロフィール取得
    sec_tags = soup.find_all("section", {"class": "spec_box02"})
    if not sec_tags:
        raise WhitePageException

    sec_tag1 = sec_tags[0]
    sec_tag2 = sec_tags[1]
    tr_tags1 = sec_tag1.find_all("tr")
    tr_tags2 = sec_tag2.find_all("tr")
    tr_tags = tr_tags1 + tr_tags2

    name, kind, sex, age_at_reg, weight, color = "", "", "", "", "", ""
    is_breedable, has_microchip, is_vaccinated = "", "", ""
    health_cond, personality, how_protected, comment, img_path = "", "", "", "", ""

    for tr_tag in tr_tags:
        cell = tr_tag.find_all(["th", "td"])
        for col in cols:
            if cell[0].get_text() == "名前":
                name = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "種類":
                kind = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "性別":
                sex = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "年齢（登録時）":
                age_at_reg = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "体重":
                weight = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "毛色":
                color = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "避妊・去勢":
                is_breedable = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "マイクロチップ":
                has_microchip = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "ワクチン接種":
                is_vaccinated = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "健康状態":
                health_cond = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "性格":
                personality = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
            elif cell[0].get_text() == "保護された経緯":
                how_protected = (
                    cell[1]
                    .get_text()
                    .replace(" ", "")
                    .replace("　", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("\t", "")
                )
    comment = (
        sec_tag2.find_all("dd")[0]
        .get_text()
        .replace(" ", "")
        .replace("　", "")
        .replace("\r", "")
        .replace("\n", "")
        .replace("\t", "")
    )
    img_tags = soup.find_all("img")
    # 犬猫の写真を取得
    picts = [t["src"] for t in img_tags if "UPLOAD" in str(t["src"])]
    for p in picts:
        img_file = p.split(r"/")[-1]
        IMG_URL = f"https://www.veterinary-adoption.com/UPLOAD/animal/{img_file}"
        r = requests.get(IMG_URL)
        img_path = IMG_PATH + petid + "/"
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        img_full_path = os.path.join(img_path, img_file)
        with open(img_full_path, "wb") as f:
            f.write(r.content)
        # print(IMG_URL)

    pdata = PageData(
        petid,
        name,
        kind,
        sex,
        age_at_reg,
        weight,
        color,
        is_breedable,
        has_microchip,
        is_vaccinated,
        comment,
        health_cond,
        personality,
        how_protected,
        img_path,
    )
    print(pdata.name)
    return pdata


def write_csv(pdata):
    if not os.path.exists(OUT_CSV):
        with open(OUT_CSV, "w") as f:
            f.write(
                '"id",'
                + '"名前",'
                + '"種類",'
                + '"性別",'
                + '"年齢（登録時）",'
                + '"体重",'
                + '"毛色",'
                + '"避妊・去勢",'
                + '"マイクロチップ",'
                + '"ワクチン接種",'
                + '"ひとこと",'
                + '"健康状態",'
                + '"性格",'
                + '"保護された経緯",'
                + '"写真ファイルパス"\n'
            )
    with open(OUT_CSV, "a") as f:
        f.write(
            '"' + pdata.petid + '",'
            '"'
            + pdata.name
            + '",'
            + '"'
            + pdata.kind
            + '",'
            + '"'
            + pdata.sex
            + '",'
            + '"'
            + pdata.age_at_reg
            + '",'
            + '"'
            + pdata.weight
            + '",'
            + '"'
            + pdata.color
            + '",'
            + '"'
            + pdata.is_breedable
            + '",'
            + '"'
            + pdata.has_microchip
            + '",'
            + '"'
            + pdata.is_vaccinated
            + '",'
            + '"'
            + pdata.comment
            + '",'
            + '"'
            + pdata.heath_cond
            + '",'
            + '"'
            + pdata.personality
            + '",'
            + '"'
            + pdata.how_protected
            + '",'
            + '"'
            + pdata.img_path
            + '"\n'
        )


if __name__ == "__main__":
    # petidの範囲指定
    # TODO 1601, 3617, 4532 がsection のクラスがおかしい(制約前)
    # TODO パラメータ指定で範囲指定できるようにする
    for n in range(0, 4639):
        petid = str(n)
        try:
            pdata = get_pagedata(BASE_URL, petid)
        except WhitePageException:
            continue
        write_csv(pdata)
