from django.shortcuts import render
from .models import AuditionPortal, DesignWorkshop, ValorantGaming, BgmiGaming
from django.http import HttpResponse
from .serializers import AuditionPortalSerializer, DesignWorkshopSerializer, ValorantGamingSerializer, BgmiGamingSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from django.conf import settings
import requests
from threading import Thread
from rest_framework.response import Response
from django.core.mail import send_mail
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate(
    "auditionApp/credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Create your views here.


def auditions(request):
    return HttpResponse("WORKSHOP 2023 API")


class AuditionPortalViewSet(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.data)
        # return
        uid = request.data.get('uid')
        token = request.data.get('token')
        email = request.data.get('email')
        name = request.data.get('name')
        recaptcha = request.data.get("g-recaptcha-response")

        # decoded_token = auth.verify_id_token(token)
        # decoded_uid = decoded_token['uid']
        # print("token :", decoded_uid)
        # return Response({
        #     "detail":"Error"
        #     },status=status.HTTP_400_BAD_REQUEST)
        # return
        data = {"secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": recaptcha}
        r = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data=data)
        result = r.json()
        # print("result :", result)
        if result["success"]:
            # if uid==decoded_uid :
            serializer = AuditionPortalSerializer(data=request.data)
            if serializer.is_valid():
                v = AuditionPortal.objects.filter(email=email)
                if v.exists():
                    # user already registered
                    return Response({
                        "detail": "user already registered"
                    }, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save()
                    subject = "CCA Audition 2024"
                    link = "https://chat.whatsapp.com/IaapkwYGVo663Rzw6tT4z6"
                    message = 'Dear ' + name + ' !\n' + "We have received your registration for CCA Audition and will contact you very soon." \
                        " Join the WhatsApp group if you haven't, through the link below for further updates and information regarding the audition updates.\n\n" + \
                        link + "\n\nHope to see you soon! \nRegards,\nCentre for Cognitive Activities, NIT Durgapur"

                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                try:
                    email_thread = Thread(target=send_mail, args=(
                        subject, message, email_from, recipient_list))
                    email_thread.start()
                    send_mail(subject, message, email_from, recipient_list)
                    pass
                except Exception as e:
                    print(e)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)

            # return Response({
            #        "detail":"token did not match"
            #        },status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "detail": "captcha not verified"
        }, status=status.HTTP_400_BAD_REQUEST)


class DesignWorkshopViewSet(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if (DesignWorkshop.objects.all().count() <= 120):
            image = request.FILES.get("payment")
            email = request.data.get("email")
            name = request.data.get("name")
            serializer = DesignWorkshopSerializer(data=request.data)
            if serializer.is_valid():
                check = DesignWorkshop.objects.filter(email=email)
                if (check.exists()):
                    return Response({
                        "message": "Email already registered"
                    }, status=status.HTTP_400_BAD_REQUEST
                    )
                else:
                    serializer.save(payment_proof=image)
                    subject = 'WDCT GD Workshop 2024'
                    link = "https://chat.whatsapp.com/BbeWqd1FsIrHxC3kK2MvMP"
                    message = 'Dear ' + name + ' !\n' + "We have received your registration for Design Workshop 2024 and will contact you very soon." \
                                                        " Join the WhatsApp group if you haven't, through the link below for further updates and information regarding the auditions.\n\n" + \
                        link + "\n\nHope to see you soon! \nRegards,\nCentre for Cognitive Activities, NIT Durgapur"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    try:
                        email_thread = Thread(target=send_mail, args=(
                            subject, message, email_from, recipient_list))
                        email_thread.start()
                        send_mail(subject, message, email_from, recipient_list)
                        pass
                    except Exception as e:
                        print(e)
                    return Response({
                        "message": "Successfully submitted your details"
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "message": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": "Sorry!No more seats are now left"}, status=status.HTTP_400_BAD_REQUEST
            )


class ValorantGamingViewSet(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if (ValorantGaming.objects.all().count() <= 120):
            image = request.FILES.get("payment")
            email = request.data.get("email")
            name = request.data.get("name")
            recaptcha = request.data.get("g-captcha-response")

            data = {"secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY2,
                    "response": recaptcha}
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", data=data)
            result = r.json()
            if result["success"]:
                serializer = ValorantGamingSerializer(data=request.data)
                if serializer.is_valid():
                    check = ValorantGaming.objects.filter(email=email)
                    if (check.exists()):
                        return Response({
                            "message": "Email already registered"
                        }, status=status.HTTP_400_BAD_REQUEST
                        )
                    else:
                        serializer.save(payment_proof=image)
                        subject = 'WDCT Valorant Gaming 2024'
                        link = "https://chat.whatsapp.com/HRjeqmPjE916fB95z2QQ3R"
                        message = 'Dear ' + name + ' !\n' + "We have received your registration for Valorant Gaming 2024 and will contact you very soon." \
                            " Join the WhatsApp group if you haven't, through the link below for further updates and information regarding the event.\n\n" + \
                            link + "\n\nHope to see you soon! \nRegards,\nCentre for Cognitive Activities, NIT Durgapur"
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [email]
                        try:

                            email_thread = Thread(target=send_mail, args=(
                                subject, message, email_from, recipient_list))
                            email_thread.start()
                            send_mail(subject, message,
                                      email_from, recipient_list)
                            pass
                        except Exception as e:
                            print(e)
                        return Response({
                            "message": "Successfully submitted your details"
                        }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "message": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response({
                    "message": "captcha not verified"
                }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": "Sorry!No more seats are now left"}, status=status.HTTP_400_BAD_REQUEST
            )


class BgmiGamingViewSet(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if (BgmiGaming.objects.all().count() <= 120):
            image = request.FILES.get("payment")
            email = request.data.get("email")
            name = request.data.get("name")
            recaptcha = request.data.get("g-captcha-response")

            data = {"secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY2,
                    "response": recaptcha}
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", data=data)
            result = r.json()
            if result["success"]:
                serializer = BgmiGamingSerializer(data=request.data)
                if serializer.is_valid():
                    check = BgmiGaming.objects.filter(email=email)
                    if (check.exists()):
                        return Response({
                            "message": "Email already registered"
                        }, status=status.HTTP_400_BAD_REQUEST
                        )
                    else:
                        serializer.save(payment_proof=image)
                        subject = 'WDCT BGMI Gaming 2024'
                        link = "https://chat.whatsapp.com/HiKleNJ58N50r5imSSWcIe"
                        message = 'Dear ' + name + ' !\n' + "We have received your registration for BGMI Gaming 2024 and will contact you very soon." \
                            " Join the WhatsApp group if you haven't, through the link below for further updates and information regarding the event.\n\n" + \
                            link + "\n\nHope to see you soon! \nRegards,\nCentre for Cognitive Activities, NIT Durgapur"
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [email]
                        try:

                            email_thread = Thread(target=send_mail, args=(
                                subject, message, email_from, recipient_list))
                            email_thread.start()
                            send_mail(subject, message,
                                      email_from, recipient_list)
                            pass
                        except Exception as e:
                            print(e)
                        return Response({
                            "message": "Successfully submitted your details"
                        }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "message": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response({
                    "message": "captcha not verified"
                }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": "Sorry!No more seats are now left"}, status=status.HTTP_400_BAD_REQUEST
            )
