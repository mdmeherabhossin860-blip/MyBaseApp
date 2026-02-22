name: Skeleton Build
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build APK
        uses: ArtemSerebrennikov/buildozer-action@v1
        with:
          buildozer_version: stable
          command: buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: MyEmptyApp
          path: bin/*.apk
