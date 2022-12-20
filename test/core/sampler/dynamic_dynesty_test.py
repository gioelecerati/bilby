import unittest
from unittest.mock import MagicMock

import bilby


class TestDynamicDynesty(unittest.TestCase):
    def setUp(self):
        self.likelihood = MagicMock()
        self.priors = bilby.core.prior.PriorDict(
            dict(a=bilby.core.prior.Uniform(0, 1), b=bilby.core.prior.Uniform(0, 1))
        )
        self.sampler = bilby.core.sampler.DynamicDynesty(
            self.likelihood,
            self.priors,
            outdir="outdir",
            label="label",
            use_ratio=False,
            plot=False,
            skip_import_verification=True,
        )

    def tearDown(self):
        del self.likelihood
        del self.priors
        del self.sampler

    def test_default_kwargs(self):
        """Only test the kwargs where we specify different defaults to dynesty"""
        expected = dict(sample="rwalk", facc=0.2, save_bounds=False)
        for key in expected:
            self.assertEqual(expected[key], self.sampler.kwargs[key])


if __name__ == "__main__":
    unittest.main()