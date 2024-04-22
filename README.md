
# This is a fork of the flatbuffers project used for OctoEverywhere.

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

### Dev Help

Building pip packages:
https://realpython.com/pypi-publish-python-package/#preparing-your-package-for-publication

Building flatbuffers:
https://google.github.io/flatbuffers/flatbuffers_guide_building.html

Use `cmake -G "Visual Studio 16" -DCMAKE_BUILD_TYPE=Release` - for vs2019
No newline at end of file
