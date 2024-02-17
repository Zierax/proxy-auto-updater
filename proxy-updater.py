import requests
import os
from rich.progress import Progress
import subprocess



current_directory = os.getcwd()
path_to_download_proxies = os.path.join(current_directory, "proxies.txt")
path_to_download_proxies_edit = os.path.join(current_directory, "proxies_edit.txt")


result_style = "bold green"
error_style = "bold red"
input_needed = "bold green"

def download_proxies(url, file_name, progress):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KiB
    with open(file_name, 'ab') as f:
        for data in progress.track(response.iter_content(block_size), total=(total_size // block_size) + 1):
            f.write(data)

def install_new_proxies():
    urls = [
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/all.txt",
        "https://raw.githubusercontent.com/casals-ar/proxy-list/main/http",
        "https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks4",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
        "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt"
    ]
    
    if os.path.exists(path_to_download_proxies):
        subprocess.run(f"sudo mv {path_to_download_proxies} proxies_edit.txt ")
    else:
        print("")

        
        
    with Progress() as progress:
        task = progress.add_task("[green]Downloading proxies...", total=len(urls))
        for url in urls:
            response = requests.head(url)
            if response.status_code == 200:
                download_proxies(url, path_to_download_proxies, progress)
                progress.update(task, advance=1)
            else:
                print(f"[{error_style}Failed to download proxies from {url}. Please check your internet connection.{error_style}]")
                break
    print(f"[{input_needed}Proxies updated successfully. You can start now!!{input_needed}]")
    
    
install_new_proxies()

if os.path.exists(path_to_download_proxies):
    os.remove(path_to_download_proxies_edit)
else: 
    subprocess.run([path_to_download_proxies_edit, path_to_download_proxies])



