import xml.etree.ElementTree as ET
import math
import os

def distance_point_to_line(px, py, x1, y1, x2, y2):
    """Calculate the perpendicular distance from a point to a line."""
    return abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

def rdp(points, epsilon):
    """Ramer-Douglas-Peucker algorithm to simplify a path."""
    if len(points) < 3:
        return points

    dmax = 0
    index = 0
    for i in range(1, len(points) - 1):
        d = distance_point_to_line(points[i][0], points[i][1], points[0][0], points[0][1], points[-1][0], points[-1][1])
        if d > dmax:
            index = i
            dmax = d

    if dmax > epsilon:
        results1 = rdp(points[:index+1], epsilon)
        results2 = rdp(points[index:], epsilon)
        return results1[:-1] + results2
    else:
        return [points[0], points[-1]]

def parse_coordinates(coordinate_string):
    """Parse a coordinate string into a list of (lon, lat, alt) tuples."""
    coords = []
    for coord in coordinate_string.strip().split():
        lon, lat, alt = map(float, coord.split(','))
        coords.append((lon, lat, alt))
    return coords

def stringify_coordinates(coords):
    """Convert a list of (lon, lat, alt) tuples into a coordinate string."""
    return ' '.join(f'{lon},{lat},{alt}' for lon, lat, alt in coords)

def simplify_kml_coordinates(file_path, epsilon):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    namespace = {'ns': 'http://www.opengis.net/kml/2.2'}
    
    for placemark in root.findall('.//ns:Placemark', namespace):
        for linestring in placemark.findall('.//ns:LineString', namespace):
            coordinates = linestring.find('ns:coordinates', namespace)
            if coordinates is not None:
                coords = parse_coordinates(coordinates.text)
                simplified_coords = rdp(coords, epsilon)
                coordinates.text = stringify_coordinates(simplified_coords)
    
    base, ext = os.path.splitext(file_path)
    output_file_path = f'{base}_simplified{ext}'
    tree.write(output_file_path)

# Usage
if __name__ == "__main__":
    kml_file_path = r'path/to/your/1.kml'
    epsilon_value = 0.0001  # Adjust this value for more or less simplification
    simplify_kml_coordinates(kml_file_path, epsilon_value)
