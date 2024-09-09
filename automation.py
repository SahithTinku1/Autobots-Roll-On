import os
import shutil

path = "C:\\Users\\91984\\Downloads"
directories = os.listdir(path)

folders = ["Images", "Documents", "Pdfs", "PythonFiles"]
extensions = {
    "python": ["py"],
    "image": ["png", "jpeg", "jpg", "avif", "gif", "bmp", "tiff", "webp", "svg"],
    "pdf": ["pdf"],
    "documents": ["docx", "xlsx", "doc", "xls", "ppt", "pptx", "txt", "rtf", "odt", "ods", "odp", "csv"],
    "video": ["mp4", "mkv", "mov", "avi", "wmv", "flv", "webm", "mpeg"],
    "audio": ["mp3", "wav", "aac", "flac", "ogg", "m4a", "wma"],
    "archive": ["zip", "rar", "7z", "tar", "gz", "bz2"],
    "code": ["html", "css", "js", "ts", "json", "xml", "yml", "yaml", "java", "cpp", "c", "h", "php", "rb", "go", "sh", "bat"],
    "fonts": ["ttf", "otf", "woff", "woff2"],
    "executables": ["exe", "msi", "apk", "bat", "sh", "bin", "dmg"],
}


for folder in folders:
    if not os.path.exists(f"{path}\\{folder}"):
        os.makedirs(f"{path}\\{folder}")

if __name__ == "__main__":
    for file in directories:
        if os.path.isfile(f"{path}\\{file}"):
            ext_index = file.rfind(".")
            extension = file[ext_index + 1:]
            source = f"{path}\\{file}"

            if extension in extensions["documents"]:
                shutil.move(source, f"{path}\\Documents\\{file}")
            elif extension in extensions["python"]:
                shutil.move(source, f"{path}\\PythonFiles\\{file}")
            elif extension in extensions["image"]:
                shutil.move(source, f"{path}\\Images\\{file}")
            elif extension in extensions["pdf"]:
                shutil.move(source, f"{path}\\Pdfs\\{file}")
