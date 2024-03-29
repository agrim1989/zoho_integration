import json

import requests
from django.http import HttpResponse

from .models import *
from django.conf import settings
import datetime
from .task_list import *


def all_projects():

    url = "https://projectsapi.zoho.com/restapi/portal/{}/projects/".format(settings.PORTAL_ID)
    token = Tokens.objects.latest("id")
    access_token = token.access_token
    headers = {
        'authorization': "Bearer {}".format(access_token),
    }

    projects = requests.request("GET", url, headers=headers)
    if projects.status_code in [204, 400, 401, 404]:
        pass
    else:
        projects = projects.json()
        projects = projects['projects']

        for p in projects:
            try:
                pro = Projects.objects.get(project_id=p['id'])
            except Exception:
                pros = Projects.objects.create(
                    project_id=p.get('id', ""),
                    name=p.get('name', ""))
            pro = Projects.objects.get(project_id=p['id'])
            try:
                start_time = p.get('start_date', "")
            except Exception:
                start_time = None
            try:
                end_time = p.get('end_date', "")
            except Exception:
                end_time = None

            try:
                created_date = p.get('created_date', "")
            except Exception:
                created_date = None
            try:
                owner_name = p.get('owner_name', "")
            except Exception:
                owner_name = None
            pro.owner_name = owner_name if owner_name else None
            pro.description = p.get('description', "")
            pro.task_count_open = p.get('task_count', "").get('open', 0)
            pro.task_count_close = p.get('task_count', "").get('closed', 0)
            pro.milestone_count_open = p.get('milestone_count', "").get('open',
                                                                        0)
            pro.milestone_count_close = p.get('milestone_count', "").get(
                'closed', 0)
            pro.status = p.get('status', "")
            pro.created_date_format = datetime.datetime.strptime(created_date,
                                                                 "%m-%d-%Y") if created_date else None
            pro.start_date_format = datetime.datetime.strptime(start_time,
                                                               "%m-%d-%Y") if start_time else None
            pro.folder_url = p.get('link', "").get('folder', "").get("url", "")
            pro.milestone_url = p.get('link', "").get('milestone', "").get(
                "url", "")
            pro.forum_url = p.get('link', "").get('forum', "").get("url", "")
            pro.document_url = p.get('link', "").get('document', "").get("url",
                                                                         "")
            pro.status_url = p.get('link', "").get('status', "").get("url", "")
            pro.event_url = p.get('link', "").get('event', "").get("url", "")
            pro.task_url = p.get('link', "").get('task', "").get("url", "")
            pro.bug_url = p.get('link', "").get('bug', "").get("url", "")
            pro.self_url = p.get('link', "").get('self', "").get("url", "")
            pro.timesheet_url = p.get('link', "").get('timesheet', "").get(
                "url", "")
            pro.user_url = p.get('link', "").get('user', "").get("url", "")
            pro.tasklist_url = p.get('link', "").get('tasklist', "").get("url",
                                                                         "")
            pro.activity_url = p.get('link', "").get('activity', "").get("url",
                                                                         "")
            pro.id_bug_enabled = p.get('id_bug_enabled', "")
            pro.end_date_format = datetime.datetime.strptime(end_time,
                                                             "%m-%d-%Y") if end_time else None
            pro.save()
    return "success"
