# -*- coding: utf-8 -*-
import io
import wave


class 音檔頭前表:
    @classmethod
    def 提掉(cls, 音):
        音檔 = io.BytesIO(音)
        音物件 = wave.open(音檔, mode='rb')
        原始 = 音物件.readframes(音物件.getnframes())
        音物件.close()
        音檔.close()
        return 原始

    @classmethod
    def 加起哩(cls, 原始, 一點幾位元組, 一秒幾點, 幾个聲道):
        音檔 = io.BytesIO()
        音物件 = wave.open(音檔, mode='wb')
        音物件.setsampwidth(一點幾位元組)
        音物件.setframerate(一秒幾點)
        音物件.setnchannels(幾个聲道)
        音物件.writeframesraw(原始)
        音物件.close()
        音 = 音檔.getvalue()
        音檔.close()
        return 音
