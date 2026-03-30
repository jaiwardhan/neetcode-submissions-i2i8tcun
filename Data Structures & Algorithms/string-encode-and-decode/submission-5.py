class Solution:

    ENC_TEMPLATE = "%c+_%d-_"
    NOONEHERE = "-NOONE-"

    def encode(self, strs: List[str]) -> str:
        def word_encoder(w):
            # If the word is "" -> ""
            enc_s = ""
            if w == "":
                return enc_s

            ch = w[0]
            count = 1
            for i in range(1, len(w)):
                if w[i] == ch:
                    count += 1
                else:
                    enc_s += Solution.ENC_TEMPLATE%(ch, count)
                    ch = w[i]
                    count = 1
            # The last one would not have been written
            enc_s += Solution.ENC_TEMPLATE%(ch, count)
            print("Encoded ",w,"into", enc_s)
            return enc_s
        
        def transmission_helper(encoded_stuff):
            return "=_".join(encoded_stuff)

        encoded_vals = []
        if len(strs) == 0:
            return Solution.NOONEHERE
        for w in strs:
            encoded_vals.append(word_encoder(w))
        
        return transmission_helper(encoded_vals)

    def decode(self, s: str) -> List[str]:
        def word_decoder(s):
            # We know that every character is added appended with --, so split on it
            op = ""
            for p in s.split("-_"):
                if p == "":
                    op += ""
                    continue
                w_parts = p.split("+_")
                op += str(w_parts[0])*int(w_parts[1])
            return op
        
        def transmission_helper(encoded_stuff):
            return encoded_stuff.split("=_")
        
        op = []
        if s == Solution.NOONEHERE:
            return op
        parts = transmission_helper(s)
        for p in parts:
            op.append(word_decoder(p))
        
        return op


"""
aaaabbbbcc -> a4b4c2
abc -> a1b1c1


Encoder:
-> Get the chars, encode the repition number for each word
-> Append encoded words by a delimiter __ (double _)

Decoder:
-> Break by delimiter
-> Decode each part by similar logic


COmplexity:
-> O(n) run for encoding all chars (sum of len of all words)
  -> Joining them
  -> Cutting them 
  -> decoding
 
constraints and cases:
- 100 words of 200 length -> 20000
- [""] -> [""]
- () nothing -> nothing
"""