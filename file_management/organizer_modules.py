import tkinter as tk
import tkinter.filedialog as filedialog
import os

categories = ['WEB', 'AUDIO', 'CODE', 'SHEET', 'IMAGE', 'ARCHIVE', 'BOOK', 'TEXT', 'EXEC', 'FONT', 'VIDEO', 'PDF',
              'OFFICE', 'ISO', 'TORRENT', 'DATABASE', 'DATA', 'CONFIG', 'DIAGRAMS', 'BACKUP', 'FOLDER', 'OTHER']

ext_typical = {
    'WEB': ['css', 'less', 'scss', 'wasm'],
    'AUDIO': ['aac', 'aiff', 'ape', 'au', 'flac', 'gsm', 'it', 'm3u', 'm4a', 'mid', 'mod', 'mp3', 'mpa', 'pls', 'ra',
              's3m', 'sid', 'wav', 'wma', 'xm'],
    'CODE': ['c', 'cc', 'class', 'clj', 'cpp', 'cs', 'cxx', 'el', 'go', 'h', 'java', 'lua', 'm', 'm4', 'php', 'pl',
             'po', 'py', 'rb', 'rs', 'swift', 'vb', 'vcxproj', 'xcodeproj', 'diff', 'patch', 'html', 'js', "htm",
             "ps1", "sql"],
    'SLIDE': ['ppt', 'odp'],
    'SHEET': ['ods', 'xls', 'xlsx', 'csv', 'ics', 'vcf'],
    'IMAGE': ['3dm', '3ds', 'max', 'bmp', 'dds', 'gif', 'jpg', 'jpeg', 'png', 'psd', 'xcf', 'tga', 'thm', 'tif',
              'tiff', 'ai', 'eps', 'ps', 'svg', 'dwg', 'dxf', 'gpx', 'kml', 'kmz', 'webp', 'ico', 'jfif', 'jpe', 'stl',
              'pdn'],
    'ARCHIVE': ['7z', 'a', 'apk', 'ar', 'bz2', 'cab', 'cpio', 'deb', 'dmg', 'egg', 'gz', 'lha', 'mar',
                'pea', 'rar', 'rpm', 's7z', 'shar', 'tar', 'tbz2', 'tgz', 'tlz', 'war', 'whl', 'xpi', 'zip', 'zipx',
                'xz', 'pak'],
    'BOOK': ['mobi', 'epub', 'azw1', 'azw3', 'azw4', 'azw6', 'azw', 'cbr', 'cbz'],
    'TEXT': ['doc', 'docx', 'ebook', 'log', 'md', 'msg', 'odt', 'org', 'pages', 'pdf', 'rtf', 'rst', 'tex', 'txt',
             'wpd', 'wps'],
    'EXEC': ['exe', 'msi', 'bin', 'command', 'sh', 'bat', 'crx', ],
    'FONT': ['eot', 'otf', 'ttf', 'woff', 'woff2', "pf2"],
    'VIDEO': ['3g2', '3gp', 'aaf', 'asf', 'avchd', 'avi', 'drc', 'flv', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov',
              'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv', 'mxf', 'nsv', 'ogg', 'ogv', 'ogm', 'qt', 'rm', 'rmvb',
              'roq', 'srt', 'svi', 'vob', 'webm', 'wmv', 'yuv', 'mov'],
    'ISO': ['iso', 'img', 'dmg'],
    'TORRENT': ['torrent'],
    'DATABASE': ['db', 'dbf', 'mdb', 'pdb'],
    'DATA': ['json', 'yaml', 'xml', 'yml'],
    'CONFIG': ['ini', 'cfg', 'conf', 'config', 'properties', 'prop', 'settings', 'inf' 'reg'],
    'DIAGRAMS': ['drawio', 'dtmp', 'nsd', 'fprg'],
    'BACKUP': ['bak'],
}

ext_personal = {
    'WEB': ['css', 'less', 'scss', 'wasm', 'html', 'js', 'htm'],
    'AUDIO': ['aac', 'aiff', 'ape', 'au', 'flac', 'gsm', 'it', 'm3u', 'm4a', 'mid', 'mod', 'mp3', 'mpa', 'pls', 'ra',
              's3m', 'sid', 'wav', 'wma', 'xm'],
    'CODE': ['c', 'cc', 'class', 'clj', 'cpp', 'cs', 'cxx', 'el', 'go', 'h', 'java', 'lua', 'm', 'm4', 'php', 'pl',
             'po', 'py', 'rb', 'rs', 'swift', 'vb', 'vcxproj', 'xcodeproj', 'diff', 'patch', 'ps1', 'sql'],
    'SHEET': ['ods', 'csv', 'ics', 'vcf'],
    'IMAGE': ['3dm', '3ds', 'max', 'bmp', 'dds', 'gif', 'jpg', 'jpeg', 'png', 'psd', 'xcf', 'tga', 'thm', 'tif',
              'tiff', 'ai', 'eps', 'ps', 'svg', 'dwg', 'dxf', 'gpx', 'kml', 'kmz', 'webp', 'ico', 'jfif', 'jpe', 'stl',
              'pdn'],
    'ARCHIVE': ['7z', 'a', 'apk', 'ar', 'bz2', 'cab', 'cpio', 'deb', 'dmg', 'egg', 'gz', 'lha', 'mar',
                'pea', 'rar', 'rpm', 's7z', 'shar', 'tar', 'tbz2', 'tgz', 'tlz', 'war', 'whl', 'xpi', 'zip', 'zipx',
                'xz', 'pak'],
    'BOOK': ['mobi', 'epub', 'azw1', 'azw3', 'azw4', 'azw6', 'azw', 'cbr', 'cbz'],
    'TEXT': ['ebook', 'log', 'md', 'msg', 'odt', 'org', 'pages', 'rtf', 'rst', 'tex', 'txt',
             'wpd', 'wps'],
    'EXEC': ['exe', 'msi', 'bin', 'command', 'sh', 'bat', 'crx', 'com', 'appimage', 'run', 'apk', 'deb', 'rpm', 'jar'],
    'FONT': ['eot', 'otf', 'ttf', 'woff', 'woff2', "pf2"],
    'VIDEO': ['3g2', '3gp', 'aaf', 'asf', 'avchd', 'avi', 'drc', 'flv', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov',
              'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv', 'mxf', 'nsv', 'ogg', 'ogv', 'ogm', 'qt', 'rm', 'rmvb',
              'roq', 'srt', 'svi', 'vob', 'webm', 'wmv', 'yuv', 'mov'],
    'PDF': ['pdf'],
    'OFFICE': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'dot', 'dotx', 'docm', 'dotm', 'xlsm', 'xltm', 'xlam'],
    'ISO': ['iso', 'img', 'dmg'],
    'TORRENT': ['torrent'],
    'DATABASE': ['db', 'dbf', 'mdb', 'pdb'],
    'DATA': ['json', 'yaml', 'xml', 'yml'],
    'CONFIG': ['ini', 'cfg', 'conf', 'config', 'properties', 'prop', 'settings', 'inf' 'reg'],
    'DIAGRAMS': ['drawio', 'dtmp', 'nsd', 'fprg'],
    'BACKUP': ['bak'],
}


def select_folder():
    # print("Select a folder")
    root = tk.Tk()
    # print("Select a folder")
    root.withdraw()
    # print("Select a folder")
    path = filedialog.askdirectory(title="Select a folder", initialdir=f"/users/{os.getlogin()}/Downloads")
    # print("Select a folder")
    if path == "":
        print("No file selected")
        exit()
    else:
        return path


# SETTINGS
SORTED_FOLDER = "SORTED"
EXT_LIST_TYPE = ext_personal  # ext_typical or ext_personal
EXCLUDE = ["desktop.ini", "Thumbs.db", "Thumbs.db:encryptable", "Thumbs.db:encryptable\$DATA",
           SORTED_FOLDER]

if __name__ == "__main__":
    print("This is a module for file_management/app.py")
    exit()
