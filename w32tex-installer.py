import tarfile
import os, sys
import wget

def download_file(package, url_prefix, archive_prefix, texmf_prefix):
    file_name, file_desc = package
    print("Downloading '%s' (%s) ..." % (file_name, file_desc))
    url_name = "%s/%s" % (url_prefix, file_name)
    archive_name = "%s/%s" % (archive_prefix, file_name)
    wget.download(url_name, out=archive_name)
    print("")

    with tarfile.open(archive_name) as tar:
        for i in tar:
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
    packages = [("latex.tar.xz", "LaTeX 2016/03/31 patch level 2"),
                ("mftools.tar.xz", "mktexmf, mktextfm, mktexpk and ps2pk"),
                ("platex.tar.xz", "pLaTeX by Japanese TeX Development Community"),
                ("pdftex-w32.tar.xz", "pdfTeX and jbig2.exe"),
                ("ptex-w32.tar.xz", "pTeX by Japanese TeX Development Community"),
                ("web2c-lib.tar.xz", "Basic library files of TeX"),
                ("web2c-w32.tar.xz", "Binary files of TeX and its friends"),
                ("datetime2.tar.xz", "datetime2 package for LaTeX"),
                ("dvipdfm-w32.tar.xz", "DVI to PDF driver dvipdfmx"),
                ("dvipsk-w32.tar.xz", "DVI to PS driver dvipsk"),
                ("jtex-w32.tar.xz", "NTT-jTeX by T. Sakurai"),
                ("ltxpkgdocs.tar.xz", "Documents on Basic packages for LaTeX"),
                ("ltxpkgs.tar.xz", "Basic packages for LaTeX"),
                ("luatexja.tar.xz", "luatex-ja package by H. Kitagawa et al."),
                ("luatex-w32.tar.xz", "LuaTeX by Taco Hoekwater et al."),
                ("makeindex-w32.tar.xz", "makeindex programs (makeindex, mendex, upmendex)"),
                ("manual.tar.xz", "Manual files"),
                ("newtxpx-boondoxfonts.tar.xz", "newtx, newpx, and boondox fonts"),
                ("pgfcontrib.tar.xz", "pgf, tikz tools"),
                ("t1fonts.tar.xz", "Type1 fonts of cm, ams and others"),
                ("tex-gyre.tar.xz", "tex-gyre and tex-gyre-math fonts"),
                ("timesnew.tar.xz", "tfm and vf for TimesNewRoman and Arial (PFB)"),
                ("ttf2pk-w32.tar.xz", "TrueType to PK driver"),
                ("txpx-pazofonts.tar.xz", "TX fonts, PX fonts and mathpazo fonts"),
                ("xetex-w32.tar.xz", "XeTeX by Jonathan Kew"),
                ("xindy-w32.tar.xz", "Indexing system XINDY by Joachim Schrod"),
                ("xypic.tar.xz", "xypic package"),
                ("aleph-w32.tar.xz", "Aleph ( e-TeX 2.1 + Omega 1.15 )"),
                ("biblatex-biber.tar.xz", "biblatex and biber.exe"),
                ("cbfonts.tar.xz", "cbgreek font"),
                ("cjkzr.tar.xz", "CJK package and various packages by T. Yato"),
                ("context-doc.tar.xz", "Documents on ConTeXt by Pragma ADE"),
                ("context.tar.xz", "ConTeXt by Pragma ADE"),
                ("cweb-w32.tar.xz", "CWEB by D. Knuth and S. Levy and CTIE by J. Gilbey"),
                ("dvi2ps-w32.tar.xz", "DVI to PS driver by T. Sakurai"),
                ("dvi2tty-w32.tar.xz", "DVI to TTY driver"),
                ("dvitools-w32.tar.xz", "dvidvi, dv2dt, dt2dv, dvipng, dvisvgm etc."),
                ("gregorio-w32.tar.xz", "Gregorio by Elie Roux et al."),
                ("lcdf-typetools-w32.tar.xz", "LCDF Typetools by Eddie Kohler"),
                ("luajittex-w32.tar.xz", "LuaJITTeX by Luigi Scarso"),
                ("minitoc.tar.xz", "minitoc package"),
                ("m-tx.tar.xz", "M-Tx preprocessor by Dirk Laurie"),
                ("omegaj-w32.tar.xz", "Omega with Japanese support"),
                ("otfbeta.tar.xz", "latest version of OTF package by S. Saito"),
                ("plain2-2.54-w32.tar.xz", "text to TeX or NROFF translator"),
                ("pmx.tar.xz", "pmx preprocessor for musixtex by Don Simons"),
                ("pstricks.tar.xz", "PSTricks"),
                ("pstoedit-w32.tar.xz", "pstoedit 3.70 by Wolfgang Glunz"),
                ("psutils-w32.tar.xz", "PostScript utilities by Angus Duggan, Reuben Thomas"),
                ("ptex-ng-w32.tar.xz", "ptex-ng by Clerk Ma"),
                ("qpdf-w32.tar.xz", "qpdf by Jay Berkenbilt"),
                ("sam2p-w32.tar.xz", "sam2p by Szabo Peter"),
                ("t1utils-w32.tar.xz", "LCDF Type1 font utilities by Eddie Kohler"),
                ("tex4htk-w32.tar.xz", "TeX4ht for Win32"),
                ("texinfotools-w32.tar.xz", "Texinfo tools with Japanese support"),
                ("tiff2png-w32.tar.xz", "TIFF to PNG driver"),
                ("ttf2pt1-w32.tar.xz", "TrueType to Type1 converter ttf2pt1"),
                ("tuftelatex.tar.xz", "Tufte-latex package"),
                ("txtutil.tar.xz", "End-Of-Line character changer"),
                ("ums.tar.xz", "ums package by A. Inagaki"),
                ("uptex-w32.tar.xz", "Unicode pTeX by Takuji Tanaka"),
                ("utf.tar.xz", "UTF package by S. Saito"),
                ("vf-n2bk.tar.xz", "Virtual fonts to be used by NTT-jTeX and dvipsk"),
                ("xymtex.tar.xz", "XyMTeX package by S. Fujita"),
                ]
    for pkg in packages:
        download_file(pkg, "https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/win32/w32tex/", "archive", "w32tex")


