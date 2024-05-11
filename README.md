# Array Statistics Calculator

This Python script calculates various statistics for a 3x3 array provided as input. It computes the mean, variance, standard deviation, maximum, minimum, and sum of the array along different axes.

## Installation

Make sure you have Python installed on your system. You also need to have NumPy library installed. If not, you can install it using pip:

```bash
pip install numpy
```

## Usage
To use this script, simply call the calculate() function with a list of nine numbers representing the elements of the 3x3 array. The script will return a dictionary containing the calculated statistics.

Example usage:
```bash
import numpy as np


# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call the calculate function
print(calculate(data))
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
