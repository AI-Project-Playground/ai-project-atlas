"""Tests for the educational OLS regression implementation."""

import numpy as np

from ols.metrics import mean_squared_error, r_squared
from ols.regression import OLSRegression


def test_ols_finds_simple_line():
    """
    Test OLS using data that follows the line:

        y = 2 + 3x

    Because we know the exact relationship, we know what the
    model should learn:

        intercept = 2
        coefficient = 3
    """

    # Input values.
    X = np.array([1, 2, 3, 4, 5])

    # Target values generated from:
    #
    #     y = 2 + 3x
    #
    # So:
    #
    # x = 1 -> y = 5
    # x = 2 -> y = 8
    # x = 3 -> y = 11
    # x = 4 -> y = 14
    # x = 5 -> y = 17
    y = np.array([5, 8, 11, 14, 17])

    # Create and train our OLS model.
    model = OLSRegression()
    model.fit(X, y)

    # Check that the model learned the expected intercept.
    assert np.isclose(model.intercept_, 2.0)

    # Check that the model learned the expected coefficient.
    assert np.isclose(model.coef_[0], 3.0)


def test_ols_predicts_correct_values():
    """
    Test that the trained model can make predictions.

    The learned equation should be:

        y = 2 + 3x
    """

    X = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 8, 11, 14, 17])

    model = OLSRegression()
    model.fit(X, y)

    # Ask the model to predict values for new X values.
    new_X = np.array([6, 7])

    predictions = model.predict(new_X)

    # Expected:
    #
    # x = 6 -> 2 + (3 * 6) = 20
    # x = 7 -> 2 + (3 * 7) = 23
    expected = np.array([20, 23])

    # Compare the model's predictions with our expected values.
    assert np.allclose(predictions, expected)


def test_mean_squared_error():
    """
    Test our MSE implementation with simple values.

    Actual values:
        [10, 20, 30]

    Predictions:
        [11, 18, 31]

    Errors:
        [-1, 2, -1]

    Squared errors:
        [1, 4, 1]

    MSE:
        (1 + 4 + 1) / 3 = 2
    """

    y_true = np.array([10, 20, 30])
    y_pred = np.array([11, 18, 31])

    mse = mean_squared_error(y_true, y_pred)

    assert np.isclose(mse, 2.0)


def test_r_squared_for_perfect_predictions():
    """
    Test R² when predictions are exactly correct.

    When a model predicts every value perfectly:

        R² = 1.0
    """

    y_true = np.array([10, 20, 30])
    y_pred = np.array([10, 20, 30])

    r2 = r_squared(y_true, y_pred)

    assert np.isclose(r2, 1.0)