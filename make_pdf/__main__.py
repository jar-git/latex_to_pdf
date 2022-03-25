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
import sys
import make_pdf


def main(args=None):
    try:
        # Create latex document from the second CLI arguments.
        document = make_pdf.Latex(sys.argv[1])

        # Check that document exists, cannot build PDF from non-existing document.
        document.must_exist()

        # Make a build directory with the document name to differentiate between documentation types.
        output_directory = "build/" + document.name

        # Generate pdf from the latex document.
        document.to_pdf(output_directory)

    except IndexError:
        print("usage: make_pdf <documentation_directory>")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
