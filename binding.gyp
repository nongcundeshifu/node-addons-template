{

  "targets": [
    {
      "target_name": "node_addons_template",
      "sources": [
        "./addons/addons.cpp",
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
          "configurations": {
            "Release": {
              "msvs_settings": {
                "VCCLCompilerTool": {
                  "ExceptionHandling": 1,
                  "RuntimeLibrary": '2',
                },
              }
            },
            "Debug": {
              "msvs_settings": {
                "VCCLCompilerTool": {
                  "ExceptionHandling": 1,
                  "RuntimeLibrary": '3',
                },
              }
            }
          },

          "libraries": [
            "<(PROJECT_ROOT)\\lib\\hello.lib",
          ],
        }]
      ],

    }
  ],
}