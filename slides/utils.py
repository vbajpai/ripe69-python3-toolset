import requests

def get_json_from_url(url):
    try: res = requests.get(url)
    except Exception as e: print(e)
    else:
        try: res_json = res.json()
        except Exception as e: print(e)
        else: return res_json

def get_total_registered_atlas_probes():
    base_uri = 'https://atlas.ripe.net'
    url = '%s/api/v1/probe'%base_uri
    try: res = get_json_from_url(url)
    except Exception as e: print(e)
    else:
        try:total_registered = res['meta']['total_count']
        except Exception as e: print(e)
        else: return total_registered

def asn_from_endpoint(endpoint):
    asn = holder = None
    base_uri = 'https://stat.ripe.net'
    url = '%s/data/prefix-overview/data.json'%base_uri
    p = {'resource' : endpoint}
    try: res = requests.get(url, params = p)
    except Exception as e: print(e)
    else:
        try:
            asn = res.json()['data']['asns'][0]['asn']
            holder = res.json()['data']['asns'][0]['holder']
        except Exception as e: print(e)
    return asn, holder

def holder_from_asn(asn):
    holder = None
    base_uri = 'https://stat.ripe.net'
    url = '%s/data/as-overview/data.json'%base_uri
    p = {'resource' : asn}
    try: res = requests.get(url, params=p)
    except Exception as e: print(e)
    else:
      try: holder = res.json()['data']['holder']
      except Exception as e: print(e)
    return holder

def create_pretty_node_names(holder, asn):
    firstname = holder.split('-')[0].split(' ')[0]
    if 'AS' in str(asn): nodename = '%s (%s)'%(firstname, asn)
    else: nodename = '%s (AS%s)'%(firstname, asn)
    return nodename