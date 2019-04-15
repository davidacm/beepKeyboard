# Beep keyboard NVDA Add-on #
Cette extension permet à l'utilisateur de configurer NVDA pour émettre des bips avec certains événements du clavier.

Copyright (C) 2019 David CM <dhf360@gmail.com>

Ce paquet est distribué sous les termes de la licence publique générale GNU, version 2 ou ultérieure.

## Caractéristiques
  Cette extension fournit les fonctionnalités suivantes que vous pouvez utiliser pour adapter le comportement du clavier NVDA:
  
* Bip pour les majuscules quand le verrouillage majuscule est activé: si cette fonctionnalité est activée, NVDA émettra un bip lorsque vous tapez une lettre majuscule et que le verrouillage majuscule est activé. Ne faites plus d'erreurs de majuscules !
* Bip pour les caractères saisis lorsque vous appuyez sur la touche maj: avec cette fonctionnalité, NVDA émettra un bip si vous tapez un caractère avec la touche maj enfoncée.
* Bip quand l'état des touches de l'interrupteur à bascule change: avec cette fonctionnalité, NVDA émettra un bip plus aigu si l'interrupteur à bascule est activé et une tonalité plus grave s'il est désactivé.
* Annoncer le changement de l'état des  touches de l'interrupteur à bascule: uniquement lorsque l'option "Bip pendant le changement de l'état des touches de l'interrupteur à bascule" est activé. Vous pouvez activer ou désactiver l'annonce des  touches de l'interrupteur à bascule lorsqu'elles changent d'état.
* Bip pour les caractères spécifiés: dans les paramètres avancés, vous pouvez configurer NVDA pour émettre un bip avec les caractères souhaités.

## Exigences
  Vous avez besoin de NVDA 2018.2 ou une version ultérieure.

## Installation
  Installez-le simplement comme n'importe quel extension NVDA.

## Utilisation
  Pour activer ou désactiver des fonctionnalités, accédez aux paramètres NVDA et sélectionnez la catégorie beep keyboard. Dans cette catégorie, vous pouvez configurer toutes les fonctionnalités prises en charge par l'extension.  
  "Bip pour les majuscules quand le verrouillage majuscule est activé" est activé par défaut.
  Si vous avez besoin de réglages supplémentaires, ouvrez la boîte de dialogue des paramètres avancés contenant les paramètres suivants:

* Ignorés les caractères saisis avec la touche maj enfoncée: tous les caractères saisis ici seront ignorés lors de l'émission du bip quand on appuie sur  la touche maj. Les séquences d'échappement sont autorisées, par exemple "\t" pour tab, "\r" pour la touche Entrée.
* Bip toujours pour les caractères suivants: insérez ici tous les caractères pour lesquels vous souhaitez que NVDA émette un bip. Les séquences d'échappement sont autorisées, par exemple "\t" pour tab, "\r" pour la touche Entrée.
* Choisir la tonalité à configurer: vous pouvez définir des paramètres pour toutes les tonalités. Sélectionnez-en une ici et ajustez les paramètres dans les zones de texte suivantes. Lors du changement des paramètres NVDA émettra  le bip de la tonalité sélectionnée avec les paramètres configurés à ce moment.
* Hauteur: hauteur pour la tonalité actuellement sélectionnée.
* Durée: durée pour la tonalité actuellement sélectionnée.
* Volume: volume pour la tonalité actuellement sélectionnée.
* Tester la tonalité: ce bouton vous permet de jouer une tonalité de test avec les paramètres actuellement définis.
* Appuyer sur le bouton OK pour sauvegarder la configuration ou sur Annuler pour les écarter.