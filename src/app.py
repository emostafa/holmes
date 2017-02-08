import inspector

if __name__ == '__main__':
    print('Inspecting your folders, please be patient...')
    i = inspector.Inspector()
    for k, v in i.stats.items():
        print(k, v)

    
