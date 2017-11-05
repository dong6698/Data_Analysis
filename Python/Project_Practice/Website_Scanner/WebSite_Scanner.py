from urllib.request import urlopen
from tld import get_tld
import os
import io


def create_Dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def write_File(path, data):
    fw = open(path, 'w')
    fw.write(data)
    fw.close()


def get_Domain_Name(url):
    domain_name = get_tld(url)
    return domain_name


def get_IP_Address(domain_name):
    command = 'host ' + domain_name
    process = os.popen(command)
    results = process.read()
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]


def get_Nmap(option, IP_adress):
    command = 'nmap ' + ' ' + option + ' ' + IP_adress
    process = os.popen(command)
    results = process.read()
    return results


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    request = urlopen(path + 'robots.txt', data=None)
    data = io.TextIOWrapper(request, encoding='utf-8')
    return data.read()


def get_Whois(domain_name):
    command = 'whois ' + domain_name
    process = os.popen(command)
    results = process.read()
    return results


ROOT_DIR = 'Companise'
create_Dir(ROOT_DIR)

def gather_Info(pro_name, url):
    domain_name  = get_Domain_Name(url)
    ip_address = get_IP_Address(domain_name)
    nmap = get_Nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_Whois(domain_name)
    create_Report(pro_name, url, domain_name, ip_address, nmap, robots_txt, whois)


def create_Report(pro_name, url, domain_name, ip_address, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + pro_name + '/'
    create_Dir(project_dir)
    write_File(project_dir + 'full_url.txt', url)
    write_File(project_dir + 'domain_name.txt', domain_name)
    write_File(project_dir + 'ip_address.txt', ip_address)
    write_File(project_dir + 'nmap.txt', nmap)
    write_File(project_dir + 'robots.txt', robots_txt)
    write_File(project_dir + 'whois.txt', whois)

gather_Info('google.ca', 'https://www.google.ca')