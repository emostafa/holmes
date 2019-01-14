import os
from collections import Counter

class Inspector:

    langs = [
        'Python',
        'Ruby',
        'Go',
        'Rust',
        'C',
        'C++',
        'C#',
        'Java',
        'Kotlin',
        'Scala',
        'Javascript',
        'Typescript',
        'ELM',
        'CSS',
        'HTML',
        'JSON',
        'YAML',
        'Markdown',
        'Dockerfile',
        'PHP',
        'Shell',
    ]

    def __init__(self, path):
        self.path = path

        self.stats = Counter(self.langs)
        self.inspect_dir(self.path)

    def get_file_extension(self, file_path):
        p, ext = os.path.splitext(file_path)
        filename = p.split('/')[-1]
        return (filename, ext)

    def inspect_dir(self, path):
        files = os.listdir(path)
        for f in files:
            try:
                file_path = os.path.join(path, f)
                if os.path.isdir(file_path):
                    self.inspect_dir(file_path)
                else:
                    filename, ext = self.get_file_extension(file_path)
                    if ext == '.py':
                        self.stats['Python'] += 1
                    elif ext == '.rb':
                        self.stats['Ruby'] += 1
                    elif ext == '.go':
                        self.stats['Go'] += 1
                    elif ext == '.cpp':
                        self.stats['C++'] += 1
                    elif ext == '.c':
                        self.stats['C'] += 1
                    elif ext == '.java':
                        self.stats['Java'] += 1
                    elif ext == '.kotlin':
                        self.stats['Kotlin'] += 1
                    elif ext == '.scala':
                        self.stats['Scala'] += 1
                    elif ext == '.rs':
                        self.stats['Rust'] += 1
                    elif ext == '.js':
                        self.stats['Javascript'] += 1
                    elif ext == '.ts':
                        self.stats['TypeScript'] += 1
                    elif ext == '.sh':
                        self.stats['Shell'] += 1
                    elif ext in ['.css', '.scss']:
                        self.stats['CSS'] += 1
                    elif ext in ['.html', '.xhtml']:
                        self.stats['HTML'] += 1
                    elif ext == '.php':
                        self.stats['PHP'] += 1
                    elif ext == '.cs':
                        self.stats['C#'] += 1
                    elif ext == '.elm':
                        self.stats['ELM'] += 1
                    elif ext == '.json':
                        self.stats['JSON'] += 1
                    elif ext in ['.yaml', '.yml']:
                        self.stats['YAML'] += 1
                    elif filename == 'Dockerfile':
                        self.stats['Dockerfile'] += 1
            except OSError:
                pass

