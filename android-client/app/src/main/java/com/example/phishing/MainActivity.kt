package com.example.phishing

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.io.IOException

class MainActivity : AppCompatActivity() {

  private val BACKEND_URL = "https://jewell-unseconded-recurringly.ngrok-free.d/predict"


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val urlInput = findViewById<EditText>(R.id.urlInput)
        val checkButton = findViewById<Button>(R.id.checkButton)
        val resultText = findViewById<TextView>(R.id.resultText)
        val client = OkHttpClient()

        checkButton.setOnClickListener {
            val url = urlInput.text.toString().trim()
            if (url.isEmpty()) {
                resultText.text = "Enter the URL"
                return@setOnClickListener
            }

            resultText.text = "Checking..."
            val json = JSONObject().apply { put("url", url) }

            // ---- FIXED OKHTTP CALLS ----
            val mediaType = "application/json; charset=utf-8".toMediaType()
            val body = json.toString().toRequestBody(mediaType)
            // ----------------------------

            val request = Request.Builder()
                .url(BACKEND_URL)
                .post(body)
                .build()

            client.newCall(request).enqueue(object : Callback {
                override fun onFailure(call: Call, e: IOException) {
                    runOnUiThread { resultText.text = "❌ Network error: ${e.message}" }
                }

                override fun onResponse(call: Call, response: Response) {
                    val respBody = response.body?.string()   
                    runOnUiThread {
                        if (!response.isSuccessful || respBody.isNullOrEmpty()) {
                            resultText.text = "❌ Server error."
                        } else {
                            try {
                                val obj = JSONObject(respBody)
                                val verdict = obj.optString("verdict")
                                val score = obj.optDouble("score")
                                resultText.text = "✅ Verdict: $verdict\n🔢 Score: $score"
                            } catch (e: Exception) {
                                resultText.text = "⚠️ Parsing error."
                            }
                        }
                    }
                }
            })
        }
    }
}
