import sys

import click
from tqdm import tqdm

import test_click as tool


@click.command()
@click.option(
    '--filter',
    '--f',
    default='.*',
    help='test를 실행한 파일 필터 : category1/, category2/device1, common etc..'
)
@click.option(
    '--phase',
    '--p',
    default='QA',
    help='test 를 실행할 phase : QA/OP/ST'
)
@click.option(
    '--email/--no-email',
    default=False,
    help='email 을 보낼지 말지 선택하는 옵션, 명시안하면 False'
)
@click.option(
    '--excel/--no-excel',
    default=False,
    help='excel로 결과를 변환할 지 여부, 명시안하면 False'
)
def test_run(filter, phase, email, excel):
    print(f'{sys.argv}')
    for i in tqdm(range(int(9e6))):
        pass
    tool.test(filter=filter, phase=phase, email=email, excel=excel)


if __name__ == "__main__":
    test_run()
