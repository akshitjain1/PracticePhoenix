from typing import List


class MessageChunker:

    @staticmethod
    def chunk_message(text: str, max_length: int = 4000) -> List[str]:
        if not text:
            return []
        if len(text) <= max_length:
            return [text]

        chunks: List[str] = []
        paragraphs = text.split("\n\n")
        current_chunk = ""

        for para in paragraphs:
            separator = "\n\n" if current_chunk else ""
            if len(current_chunk) + len(separator) + len(para) <= max_length:
                current_chunk += f"{separator}{para}"
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""

                if len(para) <= max_length:
                    current_chunk = para
                else:
                    lines = para.split("\n")
                    for line in lines:
                        line_sep = "\n" if current_chunk else ""
                        if len(current_chunk) + len(line_sep) + len(line) <= max_length:
                            current_chunk += f"{line_sep}{line}"
                        else:
                            if current_chunk:
                                chunks.append(current_chunk)
                                current_chunk = ""
                            if len(line) <= max_length:
                                current_chunk = line
                            else:
                                while len(line) > max_length:
                                    chunks.append(line[:max_length])
                                    line = line[max_length:]
                                current_chunk = line

        if current_chunk:
            chunks.append(current_chunk)

        return chunks
