# Copyright (c) 2014, David B. Curtis
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""Standard drill reference data."""

from collections import namedtuple

USNumberLetterDrill = namedtuple('USNumberLetterDrill',
        'number inch_size')

us_number_letter_drills = [
    USNumberLetterDrill('#80', 0.0135),
    USNumberLetterDrill('#79', 0.0145),
    USNumberLetterDrill('#78', 0.016),
    USNumberLetterDrill('#77', 0.018),
    USNumberLetterDrill('#76', 0.020),
    USNumberLetterDrill('#75', 0.021),
    USNumberLetterDrill('#74', 0.0225),
    USNumberLetterDrill('#73', 0.024),
    USNumberLetterDrill('#72', 0.025),
    USNumberLetterDrill('#71', 0.026),
    USNumberLetterDrill('#70', 0.028),
    USNumberLetterDrill('#69', 0.0292),
    USNumberLetterDrill('#68', 0.031),
    USNumberLetterDrill('#67', 0.032),
    USNumberLetterDrill('#66', 0.033),
    USNumberLetterDrill('#65', 0.035),
    USNumberLetterDrill('#64', 0.036),
    USNumberLetterDrill('#63', 0.037),
    USNumberLetterDrill('#62', 0.038),
    USNumberLetterDrill('#61', 0.039),
    USNumberLetterDrill('#60', 0.040),
    USNumberLetterDrill('#59', 0.041),
    USNumberLetterDrill('#58', 0.042),
    USNumberLetterDrill('#57', 0.043),
    USNumberLetterDrill('#56', 0.0465),
    USNumberLetterDrill('#55', 0.052),
    USNumberLetterDrill('#54', 0.055),
    USNumberLetterDrill('#53', 0.0595),
    USNumberLetterDrill('#52', 0.0635),
    USNumberLetterDrill('#51', 0.067),
    USNumberLetterDrill('#50', 0.070),
    USNumberLetterDrill('#49', 0.073),
    USNumberLetterDrill('#48', 0.076),
    USNumberLetterDrill('#47', 0.0785),
    USNumberLetterDrill('#46', 0.081),
    USNumberLetterDrill('#45', 0.082),
    USNumberLetterDrill('#44', 0.086),
    USNumberLetterDrill('#43', 0.089),
    USNumberLetterDrill('#42', 0.0935),
    USNumberLetterDrill('#41', 0.096),
    USNumberLetterDrill('#40', 0.098),
    USNumberLetterDrill('#39', 0.0995),
    USNumberLetterDrill('#38', 0.1015),
    USNumberLetterDrill('#37', 0.104),
    USNumberLetterDrill('#36', 0.1065),
    USNumberLetterDrill('#35', 0.110),
    USNumberLetterDrill('#34', 0.111),
    USNumberLetterDrill('#33', 0.113),
    USNumberLetterDrill('#32', 0.116),
    USNumberLetterDrill('#31', 0.120),
    USNumberLetterDrill('#30', 0.1285),
    USNumberLetterDrill('#29', 0.136),
    USNumberLetterDrill('#28', 0.1405),
    USNumberLetterDrill('#27', 0.144),
    USNumberLetterDrill('#26', 0.147),
    USNumberLetterDrill('#25', 0.1495),
    USNumberLetterDrill('#24', 0.152),
    USNumberLetterDrill('#23', 0.154),
    USNumberLetterDrill('#22', 0.157),
    USNumberLetterDrill('#21', 0.159),
    USNumberLetterDrill('#20', 0.161),
    USNumberLetterDrill('#19', 0.166),
    USNumberLetterDrill('#18', 0.1695),
    USNumberLetterDrill('#17', 0.173),
    USNumberLetterDrill('#16', 0.177),
    USNumberLetterDrill('#15', 0.180),
    USNumberLetterDrill('#14', 0.182),
    USNumberLetterDrill('#13', 0.185),
    USNumberLetterDrill('#12', 0.189),
    USNumberLetterDrill('#11', 0.191),
    USNumberLetterDrill('#10', 0.1935),
    USNumberLetterDrill('#9', 0.196),
    USNumberLetterDrill('#8', 0.199),
    USNumberLetterDrill('#7', 0.201),
    USNumberLetterDrill('#6', 0.204),
    USNumberLetterDrill('#5', 0.2055),
    USNumberLetterDrill('#4', 0.209),
    USNumberLetterDrill('#3', 0.213),
    USNumberLetterDrill('#2', 0.221),
    USNumberLetterDrill('#1', 0.228),
    USNumberLetterDrill('#A', 0.234),
    USNumberLetterDrill('#B', 0.238),
    USNumberLetterDrill('#C', 0.242),
    USNumberLetterDrill('#D', 0.246),
    USNumberLetterDrill('#E', 0.250),
    USNumberLetterDrill('#F', 0.257),
    USNumberLetterDrill('#G', 0.261),
    USNumberLetterDrill('#H', 0.266),
    USNumberLetterDrill('#I', 0.272),
    USNumberLetterDrill('#J', 0.277),
    USNumberLetterDrill('#K', 0.281),
    USNumberLetterDrill('#L', 0.290),
    USNumberLetterDrill('#M', 0.295),
    USNumberLetterDrill('#N', 0.302),
    USNumberLetterDrill('#O', 0.316),
    USNumberLetterDrill('#P', 0.323),
    USNumberLetterDrill('#Q', 0.332),
    USNumberLetterDrill('#R', 0.339),
    USNumberLetterDrill('#S', 0.348),
    USNumberLetterDrill('#T', 0.358),
    USNumberLetterDrill('#U', 0.368),
    USNumberLetterDrill('#V', 0.377),
    USNumberLetterDrill('#W', 0.386),
    USNumberLetterDrill('#X', 0.397),
    USNumberLetterDrill('#Y', 0.404),
    USNumberLetterDrill('#Z', 0.413),
]
