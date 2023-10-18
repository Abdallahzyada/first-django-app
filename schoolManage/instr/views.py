from django.shortcuts import render
# from django.http import HttpResponse,HttpResponseRedirect
# from .models import *



def Main(request):
    return render(request,'index.html',context={})

# def instractorList(request):
#     context = {}
#     inst = Instructor.objects.all()
#     context['inst'] = inst
#     return render(request,'Instrc/instrcList.html', context)

# def instractorAdd(request):
#     context={}
#     if(request.method=='POST'):
#         if(request.POST['name'] is not None):
#             Instructor.objects.create(name=request.POST['name'])
#             return  HttpResponseRedirect('/Instrc/List')
#         else:
#             context['msg']='must enter Instrctor name'
#     return  render(request,'Instrc/instrcAdd.html')

# def instractorUpdate(request , id):
#     return HttpResponse("instractor "+str(id)+" update!")


# def instractorDelete(request , id):
#     Instructor.objects.filter(id=id).delete()
#     return  HttpResponseRedirect('/Instrc/List')



from .models import *
from rest_framework.response import Response
from  rest_framework.decorators import api_view
from rest_framework import status
from .instrSerlizer import *


@api_view(['GET'])
def List(req):
    #create serizeler
    itd=Instructor.objects.all()
    itdseriz=InstrSerlizer(itd,many=True)
    return  Response({'Data':itdseriz.data,'msg':'all Instructors'})

@api_view(['GET'])
def Listbyid(req,id):
    itd=Instructor.objects.filter(id=id).first()
    serlizerdata=InstrSerlizer(itd)
    return Response({'data':serlizerdata.data},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET'])
def Add(req):
    if(req.method=='GET'):
        return  Response({'name':'value string'})
    else:
        data=req.data
        sr=InstrSerlizer(data=req.data)
        if(sr.is_valid()):
            sr.save()
        else:
            return Response(sr.data, status=status.HTTP_404_NOT_FOUND)

        return Response(sr.data,status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def Delete(req,id):
    Instructor.objects.filter(id=id).delete()
    return Response({'msg':'deleted'},status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def Update(req, id):
    itd = Instructor.objects.filter(id=id).first()
    seritd = InstrSerlizer(instance=itd, data=req.data)

    if seritd.is_valid():
        seritd.save()
        return Response(status=status.HTTP_201_CREATED, data={'msg': 'updated'})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=seritd.errors)

