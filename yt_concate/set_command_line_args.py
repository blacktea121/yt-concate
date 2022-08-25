import sys
import getopt


def print_help():
    print()
    print('Python set_command_line_args.py -c <channel_id> -s <search_word> -l <limit>')
    print('Python set_command_line_args.py --channel_id <channel_id> --search_word <search_word> --limit <limit>')
    print()
    print("Python set_command_line_args.py OPTIONS")
    print("{:>6} {:<20} {}".format('', "--cleanup", "Remove captions and videos downloaded during run"))
    print("{:>6} {:<20} {}".format('', "--fast", "Skipping downloaded captions and videos if files exist"))
    print("{:>6} {:<20} {}".format('', "--logger_level", "Set log-level to show in cmd"))


def get_cmd_args():
    """
    cleanup: 結果檔產生後，刪除程式執行中產生的檔案，如下載的影片/字幕等
    fast: 如果True(預設可以是True), 程式執行中會先檢查檔案(包括影片、字幕) 有沒有已經存在電腦上
        ，如果有則跳過，不用重複下載。如果False，則是強迫每次執行一定會重新下載所有需要的檔案。
    """
    channel_id = ''
    search_word = ''
    limit = ''
    cleanup = False
    fast = False
    logger_level = 'DEBUG'

    short_arguments = "hc:s:l:"
    long_arguments = "help channel_id= search_word= limit= cleanup= fast= logger_level=".split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_arguments, long_arguments)
        if args:
            print('useless args: ', args)
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-c", "--channel_id"):
            channel_id = arg
        elif opt in ("-s", "--search_word"):
            search_word = arg
        elif opt in ("-l", "--limit"):
            limit = arg
        elif opt == '--cleanup':
            cleanup = arg
        elif opt == '--fast':
            fast = arg
        elif opt == '--logger_level':
            logger_level = arg

    if not channel_id or not search_word or not limit:
        print_help()
        sys.exit(2)

    print('channel_id is ', channel_id)
    print('search_word is ', search_word)
    print('limit is ', limit)
    print('cleanup is ', cleanup)
    print('fast is ', fast)
    print('logger_level is ', logger_level)

    dict_args = {
        'channel_id': channel_id,
        'search_word': search_word,
        'limit': limit,
        'cleanup': cleanup,
        'fast': fast,
        'logger_level': logger_level,
    }

    return dict_args


if __name__ == "__main__":
    get_cmd_args()
