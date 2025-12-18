package com.example.phishing

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val linkEditText = findViewById<EditText>(R.id.edtLink)
        val checkButton = findViewById<Button>(R.id.btnCheck)
        val resultTextView = findViewById<TextView>(R.id.txtResult)

        checkButton.setOnClickListener {
            val link = linkEditText.text.toString()
            if (link.contains("phish")) {
                resultTextView.text = "Phishing!"
            } else {
                resultTextView.text = "Safe!"
            }
        }
    }
}
