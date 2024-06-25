# Simplify Coordinates in KML Files

This script simplifies the coordinates in KML files using the Ramer-Douglas-Peucker algorithm. It reduces the number of points in paths while maintaining their overall shape, making the KML file smaller and more efficient for applications like Google Earth.

## Features

- **Simplifies Coordinates**: Reduces the number of points in LineString paths to make KML files smaller.
- **Customizable Simplification Level**: Adjust the `epsilon` value to control the level of simplification.
- **Easy to Use**: Simply specify the path to your KML file and the script will do the rest.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Update the `kml_file_path` variable in the script with the path to your KML file:
    ```python
    kml_file_path = r'kml_file_path'
    ```
2. Adjust the `epsilon_value` to control the simplification level:
    ```python
    epsilon_value = 0.0001  # Adjust this value for more or less simplification
    ```
3. Run the script:
    ```sh
    python simplify_coordinates.py
    ```
4. The simplified KML file will be saved with `_simplified` appended to the original file name.

## Example

Original KML snippet:
```xml
<coordinates>
    49.663174424,40.590863647,0 49.662635331,40.591082307,0 49.661584764,40.591439266,0
    49.66147541599999,40.591407937,0 49.661148934,40.591863418,0 49.66162625899999,40.592062242,0
</coordinates>
 ```
Simplified KML snippet:
```xml
<coordinates>
    49.663174424,40.590863647,0 49.661584764,40.591439266,0 49.66162625899999,40.592062242,0
</coordinates>
```

## Contributing

Feel free to submit issues and enhancement requests. If you want to contribute, please fork the repository and create a pull request.
