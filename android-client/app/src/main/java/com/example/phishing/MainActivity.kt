package com.example.phishing

import android.graphics.Color
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ProgressBar
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import org.json.JSONObject
import java.io.IOException

class MainActivity : AppCompatActivity() {

    // IMPORTANT: Update this for your setup!
    // For Android Emulator: "http://10.0.2.2:5000/predict"
    // For Physical Android Phone: "http://YOUR_COMPUTER_IP:5000/predict"
    // Example: "http://192.168.1.100:5000/predict"
    // To find your IP: Mac: ifconfig | grep "inet " | grep -v 127.0.0.1
    //                  Windows: ipconfig
    private val BACKEND_URL = "http://10.0.2.2:5000/predict"

    private lateinit var urlInput: EditText
    private lateinit var checkButton: Button
    private lateinit var progressBar: ProgressBar
    private lateinit var resultText: TextView
    private lateinit var errorText: TextView

    private val client = OkHttpClient()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        urlInput = findViewById(R.id.urlInput)
        checkButton = findViewById(R.id.checkButton)
        progressBar = findViewById(R.id.progressBar)
        resultText = findViewById(R.id.resultText)
        errorText = findViewById(R.id.errorText)

        checkButton.setOnClickListener {
            val url = urlInput.text.toString().trim()
            if (url.isEmpty()) {
                showError("Please enter a URL")
                return@setOnClickListener
            }
            checkUrl(url)
        }
    }

    private fun checkUrl(url: String) {
        errorText.visibility = android.view.View.GONE
        resultText.text = ""
        progressBar.visibility = android.view.View.VISIBLE
        checkButton.isEnabled = false
        checkButton.text = "Checking..."

        val json = JSONObject()
        json.put("url", url)
        val mediaType = "application/json; charset=utf-8".toMediaType()
        val body = RequestBody.create(mediaType, json.toString())

        val request = Request.Builder()
            .url(BACKEND_URL)
            .post(body)
            .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                runOnUiThread {
                    progressBar.visibility = android.view.View.GONE
                    checkButton.isEnabled = true
                    checkButton.text = "Check URL"
                    showError("Network error. Make sure backend is running on port 5000")
                }
            }

            override fun onResponse(call: Call, response: Response) {
                val respBody = response.body?.string()
                runOnUiThread {
                    progressBar.visibility = android.view.View.GONE
                    checkButton.isEnabled = true
                    checkButton.text = "Check URL"

                    if (!response.isSuccessful) {
                        showError("Error: ${response.code}")
                    } else {
                        try {
                            val obj = JSONObject(respBody ?: "{}")
                            val verdict = obj.optString("verdict", "unknown")
                            val score = obj.optDouble("score", 0.0)
                            val reasons = obj.optJSONArray("reasons")

                            val scorePercent = (score * 100).toInt()
                            val verdictText = verdict.replaceFirstChar { it.uppercase() }
                            
                            val result = StringBuilder()
                            result.append("Result: $verdictText\n")
                            result.append("Risk Score: $scorePercent%\n\n")
                            
                            if (reasons != null && reasons.length() > 0) {
                                result.append("Reasons:\n")
                                for (i in 0 until reasons.length()) {
                                    result.append("• ${reasons.getString(i)}\n")
                                }
                            }

                            resultText.text = result.toString()
                            resultText.setTextColor(
                                if (verdict == "phishing") Color.RED else Color.GREEN
                            )
                        } catch (e: Exception) {
                            showError("Error parsing response")
                        }
                    }
                }
            }
        })
    }

    private fun showError(message: String) {
        errorText.text = message
        errorText.visibility = android.view.View.VISIBLE
        resultText.text = ""
    }
}

