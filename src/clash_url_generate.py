import sqlite3
import base64
import urllib.parse

# Step 1: 读取 SQLite 数据库中的代理配置信息
def read_proxy_config():
    # 连接到 SQLite 数据库
    # conn = sqlite3.connect('C:\etc\x-ui\x-ui.db')
    conn = sqlite3.connect('C:/etc/x-ui/x-ui.db')
    cursor = conn.cursor()

    # 从数据库中读取代理配置信息
    cursor.execute('SELECT * FROM inbounds')
    proxies = cursor.fetchall()

    # 关闭数据库连接
    conn.close()

    # 返回代理配置信息
    return proxies

# Step 2: 将代理配置信息转换为 Clash 配置文件格式
def generate_clash_config(proxies):
    clash_config = {'proxies': []}

    for proxy in proxies:
        # 将代理配置信息转换为 Clash 配置文件格式
        clash_proxy = {
            'name': proxy[0],
            'type': 'http' if proxy[1] == 'HTTP' else 'socks5',
            'server': proxy[2],
            'port': proxy[3],
            'username': proxy[4],
            'password': proxy[5]
        }

        # 添加代理到 Clash 配置文件
        clash_config['proxies'].append(clash_proxy)

    # 返回 Clash 配置文件
    return clash_config

# Step 3: 使用 Clash 配置文件生成订阅地址
def generate_clash_subscription(clash_config):
    # 将 Clash 配置文件编码为 Base64 字符串
    clash_config_str = str(clash_config).replace('\'', '\"')
    clash_config_b64 = base64.urlsafe_b64encode(clash_config_str.encode()).decode()

    # 将 Base64 字符串 URL 编码
    clash_subscription = 'clash://' + urllib.parse.quote(clash_config_b64)

    # 返回 Clash 订阅地址
    return clash_subscription

# 将以上三个步骤组合在一起
def main():
    proxies = read_proxy_config()
    # clash_config = generate_clash_config(proxies)
    # clash_subscription = generate_clash_subscription(clash_config)

    # 输出生成的 Clash 订阅地址
    # print(clash_subscription)
    print(proxies)

# 运行主程序
if __name__ == '__main__':
    main()
