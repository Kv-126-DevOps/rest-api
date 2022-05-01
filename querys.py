from flask import jsonify
from sqlalchemy import func
from db import session
from models import *


def getIssuesByLabelQuery(label: str):
    """
    The function for Selecting Issues and filtering by Label from the db.
    :param label: for filtering issues
    :return: list of Issue from db
    """

    label = str.lower(label)

    result = session.query(
        Issue.IssueId.label("IssueId"),
        State.Title.label("State"),
        Issue.Title.label("Issue"),
        Issue.HtmlUrl.label("IssueHtmlUrl"),
        User.UserId.label("UserId"),
        User.HtmlUrl.label("UserHtmlUrl"),
        User.AvatarUrl.label("UserAvatarUrl"),
        IssueAction.ModifiedDate.label("ModifiedDate"),
        Action.Title.label("Action")
    ). \
        join(IssueLabel). \
        join(Label). \
        join(IssueAction). \
        join(Action). \
        join(User). \
        join(IssueState). \
        join(State). \
        filter(func.lower(Label.Title).contains(label)). \
        order_by(Issue.IssueId, IssueAction.ModifiedDate). \
        all()

    return jsonify([
        {
            'IssueId': item.IssueId,
            'State': item.State,
            'Issue': item.Issue,
            'IssueHtmlUrl': item.IssueHtmlUrl,
            'UserId': item.UserId,
            'UserHtmlUrl': item.UserHtmlUrl,
            'UserAvatarUrl': item.UserAvatarUrl,
            'ModifiedDate': item.ModifiedDate,
            'Action': item.Action,
        } for item in result])


def getIssuesByIdQuery(issueId):
    """
    The function for Selecting Issues and filtering by IssueId from the db.
    :return: list of Issue from db
    """
    result = session.query(
        Issue.IssueId.label("IssueId"),
        State.Title.label("State"),
        Issue.Title.label("Issue"),
        Issue.HtmlUrl.label("IssueHtmlUrl"),
        User.UserId.label("UserId"),
        User.HtmlUrl.label("UserHtmlUrl"),
        User.AvatarUrl.label("UserAvatarUrl"),
        IssueAction.ModifiedDate.label("ModifiedDate"),
        Action.Title.label("Action")
    ). \
        join(IssueLabel). \
        join(Label). \
        join(IssueAction). \
        join(Action). \
        join(User). \
        join(IssueState). \
        join(State). \
        filter(Issue.IssueId == issueId). \
        order_by(IssueAction.ModifiedDate). \
        all()

    return jsonify([
        {
            'IssueId': item.IssueId,
            'State': item.State,
            'Issue': item.Issue,
            'IssueHtmlUrl': item.IssueHtmlUrl,
            'UserId': item.UserId,
            'UserHtmlUrl': item.UserHtmlUrl,
            'UserAvatarUrl': item.UserAvatarUrl,
            'ModifiedDate': item.ModifiedDate,
            'Action': item.Action,
        } for item in result])


def getLabelsQuery():
    """
    The function of Select Labels from the db.
    :return: list of Label from db
    """

    result = session.query(Label).all()
    return jsonify([
        {
            'LabelId': item.LabelId,
            'Title': item.Title,
        } for item in result])


def getStatesQuery():
    """
    The function of Select States from the db.
    :return: list of State from db
    """
    result = session.query(State).all()
    return jsonify([
        {
            'StateId': item.StateId,
            'Title': item.Title,
        } for item in result])


def getActionsQuery():
    """
    The function of Select Actions from the db.
    :return: list of Action from db
    """
    result = session.query(Action).all()
    return jsonify([
        {
            'ActionId': item.ActionId,
            'Title': item.Title,
        } for item in result])


def getUsersQuery():
    """
    The function of Select Users from the db.
    :return: list of User from db
    """

    result = session.query(User).all()
    return jsonify([
        {
            'UserId': item.UserId,
            'HtmlUrl': item.HtmlUrl,
            'AvatarUrl': item.AvatarUrl,
        } for item in result])


def getIssuesQuery():
    """
    The function of Select Issues from the db.
    :return: list of Issue from db
    """
    result = session.query(Issue).all()
    return jsonify([
        {
            'IssueId': item.IssueId,
            'HtmlUrl': item.HtmlUrl,
            'Number': item.Number,
            'Title': item.Title,
            'Body': item.Body,
        } for item in result])
