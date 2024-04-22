
# This is a fork of the flatbuffers project used for [OctoEverywhere](https://octoeverywhere.com) and [Homeway](https://homeway.io).

### Why did we fork?
1) Due to OctoPrint plugin crazyness, where all plugins share the same dependency packages, versioning is hard. Since we needed to make changes to the py code gen anyways, the easiest way to fix the version collision problem was simply to fork and create our own flatbuffer lib.
2) We made minor changes in the python code gen and lib to not require numpy in order to get byte buffers efficiently.
3) We made minor changes to the C# code gen and lib to make accessing buffer more efficient with Memory objects.
4) Having our own repo / branch helps us keep flatbuffer version alignment between our client and server.

### Changes Made

1) Renamed things in /python/* to `octoflatbuffers`
2) Changed the python package files to reflect our fork
3) Update the flatc python language builder to use the octoflatbuffer package name
4) Added support for *AsByteArray in flatc
5) Added GetVectorAsByteArray to the python package.
6) Disabled numpy loading in the py package, since it was causing the plugin to fail loading if not fully installed (by some other plugin) and we don't use it.
7) Removed all refs to "octoflatbuffers.compat.import_numpy()" since that failed to resolve on some PY setups. (unclear 100% why this was happening)

### Dev Help

Building pip packages:
    - ref
        - https://realpython.com/pypi-publish-python-package/#preparing-your-package-for-publication
    - `python -m pip install build twine`
    - `cd <repo root>\python`
    - Update any refs to the old version (search the old version in all files and update)
    - Ensure the `.\dist` folder contains nothing.
    - `python -m build`
    - Copy the output .whl file to .zip and you can look at what was packaged.
    - `twine upload dist/*`

Building flatbuffers:
https://google.github.io/flatbuffers/flatbuffers_guide_building.html

Building/Updating the cflat compiler
- Build cmake `cmake -G "Visual Studio 17" -DCMAKE_BUILD_TYPE=Release`
    - If this fails "because it can't find VS22, make sure the C++ Desktop Workload" is installed in the VS installer.
- Open FlatBuffers.sln file in the root
- Build flatc in release
    - flatbuffers\Release\flatc.exe
- Copy into the OctoEverywhere-Protocol repo.
- If the cflat exe was updated and the flatbuffer version was updated, we must also update the checked in c# flatbuffers lib in the OctoEverywhere and Homeway service logic.

