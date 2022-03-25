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
import setuptools

setuptools.setup(
    name='latex_to_pdf',
    version='0.1.0',
    packages=setuptools.find_packages(exclude=('test',)),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'latex_to_pdf = latex_to_pdf.__main__:main',
        ],
    },
    zip_safe=True
)
