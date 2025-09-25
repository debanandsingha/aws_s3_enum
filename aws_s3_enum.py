import requests
import dns.resolver as dns
import dns.reversename as rev_dns
from urllib.parse import urlparse
import sys

def get_domain(url):
    parsed = urlparse(url)
    return parsed.netloc

def identify_server(url, domain):
    response = requests.get(url)
    server_header = response.headers.get("Server")

    if server_header == "AmazonS3":
        # Identify if the website is hosted on S3
        print("[+] Amazon S3 Detected!")

        # Other Enumeration
        enum(url, domain)

    else:
        print(f"[-] {url} is not hosted on Amazon S3")


def enum(url, domain):
    # identify AWS regional endpoint of the website
    ip = dns.resolve(domain, "A")
    rev_name = rev_dns.from_address(str(ip[0]))
    endpoint = dns.resolve(rev_name, "PTR")
    clean_endpoint = str(endpoint[0]).rstrip(".")
    print(F"[+] Base endpoint found: {clean_endpoint}")

    # identify bucket name
    # 1. identify which DNS server is used
    dns_server = dns.resolve(domain, "NS")
    dns_server_name = str(dns_server[0])

    # find bucket name if AWS Route 53 DNS web serive is used
    if "awsdns" in dns_server_name:
        res = requests.get(f"{url}.{clean_endpoint}")
        if res.status_code == 200:
            print(f"[+] Bucket Name Found: {domain}")
            print(f"[+] Resource Endpoint: {url}.{clean_endpoint}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("[!] Please enter URL (http://example.com)")
    elif "http" not in sys.argv[1]:
        print("[!] Please enter scheme (http:// or https://)")
    else:
        url = sys.argv[1]
        domain = get_domain(url)
        identify_server(url, domain)