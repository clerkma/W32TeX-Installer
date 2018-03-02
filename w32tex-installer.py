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
                texmf_name = "%s/%s" % (texmf_prefix, i.name)
                if not os.path.exists(texmf_name):
                    os.mkdir(texmf_name)

if __name__ == "__main__":
    if not os.path.exists("archive"):
        os.mkdir("archive")
    if not os.path.exists("w32tex"):
        os.mkdir("w32tex")
    packages = ["latex.tar.xz", "mftools.tar.xz", "platex.tar.xz",
                "pdftex-w32.tar.xz", "ptex-w32.tar.xz", "web2c-lib.tar.xz",
                "web2c-w32.tar.xz",
                "datetime2.tar.xz", "dvipdfm-w32.tar.xz", "dvipsk-w32.tar.xz",
                "jtex-w32.tar.xz", "ltxpkgdocs.tar.xz", "ltxpkgs.tar.xz",
                "luatexja.tar.xz", "luatex-w32.tar.xz", "makeindex-w32.tar.xz",
                "manual.tar.xz", "newtxpx-boondoxfonts.tar.xz", "pgfcontrib.tar.xz",
                "t1fonts.tar.xz", "tex-gyre.tar.xz", "timesnew.tar.xz",
                "ttf2pk-w32.tar.xz", "txpx-pazofonts.tar.xz", "xetex-w32.tar.xz",
                "xindy-w32.tar.xz", "xypic.tar.xz",
                "aleph-w32.tar.xz", "biblatex-biber.tar.xz", "cbfonts.tar.xz",
                "cjkzr.tar.xz", "context-doc.tar.xz", "context.tar.xz",
                "cweb-w32.tar.xz", "dvi2ps-w32.tar.xz", "dvi2tty-w32.tar.xz",
                "dvitools-w32.tar.xz", "gregorio-w32.tar.xz", "lcdf-typetools-w32.tar.xz",
                "luajittex-w32.tar.xz", "minitoc.tar.xz", "m-tx.tar.xz",
                "omegaj-w32.tar.xz", "otfbeta.tar.xz", "plain2-2.54-w32.tar.xz",
                "pmx.tar.xz", "pstricks.tar.xz", "pstoedit-w32.tar.xz",
                "psutils-w32.tar.xz", "ptex-ng-w32.tar.xz", "qpdf-w32.tar.xz",
                "sam2p-w32.tar.xz", "t1utils-w32.tar.xz", "tex4htk-w32.tar.xz",
                "texinfotools-w32.tar.xz", "tiff2png-w32.tar.xz", "ttf2pt1-w32.tar.xz",
                "tuftelatex.tar.xz", "txtutil.tar.xz", "ums.tar.xz",
                "uptex-w32.tar.xz", "utf.tar.xz", "vf-n2bk.tar.xz",
                "xymtex.tar.xz"]
    for pkg in packages:
        download_file(pkg, "http://ctan.ijs.si/mirror/w32tex/current/", "archive", "w32tex")


