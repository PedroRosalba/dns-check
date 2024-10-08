import dns.resolver
import socket

def check_spf_record(domain):
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for record in txt_records:
            spf_record = str(record)
            if "v=spf1" in spf_record:
                ip_addresses = [part for part in spf_record.split() if part.startswith("ip4:")]
                for ip in ip_addresses:
                    ip_address = ip.split(":")[1]
                    
                    try:
                        host_name = socket.gethostbyaddr(ip_address)[0]
                        print(f"IP {ip_address} resolves to: {host_name}")
                        
                        if "university" in host_name or "college" in host_name:
                            return True
                    except socket.herror:
                        print(f"Unable to resolve IP {ip_address} to a host.")
                        continue 
        return False 
    except dns.resolver.NoAnswer:
        print(f'No TXT records found for {domain}.')
        return False
    except dns.resolver.NXDOMAIN:
        print(f'The domain {domain} does not exist.')
        return False
    except Exception as e:
        print(f'Error fetching SPF records: {e}')
        return False

print(check_spf_record("ufrj.br"))
