"""
predict.py
----------
This module provides a main method for prediction.
By: Sebastian D. Goodfellow, Ph.D., 2018
"""

# Compatibility imports
from __future__ import absolute_import, division, print_function

# 3rd party imports
import os
import sys
import pickle
import numpy as np
import pandas as pd
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# Add root path
sys.path.append('../')

# Local imports
from titanic.data.type_conversions import sex_type_conversion, embarked_type_conversion


def main(args):
    """Predict passenger mortality."""
    # Load model
    model = pickle.load(open(os.path.join(os.getcwd(), 'models', 'production', 'model.pickle'), 'rb'))

    # Create input
    input_features = pd.Series({'pclass': args.pclass, 'sex': sex_type_conversion(sex=args.sex), 'age': args.age,
                                'sibsp': args.sibsp, 'parch': args.parch, 'fare': args.fare,
                                'embarked': embarked_type_conversion(embarked=args.embarked)})
    # Get prediction
    prediction = np.squeeze(model.predict(input_features.values.reshape(1, -1)))

    return 'You Died!' if prediction == 1 else 'You Lived!'


def get_parser():
    """Get parser object for script predict.py."""
    # Initialize parser
    parser = ArgumentParser(description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter)

    # Setup arguments
    parser.add_argument("--pclass", dest="pclass", type=int, help="passenger class")
    parser.add_argument("--sex", dest="sex", type=str, help="passenger sex")
    parser.add_argument("--age", dest="age", type=int, help="passenger age")
    parser.add_argument("--sibsp", dest="sibsp", type=int, help="passenger siblings/spouses aboard")
    parser.add_argument("--parch", dest="parch", type=int, help="passenger parents/children aboard")
    parser.add_argument("--fare", dest="fare", type=float, help="passenger fare")
    parser.add_argument("--embarked", dest="embarked", type=str, help="passenger port embarked")

    return parser


if __name__ == "__main__":

    # Parse arguments
    arguments = get_parser().parse_args()

    # Run main function
    pred = main(args=arguments)

    # Print output
    print('\nPrediction: {}\n'.format(pred))
