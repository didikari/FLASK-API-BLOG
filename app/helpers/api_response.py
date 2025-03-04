from flask import jsonify


class ApiResponse:
    @staticmethod
    def format(data=None, code=200, message="Request successful"):
        return jsonify({"data": data, "code": code, "message": message}), code

    @staticmethod
    def success(message="Request successful", code=200):
        return ApiResponse.format(None, code, message)

    @staticmethod
    def error(message="Something went wrong", code=400):
        return ApiResponse.format(None, code, message)
