class MainActivity : AppCompatActivity() {
    private val BACKEND_URL = "http://10.0.2.2:5000/predict" // For Emulator
    private val client = OkHttpClient()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val urlInput = findViewById<EditText>(R.id.urlInput)
        val checkButton = findViewById<Button>(R.id.checkButton)
        val resultText = findViewById<TextView>(R.id.resultText)
        val progressBar = findViewById<ProgressBar>(R.id.progressBar)

        checkButton.setOnClickListener {
            val url = urlInput.text.toString().trim()
            if (url.isEmpty()) return@setOnClickListener

            progressBar.visibility = android.view.View.VISIBLE
            resultText.text = "Checking..."

            val json = JSONObject().put("url", url)
            val body = RequestBody.create("application/json".toMediaType(), json.toString())
            val request = Request.Builder().url(BACKEND_URL).post(body).build()

            client.newCall(request).enqueue(object : Callback {
                override fun onResponse(call: Call, response: Response) {
                    val respBody = response.body?.string()
                    runOnUiThread {
                        progressBar.visibility = android.view.View.GONE
                        try {
                            val obj = JSONObject(respBody ?: "{}")
                            val verdict = obj.optString("verdict", "unknown")
                            
                            // Color-coded display: Red for Phishing, Green for Legitimate
                            resultText.text = "VERDICT: ${verdict.uppercase()}"
                            resultText.setTextColor(if (verdict == "phishing") Color.RED else Color.GREEN)
                        } catch (e: Exception) {
                            resultText.text = "Error parsing result"
                        }
                    }
                }
                override fun onFailure(call: Call, e: IOException) {
                    runOnUiThread { 
                        progressBar.visibility = android.view.View.GONE
                        resultText.text = "❌ Network Error" 
                    }
                }
            })
        }
    }
}
