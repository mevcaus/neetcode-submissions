class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += str(len(word)) + "#" + word
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        current_string = ""
        current_word_length = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                current_word_length += s[i]
                i += 1
            else:
                ret.append(s[i + 1: i + 1 + int(current_word_length)])
                i += int(current_word_length) + 1
                current_word_length = ""  
        return ret
            
