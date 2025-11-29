package com.example.phishing

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import okhttp3.*
import org.json.JSONObject
import java.io.IOException

class MainActivity : AppCompatActivity() {

    // change this to your backend URL when deployed (e.g., https://your-service.com/predict)
    private val BACKEND_URL = "http://10.0.2.2:5000/predict" // for Android emulator to reach localhost of host machine

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
                resultText.text = "Please enter a URL"
                return@setOnClickListener
            }

            val json = JSONObject()
            json.put("url", url)
            val body = RequestBody.create(MediaType.get("application/json; charset=utf-8"), json.toString())

            val request = Request.Builder()
                .url(BACKEND_URL)
                .post(body)
                .build()

            client.newCall(request).enqueue(object : Callback {
                override fun onFailure(call: Call, e: IOException) {
                    runOnUiThread {
                        resultText.text = "Network error: " + e.localizedMessage
                    }
                }

                override fun onResponse(call: Call, response: Response) {
                    val respBody = response.body()?.string()
                    runOnUiThread {
                        if (!response.isSuccessful) {
                            resultText.text = "Error: $respBody"
                        } else {
                            try {
                                val obj = JSONObject(respBody)
                                val verdict = obj.optString("verdict")
                                val score = obj.optDouble("score")
                                val reasons = obj.optJSONArray("reasons")
                                val reasonStr = StringBuilder()
                                if (reasons != null) {
                                    for (i in 0 until reasons.length()) {
                                        reasonStr.append("- ").append(reasons.getString(i)).append("\n")
                                    }
                                }
                                resultText.text = "Verdict: $verdict\nScore: $score\nReasons:\n$reasonStr"
                            } catch (e: Exception) {
                                resultText.text = "Parsing error: ${e.localizedMessage}"
                            }
                        }
                    }
                }
            })
        }
    }
}

