# AI Context — CNN Basics

## Project Identity

- **Project title:** CNN Basics: Convolution, Feature Maps, and Classification
- **Learning track:** P0 — Day 9, Track I: CV & Sequence Models, Subtopic 1
- **Suggested Atlas ID:** `ml-004`
- **Primary domain:** Machine Learning
- **Difficulty:** Beginner
- **Current status:** In progress

This is a hands-on learning project designed to explain what a convolutional neural network computes. The core CNN is implemented using NumPy rather than a deep-learning framework, so the learner can inspect the operations and understand the mathematics behind them.

## Project Goal

Understand the mechanics of a small CNN by implementing convolution, feature extraction, classification, backpropagation, and parameter updates from scratch, then compare the CNN with a logistic regression baseline.

## What the Project Does

The project uses the handwritten digits dataset provided by scikit-learn. It contains 1,797 grayscale images, each with an 8 × 8 pixel grid, representing digit classes 0 through 9. The dataset is loaded through `sklearn.datasets.load_digits`; no separate dataset download or user-provided input is required.

The core implementation has four main parts:

1. **2D convolution:** Implements convolution with nested Python loops and a vectorized NumPy implementation using `sliding_window_view` and `einsum`.
2. **Feature filters:** Applies vertical and horizontal Sobel edge filters to a handwritten digit to demonstrate how a filter responds to image patterns.
3. **Tiny CNN training:** Implements a small CNN with convolution, ReLU, flattening, a dense layer, and softmax. The project includes hand-written backpropagation, numerical gradient checking, and an Adam optimizer.
4. **Baseline comparison:** Trains scikit-learn Logistic Regression on the raw image pixels and compares its test performance with the CNN.

The train/test split uses `test_size=0.2`, `random_state=42`, and stratification by digit label. The NumPy CNN uses four 3 × 3 filters, 30 training epochs, and a batch size of 64 in the documented baseline run.

## Model Architecture and Data Flow

The core model follows this sequence:

`8 × 8 grayscale image`
→ `Convolution: 4 filters, each 3 × 3`
→ `4 feature maps, each 6 × 6`
→ `ReLU`
→ `Flatten: 144 values`
→ `Dense layer: 144 inputs to 10 outputs`
→ `Softmax: probabilities for digit classes 0–9`

The convolution uses valid positioning (no padding) and stride 1. Therefore, each spatial dimension is:

`(8 - 3) / 1 + 1 = 6`

The output feature-map shape is `4 × 6 × 6`, containing 144 values per image.

For the default four-filter architecture:

- Convolution weights: `4 × 3 × 3 = 36`
- Convolution biases: `4`
- Convolution parameters: `40`
- Dense weights: `144 × 10 = 1,440`
- Dense biases: `10`
- Dense parameters: `1,450`
- Total trainable parameters: `1,490`

The ten output scores correspond to digit classes 0 through 9.

## Main Concepts Demonstrated

### Convolution and Feature Maps

A small kernel is moved across an image. At each valid position, corresponding image and kernel values are multiplied and summed. The resulting grid is a feature map. A large response indicates that the pattern represented by the filter is present at that location.

The project includes a loop-based implementation and a vectorized implementation. Deep-learning libraries commonly call this operation convolution, although the kernel is not flipped; mathematically, this is cross-correlation.

### Local Receptive Fields

Each convolution output depends on a small local patch of the input image rather than every pixel.

### Parameter Sharing

The same filter weights are reused at every spatial position. This allows a pattern to be detected in different image locations without learning a separate set of weights for every location.

### ReLU and Flattening

ReLU replaces negative activations with zero and introduces non-linearity. Flatten converts the four 6 × 6 feature maps into a vector of 144 values before the dense classification layer.

### Dense Classification Layer

The dense layer maps the 144 extracted features to ten class scores. Softmax converts these scores into a probability distribution over digit classes.

### Backpropagation and Gradient Checking

The NumPy implementation calculates gradients manually. A finite-difference gradient check compares the analytical gradients with numerical approximations to help verify the backward pass.

The project documents an important numerical issue: ReLU is non-differentiable at zero. A finite-difference check can be misleading when a perturbation crosses that point. The implementation uses small random biases during gradient checking to avoid testing exactly at the kink.

### Optimization

The project uses a hand-written Adam optimizer to update the model parameters during training.

## Streamlit Interactive Experience

The companion Streamlit application provides an interactive learning interface with these areas:

1. **Convolution Explorer:** Select a handwritten digit and inspect the image, selected edge filter, resulting feature map, and agreement between loop-based and vectorized convolution.
2. **Parameter Sharing:** Change the number of filters and compare convolution parameter counts with a dense-layer alternative.
3. **Train Tiny CNN:** Adjust training settings such as filter count, epochs, learning rate, and batch size; inspect training and evaluation results and learned filters.
4. **Concepts & Formulas:** Review CNN concepts, data flow, and output-size calculations.

The Streamlit app is intended to run locally. No public hosted demo URL is currently specified.

## Optional PyTorch Comparison

An optional PyTorch implementation is provided separately from the core NumPy learning path. It uses the same basic architecture:

`Conv2d(1, 4, kernel_size=3)` → `ReLU` → `Flatten` → `Linear(144, 10)`

PyTorch uses automatic differentiation for gradient calculation and its optimizer for parameter updates. This comparison is intended to show how a deep-learning framework expresses the same model more concisely.

PyTorch is optional for the core NumPy project. The core implementation and Streamlit explorer do not require PyTorch. The optional comparison should only be run when PyTorch is installed.

## Technologies

- Python
- NumPy
- scikit-learn
- Streamlit
- PyTorch (optional comparison)

## Reported Baseline Results

The README records one run using seed 42:

- NumPy TinyCNN: 1,490 parameters and 97.2% test accuracy.
- Logistic Regression: 650 parameters and 95.6% test accuracy.
- Gradient check: worst relative error approximately `1e-9`.

These are results from one train/test split, not guaranteed results for every run or configuration. The project notes that the accuracy difference is too small to draw broad conclusions from a single split and recommends trying other seeds or cross-validation.

## What the Project Does Not Cover

- It is not a production-grade image recognition system.
- It does not use large image datasets or high-resolution colour images.
- The core CNN is intentionally small and is implemented with NumPy for learning purposes.
- It does not demonstrate a deep stack of convolution and pooling layers.
- Pooling and padding are follow-up topics, not core completed topics in this subtopic.
- The optional PyTorch comparison is not required to run the NumPy implementation.
- The reported accuracy is not a benchmark claim about CNNs in general.

## Who Should Build It

Beginner learners who understand basic Python and NumPy and want to understand the mechanics of CNNs before relying on high-level deep-learning frameworks.

## Suggested Follow-up Topics

- Pooling and padding
- Stride and padding experiments
- Multiple convolutional layers
- CNNs on larger image datasets
- Comparing NumPy implementations with PyTorch implementations
- Repeated train/test splits or cross-validation for more reliable evaluation

## Key Learning Principle

A CNN uses local connections and shared weights to extract spatial features efficiently. The convolution layers learn useful image patterns, while the dense layer combines those features to classify the image.
