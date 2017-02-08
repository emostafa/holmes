import os

class Inspector(object):
    path = os.path.expanduser('~')
    stats = {}

    def __init__(self):
        self.prepare_stats()
        self.inspect_dir(self.path)

    def inspect_dir(self, path):
        files = os.listdir(path)
        for f in files:
            file_path = os.path.join(path, f)
            if os.path.isdir(file_path):
                self.inspect_dir(file_path)
            else:
                if file_path.endswith('.py'):
                    self.stats['Python'] += 1
                elif file_path.endswith('.rb'):
                    self.stats['Ruby'] += 1
                elif file_path.endswith('.go'):
                    self.stats['Go'] += 1
                elif file_path.endswith('.cpp'):
                    self.stats['C++'] += 1
                elif file_path.endswith('.c'):
                    self.stats['C'] += 1
                elif file_path.endswith('.java'):
                    self.stats['Java'] += 1
                elif file_path.endswith('.rs'):
                    self.stats['Rust'] += 1
                elif file_path.endswith('.js'):
                    self.stats['Javascript'] += 1
                elif file_path.endswith('.ts'):
                    self.stats['TypeScript'] += 1
                elif file_path.endswith('.kotlin'):
                    self.stats['Kotlin'] += 1
                elif file_path.endswith('.sh'):
                    self.stats['Shell'] += 1
                elif file_path.endswith('.css'):
                    self.stats['CSS'] += 1
                elif file_path.endswith('.html') or file_path.endswith('.xhtml'):
                    self.stats['HTML'] += 1
                elif file_path.endswith('.php'):
                    self.stats['PHP'] += 1
                elif file_path.endswith('.cs'):
                    self.stats['C#'] += 1
                elif file_path.endswith('.elm'):
                    self.stats['ELM'] += 1

    def prepare_stats(self):
        self.stats['Python'] = 0
        self.stats['Ruby'] = 0
        self.stats['Go'] = 0
        self.stats['C++'] = 0
        self.stats['C'] = 0
        self.stats['Java'] = 0
        self.stats['Rust'] = 0
        self.stats['Javascript'] = 0
        self.stats['TypeScript'] = 0
        self.stats['Kotlin'] = 0
        self.stats['Shell'] = 0
        self.stats['CSS'] = 0
        self.stats['HTML'] = 0
        self.stats['PHP'] = 0
        self.stats['C#'] = 0
        self.stats['ELM'] = 0
