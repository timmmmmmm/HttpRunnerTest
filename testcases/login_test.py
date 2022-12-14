# NOTE: Generated By HttpRunner v4.0.0
# FROM: testcases/login.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLogin(HttpRunner):

    config = (
        Config("Login")
        .variables(
            **{"twoFAToken": "check", "secret": "${ENV(secret)}", "userToken": ""}
        )
        .base_url("${ENV(base_url)}")
        .export(*["userToken"])
    )

    teststeps = [
        Step(
            RunRequest("Login with user name")
            .with_variables(
                **{
                    "userName": "TimmyHong",
                    "password": "02ee0be1761db38a2ab3cb3adab0d4886def79f00fab7ff2c4ec115c26cd3b71",
                    "deviceFingerprint": "_vmhjlh1667276599542",
                }
            )
            .post("/api/login/")
            .with_params(
                **{
                    "password": "$password",
                    "captchaId": False,
                    "captchaNumber": "",
                    "deviceFingerprint": "$deviceFingerprint",
                    "loginName": "$userName",
                    "keepLogin": False,
                }
            )
            .with_headers(
                **{
                    "content-type": "application/json",
                    "Accept": "application/json",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                }
            )
            .extract()
            .with_jmespath("body.data.token", "twoFAToken")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 1)
        ),
        Step(
            RunRequest("2FA check")
            .post("/api/user/check/2FA")
            .with_params(
                **{"token": "$twoFAToken", "otpCode": "${add_2FA_code($secret)}"}
            )
            .with_headers(
                **{
                    "content-type": "application/json",
                    "Accept": "application/json",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                }
            )
            .extract()
            .with_jmespath("body.data.token", "userToken")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
