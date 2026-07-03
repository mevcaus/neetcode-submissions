class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + '#' + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] != "#":
                j += 1
            else:
                num_of_chars = int(s[i:j])
                decoded_str.append(s[j + 1: j + 1 + num_of_chars])
                i = j + 1 + num_of_chars
                j = i
        return decoded_str
