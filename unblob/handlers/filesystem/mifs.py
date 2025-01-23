from ...models import File, HexString, StructHandler, ValidChunk
from ...extractors import Command
from unblob.file_utils import InvalidInputFormat
from typing import Optional
from pathlib import Path
from structlog import get_logger

logger = get_logger()

custum_tools = Path(__file__).parent.parent.parent / "custum_tools"
mifs_extractor = str(custum_tools / "dumpifs")

class MIFSHandler(StructHandler):
    NAME = "mifs"

    PATTERNS = [HexString("41 52 4d 64 41 52 4d 64 41 52 4d 64 41 52 4d 64")]
    
    C_DEFINITIONS = ""

    HEADER_STRUCT = ""
    
    EXTRACTOR = Command(mifs_extractor, "{inpath}", "-d", "{outdir}")

    def calculate_chunk(self, file: File, start_offset: int) -> Optional[ValidChunk]:
        
        #返回一个ValidChunk对象，表示整个文件都是有效的
        return ValidChunk(
            start_offset=0,
            end_offset=file.size(),
        )