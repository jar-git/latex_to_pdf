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
import subprocess
import latex_to_pdf
import shutil


class Latex(latex_to_pdf.Document):
    def __init__(self, document_directory, latex="latex", bibtex="bibtex"):
        # Initialize Document class
        super().__init__(document_directory)
        # Initialize attributes
        self.latex = latex
        self.latex_arguments = ["-halt-on-error"]
        self.bibtex = bibtex

    def to_pdf(self, output_directory):
        print('Generating PDF for document: "{}"'.format(self.name))

        # Get the absolute path to the output directory.
        absolute_output_directory = os.path.abspath(output_directory)

        # Define the temporary directory for the build.
        temporary_directory = "build"

        # Create arguments for latex, copy to avoid clean up.
        arguments = self.latex_arguments
        arguments.append("-output-format=pdf")
        arguments.append("-output-directory=" + temporary_directory)
        arguments.append(self.name + ".tex")

        # Save the current working directory
        working_directory = os.getcwd()

        # Get the document directory and change the working directory to the document directory. This is required to
        # make the latex input commands work (latex and bibtex cannot seem to handle relative directories).
        os.chdir(self.directory)

        # Make a temporary build directory to the current directory.
        os.makedirs(temporary_directory, exist_ok=True)

        # Direct the out put to dev/null (latex is very verbose).
        with open(os.devnull, "w") as devnull:
            # Call latex to generate the aux file for bibtex.
            subprocess.call([self.latex] + self.latex_arguments, stdout=devnull)

            # Create references and cites with bibtex from the aux file.
            subprocess.call([self.bibtex, temporary_directory + "/" + self.name + ".aux"], stdout=devnull)

            # Re-run latex to generate bibtex references correctly (when in doubt, run it twice?).
            subprocess.call([self.latex] + self.latex_arguments, stdout=devnull)
            subprocess.call([self.latex] + self.latex_arguments, stdout=devnull)

        # Copy the output and move to parent directory because bibtex won't work otherwise.
        shutil.rmtree(absolute_output_directory, ignore_errors=True)
        shutil.copytree(temporary_directory, absolute_output_directory)
        shutil.rmtree(temporary_directory)

        print('Generated PDF for document "{}" to directory: {}'.format(self.name, output_directory))

        # Go back to the previous working directory before returning.
        os.chdir(working_directory)
