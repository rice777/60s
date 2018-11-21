# -*- coding:utf-8 -*-
# -*- mode: python -*-

block_cipher = None

added_files = [
         ('resources\\*.ico', 'resources'),
         ('resources\\images\\*.png', 'resources\\images'),
         ('resources\\audios\\*.mp3', 'resources\\audios'),
         ('resources\\audios\\*.ogg', 'resources\\audios'),
         ]

a = Analysis(['60s.py'],
             pathex=['D:\\60s'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='60s',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='resources\\icon.ico',
          version='file_version_info.txt')