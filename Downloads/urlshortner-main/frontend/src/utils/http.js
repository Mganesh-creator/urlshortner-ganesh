import axios from "axios";

function joinURL(baseURL, url) {
  return `${baseURL}/${url}`;
}

class Service {
  constructor() {
    this.domain = "";

    if (import.meta.env.VITE_BZENV === "development") {
      this.domain = import.meta.env.VITE_DEV_PROXY;
    }
  }

  async request(url, method = "POST", data) {
    url = joinURL(this.domain, "api/" + url);

    const token = localStorage.getItem("token");

    console.log("TOKEN:", token);

    const res = await axios.request({
      url,
      method,
      data,
      headers: {
        "Content-Type": "application/json",
        Authorization: token ? `Bearer ${token}` : "",
      },
    });

    return res.data;
  }

  post(url, data) {
    return this.request(url, "POST", data);
  }

  get(url) {
    return this.request(url, "GET");
  }

  delete(url, data) {
    return this.request(url, "DELETE", data);
  }

  put(url, data) {
    return this.request(url, "PUT", data);
  }

  patch(url, data) {
    return this.request(url, "PATCH", data);
  }

  getBaseURL = () => {
    if (import.meta.env.VITE_BZENV === "development") {
      return import.meta.env.VITE_DEV_PROXY || "http://localhost:3000";
    }

    return window.location.origin;
  };
}

export default Service;
