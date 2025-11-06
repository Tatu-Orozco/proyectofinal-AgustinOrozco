from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    msgs = Message.objects.filter(receiver=request.user)
    if not msgs.exists():
        messages.info(request, 'No tienes mensajes aún.')
    return render(request, 'messages/inbox.html', {'messages_list': msgs})

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk, receiver=request.user)
    if not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'messages/detail.html', {'msg': msg})

@login_required
def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.sender = request.user
            m.save()
            messages.success(request, 'Mensaje enviado.')
            return redirect('messages:inbox')
    else:
        form = MessageForm()
    return render(request, 'messages/create.html', {'form': form})