import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from pitch import app, db, bcrypt
from .forms import RegistrationForm, LoginForm, UpdateAccountForm, PitchForm
from .models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


