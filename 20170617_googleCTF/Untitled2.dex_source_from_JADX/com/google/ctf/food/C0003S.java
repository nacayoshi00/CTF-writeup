package com.google.ctf.food;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.util.TypedValue;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup.LayoutParams;
import android.widget.Button;
import android.widget.GridLayout;

/* renamed from: com.google.ctf.food.S */
public class C0003S {
    public static String f3I;
    public static Activity f4a;

    /* renamed from: com.google.ctf.food.S.1 */
    class C00021 implements OnClickListener {
        final /* synthetic */ Activity val$a;
        final /* synthetic */ int val$id;

        C00021(int i, Activity activity) {
            this.val$id = i;
            this.val$a = activity;
        }

        public void onClick(View view) {
            view.playSoundEffect(0);
            Intent intent = new Intent(C0003S.f3I);
            intent.putExtra("id", this.val$id);
            this.val$a.sendBroadcast(intent);
        }
    }

    static {
        f3I = "FLAG_FACTORY";
    }

    public C0003S(Activity activity) {
        int i = 0;
        f4a = activity;
        Context applicationContext = activity.getApplicationContext();
        GridLayout gridLayout = (GridLayout) activity.findViewById(C0001R.id.foodLayout);
        String[] strArr = new String[]{"\ud83c\udf55", "\ud83c\udf6c", "\ud83c\udf5e", "\ud83c\udf4e", "\ud83c\udf45", "\ud83c\udf59", "\ud83c\udf5d", "\ud83c\udf53", "\ud83c\udf48", "\ud83c\udf49", "\ud83c\udf30", "\ud83c\udf57", "\ud83c\udf64", "\ud83c\udf66", "\ud83c\udf47", "\ud83c\udf4c", "\ud83c\udf63", "\ud83c\udf44", "\ud83c\udf4a", "\ud83c\udf52", "\ud83c\udf60", "\ud83c\udf4d", "\ud83c\udf46", "\ud83c\udf5f", "\ud83c\udf54", "\ud83c\udf5c", "\ud83c\udf69", "\ud83c\udf5a", "\ud83c\udf68", "\ud83c\udf3e", "\ud83c\udf3d", "\ud83c\udf56"};
        while (i < 32) {
            View button = new Button(applicationContext);
            LayoutParams layoutParams = new GridLayout.LayoutParams();
            layoutParams.width = (int) TypedValue.applyDimension(1, 60.0f, activity.getResources().getDisplayMetrics());
            layoutParams.height = (int) TypedValue.applyDimension(1, 60.0f, activity.getResources().getDisplayMetrics());
            button.setLayoutParams(layoutParams);
            button.setText(strArr[i]);
            button.setOnClickListener(new C00021(i, activity));
            gridLayout.addView(button);
            i++;
        }
        IntentFilter intentFilter = new IntentFilter();
        intentFilter.addAction(f3I);
        activity.registerReceiver(new C0000F(activity), intentFilter);
    }
}
