const sjclogin = "sjc-login-site-v1"
const assets = [
  "/",
  "https://devagiricollege.net/sjc/asset/demo/s1.jpg"
]

self.addEventListener("install", installEvent => {
  installEvent.waitUntil(
    caches.open(sjclogin).then(cache => {
      cache.addAll(assets)
    })
  )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
      caches.match(fetchEvent.request).then(res => {
        return res || fetch(fetchEvent.request)
      })
    )
  })