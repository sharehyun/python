# bool, int, float, str
# list - 배열

a = "바나나"
fruit = ["사과", "배", "딸기",'포도']
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])

item = [
    {"galContentId":"2586952","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/52/2586952.jpg","galCreatedtime":"20190109152342","galModifiedtime":"20190109152354","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586949","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/49/2586949.jpg","galCreatedtime":"20190109152321","galModifiedtime":"20190109152332","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586948","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/48/2586948.jpg","galCreatedtime":"20190109152256","galModifiedtime":"20190109152311","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586938","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/38/2586938.jpg","galCreatedtime":"20190109152129","galModifiedtime":"20190109152253","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586944","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/44/2586944.jpg","galCreatedtime":"20190109152218","galModifiedtime":"20190109152232","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586942","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/42/2586942.jpg","galCreatedtime":"20190109152156","galModifiedtime":"20190109152207","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586935","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/35/2586935.jpg","galCreatedtime":"20190109152104","galModifiedtime":"20190109152117","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586932","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/32/2586932.jpg","galCreatedtime":"20190109152021","galModifiedtime":"20190109152054","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586923","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/23/2586923.jpg","galCreatedtime":"20190109151829","galModifiedtime":"20190109151915","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"},
{"galContentId":"2586914","galContentTypeId":"17","galTitle":"서울빛초롱축제","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/14/2586914.jpg","galCreatedtime":"20190109151703","galModifiedtime":"20190109151720","galPhotographyMonth":"201811","galPhotographyLocation":"서울특별시 종로구","galPhotographer":"라이브스튜디오","galSearchKeyword":"서울빛초롱축제, 서울특별시 종로구, 2018 하반기 기획사진, 청계천 야경, 서울 등 축제, 서울 축제"}
]

# dict타입
print(item[0]['galTitle'])


#2,4,6,8번째 방의 값들의 합을 구하시오.
num = [1,2,3,4,5,6,7,8,9]
print(num[2]+num[4]+num[6]+num[8])

in_num = int(input("숫자를 입력하시오.>> "))
if in_num in num:
    print("{}번 숫자가 있습니다.".format(in_num))
else:
    print("{}번 숫자는 없습니다.".format(in_num))