import http.client

conn = http.client.HTTPSConnection("sssinstagram.com")
headers = {"content-type": "application/json"}


def main(reelLink):
    payload = {
        "url": reelLink,
        "ts": 1742551623780,
        "_ts": 1742202103562,
        "_tsc": 0,
        "_s": "9334c0eab80c2e4d2f1fa34c83081e87f32c2b2496e82f1cbfc2866fe1a84e67",
    }
    conn.request("POST", "/api/convert", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    return data




# import urllib.parse
# import re
# url = "https://media.sssinstagram.com/get?__sig=kdp71CcT2w5UkccP8c8UwA&__expires=1742553678&uri=https%3A%2F%2Finstagram.fbkk29-8.fna.fbcdn.net%2Fo1%2Fv%2Ft16%2Ff2%2Fm86%2FAQM-VZGO75HhrycJpRNIWopgWYw-pLkGsPRnN1t3yWaPzqsDAN3EpgYR8gWzjYocRe75csyWZ25R1WPsjMIr5WktkwJ3twDQ-kxpmTU.mp4%3Fstp%3Ddst-mp4%26efg%3DeyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2xpcHMuYzIuNzIwLmJhc2VsaW5lIn0%26_nc_cat%3D105%26vs%3D994286562090475_4280021620%26_nc_vs%3DHBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC81NjQxNDVGNDBEM0RGQjFDQTAxQTExNzgyN0E1QzY5OV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dIbzl5eHpIQXFOQV91Y0JBSm13YWtkZmdsODlicV9FQUFBRhUCAsgBACgAGAAbABUAACbk9bSs6NmeQBUCKAJDMywXQEHu2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HAA%253D%253D%26_nc_rid%3Dc99d5c1e32%26ccb%3D9-4%26oh%3D00_AYGPAvAsg0rcuGpu6Fnnzny1darEywKGEui229EnKwW5Tg%26oe%3D67DDF944%26_nc_sid%3Dd885a2%26dl%3D1&filename=Tag%20that%20betting%20raja%20%23viral%20%23reels%20%23explore%20%23trending%20%23india%20%23vijayawada%20%23ipl%20%23rcb%20%23csk%20%23kkr%20%23srh%20%23betting%20%23cricket%20%23share%20%23ipl2025%20%23dhoni%20%23viratkohli%20%23bramhanandam.mp4&ua=-&referer=https%3A%2F%2Fwww.instagram.com%2F"
# match = re.search(r'(?<=uri=)https%3A%2F%2F[^&]+', url)
# if match:
#     urlDe = match.group(0)
#     decoded_url = urllib.parse.unquote(urlDe)
#     print(decoded_url)
