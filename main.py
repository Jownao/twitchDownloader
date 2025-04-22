import os
import subprocess

# Diretório para salvar os clipes
output_dir = "clips_baixados"
os.makedirs(output_dir, exist_ok=True)

# === CONFIGURAÇÃO: Escolha como carregar os links ===
usar_arquivo_txt = True  

# === Caminho do arquivo txt (caso usar_arquivo_txt = True) ===
caminho_arquivo_txt = "links_clipes.txt"

# Lista de links dos clipes
clips_manualmente  = [
    "https://www.twitch.tv/jownao/clip/ShakingGlamorousOryxTriHard-o6afrAuSAU50vNd_",
"https://www.twitch.tv/jownao/clip/FitSmoothPenguinFeelsBadMan-8bwqNynX9l_QHSQW",
"https://www.twitch.tv/jownao/clip/KathishSuccessfulEndiveWoofer-A-8f81m6DUO1LFSL",
"https://www.twitch.tv/jownao/clip/CalmLitigiousLegDxCat-4SlkDLJ-FaMfhhcj",
"https://www.twitch.tv/jownao/clip/NastyShakingRingRiPepperonis-21WAcWam5W74lxSS",
"https://www.twitch.tv/jownao/clip/VictoriousResilientMacaroniOptimizePrime-8WEV9sZjOzU01qo5",
"https://www.twitch.tv/jownao/clip/VivaciousSpikyHeronPicoMause-lSBTwTBvusq0yiHw",
"https://www.twitch.tv/jownao/clip/TubularSillyStarlingUnSane-Gy3vgO00TcH2862g",
"https://www.twitch.tv/jownao/clip/CovertKawaiiBubbleteaDxCat-h0dJU8vSK9HBjwG2",
"https://www.twitch.tv/jownao/clip/MoistStylishWolverineYouDontSay-zMlfEW2VEQzoqMXi",
"https://www.twitch.tv/jownao/clip/StormyAmazonianWrenRiPepperonis-1bu20Thsu8QGmcF6",
"https://www.twitch.tv/jownao/clip/CuriousPleasantAsparagusPanicVis-BL349P_p_ucmmJiy"
]

# === Caminho do arquivo txt (caso usar_arquivo_txt = True) ===
caminho_arquivo_txt = "links_clipes.txt"

# === Função para carregar os links ===
def carregar_links():
    if usar_arquivo_txt:
        with open(caminho_arquivo_txt, "r", encoding="utf-8") as f:
            return [linha.strip() for linha in f if linha.strip()]
    else:
        return clips_manualmente

# === Função para gerar nome único de arquivo ===
def gerar_nome_unico(base_path):
    if not os.path.exists(base_path):
        return base_path
    base, ext = os.path.splitext(base_path)
    i = 1
    while True:
        new_path = f"{base}_{i}{ext}"
        if not os.path.exists(new_path):
            return new_path
        i += 1

# === Começar download dos clipes ===
clips = carregar_links()

for clip in clips:
    print(f"\n🔽 Baixando: {clip}")
    
    # Obtem título do clipe com twitch-dl info
    result = subprocess.run(
        ["twitch-dl", "info", clip],
        capture_output=True, text=True
    )
    
    # Extrai título da saída
    title_line = next(
        (line for line in result.stdout.splitlines() if line.strip().startswith("Title:")),
        None
    )
    title = title_line.split("Title:")[1].strip() if title_line else "clip"
    safe_title = "".join(c for c in title if c.isalnum() or c in " _-").rstrip()

    # Gera nome único para o arquivo
    output_path = gerar_nome_unico(os.path.join(output_dir, f"{safe_title}.mp4"))

    # Baixa o clipe
    subprocess.run([
        "twitch-dl", "download", clip,
        "-q", "best",
        "-o", output_path
    ])