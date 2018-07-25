#!/usr/bin/env python
#
# Copyright 2018 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import optparse
import os
import sys

REPOSITORY_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', '..', '..', '..'))

sys.path.append(os.path.join(REPOSITORY_ROOT, 'build', 'android', 'gyp',
                             'util'))
import build_utils


def BuildWithGradle(options):
  gradle_path = os.path.join(REPOSITORY_ROOT, 'third_party', 'gradle_wrapper',
                             'gradlew')
  gradle_cmd = [gradle_path, 'assembleDebug', 'assembleAndroidTest']
  build_utils.CheckOutput(gradle_cmd, cwd=options.project_dir)


def main():
  parser = optparse.OptionParser()
  build_utils.AddDepfileOption(parser)
  parser.add_option('--project-dir', help='Gradle project directory.')
  parser.add_option('--stamp', help='Path to touch on success.')

  options, _ = parser.parse_args()

  BuildWithGradle(options)

  if options.depfile:
    assert options.stamp
    build_utils.WriteDepfile(options.depfile, options.stamp)

  if options.stamp:
    build_utils.Touch(options.stamp)


if __name__ == '__main__':
  sys.exit(main())

