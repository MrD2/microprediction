from microprediction.simplecrawler import SimpleCrawler
import numpy as np

# from vendor import VendorModel

# Pseudo-code for Automated time series prediction algorithms.
# Hack this example to benchmark open source of vendor libraries.


class MockFastVendorModel(object):

    def __init__(self):
        pass

    def fit(self, lagged_values: [float]):
        self.mu = 0.5 * (lagged_values[0] + lagged_values[1])
        self.sigma = 1.0

    def invcdf(self, p: float) -> float:
        """
             p   float
             returns:
        """
        return self.sigma * SimpleCrawler.norminv(p) + self.mu


class BenchmarkCrawlerExample(SimpleCrawler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def sample(self, lagged_values, lagged_times, **ignored):
        try:
            from vendor import VendorModel   # pseudo code
            model = VendorModel()
        except:
            model = MockFastVendorModel()

        model.fit(lagged_values)
        half_width = 0.5 / self.num_predictions
        prctls = np.linspace(half_width, 1 - half_width, self.num_predictions)
        return [model.invcdf(p) for p in prctls]


if __name__ == "__main__":
    crawler = BenchmarkCrawlerExample()
    crawler.run()
