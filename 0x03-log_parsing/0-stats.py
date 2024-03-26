#!/usr/bin/python3
"""Log parsing task"""
import sys
import re


def log_parsing():
    """
     log_parsing: reads stdin line by line and computes metrics.

     Args: from stdin
     <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
     <status code> <file size>

     Return:
    """
    input_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '\
        r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    total_file_size = 0

    status_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }

    try:
        for i, line in enumerate(sys.stdin, start=1):
            match = re.match(input_pattern, line)
            if match:
                file_size = int(match.group(4))
                total_file_size += file_size

                file_code = int(match.group(3))

                for code in status_code:
                    if file_code == code:
                        status_code[code] += 1

                if i % 10 == 0:
                    print(f'File size: {total_file_size}')
                    for code, count in status_code.items():
                        if count > 0:
                            print(f'{code}: {count}')
    except BrokenPipeError:
        pass


if __name__ == "__main__":
    log_parsing()
