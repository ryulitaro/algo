import argparse

import test_click as tool


def test_run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', '--f', type=str, default='/.*',
                        help='test를 실행한 파일 필터 : category1/, category2/device1, common etc..')
    parser.add_argument('--email', '--e,', type=bool, default=False, help='test 를 실행할 phase : QA/OP/ST')
    parser.add_argument('--excel', type=bool, default=False)
    parser.add_argument('--phase', type=str, default='QA')
    args = parser.parse_args()
    print(f'{args}')

    print(f'{args.filter} {args.excel} {args.email} {args.phase}')
    tool.test(filter=args.filter, phase=args.phase, email=args.email, excel=args.excel)


if __name__ == "__main__":
    test_run()
