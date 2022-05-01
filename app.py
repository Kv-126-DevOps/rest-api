from flask import Flask
from config import Config
from querys import *

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/issues/by-label/<label>", methods=['GET'])
def getIssuesByLabel(label):
    return getIssuesByLabelQuery(label)


@app.route("/", methods=['GET'])
@app.route("/issues/", methods=['GET'])
def getIssues():
    return getIssuesQuery()


@app.route("/issues/by-id/<int:id>", methods=['GET'])
def getIssueById(id=None):
    return getIssuesByIdQuery(id)


@app.route("/labels/", methods=['GET'])
def getLabels():
    return getLabelsQuery()


@app.route("/states/", methods=['GET'])
def getStates():
    return getStatesQuery()


@app.route("/actions/", methods=['GET'])
def getActions():
    return getActionsQuery()


@app.route("/users/", methods=['GET'])
def getUsers():
    return getUsersQuery()


if __name__ == '__main__':
    app.run(debug=True)



@app.route("/", methods=['GET'])
@app.route("/hello/", methods=['GET'])
def getSlavik():
    return "hello"
