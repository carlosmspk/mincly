from mincly.io.common import (
    Io as _Io,
    Writer as _Writer,
    Reader as _Reader,
    HybridIo as _HybridIo,
)
from mincly.io.standard import (
    StandardTerminalReader as _StandardTerminalReader,
    StandardTerminalWriter as _StandardTerminalWriter,
    StandardTerminalIo as _StandardTerminalIo,
)
import typing as _t


class Menu:
    def __init__(
        self,
        input_output: _t.Optional[_Io] = None,
        input: _t.Optional[_Reader] = None,
        output: _t.Optional[_Writer] = None,
    ) -> None:
        self._io: _Io
        if input_output is not None:
            self._io = input_output
        elif input is not None or output is not None:
            input_or_standard = (
                input if input is not None else _StandardTerminalReader()
            )
            output_or_standard = (
                output if output is not None else _StandardTerminalWriter()
            )
            self._io = _HybridIo(input_or_standard, output_or_standard)
        else:
            self._io = _StandardTerminalIo()
