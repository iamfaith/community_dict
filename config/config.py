# from config import headers


'''
全局配置
'''

# 通用headers
universal_headers = {

"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Cookie": "lianjia_ssid=2cce8233-b7a6-4502-afea-55e363fb0a66; lianjia_uuid=214dbe91-3040-4246-ab20-761a6f52d16a; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22%24device_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1730620115; HMACCOUNT=D875B101FB3896AF; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; crosSdkDT2019DeviceId=-rh6w8k--yidxgw-xylvrsjnn1fizje-rqr5qav7g; _ga=GA1.2.2066249775.1730620469; _gid=GA1.2.489027613.1730620469; _jzqa=1.1564590908711824000.1730620488.1730620488.1730620488.1; _jzqc=1; _jzqx=1.1730620488.1730620488.1.jzqsr=zh%2Eke%2Ecom|jzqct=/.-; _jzqckmp=1; _qzjc=1; ke_uuid=f37f7e520998f0e9f760ac2531f0c462; search_position=sug_click; digData=%7B%22key%22%3A%22loupan_view%22%7D; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1730620621; _qzja=1.1158472583.1730620487762.1730620487762.1730620487762.1730620602754.1730620621057.0.0.0.6.1; _qzjb=1.1730620487762.6.0.0.0; _qzjto=6.1.0; _jzqb=1.6.10.1730620488.1; srcid=eyJ0IjoiXCJ7XFxcImRhdGFcXFwiOlxcXCJlMDk5MDY3Y2U5MDg1ZDNmNjBiYTE3MzliN2Y5MDRhMmNiZjFkOGU5YmI0ZjQxOGU2MDQ2ZjExMzAyZGQ3N2NkMzk3M2UyYWFmZWE0MDYzYzU0Y2NjNTFmOGMyZGNhYzZjYTk0ODAwMzUxNGE3N2I3YjExNTM1YzhmYWY0MDJhZDc4NDkxOTU1OTkxZDJkODY0ZjZmN2I3ZDBhZmIwMmQwMmQ1NDI2OGE5YjdlNjJmNDlhZjFlYzRmZWQ4ZDY0YzYwYzMyOWQ5MjliNWNmOGU0ZTdkMTkwN2Q4ZWMzZDI2OGMxNWFmNWEyMTIzN2M1YjZmOTRmOGYwZDIwNTBmZmM2Nzk5ZDUxMzZlYjFmZGExMThkNGM3OWQ4NmQ5YTY2ZDA4NGRmMzIxMDc3ODc4NjdjYjdhNWUzN2VjMWIwNDUyMVxcXCIsXFxcImtleV9pZFxcXCI6XFxcIjFcXFwiLFxcXCJzaWduXFxcIjpcXFwiZTk1NmM0OWJcXFwifVwiIiwiciI6Imh0dHBzOi8vemguZmFuZy5rZS5jb20vbG91cGFuL3BfemdxY2h5Ym5wZmUvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; select_city=440400; lj_newh_session=eyJpdiI6ImYxTDQ1NG9vOEVUXC85QjVIXC9TUGpGdz09IiwidmFsdWUiOiI4QW11K094eDh0Z1BBN1FKZmFLYW1DMWg4S3diM2ZPQkN4MFVLTUJCdkNrWmdheW9JakdcL3RLQnMrdGhmamxDamtVVk5pS2I3ZlhmbFRGTEN0d0F0TXc9PSIsIm1hYyI6ImYwZTUzOGJhYzFjZmUyNGU4MjEzNjBjNjNjZTcyNWEwMTM0NDllNjQxOTViYzcyYWU0YzNjNjE2YTJiZTU4MTgifQ%3D%3D; __xsptplus788=788.1.1730620477.1730620621.6%234%7C%7C%7C%7C%7C%23%23%23",
"Host": "zh.fang.ke.com",
"Pragma": "no-cache",
"Referer": "https://zh.ke.com/",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}


universal_headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Cookie": "SECKEY_ABVK=IpfTw7F6hqBzBqHg3jjqEqQ1v81JS4dX3ECOAZmwPUpWv+VwBUiVg0MmiFq6MGpkY6eCKN8XtTCqB9y0MEAPyg%3D%3D; lianjia_uuid=214dbe91-3040-4246-ab20-761a6f52d16a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22%24device_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; crosSdkDT2019DeviceId=-rh6w8k--yidxgw-xylvrsjnn1fizje-rqr5qav7g; _ga=GA1.2.2066249775.1730620469; _gid=GA1.2.489027613.1730620469; ke_uuid=f37f7e520998f0e9f760ac2531f0c462; select_city=440400; __xsptplus788=788.1.1730620477.1730621599.7%234%7C%7C%7C%7C%7C%23%23%23; lianjia_ssid=835d7be3-3745-482a-9254-5a7fbcc3c929; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1730620115,1730681795; HMACCOUNT=D875B101FB3896AF; hip=odi1zXzohs81BXtagKygT0bTiCkDjKIGshuRQWLHWoewbqJdebB4cWqzriOuO67M0lo4N5p_3F7nrWcdgaota2XAsq8p5wacVK0ihcdfQZKoOCZfaBW8iTWXei8F8PdFDXtWtgi9MB1hU2B5-zv3-AmgGT1XOxErkTQlx_adZhv11qsxtiw%3D; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1730682317; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZTA5OTA2N2NlOTA4NWQzZjYwYmExNzM5YjdmOTA0YTJjYmYxZDhlOWJiNGY0MThlNjA0NmYxMTMwMmRkNzdjZGJiMzQ1NTljZDQyOWIxZWExYmViMDVmMGYzNTI3MTBhNzM4MTllMThhZjAzN2JlNWUzM2RlMWM4ZjViZTRiNmY5ODZjYTJiZTkyMGI4Y2RlNGNjOGNhMWQwZDBlYTU5OGM1YTk1OTNhZGQ0OWQ0ZDI4MTY3MjNkOGFhM2FkZmZjNTU1ZTA4M2Q4MjYwYzMwNzgwYjU1MzViM2JhMjk4M2M2MTI4ZWYxNDA3N2MxMGJlOGEwZjA1NjQ3MGVjN2UwMTg4MDk1NmU0NzQ2ZGFlODU3ZGUyNDQzNmUwZTQwNWY1NmM4ZGJmYzgxZTIxYzZjZWZkZGZkNDI3NzRhNGRhOWVcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiYTc4MzUzMTdcIn0iLCJyIjoiaHR0cHM6Ly96aC5rZS5jb20veGlhb3F1LzYzMjAwNDE1NzcxNjM1MTkvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=",
"Host": "zh.ke.com",
"Pragma": "no-cache",
"Referer": "https://hip.ke.com/",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
"sec-ch-ua": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows"
}

# 每次采集时间间隔
time_interval = 5

# 小区详情获取数量后保存文件
save_file_number = 2
