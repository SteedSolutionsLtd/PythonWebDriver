from api.request_builder import RequestBuilder

def test_api():
    requestBuilder = RequestBuilder('https://httpbin.org/post')

    resp = requestBuilder.postRequest()

    print(resp.status_code)
    assert resp.status_code == 200