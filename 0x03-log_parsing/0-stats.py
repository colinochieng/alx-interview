#!/usr/bin/python3
'''
Module for log parsing
log data passed in format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
84.27.67.17 - [2023-10-19 10:40:59.756530] "GET /projects/260 HTTP/1.1" 200 437
'''
import re
import sys


def print_logs(lines, regex, global_log_data):
    '''
    description: function to output global log file data and status logs
    Args:
        lines (list): list of log data
        regex (re.Pattern): patter to extract file size and status code
    return: None
    out format:
        File size: <total size>
        <status code>: <number>
        <status code>: <number>
    if a status code doesn't appear or is not an integer,
    don't print anything for this status code
    '''
    file_sizes_archive = {}

    list_status_code_count = []

    for line in lines:
        match_data = regex.match(line)
        statu_code, file_size = match_data.group(3), match_data.group(4)

        if file_size not in file_sizes_archive:
            file_sizes_archive.update({file_size: {statu_code: 1}})
        else:
            if statu_code not in file_sizes_archive[file_size]:
                file_sizes_archive[file_size].update({statu_code: 1})
            else:
                file_sizes_archive[file_size][statu_code] += 1

    for key in file_sizes_archive.keys():
        global_log_data['file_size'] += int(key)

    print(f'File size: {global_log_data["file_size"]}')

    for value in file_sizes_archive.values():
        for code, count in value.items():
            if code in global_log_data['codes']:
                global_log_data['codes'][code] += count
            else:
                global_log_data['codes'].update({code: count})

    for code, count in global_log_data['codes'].items():
        try:
            list_status_code_count.append((int(code), count))
        except TypeError:
            continue

    # status codes should be printed in ascending order
    sorted_list = sorted(list_status_code_count, key=lambda item: item[0])

    for items in sorted_list:
        print(f'{items[0]}: {items[1]}')


if __name__ == '__main__':
    pattern1 = r'^([\d.]+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]'
    pattern2 = r' "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    log_pattern = pattern1 + pattern2

    log_regex = re.compile(log_pattern)

    global_log_data = {'file_size': 0, 'codes': {}}

    line_count = 1
    lines = []

    try:
        for line in sys.stdin:

            if log_regex.match(line):
                lines.append(line)
                line_count += 1

            if line_count % 10 == 0:
                print_logs(lines, log_regex, global_log_data)
    except KeyboardInterrupt:
        print_logs(lines, log_regex, global_log_data)
