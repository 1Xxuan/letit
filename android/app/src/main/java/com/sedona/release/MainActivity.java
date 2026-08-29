package com.sedona.release;

import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // 保证 WebView 内输入框可长按弹出系统粘贴菜单
        bridge.getWebView().setLongClickable(true);
        bridge.getWebView().setHapticFeedbackEnabled(true);
    }
}
