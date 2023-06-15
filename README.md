# Cheader2PythonDict
Convert the C header format file exported from IDA Pro's local type into a custom Python dictionary format for easy reading in Python.
# example
The content of C header format file exported from IDA Pro is as follows:
```C
struct EFI_HII_DATE
{
  UINT16 Year;
  UINT8 Month;
  UINT8 Day;
};
```
We should convert it to the python dictionary as follows:
```python
{'EFI_HII_DATE':[32, ['Year', 'Month', 'Day']], 'Year':'UINT16', 'Month':'UINT8', 'Day':'UINT8', 'UINT16':[16, []], 'UINT8':[8, []]}
```
In this Python dictionary, there are two key-value pairs. In the first key-value pairs, the key represents the name of a field in a structure or a struct, and the value is a two-dimensional list. The first element indicates the length of the field, i.e., the amount of space it occupies, while the second element lists the fields in the structure. In the second key-value pair, the key is the name of the field and the value is the type of the field.
