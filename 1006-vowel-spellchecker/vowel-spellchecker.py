class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_set=set(wordlist)
        case_map={}
        vowel_map={}
        def mask_vowels(word):
            vowels=set('aeiou')
            return ''.join('*' if ch in vowels else ch for ch in word)
        for word in wordlist:
            lower=word.lower()
            masked=mask_vowels(lower)
            if lower not in case_map:
                case_map[lower]=word
            if masked not in vowel_map:
                vowel_map[masked]=word
        ans=[]
        for q in queries:
            if q in words_set:
                ans.append(q)
            else:
                lower=q.lower()
                masked=mask_vowels(lower)
                if lower in case_map:
                    ans.append(case_map[lower])
                elif masked in vowel_map:
                    ans.append(vowel_map[masked])
                else:
                    ans.append("")
        return ans