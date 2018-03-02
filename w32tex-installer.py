import tarfile
import os
import wget

def download_file(file_name, url_prefix, archive_prefix, texmf_prefix):
    print("Downloading '%s'" % file_name)
    url_name = "%s/%s" % (url_prefix, file_name)
    archive_name = "%s/%s" % (archive_prefix, file_name)
    wget.download(url_name, out=archive_name)
    with tarfile.open(archive_name) as tar:
        for i in tar:
            print(i.name)
            if i.isreg():
                tar.extract(i, path=texmf_prefix)
            if i.isdir():
                if os.path.exists("%s/%s" % (texmf_prefix, i.name)) == False:
                    os.mkdir("%s/%s" % (texmf_prefix, i.name))

if __name__ == "__main__":
    if os.path.exists("archive") == False:
        os.mkdir("archive")
    if os.path.exists("w32tex") == False:
        os.mkdir("w32tex")
    packages = ["latex.tar.xz", "mftools.tar.xz", "platex.tar.xz", "pdftex-w32.tar.xz", "ptex-w32.tar.xz", "web2c-lib.tar.xz", "web2c-w32.tar.xz"]
    for pkg in packages:
        download_file(pkg, "http://ctan.ijs.si/mirror/w32tex/current/", "archive", "w32tex")


