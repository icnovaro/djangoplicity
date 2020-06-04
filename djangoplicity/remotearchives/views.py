# -*- coding: utf-8 -*-
#
# djangoplicity-remotearchives
# Copyright (c) 2007-2016, European Southern Observatory (ESO)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the European Southern Observatory nor the names
#      of its contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY ESO ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL ESO BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE

from django.conf import settings
from django.utils import translation
from django.views.generic import DetailView, ListView


class RemoteArchiveDetailView(DetailView):
    def get_object(self, queryset=None):
        remote = super(RemoteArchiveDetailView, self).get_object(queryset)

        if settings.USE_I18N:
            remote.lang = translation.get_language()

        return remote

    def get_qeryset(self):
        queryset = super(RemoteArchiveDetailView, self).get_qeryset()

        queryset.filter(published=True)
        return queryset


class RemoteArchiveListView(ListView):
    def get_context_data(self, **kwargs):
        context = super(RemoteArchiveListView, self).get_context_data(**kwargs)

        context['archive_title'] = self.model.archive_title
        return context

    def get_qeryset(self):
        queryset = super(RemoteArchiveListView, self).get_qeryset()

        queryset.filter(published=True)
        return queryset
