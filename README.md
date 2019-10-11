# note-app

__To run program create batch file with code:__
```
@echo off
pushd <path_to_file>\note_app\notes
python ..\app.py %1 %2 %3
popd
```