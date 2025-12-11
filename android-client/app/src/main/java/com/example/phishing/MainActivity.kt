package com.example.phishing

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.io.IOException

class MainActivity : AppCompatActivity() {

    
    private val BACKEND_URL = "http://10.0.2.2:5001/predict"


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val urlInput = findViewById<EditText>(R.id.urlInput)
        val checkButton = findViewById<Button>(R.id.checkButton)
        val copyButton = findViewById<Button>(R.id.copyButton)
        val shareButton = findViewById<Button>(R.id.shareButton)
        val resultText = findViewById<TextView>(R.id.resultText)
        val historyText = findViewById<TextView>(R.id.historyText)
        val client = OkHttpClient()
        val prefs = getSharedPreferences("history", MODE_PRIVATE)

        
        val lastUrl = prefs.getString("last_url", "none")
        historyText.text = "Last checked: $lastUrl"

        checkButton.setOnClickListener {
            val url = urlInput.text.toString().trim()
            if (url.isEmpty()) {
                resultText.text = "Enter the URL"
                return@setOnClickListener
            }

            resultText.text = "Checking..."
            val json = JSONObject().apply { put("url", url) }
            val mediaType = "application/json; charset=utf-8".toMediaType()
            val body = json.toString().toRequestBody(mediaType)

            val request = Request.Builder()
                .url(BACKEND_URL)
                .post(body)
                .build()

            client.newCall(request).enqueue(object : Callback {
                override fun onFailure(call: Call, e: IOException) {
                    runOnUiThread {
                        resultText.text = " Network error: ${e.message}"
                    }
                }

                override fun onResponse(call: Call, response: Response) {
                    val respBody = response.body?.string()
                    runOnUiThread {
                        if (!response.isSuccessful || respBody.isNullOrEmpty()) {
                            resultText.text = "Server error."
                        } else {
                            try {
                                val obj = JSONObject(respBody)
                                val verdict = obj.optString("verdict")
                                val score = obj.optDouble("score")
                                resultText.text = " Verdict: $verdict\n🔢 Score: $score"

                               
                                prefs.edit().putString("last_url", url).apply()
                                historyText.text = "Last checked: $url"

                            } catch (e: Exception) {
                                resultText.text = "Parsing error."
                            }
                        }
                    }
                }
            })
        }

      
        copyButton.setOnClickListener {
            val textToCopy = resultText.text.toString()
            if (textToCopy.isNotEmpty()) {
                val clipboard = getSystemService(CLIPBOARD_SERVICE) as android.content.ClipboardManager
                val clip = android.content.ClipData.newPlainText("Phishing Result", textToCopy)
                clipboard.setPrimaryClip(clip)
                Toast.makeText(this, "Result copied!", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "No result yet!", Toast.LENGTH_SHORT).show()
            }
        }

     
        shareButton.setOnClickListener {
            val textToShare = resultText.text.toString()
            if (textToShare.isNotEmpty()) {
                val sendIntent = Intent().apply {
                    action = Intent.ACTION_SEND
                    putExtra(Intent.EXTRA_TEXT, textToShare)
                    type = "text/plain"
                }
                startActivity(Intent.createChooser(sendIntent, "Share via"))
            } else {
                Toast.makeText(this, "No result yet!", Toast.LENGTH_SHORT).show()
            }
        }
    }
}
