import sys
import argparse
import os


class MemIdxOutofRange(Exception):
    def __init__(self, *args, **kwargs):
        super(MemIdxOutofRange, self).__init__(*args, **kwargs)


def Format_Code(Code):
    charset = {',', '.', '+', '-', '[', ']', '>', '<'}
    Codelist = [x for x in Code if x in charset]
    return ''.join(Codelist)


def Eval(init_pos, curr_pos, MemPool, Code, input_buffer, input_pos):
    if MemPool[0] < 0 or MemPool[0] > len(MemPool):
        raise MemIdxOutofRange(
            f"[Error] {len(MemPool)} bytes of Memory Allocated" + \
            f"Index {MemPool[0]} out of Range"
        )

    if curr_pos >= len(Code):
        return 0

    if input_pos >= len(input_buffer):
        return -1
    







if __name__ == '__main__':
    parser = argparse.ArgumentParser('Interface for BrainFuck Interpreter')
    parser.add_argument(
        '-bf', '--bf', type=str,
        help='the source code of brainfuck'
    )
    parser.add_argument(
        '-ip', '--input', type=str,
        help='the input of the program'
    )
    parser.add_argument(
        '-m', '--memory', type=int, default=1000,
        help='the size of allocated memory, counted on byte'
    )
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit(0)

    if args.bf is None or args.input is None:
        content_name = 'A Toy BrainFuck Interpreter Done by Zeng Kaipeng,' + \
            ' Shanghai Jiao Tong University'
        print('%s\n' % (content_name))
        exit(0)
    
    if args.memory <= 0:
        print('[Error] Size of Allocated Memory should be positive')
        exit(0)

    if not os.path.exists(args.bf) or not os.path.exists(args.input):
        print('[Error] Input or Source does not Exist')
        exit(0)


    with open(args.bf) as Fin:
        original_code = Fin.read()

    with open(args.input) as Fin:
        program_input = Fin.read()
    
    formatted_code = Format_Code(original_code)

    mempool = [0 for i in range(args.memory + 1)]

    try:
        return_code = Eval(0, 0, mempool, formatted_code, program_input, 0)
        if return_code == -1:
            print('[INFO] Input Content is Used Up. Prog Terminated.')
    except Exception as e:
        print(e)
