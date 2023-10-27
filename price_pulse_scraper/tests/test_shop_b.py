import pytest
from scrapy.http import HtmlResponse
from price_pulse_scraper.spiders.shop_b import ShopBSpider

@pytest.fixture()
def spider():
    """
    Fixture to create an instance of ShopBSpider.
    """
    return ShopBSpider()

def test_parse(spider):
    """
    Test the parsing of product information from an HTML response.
    """
    url = "https://www.idealo.fr/prix/202069623/apple-iphone-14-pro-max.html"
    body = """
    <a class="productVariants-listItemWrapper" href="/prix/202093749/apple-iphone-14-pro-max-256-go-noir-sideral.html" 
    rel="" data-update-query="" data-gtm-event="productstage.click" data-gtm-payload="{&quot;event_category&quot;
    :&quot;productstage&quot;,&quot;event_action&quot;:&quot;inline.click&quot;,&quot;event_label&quot;
    :&quot;variants&quot;}">
        <div class="productVariants-listItemWrapperImageHolder">
            <img class="productVariants-listItemWrapperImage" 
            src="//cdn.idealo.com/folder/Product/202093/7/202093749/s4_produktbild_mittelgross/
            apple-iphone-14-pro-max-256-go-noir-sideral.jpg" 
            alt="Apple iPhone 14 Pro Max 256 Go noir sidéral">
            <div class="sales-badge-container">
                <span class="productVariants-listItemWrapperBadge">
                        Meilleure vente
                </span>
            </div>
        </div>
        <div class="productVariants-listItemWrapperDescription">
            <div class="price">
                <span class="priceFrom">à partir de&nbsp;</span><span class="">1239,<span class="priceSup">&nbsp;00
                </span></span>&nbsp;€</div>
                <span class="productVariants-listItemWrapperTitle-short">
                    256 Go noir sidéral
                </span>
            </div>
    </a>
    """
    response = HtmlResponse(url=url, body=body.encode('utf-8'), request=next(spider.start_requests()))

    results = list(spider.parse(response))

    expected = [
        {"link": "https://www.idealo.fr//prix/202093749/apple-iphone-14-pro-max-256-go-noir-sideral.html",
         "series": "iPhone 14 Pro Max 256 Go noir sidéral", "price": 1239.00}
    ]
