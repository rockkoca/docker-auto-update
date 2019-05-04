#!/usr/bin/env python

from runlike.inspector import Inspector
import re
import subprocess
import click
import time


@click.command(
    help="Auto upgrade docker containers")
@click.argument("image_name")
@click.option(
    "--exact",
    is_flag=False,
    help="exact match image name or any image starts with image name")
@click.option(
    "-i", "--interval",
    type=click.IntRange(1, 24),
    default=1,
    help="Check update interval in hours. Range is [1,24]. The default value is 1 hour.")
def main(image_name: str, exact: bool, interval: int):
    while True:
        try:
            output: str = subprocess.check_output('docker ps', shell=True).decode()
            print(output)
            containers = []
            for i, line in enumerate(output.split('\n')):
                if i > 0:
                    line = re.split(r'\s{2,}', line)
                    if len(line) > 1 and line[1].startswith(image_name) if not exact else line[1] == image_name:
                        if line[1].startswith('rockkoca/docker-auto-update'):
                            continue
                        containers.append(line)
            print(containers)
            for container in containers:
                result: str = subprocess.check_output(f'docker pull {container[1]}', shell=True).decode()
                print(result)
                if 'Downloaded newer image' in result:
                    ins = Inspector(container[-1], no_name=True, pretty=True)
                    ins.inspect()
                    cli = ins.format_cli()
                    clis = cli.split('\\')
                    clis = clis[:1] + [f'\n\t--name={container[-1]} '] + clis[1:]
                    cli = '\\'.join(clis)
                    print(cli)
                    out: str = subprocess.check_output(
                        f'docker stop {container[-1]};docker system prune -f;{cli};docker ps',
                        shell=True).decode()
                    print(out)
            time.sleep(interval * 3600)
        except Exception as e:
            print(e)
            raise


if __name__ == '__main__':
    main()
