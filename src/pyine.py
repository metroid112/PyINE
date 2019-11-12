from requests_html import HTMLSession

session = HTMLSession()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
url = 'https://www.brou.com.uy/cotizaciones'
response = session.get(url, headers=header)
