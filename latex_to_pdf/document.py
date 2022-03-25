# Copyright 2017 Jani Arola, All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import shutil


class Document(object):
    @staticmethod
    def __get_document(document_directory):
        # If the path does not exist, return an empty document name.
        if not os.path.exists(document_directory):
            return ""
        # Otherwise, look for the document name from the directory.
        for file in os.listdir(document_directory):
            if file.endswith(".tex") and file != "packages.tex":
                return os.path.splitext(file)[0]
        # If document file does not exist, raise an error because this directory would be halfway done.
        raise RuntimeError('Cannot get document name from directory: {}'.format(document_directory))

    def __init__(self, document_directory):
        self.name = Document.__get_document(document_directory)
        self.directory = document_directory

    def exists(self):
        return os.path.exists(self.directory) and os.path.isdir(self.directory)

    def must_exist(self):
        if not self.exists():
            raise RuntimeError('Document "{}" does not exist in directory: {}'.format(self.name, self.directory))

    def copy(self, target_directory):
        # Check that this document exists.
        self.must_exist()
        # Copy the document directory to the target directory.
        shutil.copytree(self.directory, target_directory)
