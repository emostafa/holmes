from inspector import Inspector

if __name__ == '__main__':
    print('Inspecting your folders, please be patient...')
    i = Inspector()
    for k, v in i.stats.items():
        print(k, v)

