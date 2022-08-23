# Copyright (c) 2022 Zhendong Peng (pzd17@tsinghua.org.cn)
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

from processors.cardinal import Cardinal
from processors.processor import Processor

from pynini.lib.pynutil import delete, insert


class Fraction(Processor):

    def __init__(self):
        super().__init__(name='fraction')
        self.build_tagger()
        self.build_verbalizer()

    def build_tagger(self):
        cardinal = Cardinal().cardinal
        tagger = (insert('numerator: "') + cardinal + delete(' ').ques +
                  delete('/') + delete(' ').ques + insert('" denominator: "') +
                  cardinal + insert('"')).optimize()
        self.tagger = self.add_tokens(tagger)

    def build_verbalizer(self):
        verbalizer = (delete('denominator: "') + self.SIGMA + delete('" ') +
                      insert('分之') + delete('numerator: "') + self.SIGMA +
                      delete('"'))
        self.verbalizer = self.delete_tokens(verbalizer)
