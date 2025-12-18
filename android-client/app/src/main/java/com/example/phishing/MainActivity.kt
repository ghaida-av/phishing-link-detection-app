import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText edtLink;
    Button btnCheck;
    TextView txtResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        edtLink = findViewById(R.id.edtLink);
        btnCheck = findViewById(R.id.btnCheck);
        txtResult = findViewById(R.id.txtResult);

        btnCheck.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String link = edtLink.getText().toString();
                // For simplicity, let's just check if the link contains the word 'phishing'
                if (link.contains("phishing")) {
                    txtResult.setText("Phishing!");
                } else {
                    txtResult.setText("Safe!");
                }
            }
        });
    }
}
