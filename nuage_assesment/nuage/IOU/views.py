import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import User


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data["user"]
            if User.objects.filter(name=name).exists():
                return HttpResponse("You are already enrolled.")
            user = User.objects.create(name=name)
            user.save()

            return HttpResponse(
                f"{user.name} acount is created.", status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return HttpResponse(
                dict(message=str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return HttpResponse("Invalid method. ", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def create_iou(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lender = data["lender"]
        borrower = data["borrower"]
        amount = data["amount"]
        try:
            lenderobject = User.objects.get(name=lender)
            lenderobject_total_owedby = 0.0
            lenderobject_total_owes = 0.0

            if borrower in lenderobject.owedby:
                lenderobject.owedby[borrower] += amount
            else:
                lenderobject.owedby[borrower] = amount

            for values in lenderobject.owedby.values():
                lenderobject_total_owedby += values
            for values in lenderobject.owes.values():
                lenderobject_total_owes += values

            lenderobject.balance = lenderobject_total_owedby - lenderobject_total_owes
            lenderobject.save()
            borrowerobject = User.objects.get(name=borrower)
            borrowerobject_total_owedby, borrowerobject_total_owes = 0, 0

            if lender in borrowerobject.owes:
                borrowerobject.owes[lender] += amount
            else:
                borrowerobject.owes[lender] = amount

            for values in borrowerobject.owedby.values():
                borrowerobject_total_owedby += values
            for values in borrowerobject.owes.values():
                borrowerobject_total_owes += values

            borrowerobject.balance = (
                borrowerobject_total_owedby - borrowerobject_total_owes
            )
            borrowerobject.save()

            return HttpResponse(
                f"Updated Userobjects for {lenderobject} and {borrowerobject}",
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return HttpResponse(
                dict(message=str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return HttpResponse("Invalid method ", status=status.HTTP_400_BAD_REQUEST)


def get_users(request):
    if request.method == "GET":
        try:
            data = json.loads(request.body)
            context = []
            if data["users"]:
                data["users"].sort()
                for name in data["users"]:
                    userobject = User.objects.get(name=name)
                    context.append(userobject.name)
            else:
                userobject = User.objects.all()
                context.append(userobject)

            return JsonResponse(context, safe=False, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return HttpResponse(
                dict(message=str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    else:
        return HttpResponse(
            dict(message="Invalid Key"), status=status.HTTP_400_BAD_REQUEST
        )
