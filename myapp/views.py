from django.shortcuts import render
from APS import sch


def home(request):
    return render(request, "index.html")


def start(request):
    sch.start()
    return render(request, "start.html")


def stop(request):
    sch.shutdown()
    return render(request, "stop.html")


def resume(request):
    sch.resume()
    return render(request, "resume.html")


def pause(request):
    sch.pause()
    return render(request, "pause.html")

def wakeup(request):
    sch.wakeup()
    return render(request, "wakeup.html")
