def download_aeta_data_to_file(
    data_type, date_range_str, save_to, token, oversea=False
):
    assert data_type in ("EM", "GA", "EM&GA", "EC")
    import requests

    oversea = "true" if oversea else "false"
    url = "https://api.competition.aeta.cn/downloadByToken"
    params = {
        "dataType": data_type,
        "date": date_range_str,
        "oversea": oversea,
    }
    resp = requests.get(url, params=params, headers={"Authorization": token})
    resp.raise_for_status()
    with open(save_to, "wb") as fd:
        for chunk in resp.iter_content(chunk_size=128):
            fd.write(chunk)


download_aeta_data_to_file(
    "EM&GA",
    "20210307-20210313",
    "./20210307-20210313.zip",
    "aea80c07f02045029c0908ba42294c2d",
)
