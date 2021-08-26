from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user, UserMixin
from .models import Note
from . import db
import json

class User(db.Mobdel, UserMixin)
    id = db.Column(db.Integer, primary_key=TrueEmail = db.coo