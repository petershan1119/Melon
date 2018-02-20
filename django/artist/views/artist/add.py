from django.shortcuts import render, redirect
from ...models import Artist

__all__ = (
    'artist_add',
)


def artist_add(request):
    # Artist클래스가 받을 수 있는 모든 input을 구현
    # img_pofile은 제외
    # method가 POST면 request.POST에서 해당 데이터 처리
    # 새 Artist객체 만들고 artist_list 이동
    # method가 GET이면 artist_add.html표시

    # context = {}

    # if request.method == 'POST':
    #     name = request.POST['name']
    #     real_name = request.POST['real_name']
    #     nationality = request.POST['nationality']
    #     birth_date = datetime.datetime.strptime(request.POST['birth_date'],  '%Y-%m-%d')
    #     # birth_date = request.POST['birth_date']
    #     constellation = request.POST['constellation']
    #     blood_type = request.POST['blood_type']
    #     intro = request.POST['intro']
    #
    #     artist = Artist.objects.create(
    #         name=name,
    #         real_name=real_name,
    #         nationality=nationality,
    #         birth_date=birth_date,
    #         constellation=constellation,
    #         blood_type=blood_type,
    #         intro=intro,
    #     )
    #     return redirect('artist:artist-list')
    #
    # # context['form_error'] = "제목이나 내용을 입력해주세요."
    #
    # return render(request, 'artist/artist_add.html')

    if request.method == 'POST':
        name = request.POST['name']
        Artist.objects.create(
            name=name,
        )
        return redirect('artist:artist-list')
    else:
        return render(request, 'artist/artist_add.html')
