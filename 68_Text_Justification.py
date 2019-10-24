class Solution:
    def fullJustify(self, words, maxWidth):
        split=[]
        string_len = 0
        each_row = []
        last_row = None
        while len(words) > 0:
            curr_len = words[0]
            if string_len + len(each_row) + len(curr_len) > maxWidth:
                split.append((string_len,each_row))
                string_len = 0
                each_row = []
            else:
                string_len += len(words[0])
                each_row.append(words.pop(0))
                if len(words) == 0:
                    last_row= (string_len,each_row)
        # print(split)
        # print(last_row)
        ret = []
        for row in split:
            normal_spaces = len(row[1]) - 1
            extra_spaces = maxWidth - row[0] - normal_spaces 
            if len(row[1]) < 2:
                space_arr = [0]
            else:
                space_arr = [1] * (len(row[1])-1)
            i = 0
            while(extra_spaces > 0):
                space_arr[i] += 1
                extra_spaces -= 1
                i+=1
                i %= len(space_arr)
            
            for index, space in enumerate(space_arr):
                row[1][index]+=(" "*space)

            ret.append("".join(row[1]))
        normal_spaces = len(last_row[1]) - 1
        extra_spaces = maxWidth - last_row[0] - normal_spaces
        ret.append(" ".join(last_row[1]) + " "*extra_spaces)

        return ret

                


s = Solution()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"],16))

                