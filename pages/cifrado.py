import streamlit as st
st.markdown("---")
st.title("Cifrado césar")

st.markdown("En el cifrado César a cada letra del abecedario se desplaza x cantidad de puestos quedando $C=(P+K) mod 27$ donde C es la posición de la letra en el texto cifrado, P es la posición de la letra en el texto original, K es el desplazamiento y $mod 27$ es el modulo del alfabeto ya que tiene 27 letras. ")
st.markdown("---")

def cifrado_cesar(texto, desplazamiento):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto_cifrado = ""
    for letra in texto.lower():
        if letra in abecedario:
            posicion = abecedario.find(letra)
            nueva_posicion = (posicion + desplazamiento) % len(abecedario)
            letra_cifrada = abecedario[nueva_posicion]
            texto_cifrado += letra_cifrada
        else:
            texto_cifrado += letra
    return texto_cifrado
st.title("Primer paso del cifrado.")
st.markdown("Se identifica el texto que se desea cifrar.")
mensaje_original = st.text_area("Ingresa el texto a cifrar:")

st.markdown("---")
st.title("Segundo paso.")
st.markdown("Se identifica el numero de digitos que se desea desplazar el texto.")
desplazamiento = st.slider("Ingrese el digito de numeros que desea desplazar el texto:", min_value=1, max_value=27, value=3)
st.markdown("---")
st.title("Tercer paso.")
st.markdown("Se hace el cifrado moviendo las K unidades de desplazamiento a cada letra en el texto.")
if st.button("Cifrar"):
    mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
    st.success(f"Texto cifrado: {mensaje_cifrado}")
st.markdown("---")