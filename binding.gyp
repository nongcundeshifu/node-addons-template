{

  "targets": [
    {
      "target_name": "addonsName",
      "sources": [
        "./addons/library.cpp",
      ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "include_dirs": [
        "include",
        "<!(node -p \"require('node-addon-api').include_dir\")"
      ],
      "defines": [
        "_HAS_EXCEPTIONS=1",
      ],
      "conditions": [
        ['OS=="win"', {
          "variables": {
            "PROJECT_ROOT": "<!(node -p \"process.cwd()\")"
          },
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1
            },
          },
          "libraries": [
            "<(PROJECT_ROOT)\\lib\\test.lib"
          ],
        }]
      ]
    }
  ],
}