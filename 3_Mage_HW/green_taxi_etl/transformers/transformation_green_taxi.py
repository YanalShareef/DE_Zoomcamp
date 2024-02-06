if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import re

# Function to convert CamelCase to snake_case 
def camel_to_snake(name):
    # First capital to lower case
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Remaining capitals to lower case
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

@transformer
def transform(data, *args, **kwargs):

    # check how mant rides with zero passangers or trip distance is equal to zero  
    print("rides with zero passangers or trip distance is equal to zero ",
    data[(data["passenger_count"]==0) | (data["trip_distance"]==0) ]['VendorID'].count() )

    # Add dates columns 
    data["lpep_pickup_date"]  = data["lpep_pickup_datetime"].dt.date

    # Rename columns in Camel Case to Snake Case    
    data.columns = [camel_to_snake(col) for col in data.columns]

    return data[(data["passenger_count"]> 0) & (data["trip_distance"]> 0)]



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert "vendor_id" in output.columns, 'Column "vendor_id" is missing'
    assert (output["passenger_count"].isin([0]) | (output["trip_distance"]==0)).sum() == 0, 'The are rides with zero passangers'
