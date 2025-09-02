%pip install pyarrow
import pandas as pd
import openpyxl #for reading xlsx file
import xlrd   # needed for reading .xls
import pyarrow

#dbutils.fs.cp("dbfs:/FileStore/tables/test_json-1.json", "file:/tmp/test_json-1.json")
#dbutils.fs.cp("dbfs:/FileStore/tables/test_parquet.parquet", "file:/tmp/test_parquet.parquet")

def input_file_extension_logic(input_file_path, extension, delimiter, row_limit, header, skip_footer, excel_sheet_name, json_orient, json_lines,columns):
    if extension == "xlsx":
        #pd.read_excel(io, sheet_name=0, *, header=0, names=None, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=<no_default>, date_format=None, thousands=None, decimal='.', comment=None, skipfooter=0, storage_options=None, dtype_backend=<no_default>, engine_kwargs=None)
        if excel_sheet_name == "all":
            df = pd.read_excel(input_file_path, header=header, sheet_name=None, engine="openpyxl")
        else:
            df = pd.read_excel(input_file_path, header=header, sheet_name=excel_sheet_name, engine="openpyxl")
    elif extension =="xls":
        if excel_sheet_name == "all":
            df = pd.read_excel(input_file_path, header=header, sheet_name=None, engine="xlrd")
        else:
            df = pd.read_excel(input_file_path, header=header, sheet_name=excel_sheet_name, engine="xlrd")
    elif extension =="xlsb":
        if excel_sheet_name == "all":
            df = pd.read_excel(input_file_path, header=header, sheet_name=None, engine="pyxlsb")
        else:
            df = pd.read_excel(input_file_path, header=header, sheet_name=excel_sheet_name, engine="pyxlsb")
    #elif extension in ["xla", "xlb"]:
        #if excel_sheet_name == "all":
            #df = pd.read_excel(input_file_path, header=header, sheet_name=None, engine="openpyxl")
        #else:
            #df = pd.read_excel(input_file_path, header=header, sheet_name=excel_sheet_name, engine="openpyxl")
    elif extension in ["csv", "txt"]:
        #pd.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=<no_default>, skip_blank_lines=True, parse_dates=None, infer_datetime_format=<no_default>, keep_date_col=<no_default>, date_parser=<no_default>, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', delim_whitespace=<no_default>, low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=<no_default>)
        df = pd.read_csv(
            input_file_path,
            delimiter=delimiter,
            header=header,
            nrows=row_limit,
            skipfooter=skip_footer,
            engine="python"  # required if skipfooter > 0
        )
    elif extension == "json":
        #pd.read_json(path_or_buf, *, orient=None, typ='frame', dtype=None, convert_axes=None, convert_dates=True, keep_default_dates=True, precise_float=False, date_unit=None, encoding=None, encoding_errors='strict', lines=False, chunksize=None, compression='infer', nrows=None, storage_options=None, dtype_backend=<no_default>, engine='ujson')
        df = pd.read_json(
            input_file_path,
            orient=json_orient,
            lines=json_lines
        )
    elif extension == "parquet":
        #pd.read_parquet(path, engine='auto', columns=None, storage_options=None, use_nullable_dtypes=<no_default>, dtype_backend=<no_default>, filesystem=None, filters=None, **kwargs)
        df = pd.read_parquet(input_file_path,engine="pyarrow",columns=columns)
    else:
        raise ValueError(f"Unsupported file extension: {extension}")
    
    return df

# Parameters
input_file_path = "file:/tmp/test_parquet.parquet"
extension = "parquet"
delimiter = ""   # not needed for excel
row_limit = 10
header = 0
skip_footer = 0
excel_sheet_name = "all"
json_orient=None
json_lines=False
columns=None

# Calling the function 
df = input_file_extension_logic(
    input_file_path, extension, delimiter, row_limit, header, skip_footer, excel_sheet_name, json_orient,json_lines,columns
)

print(df)
