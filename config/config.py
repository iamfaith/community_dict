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
"Cookie": "SECKEY_ABVK=IpfTw7F6hqBzBqHg3jjqEqQ1v81JS4dX3ECOAZmwPUqSj0Pw+bnzhZNCGGL2Ytyv2IL1b8UDovlndHga4W5upg%3D%3D; lianjia_uuid=214dbe91-3040-4246-ab20-761a6f52d16a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22%24device_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; crosSdkDT2019DeviceId=-rh6w8k--yidxgw-xylvrsjnn1fizje-rqr5qav7g; _ga=GA1.2.2066249775.1730620469; _gid=GA1.2.489027613.1730620469; ke_uuid=f37f7e520998f0e9f760ac2531f0c462; select_city=440400; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1730620115,1730681795; HMACCOUNT=D875B101FB3896AF; lianjia_ssid=38b134e9-76c3-40ca-ba01-0959936d6dfe; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; __xsptplusUT_788=1; __xsptplus788=788.2.1730685489.1730686663.3%234%7C%7C%7C%7C%7C%23%23%23; hip=BIcbHBMshn4vzgvxXyb1D-kjN6oN2fkV1p-M7SB8-sTiKgrHF5VwMqYXznV9NfsCS38pfkhdbWT0FPKJdILuFN7UYRfie-3tMVsXSTufdxNvjgZfsxEuj55sfGz27xiS_eN2K44dxOBFAGX0le13tNvyy1r6q-UNW3G8g2nc5HiXAigDu20%3D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZTA5OTA2N2NlOTA4NWQzZjYwYmExNzM5YjdmOTA0YTJjYmYxZDhlOWJiNGY0MThlNjA0NmYxMTMwMmRkNzdjZGJiMzQ1NTljZDQyOWIxZWExYmViMDVmMGYzNTI3MTBhNzM4MTllMThhZjAzN2JlNWUzM2RlMWM4ZjViZTRiNmY5ODZjYTJiZTkyMGI4Y2RlNGNjOGNhMWQwZDBlYTU5OGM1YTk1OTNhZGQ0OWQ0ZDI4MTY3MjNkOGFhM2FkZmZjOWQzNzg3MzFiN2MyNjc5ODI2NDhjNzYwZjEwMGViYjBjNjc3NGY1YzNmN2Y5MGVlMDcwMDZkMTBhODVjMDAzMDc3Yzc1ZjIzNWViNjNhM2FhZWYzNGEwOGVkNWExMWZjZmFiN2MwNjg2YTYzNWMwMTUyNTJiZDZmOTE3MjE4ZjBcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiMGY3ZjExZjJcIn0iLCJyIjoiaHR0cHM6Ly96aC5rZS5jb20veGlhb3F1LzYzMjAwMzM2OTM4ODA4NzIvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1730686854",
"Host": "zh.ke.com",
"Pragma": "no-cache",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
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
