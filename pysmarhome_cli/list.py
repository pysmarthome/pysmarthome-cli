from .graphql.request import graphql_request
from .graphql.queries import devs_query


def print_line_sep(*args):
    for columns in args:
        print('|', end='')
        [ print('-', end='') for i in range(columns) ]
    print('|')


def print_formatted_line(*data):
    for data, size in data:
        column_data = f'| {data}' + ' ' * (size - len(data) - 2)
        print(column_data, end=' ')
    print('|')


def create_table_fields(data, filter_columns=[]):
    column_data = []
    for dev in data:
        dev_keys = filter(lambda x: x not in filter_columns and
            x not in column_data, dev.keys())
        column_data.extend(dev_keys)
    return column_data


def fill_table(data, fields):
    column_sizes = []
    row_data = [fields]
    [ row_data.append([''] * len(fields)) for i in range(len(data)) ]

    for k, key in enumerate(fields):
        # consider a blank spaces on the left and right
        size = len(key) + 2
        # skiping the first row (field names)
        for j, dev in enumerate(data, 1):
            if key in dev:
                size = max(size, len(str(dev[key])) + 2)
                row_data[j][k] = str(dev[key])
        column_sizes.append(size)
    return row_data, column_sizes


def render_list(data):
    column_fields = create_table_fields(data)
    row_data, column_sizes = fill_table(data, column_fields)

    for col in row_data:
        print_line_sep(*column_sizes)
        column_data = [ (d, column_sizes[j]) for j, d in enumerate(col) ]
        print_formatted_line(*column_data)
    print_line_sep(*column_sizes)


def list_devs(args):
    devs = graphql_request(args.host, args.api_key, devs_query)['devices']
    for i in range(len(devs)):
        devs[i] |= devs[i].pop('state')
    render_list(devs)
