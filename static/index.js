window.onload = async () => {
  const aotButton = document.getElementById('attack-on-titan-button');
  const loadingText = document.getElementById('loading-text');
  aotButton.onclick = async () => {
    loadingText.style.visibility = 'visible';
    await fetch('/attack-on-titan', {
      method: 'POST'
    });
    loadingText.style.visibility = 'hidden';
  }
}
