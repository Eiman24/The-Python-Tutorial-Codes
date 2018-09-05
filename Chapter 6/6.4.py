'''
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
'''
# From the surround module for example, you might use:

# 在同一个父级中导入
from . import echo
# 在父级的父级中导入
from .. import formats
# 在与同父级相同层级的父级中导入子级
from ..filters import equalizer