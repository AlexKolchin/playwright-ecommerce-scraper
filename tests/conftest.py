import pytest
from typing import Dict


@pytest.fixture
def sample_catalog_html() -> str:
    """Returns a fake HTML page containing 2 product cards for testing."""
    return """
    <html>
        <body>
            <section>
                <ol class="row">
                    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                        <article class="product_pod">
                            <h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the Attic</a></h3>
                            <div class="product_price">
                                <p class="price_color">£51.77</p>
                                <p class="instock availability"><i class="icon-ok"></i>In stock</p>
                            </div>
                            <p class="star-rating Three"></p>
                        </article>
                    </li>
                    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                        <article class="product_pod">
                            <h3><a href="tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>
                            <div class="product_price">
                                <p class="price_color">£53.74</p>
                                <p class="instock availability"><i class="icon-ok"></i>Out of stock</p>
                            </div>
                            <p class="star-rating One"></p>
                        </article>
                    </li>
                </ol>
                <div class="current">Page 1 of 2</div>
                <ul class="pager">
                    <li class="next"><a href="page-2.html">next</a></li>
                </ul>
            </section>
        </body>
    </html>
"""
