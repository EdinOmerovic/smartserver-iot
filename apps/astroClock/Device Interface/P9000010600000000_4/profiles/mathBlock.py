# Copyright (C) 2013-2021 Echelon Corporation.  All Rights Reserved.
# Use of this code is subject to your compliance with the terms of the
# Echelon IzoT(tm) Software Developer's Kit License Agreement which is
# available at www.echelon.com/license/izot_sdk/.

# IzoT resources contained in this file are generated by an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.
# Names of resources and fields or members defined within a resource are
# derived from the same sources.  Names, capitalization and aspects of source
# code formatting may fail to comply with PEP-8 and PEP-257 recommendations
# due to the automated generation of these IzoT definitions.
# Generated at 25-Aug-2021 13:17.

"""mathBlock userdefined profile, originally defined in resource file set
apollodev 90:00:01:06:00:00:00:00-4."""


import izot.resources.base
from P9000010600000000_4.userdefined import userdefined
import izot.resources.datapoints.count_inc
import izot.resources.datapoints.str_asc
import P9000010600000000_4.properties.mathOp


class mathBlock(izot.resources.base.Profile):
    """mathBlock userdefined profile.  """

    def __init__(self):
        super().__init__(
            key=20006,
            scope=4
        )
        self.datapoints['nviOperand_1'] = izot.resources.base.Profile.DatapointMember(
            doc="""Increment count.  """,
            name='nviOperand_1',
            profile=self,
            number=1,
            datatype=izot.resources.datapoints.count_inc.count_inc,
            mandatory=True,
            direction=izot.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nviOperand_2'] = izot.resources.base.Profile.DatapointMember(
            doc="""Increment count.  """,
            name='nviOperand_2',
            profile=self,
            number=2,
            datatype=izot.resources.datapoints.count_inc.count_inc,
            mandatory=True,
            direction=izot.resources.base.Profile.DatapointMember.INPUT
        )
        self.datapoints['nvoResult'] = izot.resources.base.Profile.DatapointMember(
            doc="""Increment count.  """,
            name='nvoResult',
            profile=self,
            number=3,
            datatype=izot.resources.datapoints.count_inc.count_inc,
            mandatory=True,
            direction=izot.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.datapoints['nvoError'] = izot.resources.base.Profile.DatapointMember(
            doc="""Character string (30 characters max) """,
            name='nvoError',
            profile=self,
            number=4,
            datatype=izot.resources.datapoints.str_asc.str_asc,
            mandatory=True,
            direction=izot.resources.base.Profile.DatapointMember.OUTPUT
        )
        self.properties['cpOperator'] = izot.resources.base.Profile.PropertyMember(
            doc=""" """,
            name='cpOperator',
            profile=self,
            number=1,
            datatype=P9000010600000000_4.properties.mathOp.mathOp,
            minimum=b'\x00',
            maximum=b'\x03',
            default=b'\x00',
            mandatory=True
        )
        self._original_name = 'UFPTmathBlock'
        self._definition = userdefined.add(self)
        self.finalize()


if __name__ == '__main__':
    # unit test code.
    item = mathBlock()
    pass
