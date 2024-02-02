import requests
import urllib.parse

from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def main():
    url = "https://zip5.5432.tw/zip/"
    addr = input("Enter Address: ")
    uri_encoded = urllib.parse.quote(addr)
    full_url = url + uri_encoded
    ua = UserAgent()
    headers = {"User-Agent": ua.chrome}
    res = requests.get(full_url, headers=headers)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        zip_code = soup.find("span", id="zipcode")
        zip_code_6 = soup.find("span", id="zipcode6")
        print(zip_code.string, zip_code_6.string)  # type: ignore
    else:
        print("Unable to find postal code.")


if __name__ == "__main__":
    main()
