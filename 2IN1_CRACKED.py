import sys
import re
import json
import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QGroupBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
    QSpinBox,
    QCheckBox,
    QHBoxLayout,
    QTextEdit,
    QDialog,
    QRadioButton,
)
import uuid
import urllib.parse
from PyQt5.QtCore import Qt, pyqtSignal

# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL
# FOXYCROWN NUMBER 1 VIP TOOL


proxies = {
    "http": "http://127.0.0.1:60000",
    "https": "http://127.0.0.1:60000"
}
def get_fb_dtsg(cookies):
    """Get fb_dtsg token from Facebook"""
    url = "https://www.facebook.com"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "DNT": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "cookie": cookies,
    }

    response = requests.get(url, headers=headers, proxies=proxies)
    # open("response.html", "w", encoding="utf-8").write(response.text)
    # Extract fb_dtsg token using regex
    match = re.search(r'DTSGInitialData.*?"token":"(.*?)"', response.text)
    if match:
        return match.group(1)
    else:
        raise Exception(
            f"Unable to fetch fb_dtsg token. Response: {response.text[:500]}"
        )
def generate_uuid():
    """Generate UUID"""
    return str(uuid.uuid4())
def getToken(cookie):
    fb_dtsg = get_fb_dtsg(cookie)
    try:
        uid = re.search(r"c_user=(\d+);", cookie).group(1)
    except AttributeError:
        return ""

    url = "https://www.facebook.com/api/graphql/"
    payload = {
        "av": uid,
        "dpr": "1",
        "fb_dtsg": fb_dtsg,
        "jazoest": "25432",
        "lsd": "wOUwVBp8tQ44TcnDdxQYBJ",
        "fb_api_caller_class": "RelayModern",
        "variables": '{"input":{"client_mutation_id":"4","actor_id":"'
        + uid
        + '","config_enum":"GDP_CONFIRM","device_id":null,"experience_id":"'
        + generate_uuid()
        + '","extra_params_json":"{\\"app_id\\":\\"350685531728\\",\\"kid_directed_site\\":\\"false\\",\\"logger_id\\":\\"\\\\\\"'
        + generate_uuid()
        + '\\\\\\"\\",\\"next\\":\\"\\\\\\"confirm\\\\\\"\\",\\"redirect_uri\\":\\"\\\\\\"https:\\\\\\\\\\\\/\\\\\\\\\\\\/www.facebook.com\\\\\\\\\\\\/connect\\\\\\\\\\\\/login_success.html\\\\\\"\\",\\"response_type\\":\\"\\\\\\"token\\\\\\"\\",\\"return_scopes\\":\\"false\\",\\"scope\\":\\"[\\\\\\"user_subscriptions\\\\\\",\\\\\\"user_videos\\\\\\",\\\\\\"user_website\\\\\\",\\\\\\"user_work_history\\\\\\",\\\\\\"friends_about_me\\\\\\",\\\\\\"friends_actions.books\\\\\\",\\\\\\"friends_actions.music\\\\\\",\\\\\\"friends_actions.news\\\\\\",\\\\\\"friends_actions.video\\\\\\",\\\\\\"friends_activities\\\\\\",\\\\\\"friends_birthday\\\\\\",\\\\\\"friends_education_history\\\\\\",\\\\\\"friends_events\\\\\\",\\\\\\"friends_games_activity\\\\\\",\\\\\\"friends_groups\\\\\\",\\\\\\"friends_hometown\\\\\\",\\\\\\"friends_interests\\\\\\",\\\\\\"friends_likes\\\\\\",\\\\\\"friends_location\\\\\\",\\\\\\"friends_notes\\\\\\",\\\\\\"friends_photos\\\\\\",\\\\\\"friends_questions\\\\\\",\\\\\\"friends_relationship_details\\\\\\",\\\\\\"friends_relationships\\\\\\",\\\\\\"friends_religion_politics\\\\\\",\\\\\\"friends_status\\\\\\",\\\\\\"friends_subscriptions\\\\\\",\\\\\\"friends_videos\\\\\\",\\\\\\"friends_website\\\\\\",\\\\\\"friends_work_history\\\\\\",\\\\\\"ads_management\\\\\\",\\\\\\"create_event\\\\\\",\\\\\\"create_note\\\\\\",\\\\\\"export_stream\\\\\\",\\\\\\"friends_online_presence\\\\\\",\\\\\\"manage_friendlists\\\\\\",\\\\\\"manage_notifications\\\\\\",\\\\\\"manage_pages\\\\\\",\\\\\\"photo_upload\\\\\\",\\\\\\"publish_stream\\\\\\",\\\\\\"read_friendlists\\\\\\",\\\\\\"read_insights\\\\\\",\\\\\\"read_mailbox\\\\\\",\\\\\\"read_page_mailboxes\\\\\\",\\\\\\"read_requests\\\\\\",\\\\\\"read_stream\\\\\\",\\\\\\"rsvp_event\\\\\\",\\\\\\"share_item\\\\\\",\\\\\\"sms\\\\\\",\\\\\\"status_update\\\\\\",\\\\\\"user_online_presence\\\\\\",\\\\\\"video_upload\\\\\\",\\\\\\"xmpp_login\\\\\\"]\\",\\"steps\\":\\"{}\\",\\"tp\\":\\"\\\\\\"unspecified\\\\\\"\\",\\"cui_gk\\":\\"\\\\\\"[PASS]:\\\\\\"\\",\\"is_limited_login_shim\\":\\"false\\"}","flow_name":"GDP","flow_step_type":"STANDALONE","outcome":"APPROVED","source":"gdp_delegated","surface":"FACEBOOK_COMET"}}',
        "doc_id": "6494107973937368",
        "locale": "en_US",
        "server_timestamps": "true",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "same-origin",
        "sec-fetch-dest": "empty",
        "accept-language": "en-US,en;q=0.9",
        "sec-fetch-mode": "cors",
        "referer": "https://www.facebook.com/",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-fb-lsd": "wOUwVBp8tQ44TcnDdxQYBJ",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Host": "www.facebook.com",
        "Cookie": cookie,
        "Expect": "100-continue",
        "Accept-Encoding": "gzip",
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, proxies=proxies
    )

    try:
        response_json = response.json()
        if (
            "data" in response_json
            and "run_post_flow_action" in response_json["data"]
            and "uri" in response_json["data"]["run_post_flow_action"]
        ):
            uri = response_json["data"]["run_post_flow_action"]["uri"]
            parsed_url = urllib.parse.urlparse(uri)
            query_params = urllib.parse.parse_qs(parsed_url.query)

            close_uri = urllib.parse.unquote(query_params.get("close_uri", [""])[0])
            fragment_url = urllib.parse.urlparse(close_uri)

            if fragment_url.fragment:
                fragment_params = urllib.parse.parse_qs(fragment_url.fragment)
                access_token = fragment_params.get("access_token", [None])[0]
                return access_token
    except:
        return ""


# ================== HỘP THOẢ THUẬN ==================
class TermsDialog(QDialog):
    def __init__(self, url: str):
        super().__init__()
        self.setWindowTitle("Điều khoản sử dụng")
        self.resize(1200, 1200)

        layout = QVBoxLayout(self)

        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            content = resp.text
        except Exception as e:
            content = f"Không thể tải điều khoản!\n\n{e}"

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setHtml(content)
        layout.addWidget(self.text_edit)

        btn_layout = QHBoxLayout()
        self.accept_btn = QPushButton("Đồng ý")
        self.reject_btn = QPushButton("Thoát")

        self.accept_btn.clicked.connect(self.accept)
        self.reject_btn.clicked.connect(self.reject)

        btn_layout.addWidget(self.accept_btn)
        btn_layout.addWidget(self.reject_btn)
        layout.addLayout(btn_layout)


# ================== APP CHÍNH ==================
class MainApp(QWidget):
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TOOL XÓA MAIL FB BY @FOXYCROWN")
        self.resize(1200, 1200)

        self.is_updating = False
        self.executor = None
        self.running = False
        self.api_mode = 1  # mặc định API 1

        layout = QVBoxLayout(self)

        # Cookie / Token box
        cookie_box = QGroupBox("Nhập Cookie Hoặc Token")
        c_layout = QVBoxLayout(cookie_box)

        self.cookie_input = QPlainTextEdit()
        self.cookie_input.setPlaceholderText("Nhập Cookie...")
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Nhập Access Token...")

        self.check_btn = QPushButton("Check Live Cookie/Token")
        self.check_btn.setEnabled(False)

        self.load_info_btn = QPushButton("Lấy thông tin tài khoản")
        self.load_info_btn.setEnabled(False)

        self.cookie_input.textChanged.connect(self.handle_cookie_change)
        self.token_input.textChanged.connect(self.handle_token_change)

        c_layout.addWidget(QLabel("Cookie:"))
        c_layout.addWidget(self.cookie_input)
        c_layout.addWidget(QLabel("Access Token:"))
        c_layout.addWidget(self.token_input)
        c_layout.addWidget(self.check_btn)
        c_layout.addWidget(self.load_info_btn)

        # Bảng thông tin account
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Thông tin"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.MultiSelection)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.selectionModel().selectionChanged.connect(self.update_run_button)

        # Cấu hình chạy
        config_box = QGroupBox("Cấu hình chạy")
        cfg_layout = QHBoxLayout(config_box)

        self.thread_input = QSpinBox()
        self.thread_input.setMinimum(1)
        self.thread_input.setMaximum(999999)
        self.thread_input.setValue(2000)

        self.delay_input = QSpinBox()
        self.delay_input.setMinimum(0)
        self.delay_input.setMaximum(60000)
        self.delay_input.setValue(0)

        self.auto_stop_chk = QCheckBox("Tự động dừng khi gặp rate limit")
        self.loop_mode_chk = QCheckBox("Chạy lặp vô hạn")

        # 🔥 Thêm lựa chọn API
        self.api1_radio = QRadioButton("Xóa qua API 1")
        self.api2_radio = QRadioButton("Xóa qua API 2")
        self.api1_radio.setChecked(True)

        self.api1_radio.toggled.connect(lambda: self.set_api_mode(1))
        self.api2_radio.toggled.connect(lambda: self.set_api_mode(2))

        cfg_layout.addWidget(QLabel("Số luồng:"))
        cfg_layout.addWidget(self.thread_input)
        cfg_layout.addWidget(QLabel("Delay (ms):"))
        cfg_layout.addWidget(self.delay_input)
        cfg_layout.addWidget(self.auto_stop_chk)
        cfg_layout.addWidget(self.loop_mode_chk)
        cfg_layout.addWidget(self.api1_radio)
        cfg_layout.addWidget(self.api2_radio)

        # Nút chạy / dừng
        self.run_btn = QPushButton("▶ Chạy")
        self.run_btn.setEnabled(False)
        self.stop_btn = QPushButton("■ Dừng")
        self.stop_btn.setEnabled(False)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.run_btn)
        btn_layout.addWidget(self.stop_btn)

        # Ô log
        log_box = QGroupBox("Log")
        log_layout = QVBoxLayout(log_box)
        self.log_output = QPlainTextEdit()
        self.log_output.setReadOnly(True)
        log_layout.addWidget(self.log_output)

        # Events
        self.check_btn.clicked.connect(self.check_cookie_or_token)
        self.load_info_btn.clicked.connect(self.load_account_info)
        self.run_btn.clicked.connect(self.start_run)
        self.stop_btn.clicked.connect(self.stop_run)

        # Layout chính
        layout.addWidget(cookie_box)
        layout.addWidget(QLabel("Thông Tin Account:"))
        layout.addWidget(self.table)
        layout.addWidget(config_box)
        layout.addLayout(btn_layout)
        layout.addWidget(log_box)

        self.log_signal.connect(self.log)

    # ============ FUNCTION ============
    def set_api_mode(self, mode):
        if mode == 1 and self.api1_radio.isChecked():
            self.api_mode = 1
            self.log_signal.emit("⚡ Đã chọn API 1")
        elif mode == 2 and self.api2_radio.isChecked():
            self.api_mode = 2
            self.log_signal.emit("⚡ Đã chọn API 2")

    def log(self, message: str):
        self.log_output.appendPlainText(message)

    def handle_cookie_change(self):
        if self.is_updating:
            return
        if self.cookie_input.toPlainText().strip():
            self.token_input.blockSignals(True)
            self.token_input.clear()
            self.token_input.blockSignals(False)
            self.check_btn.setEnabled(True)
        else:
            self.check_btn.setEnabled(False)

    def handle_token_change(self):
        if self.is_updating:
            return
        if self.token_input.text().strip():
            self.cookie_input.blockSignals(True)
            self.cookie_input.clear()
            self.cookie_input.blockSignals(False)
            self.check_btn.setEnabled(True)
        else:
            self.check_btn.setEnabled(False)

    def check_cookie_or_token(self):
        cookie = self.cookie_input.toPlainText().strip()
        token = self.token_input.text().strip()

        if cookie:
            self.get_token_from_cookie(cookie)
        elif token:
            self.get_cookie_from_token(token)
        else:
            QMessageBox.warning(self, "Lỗi", "Bạn cần nhập Cookie hoặc Token!")

    def get_token_from_cookie(self, cookie: str):
        self.log_signal.emit("🔍 Đang gửi yêu cầu lấy token từ server...")
        try:
            token = getToken(cookie)
            self.is_updating = True
            self.token_input.setText(token)
            self.cookie_input.setPlainText(cookie)
            self.is_updating = False
            self.log_signal.emit("✅ Lấy token thành công")
            self.load_info_btn.setEnabled(True)
        except Exception as e:
            self.log_signal.emit(f"❌ Lỗi khi gọi API: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể kết nối API!\n{e}")

    def get_cookie_from_token(self, token: str):
        self.log_signal.emit("🔍 Đang gửi yêu cầu lấy cookie từ server...")
        try:
            url = f"{API}/v1/get_cookie.php?token={token}&key={KEY}&telegram={TELEGRAM_THONGBAO}"
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            if data.get("status") == "success":
                cookie = data.get("cookie", "")
                self.is_updating = True
                self.token_input.setText(token)
                self.cookie_input.setPlainText(cookie)
                self.is_updating = False
                self.log_signal.emit("✅ Lấy cookie thành công")
                self.load_info_btn.setEnabled(True)
            else:
                msg = data.get("message", "Không rõ lỗi")
                self.log_signal.emit(f"❌ Lỗi: {msg}")
                QMessageBox.warning(self, "Lỗi", msg)
        except Exception as e:
            self.log_signal.emit(f"❌ Lỗi khi gọi API: {e}")
            QMessageBox.critical(self, "Lỗi", f"Không thể kết nối API!\n{e}")

    def load_account_info(self):
        cookie = self.cookie_input.toPlainText().strip()
        token = self.token_input.text().strip()
        if not cookie or not token:
            QMessageBox.warning(
                self, "Lỗi", "Vui Lòng Check Live Cookie/Token Trước Khi Chạy!"
            )
            return
        headers = {"user-agent": "Mozilla/5.0", "cookie": cookie}

        try:
            resp = requests.get(
                "https://accountscenter.facebook.com/personal_info",
                headers=headers,
                timeout=30,
            )
            resp.raise_for_status()
            html = resp.text

            fb_dtsg = re.search(r'"token":"(.*?)"', html)
            lsd_token = re.search(r'"LSD",\[\],{[^}]*"token":"(.*?)"', html)
            jazoest = re.search(r"jazoest=(\d+)", html)
            c_user = re.search(r"c_user=(\d+)", cookie)

            fb_dtsg = fb_dtsg.group(1) if fb_dtsg else ""
            lsd_token = lsd_token.group(1) if lsd_token else ""
            jazoest = jazoest.group(1) if jazoest else ""
            c_user = c_user.group(1) if c_user else ""

            if not (fb_dtsg and lsd_token and jazoest and c_user):
                QMessageBox.critical(self, "Lỗi", "Không thể lấy thông tin account!")
                return

            payload = {
                "__user": c_user,
                "fb_dtsg": fb_dtsg,
                "jazoest": jazoest,
                "lsd": lsd_token,
                "variables": json.dumps({"interface": "FB_WEB"}),
                "doc_id": "9849298431773678",
            }

            post_headers = {
                "user-agent": "Mozilla/5.0",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": lsd_token,
                "cookie": cookie,
            }

            res = requests.post(
                "https://accountscenter.facebook.com/api/graphql/",
                data=payload,
                headers=post_headers,
                timeout=30,
            )
            res.raise_for_status()
            data = res.json()

            confirmed = []
            cps = (
                data.get("data", {})
                .get("fxcal_settings", {})
                .get("node", {})
                .get("all_contact_points", [])
            )
            for cp in cps:
                if cp.get("contact_point_type") in ["EMAIL", "PHONE"] and not cp.get(
                    "has_any_pending_status"
                ):
                    confirmed.append(cp.get("normalized_contact_point"))

            if not confirmed:
                QMessageBox.information(
                    self, "Kết quả", "Không tìm thấy email nào đã xác nhận!"
                )
                return

            self.table.setRowCount(len(confirmed))
            for row, v in enumerate(confirmed):
                self.table.setItem(row, 0, QTableWidgetItem(v))

            self.log_signal.emit("📥 Đã tải thông tin account thành công")

        except Exception as e:
            self.log_signal.emit(f"❌ Lỗi khi lấy thông tin: {e}")
            QMessageBox.critical(self, "Lỗi", str(e))

    def update_run_button(self):
        if self.table.selectionModel().hasSelection():
            self.run_btn.setEnabled(True)
        else:
            self.run_btn.setEnabled(False)

    def start_run(self):
        selected = self.table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self, "Lỗi", "Bạn chưa chọn thông tin nào để chạy!")
            return

        mails = [self.table.item(r.row(), 0).text() for r in selected]
        threads = self.thread_input.value()
        delay = self.delay_input.value() / 1000.0
        auto_stop = self.auto_stop_chk.isChecked()
        loop_mode = self.loop_mode_chk.isChecked()

        cookie = self.cookie_input.toPlainText().strip()
        token = self.token_input.text().strip()
        uid_match = re.search(r"c_user=(\d+)", cookie)
        uid = uid_match.group(1) if uid_match else ""

        if not (token and uid):
            QMessageBox.critical(self, "Lỗi", "Thiếu token hoặc UID!")
            return

        self.log_signal.emit(
            f"▶ Bắt đầu chạy: {len(mails)} mail × {threads} luồng (API {self.api_mode})"
        )
        self.run_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.running = True

        def batch_runner():
            batch_num = 0
            while self.running:
                batch_num += 1
                self.log_signal.emit(f"🚀 Batch {batch_num} bắt đầu")

                self.executor = ThreadPoolExecutor(max_workers=threads * len(mails))
                futures = []
                for mail in mails:
                    for _ in range(threads):
                        if not self.running:
                            break
                        try:
                            f = self.executor.submit(
                                self.send_delete_request,
                                mail,
                                uid,
                                token,
                                delay,
                                auto_stop,
                            )
                            futures.append(f)
                        except RuntimeError:
                            break

                for _ in as_completed(futures):
                    if not self.running:
                        break

                if self.executor:
                    self.executor.shutdown(wait=False, cancel_futures=True)
                    self.executor = None

                self.log_signal.emit(f"✅ Batch {batch_num} hoàn thành")

                if not loop_mode or not self.running:
                    break

            if self.running:
                self.log_signal.emit("🎉 Tất cả batch đã hoàn thành")
            self.stop_run()

        threading.Thread(target=batch_runner, daemon=True).start()

    def send_delete_request(self, mail, uid, token, delay, auto_stop):
        try:
            url = "https://graph.facebook.com/graphql"

            payload_1 = {
                "locale": "en_US",
                "doc_id": "9452525451539774",
                "variables": "{'normalized_contact_point':'"
                + mail
                + "','contact_point_type':'EMAIL','selected_accounts':['"
                + uid
                + "'],'client_mutation_id':'mutation_id_1757676815878','family_device_id':'device_id_fetch_datr'}",
            }

            payload_2 = {
                "locale": "en_US",
                "client_doc_id": "11994080426665102886081222100",
                "variables": '{"params":{"params":"{\\"params\\":\\"{\\\\\\"client_input_params\\\\\\":{\\\\\\"family_device_id\\\\\\":\\\\\\"8a21cb3b-3109-43f3-bf9f-cb4d79675213\\\\\\"},\\\\\\"server_params\\\\\\":{\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\":36707139,\\\\\\"contact_point_source\\\\\\":\\\\\\"fx_settings\\\\\\",\\\\\\"requested_screen_component_type\\\\\\":null,\\\\\\"machine_id\\\\\\":null,\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\":2.1344974730022E14,\\\\\\"normalized_contact_point\\\\\\":\\\\\\"'
                + mail
                + '\\\\\\",\\\\\\"selected_accounts\\\\\\":\\\\\\"'
                + uid
                + '\\\\\\",\\\\\\"contact_point_type\\\\\\":\\\\\\"email\\\\\\"}}\\"}","bloks_versioning_id":"490f12c5d97f41f602f94b2cdc531342424a878f28bc759193bbff31792aac5a","app_id":"com.bloks.www.fx.settings.contact_point.delete.async"},"scale":"2","use_native_entrypoint_for_stars_on_reels":true,"nt_context":{"using_white_navbar":true,"styles_id":"68d27780b9e4060fbcdc47bb19ac41b2","pixel_ratio":2,"is_push_on":true,"debug_tooling_metadata_token":null,"is_flipper_enabled":false,"theme_params":[{"value":["BLUEPRINT_TEST_GUTTER","BLUEPRINT_TEST_ROUNDED_CORNERS_NO_GUTTERS"],"design_system_name":"FDS"}],"bloks_version":"490f12c5d97f41f602f94b2cdc531342424a878f28bc759193bbff31792aac5a"}}',
            }

            headers = {
                "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
                "authorization": f"OAuth {token}",
            }

            if self.api_mode == 1:
                res = requests.post(url, data=payload_1, headers=headers)
            else:
                res = requests.post(url, data=payload_2, headers=headers)

            kqua = res.text
            self.log_signal.emit(f"{mail} → {kqua}")

        except Exception as e:
            self.log_signal.emit(f"❌ {mail} → Có Lỗi: {e}")
            if auto_stop:
                self.stop_run()
                return

        if delay > 0:
            time.sleep(delay)

    def stop_run(self):
        self.running = False
        self.log_signal.emit("■ Đã dừng quá trình chạy")
        QApplication.processEvents()
        try:
            if self.executor:
                self.executor.shutdown(wait=False, cancel_futures=True)
                self.executor = None
        except Exception as e:
            self.log_signal.emit(f"Lỗi khi dừng executor: {e}")

        self.run_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)


# ================== MAIN ==================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainApp()
    win.show()
    sys.exit(app.exec_())
