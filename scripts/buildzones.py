# main.py
import urllib.request
commentChar = "#"
specialnets = ("127.0.0.1", "255.255.255.255", "::1", "f")
defaultRoute = "0.0.0.0"
blocklist = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
zoneHeader = """$TTL 2w
@ IN SOA localhost. root.localhost. (
       2   ; serial 
       2w  ; refresh 
       2w  ; retry 
       2w  ; expiry 
       2w) ; minimum 
    IN NS localhost."""
print(zoneHeader)
with urllib.request.urlopen(blocklist) as f:
 for bytes in f:
 
  line = bytes.decode("utf-8").strip()
  
  if (not line or line.startswith(commentChar) or line.startswith(specialnets)):
   continue
  
  # ignore the ip address; extract the domain
  domain = line[8:]
  
  if domain == defaultRoute:
   continue
  
  print(domain, " CNAME .", sep="")
  print("*.", domain, " CNAME .", sep="")
