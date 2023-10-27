import pytest
from scrapy.http import HtmlResponse
from price_pulse_scraper.spiders.shop_a import ShopASpider

@pytest.fixture
def spider():
    """
    Fixture to create an instance of ShopASpider.
    """
    return ShopASpider()

def test_parse(spider):
    """
    Test the parsing of product information from an HTML response.
    """
    url = 'https://www.pixmania.com/fr/fr/smartphones-iphone-14-pro-max.html'
    body = """
    <a href="/fr/fr/iphone-14-pro-max-256-go-argent-129973.html" title="iPhone 14 Pro Max 256 Go, 
    Argent" class="producttile" datamobileid="" datagtm-title="iPhone 14 Pro Max 256 Go, Argent" datagtm-price="1290" 
    datagtm-brand="Apple" datagtm-category="Smartphones" datagtm-pos="1">
        <div class="bloc-info">
            <div class="pt-title-product  order-1 d-flex flex-column">
                <h2 class="reconditionne  order-2">
                    iPhone 14 Pro Max 256 Go, Argent<br>
                </h2>
                <div class="detail order-1">
                    <span class="uppercase pixel-10">Apple</span>
                </div>
            </div>
        </div>
        <div class="prdt-tile-price-line order-2  align-items-end d-flex flex-row">
            <div class="mr-auto">
                <div class="producttile-price price  black">1290,00€</div>
            </div>
        </div>    
    </a>
    """
    response = HtmlResponse(url=url, body=body.encode('utf-8'), request=next(spider.start_requests()))

    results = list(spider.parse(response))

    expected = [
        {"link": "https://www.pixmania.com/fr/fr/iphone-14-pro-max-256-go-argent-129973.html",
         "series": "iPhone 14 Pro Max 256 Go, Argent", "price": 1290.0}
    ]

    for i, item in enumerate(expected):
        assert results[i]['link'] == item['link']
        assert results[i]['series'] == item['series']
        assert results[i]['price'] == item['price']

    assert len(results) == len(expected)
