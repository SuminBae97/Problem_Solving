#
# #s = "abcabcabcabcdededededede"
#
# #
# def check_min_len(s,l):
#     al=[]
#     al =""
#     ct=1
#     temp=0
#     #new_ct=2
#     for i in range(0, len(s), l):
#         val = s[i:i + l]
#
#         #처음 삽입 그냥 그대로 insert
#         if i == 0:
#             al += (str(ct) + val)
#             temp=val
#             continue
#
#         #if i!=0 and val==s[:i-1]:
#         #if i!=0 and val == s[i:i+l+1]:
#         if i!=0 and val==temp:
#             ct+=1
#             #new_ct = new_ct+1
#             #al = al.replace(str(ct), str(ct + 1), 2)
#             al = al.replace((str(ct-1)+val) ,(str(ct)+val) )
#             temp=val
#             continue
#
#         #if i!=0 and val!=s[i:i+l+1]:
#         if i!=0 and val!=temp:
#             ct=1
#             al += str(ct) + val
#             temp=val
#             continue
#
#
#         else:
#             temp = al[-l]
#             if temp == val:
#                 al = al.replace(str(ct), str(ct + 1),2)
#                 #al[-l - 1] = str(ct + 1)
#
#             else:
#                 temp_ct = al[-l - 1:-l]
#                 al += str(ct) + val
#                 # al.append(str(ct))
#                 # al.append(val)
#
#     one_count = al.count("1")
#
#
#     return len(al)-one_count
#
#
# def solution(s):
#     min_answer= check_min_len(s,1)
#     for i in range(2,len(s)):
#         answer = check_min_len(s,i)
#         if answer < min_answer:
#             min_answer = answer
#
#     return min_answer
# # s="ababcdcdababcdcd"
# # #s="aabbaccc"
# # print(solution(s))
# # #print(check_min_len(s,1))
# #
#
#
# # l=8
# # s="ababcdcdababcdcd"
# # #
# # # s="aabbaccc"
# # # l=1
# # # ct=1
# #
# # for i in range(0,len(s),l):
# #     val = s[i:i+l]
# #
# #
# #     print(val)
# #
# #
#

def solution(s):
    length=[]
    result=""

    if len(s)==1:
        return 1

    for cut in range(1,len(s)//2+1):
        count=1
        tempstr = s[:cut]
        for i in range(cut,len(s),cut):
            if tempstr==s[i:i+cut]:
                count+=1

            else:
                if count==1:
                    count=""
                result+=str(count)+tempstr
                tempstr = s[i:i+cut]
                count=1
        if count==1:
            count=""
        result +=str(count)+tempstr
        length.append(len(result))
        result=""
    return min(length)





습