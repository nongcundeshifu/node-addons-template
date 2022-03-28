{

  "targets": [
    {
      "target_name": "addonsName",
      "sources": [
        "./addons/library.cpp",
      ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "include_dirs": ["<!(node -p \"require('node-addon-api').include_dir\")"],
      "defines": [
        "_HAS_EXCEPTIONS=1",
      ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        },
      }
    }
  ],
}