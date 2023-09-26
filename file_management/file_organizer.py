import os
import shutil
import tkinter as tk
import tkinter.filedialog as filedialog

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
    'ARCHIVE': ['7z', 'a', 'apk', 'ar', 'bz2', 'cab', 'cpio', 'deb', 'dmg', 'egg', 'gz', 'iso', 'jar', 'lha', 'mar',
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
    'ARCHIVE': ['7z', 'a', 'apk', 'ar', 'bz2', 'cab', 'cpio', 'deb', 'dmg', 'egg', 'gz', 'iso', 'jar', 'lha', 'mar',
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

# SETTINGS
SORTED_FOLDER = "SORTED"
EXT_LIST_TYPE = ext_personal  # ext_typical or ext_personal
EXCLUDE = ["desktop.ini", "Thumbs.db", "Thumbs.db:encryptable", "Thumbs.db:encryptable\$DATA",
           SORTED_FOLDER]


# COUNTER
count = 0


def select_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory(title="Select a folder")
    if path == "":
        print("No file selected")
        exit()
    else:
        return path


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def move_files(src_path, path):
    global count
    try:
        shutil.move(src_path, path)
    except Exception as e:
        print(f"ERROR with: {path}")
        print(e)
    count += 1


def sort_files(ex, src_path, path):
    os.chdir(src_path)
    check_path(path)

    for item in os.listdir():
        if item in EXCLUDE:
            continue
        item_path = src_path + "/" + item
        if os.path.isfile(item_path):
            for cat, extension in ex.items():
                # print("EXT: " + str(extension))
                # print(item.split(".")[-1].lower())
                if item.split(".")[-1].lower() in extension:
                    print(f"FILE ({cat}): " + item)
                    check_path(path + "/" + cat)
                    move_files(item_path, path + "/" + cat.upper() + "/" + item)
                else:
                    break

            print(f"FILE (OTHER): " + item)
            check_path(path + "/OTHER")
            move_files(item_path, path + "/OTHER/" + item)

        elif os.path.isdir(item_path):
            print(f"FOLDER: " + item)
            check_path(path + "/FOLDERS")
            move_files(item_path, path + "/FOLDERS/" + item)


if __name__ == "__main__":
    folder_to_organize = select_folder()
    sort_files(EXT_LIST_TYPE, folder_to_organize, folder_to_organize + "/" + SORTED_FOLDER)
    print(f"Sorted {count} files/folders")

