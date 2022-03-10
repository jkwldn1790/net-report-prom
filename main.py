import time
import prometheus_client as prom
import speedtest

DOWNLOAD_SPEED_GUAGE = prom.Gauge('download_speed', 'internet download speed from speedtest in Mbps')

def get_download_speed():
    """
    Pull download speed and post to prometheus guage
    """
    while True:
        s = speedtest.Speedtest()
        download = round(s.download() / 1000000,2)
        DOWNLOAD_SPEED_GUAGE.set(download)
        time.sleep(5)

if __name__ == '__main__':
    prom.start_http_server(3200)
    get_download_speed()