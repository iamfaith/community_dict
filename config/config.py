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
"Cookie": "lianjia_uuid=214dbe91-3040-4246-ab20-761a6f52d16a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22%24device_id%22%3A%22192f0ff45ff88-072e17ed8fd34f-4c657b58-1569800-192f0ff4600250c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; crosSdkDT2019DeviceId=-rh6w8k--yidxgw-xylvrsjnn1fizje-rqr5qav7g; _ga=GA1.2.2066249775.1730620469; _gid=GA1.2.489027613.1730620469; _jzqckmp=1; ke_uuid=f37f7e520998f0e9f760ac2531f0c462; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1730620115,1730681795; HMACCOUNT=D875B101FB3896AF; lianjia_ssid=38b134e9-76c3-40ca-ba01-0959936d6dfe; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; _qzjc=1; _jzqa=1.1564590908711824000.1730620488.1730620488.1730685490.2; _jzqc=1; _jzqx=1.1730620488.1730685490.1.jzqsr=zh%2Eke%2Ecom|jzqct=/.-; hip=BIcbHBMshn4vzgvxXyb1D-kjN6oN2fkV1p-M7SB8-sTiKgrHF5VwMqYXznV9NfsCS38pfkhdbWT0FPKJdILuFN7UYRfie-3tMVsXSTufdxNvjgZfsxEuj55sfGz27xiS_eN2K44dxOBFAGX0le13tNvyy1r6q-UNW3G8g2nc5HiXAigDu20%3D; __xsptplus788=788.2.1730685489.1730687464.4%234%7C%7C%7C%7C%7C%23%23%23; digData=%7B%22key%22%3A%22loupan_index%22%7D; select_city=440400; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1730689492; lj_newh_session=eyJpdiI6ImFwNTdxUWlZRFVGUkJ1cVlXakJySHc9PSIsInZhbHVlIjoiZjhWN0t3bytkSlZYNVQ0Q2Z0dlNwY1wvZHdyQzhyakJXazdtMG9nVkRsbXhGdXZVSTRMaHRZSHJPMEJoQkNEXC8zRFZmM1RBdGJOdkVBT2VOUjJyRUt6Zz09IiwibWFjIjoiZTBlNWMwMzhlZDM2NWRkYmVmOWIxN2FiMTFkMWVjYmM3ZjMyYjc3ODc3MTQ3Yjk0M2JkMTg0ZmVkMmFlNTc5MiJ9; _jzqb=1.7.10.1730685490.1; _qzja=1.1158472583.1730620487762.1730620487762.1730685489972.1730688755306.1730689492998.0.0.0.14.2; _qzjb=1.1730685489972.7.0.0.0; _qzjto=7.1.0; srcid=eyJ0IjoiXCJ7XFxcImRhdGFcXFwiOlxcXCJlMDk5MDY3Y2U5MDg1ZDNmNjBiYTE3MzliN2Y5MDRhMmNiZjFkOGU5YmI0ZjQxOGU2MDQ2ZjExMzAyZGQ3N2NkYmIzNDU1OWNkNDI5YjFlYTFiZWIwNWYwZjM1MjcxMGE3MzgxOWUxOGFmMDM3YmU1ZTMzZGUxYzhmNWJlNGI2Zjk4NmNhMmJlOTIwYjhjZGU0Y2M4Y2ExZDBkMGVhNTk4YzVhOTU5M2FkZDQ5ZDRkMjgxNjcyM2Q4YWEzYWRmZmNiZGM3NTNjOGQyMDkxMDYxOThkMTM2NTI0NDFjNDdmMjJlZGNjNzJhOTNkMTFkOTNlMTE5YWMyOGFkZmY2NWE1ZmIxMDhiZTFiOGIwYjdiM2MyODUwMWYwYmZlNmM4ODI3YmYxYTJjMzY5MmUzOTgzZDQ4MWQ1MDA1ZTM5Nzg0MlxcXCIsXFxcImtleV9pZFxcXCI6XFxcIjFcXFwiLFxcXCJzaWduXFxcIjpcXFwiNmY2ZDFiNjBcXFwifVwiIiwiciI6Imh0dHBzOi8vemguZmFuZy5rZS5jb20vbG91cGFuL3BnMS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
"Host": "zh.fang.ke.com",
"Pragma": "no-cache",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
}

# 每次采集时间间隔
time_interval = 5

# 小区详情获取数量后保存文件
save_file_number = 1
