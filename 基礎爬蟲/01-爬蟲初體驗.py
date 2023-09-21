import requests as req
url = 'https://tw.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAM04zois-eqg-Cckpk4guGrJ4z4IZlfTL0vAmGvh7p5GCDqsVVR89bDjyyIJts-MPtr960Xm19eM138iD0N7jR72xeileIzvqeVVhsyR-t15VkgWmMF4hNoOCTWQ7bS1eEyixAgzOZ1f8TNzfUuE7ZXi64oXcpDDjQuL7LtmWtbs'
r =  req.get(url)
print(r.text)
print(r.headers)