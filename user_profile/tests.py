from django.test import TestCase
# Create your tests here.
# Create your tests here.
from django.shortcuts import redirect,render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from .models import MyUser
from user_profile.models import Student_profile
from django.contrib.sites.shortcuts import get_current_site
import json,os
from django.http import HttpResponse,Http404,FileResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from smtplib import SMTPException
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import uuid
from django.views.generic.edit import FormView
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from django.utils.http import (
#     url_has_allowed_host_and_scheme, urlsafe_base64_decode,
# )
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import PasswordContextMixin
import re
from .utils import generate_token
#from .token import account_activation_token
from django.utils.encoding import force_bytes, force_str, force_text
from django.template.loader import render_to_string
from validate_email import validate_email