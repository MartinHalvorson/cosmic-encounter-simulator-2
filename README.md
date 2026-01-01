# Cosmic Encounter Simulator

<!-- NOTE: Only update the stats table below or feature implementation status. Do not modify other sections unless specifically requested. -->

A simulation of the board game Cosmic Encounter for analyzing alien power balance. Features **4022+ alien powers**, multiple AI strategies (including AggressiveAI, CautiousAI, OpportunisticAI, SocialAI, AdaptiveAI, LearningAI), and comprehensive statistics tracking across 2-6 player games.

## Alien Power Rankings

> **21,800,000+** games simulated | Last updated: 2025-12-31
>
> **Tier Guide:** 🟣 S (1600+) | 🔵 A (1550+) | 🟢 B (1500+) | 🟡 C (1450+) | 🔴 D (<1450)


<table id="rankings">
<thead>
<tr>
<th align="left" data-sort="rank">Rank</th>
<th align="left" data-sort="power">Power ⇅</th>
<th align="right" data-sort="elo">ELO ⇅</th>
<th align="right" data-sort="overall">Overall ⇅</th>
<th align="right" data-sort="2p">2P ⇅</th>
<th align="right" data-sort="3p">3P ⇅</th>
<th align="right" data-sort="4p">4P ⇅</th>
<th align="right" data-sort="5p">5P ⇅</th>
<th align="right" data-sort="6p">6P ⇅</th>
<th align="right" data-sort="games">Games ⇅</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">1</td>
<td align="left">🔵 Machine</td>
<td align="right"><b>1583</b></td>
<td align="right">56.8%</td>
<td align="right">70.5%</td>
<td align="right">69.8%</td>
<td align="right">65.1%</td>
<td align="right">56.9%</td>
<td align="right">44.7%</td>
<td align="right">2511</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🔵 Parasite</td>
<td align="right"><b>1579</b></td>
<td align="right">45.2%</td>
<td align="right">51.2%</td>
<td align="right">45.3%</td>
<td align="right">46.4%</td>
<td align="right">45.9%</td>
<td align="right">43.3%</td>
<td align="right">2607</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Lizard</td>
<td align="right"><b>1544</b></td>
<td align="right">99.6%</td>
<td align="right">95.7%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 The Meek</td>
<td align="right"><b>1544</b></td>
<td align="right">94.2%</td>
<td align="right">86.1%</td>
<td align="right">97.4%</td>
<td align="right">90.5%</td>
<td align="right">96.2%</td>
<td align="right">95.3%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Anarchist</td>
<td align="right"><b>1544</b></td>
<td align="right">99.5%</td>
<td align="right">94.6%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Mycelia</td>
<td align="right"><b>1544</b></td>
<td align="right">50.5%</td>
<td align="right">61.3%</td>
<td align="right">72.2%</td>
<td align="right">62.4%</td>
<td align="right">49.6%</td>
<td align="right">30.2%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Industrialist</td>
<td align="right"><b>1542</b></td>
<td align="right">46.4%</td>
<td align="right">96.1%</td>
<td align="right">71.4%</td>
<td align="right">51.2%</td>
<td align="right">27.7%</td>
<td align="right">26.2%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Corona</td>
<td align="right"><b>1539</b></td>
<td align="right">44.7%</td>
<td align="right">87.5%</td>
<td align="right">66.2%</td>
<td align="right">41.8%</td>
<td align="right">34.0%</td>
<td align="right">29.7%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Warpish</td>
<td align="right"><b>1533</b></td>
<td align="right">33.4%</td>
<td align="right">71.7%</td>
<td align="right">52.8%</td>
<td align="right">42.3%</td>
<td align="right">25.3%</td>
<td align="right">23.6%</td>
<td align="right">2471</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Symbiote</td>
<td align="right"><b>1529</b></td>
<td align="right">31.6%</td>
<td align="right">75.0%</td>
<td align="right">51.9%</td>
<td align="right">35.8%</td>
<td align="right">26.5%</td>
<td align="right">19.8%</td>
<td align="right">2440</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 Disease</td>
<td align="right"><b>1528</b></td>
<td align="right">28.1%</td>
<td align="right">46.0%</td>
<td align="right">41.5%</td>
<td align="right">27.9%</td>
<td align="right">22.8%</td>
<td align="right">24.4%</td>
<td align="right">2602</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 Helix</td>
<td align="right"><b>1525</b></td>
<td align="right">36.6%</td>
<td align="right">84.0%</td>
<td align="right">49.0%</td>
<td align="right">26.6%</td>
<td align="right">32.4%</td>
<td align="right">22.4%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Investor</td>
<td align="right"><b>1524</b></td>
<td align="right">37.5%</td>
<td align="right">66.0%</td>
<td align="right">50.9%</td>
<td align="right">48.4%</td>
<td align="right">21.7%</td>
<td align="right">22.5%</td>
<td align="right">400</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Tripler</td>
<td align="right"><b>1523</b></td>
<td align="right">29.8%</td>
<td align="right">79.5%</td>
<td align="right">49.2%</td>
<td align="right">29.8%</td>
<td align="right">25.3%</td>
<td align="right">20.9%</td>
<td align="right">2642</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Mutant</td>
<td align="right"><b>1523</b></td>
<td align="right">27.3%</td>
<td align="right">62.2%</td>
<td align="right">45.4%</td>
<td align="right">30.6%</td>
<td align="right">23.6%</td>
<td align="right">17.8%</td>
<td align="right">2649</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Pearl</td>
<td align="right"><b>1521</b></td>
<td align="right">33.5%</td>
<td align="right">69.4%</td>
<td align="right">50.7%</td>
<td align="right">34.1%</td>
<td align="right">27.7%</td>
<td align="right">20.9%</td>
<td align="right">465</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Fortress</td>
<td align="right"><b>1521</b></td>
<td align="right">37.1%</td>
<td align="right">77.3%</td>
<td align="right">57.5%</td>
<td align="right">30.0%</td>
<td align="right">29.4%</td>
<td align="right">20.3%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Baker</td>
<td align="right"><b>1519</b></td>
<td align="right">38.0%</td>
<td align="right">78.3%</td>
<td align="right">47.5%</td>
<td align="right">37.1%</td>
<td align="right">33.3%</td>
<td align="right">23.2%</td>
<td align="right">245</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Pulsar</td>
<td align="right"><b>1519</b></td>
<td align="right">32.2%</td>
<td align="right">58.3%</td>
<td align="right">38.5%</td>
<td align="right">37.1%</td>
<td align="right">25.2%</td>
<td align="right">24.8%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Pacifist</td>
<td align="right"><b>1518</b></td>
<td align="right">28.7%</td>
<td align="right">71.1%</td>
<td align="right">51.7%</td>
<td align="right">34.1%</td>
<td align="right">19.8%</td>
<td align="right">19.0%</td>
<td align="right">2606</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 Ranger</td>
<td align="right"><b>1518</b></td>
<td align="right">34.3%</td>
<td align="right">65.1%</td>
<td align="right">44.9%</td>
<td align="right">34.0%</td>
<td align="right">34.2%</td>
<td align="right">20.0%</td>
<td align="right">472</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Coral</td>
<td align="right"><b>1518</b></td>
<td align="right">34.8%</td>
<td align="right">74.5%</td>
<td align="right">39.7%</td>
<td align="right">36.2%</td>
<td align="right">31.1%</td>
<td align="right">19.6%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Superposition</td>
<td align="right"><b>1517</b></td>
<td align="right">32.4%</td>
<td align="right">55.8%</td>
<td align="right">38.6%</td>
<td align="right">42.0%</td>
<td align="right">36.1%</td>
<td align="right">16.2%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Cultist</td>
<td align="right"><b>1517</b></td>
<td align="right">39.0%</td>
<td align="right">81.5%</td>
<td align="right">59.0%</td>
<td align="right">50.0%</td>
<td align="right">20.8%</td>
<td align="right">20.0%</td>
<td align="right">249</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Ritualist</td>
<td align="right"><b>1516</b></td>
<td align="right">35.1%</td>
<td align="right">67.4%</td>
<td align="right">38.6%</td>
<td align="right">31.5%</td>
<td align="right">31.1%</td>
<td align="right">25.9%</td>
<td align="right">407</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Debugger</td>
<td align="right"><b>1516</b></td>
<td align="right">33.9%</td>
<td align="right">72.7%</td>
<td align="right">55.2%</td>
<td align="right">33.0%</td>
<td align="right">24.8%</td>
<td align="right">19.7%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 GammaRay</td>
<td align="right"><b>1516</b></td>
<td align="right">32.7%</td>
<td align="right">65.9%</td>
<td align="right">50.7%</td>
<td align="right">34.1%</td>
<td align="right">24.1%</td>
<td align="right">20.8%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Glacier</td>
<td align="right"><b>1516</b></td>
<td align="right">31.9%</td>
<td align="right">63.6%</td>
<td align="right">46.6%</td>
<td align="right">24.1%</td>
<td align="right">20.2%</td>
<td align="right">27.1%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟢 Speedrunner</td>
<td align="right"><b>1516</b></td>
<td align="right">52.0%</td>
<td align="right">100.0%</td>
<td align="right">83.3%</td>
<td align="right">38.5%</td>
<td align="right">50.0%</td>
<td align="right">30.8%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟢 Farmer</td>
<td align="right"><b>1516</b></td>
<td align="right">30.5%</td>
<td align="right">57.5%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">21.9%</td>
<td align="right">20.5%</td>
<td align="right">403</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟢 Neighbor</td>
<td align="right"><b>1516</b></td>
<td align="right">32.6%</td>
<td align="right">63.9%</td>
<td align="right">63.4%</td>
<td align="right">25.4%</td>
<td align="right">23.7%</td>
<td align="right">18.7%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟢 Macron</td>
<td align="right"><b>1515</b></td>
<td align="right">29.5%</td>
<td align="right">85.2%</td>
<td align="right">46.5%</td>
<td align="right">30.4%</td>
<td align="right">25.3%</td>
<td align="right">20.0%</td>
<td align="right">2562</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟢 Martyr</td>
<td align="right"><b>1515</b></td>
<td align="right">32.6%</td>
<td align="right">70.0%</td>
<td align="right">46.3%</td>
<td align="right">27.7%</td>
<td align="right">23.9%</td>
<td align="right">20.2%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟢 Steward</td>
<td align="right"><b>1515</b></td>
<td align="right">31.9%</td>
<td align="right">71.4%</td>
<td align="right">40.8%</td>
<td align="right">31.3%</td>
<td align="right">26.6%</td>
<td align="right">19.1%</td>
<td align="right">398</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟢 Banker</td>
<td align="right"><b>1515</b></td>
<td align="right">33.1%</td>
<td align="right">60.4%</td>
<td align="right">46.7%</td>
<td align="right">33.7%</td>
<td align="right">22.3%</td>
<td align="right">26.3%</td>
<td align="right">478</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟢 Exile</td>
<td align="right"><b>1514</b></td>
<td align="right">33.0%</td>
<td align="right">56.0%</td>
<td align="right">51.6%</td>
<td align="right">38.1%</td>
<td align="right">22.7%</td>
<td align="right">19.8%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟢 Dervish</td>
<td align="right"><b>1514</b></td>
<td align="right">32.1%</td>
<td align="right">77.8%</td>
<td align="right">43.8%</td>
<td align="right">34.1%</td>
<td align="right">21.9%</td>
<td align="right">16.4%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟢 Giant</td>
<td align="right"><b>1514</b></td>
<td align="right">31.5%</td>
<td align="right">72.5%</td>
<td align="right">48.5%</td>
<td align="right">30.6%</td>
<td align="right">24.0%</td>
<td align="right">17.5%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟢 Pygmy</td>
<td align="right"><b>1513</b></td>
<td align="right">30.5%</td>
<td align="right">57.4%</td>
<td align="right">43.8%</td>
<td align="right">33.3%</td>
<td align="right">21.0%</td>
<td align="right">20.0%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟢 Compiler</td>
<td align="right"><b>1513</b></td>
<td align="right">31.4%</td>
<td align="right">78.0%</td>
<td align="right">53.2%</td>
<td align="right">23.5%</td>
<td align="right">19.2%</td>
<td align="right">16.2%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟢 Merger</td>
<td align="right"><b>1513</b></td>
<td align="right">30.7%</td>
<td align="right">38.6%</td>
<td align="right">36.8%</td>
<td align="right">27.5%</td>
<td align="right">32.4%</td>
<td align="right">24.4%</td>
<td align="right">473</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟢 Recover</td>
<td align="right"><b>1513</b></td>
<td align="right">30.0%</td>
<td align="right">51.9%</td>
<td align="right">45.8%</td>
<td align="right">36.2%</td>
<td align="right">21.0%</td>
<td align="right">15.7%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟢 Core</td>
<td align="right"><b>1513</b></td>
<td align="right">30.5%</td>
<td align="right">56.2%</td>
<td align="right">41.3%</td>
<td align="right">28.6%</td>
<td align="right">21.8%</td>
<td align="right">21.5%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟢 Human</td>
<td align="right"><b>1513</b></td>
<td align="right">26.3%</td>
<td align="right">59.6%</td>
<td align="right">42.4%</td>
<td align="right">28.1%</td>
<td align="right">20.2%</td>
<td align="right">19.8%</td>
<td align="right">2495</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟢 Knight</td>
<td align="right"><b>1513</b></td>
<td align="right">28.8%</td>
<td align="right">54.2%</td>
<td align="right">40.7%</td>
<td align="right">24.4%</td>
<td align="right">24.5%</td>
<td align="right">21.0%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟢 Lender</td>
<td align="right"><b>1513</b></td>
<td align="right">29.9%</td>
<td align="right">59.0%</td>
<td align="right">39.3%</td>
<td align="right">37.2%</td>
<td align="right">23.5%</td>
<td align="right">18.4%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟢 Chrysalis</td>
<td align="right"><b>1513</b></td>
<td align="right">28.6%</td>
<td align="right">73.2%</td>
<td align="right">45.5%</td>
<td align="right">33.3%</td>
<td align="right">24.3%</td>
<td align="right">18.0%</td>
<td align="right">1854</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟢 Aurora</td>
<td align="right"><b>1513</b></td>
<td align="right">30.2%</td>
<td align="right">64.4%</td>
<td align="right">43.8%</td>
<td align="right">29.5%</td>
<td align="right">23.0%</td>
<td align="right">17.6%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟢 Negotiator</td>
<td align="right"><b>1512</b></td>
<td align="right">29.5%</td>
<td align="right">59.1%</td>
<td align="right">32.9%</td>
<td align="right">24.7%</td>
<td align="right">23.5%</td>
<td align="right">25.8%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟢 Smasher</td>
<td align="right"><b>1512</b></td>
<td align="right">30.4%</td>
<td align="right">65.5%</td>
<td align="right">50.0%</td>
<td align="right">28.4%</td>
<td align="right">26.6%</td>
<td align="right">10.5%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟢 Defender</td>
<td align="right"><b>1512</b></td>
<td align="right">30.0%</td>
<td align="right">57.9%</td>
<td align="right">32.4%</td>
<td align="right">34.1%</td>
<td align="right">25.3%</td>
<td align="right">21.7%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟢 Xenophobe</td>
<td align="right"><b>1512</b></td>
<td align="right">31.8%</td>
<td align="right">73.7%</td>
<td align="right">42.6%</td>
<td align="right">28.3%</td>
<td align="right">19.6%</td>
<td align="right">20.5%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟢 Predator_Alt</td>
<td align="right"><b>1512</b></td>
<td align="right">31.2%</td>
<td align="right">81.0%</td>
<td align="right">37.3%</td>
<td align="right">35.5%</td>
<td align="right">20.7%</td>
<td align="right">14.4%</td>
<td align="right">388</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟢 Shadow</td>
<td align="right"><b>1512</b></td>
<td align="right">27.6%</td>
<td align="right">66.7%</td>
<td align="right">43.8%</td>
<td align="right">33.2%</td>
<td align="right">21.4%</td>
<td align="right">17.7%</td>
<td align="right">2630</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟢 Fossil</td>
<td align="right"><b>1512</b></td>
<td align="right">31.0%</td>
<td align="right">64.0%</td>
<td align="right">35.3%</td>
<td align="right">27.1%</td>
<td align="right">29.2%</td>
<td align="right">20.9%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟢 Merchant</td>
<td align="right"><b>1512</b></td>
<td align="right">28.9%</td>
<td align="right">57.4%</td>
<td align="right">41.1%</td>
<td align="right">36.2%</td>
<td align="right">20.1%</td>
<td align="right">16.5%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟢 Monsoon</td>
<td align="right"><b>1511</b></td>
<td align="right">29.7%</td>
<td align="right">60.5%</td>
<td align="right">41.2%</td>
<td align="right">29.9%</td>
<td align="right">22.4%</td>
<td align="right">18.5%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟢 Feral</td>
<td align="right"><b>1511</b></td>
<td align="right">31.9%</td>
<td align="right">60.5%</td>
<td align="right">58.9%</td>
<td align="right">30.1%</td>
<td align="right">20.0%</td>
<td align="right">16.9%</td>
<td align="right">407</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟢 Geologist</td>
<td align="right"><b>1511</b></td>
<td align="right">41.4%</td>
<td align="right">85.7%</td>
<td align="right">43.8%</td>
<td align="right">33.3%</td>
<td align="right">34.4%</td>
<td align="right">45.5%</td>
<td align="right">87</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟢 Quasar</td>
<td align="right"><b>1511</b></td>
<td align="right">29.8%</td>
<td align="right">52.3%</td>
<td align="right">38.6%</td>
<td align="right">40.2%</td>
<td align="right">27.4%</td>
<td align="right">17.9%</td>
<td align="right">473</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟢 Velocity</td>
<td align="right"><b>1511</b></td>
<td align="right">30.7%</td>
<td align="right">49.0%</td>
<td align="right">46.0%</td>
<td align="right">31.6%</td>
<td align="right">24.3%</td>
<td align="right">21.7%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟢 Trader</td>
<td align="right"><b>1511</b></td>
<td align="right">26.7%</td>
<td align="right">64.0%</td>
<td align="right">45.7%</td>
<td align="right">28.6%</td>
<td align="right">22.4%</td>
<td align="right">16.9%</td>
<td align="right">2569</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟢 Magnetar</td>
<td align="right"><b>1511</b></td>
<td align="right">29.6%</td>
<td align="right">56.4%</td>
<td align="right">44.0%</td>
<td align="right">27.3%</td>
<td align="right">28.1%</td>
<td align="right">19.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟢 Partner</td>
<td align="right"><b>1511</b></td>
<td align="right">29.0%</td>
<td align="right">61.1%</td>
<td align="right">41.6%</td>
<td align="right">25.5%</td>
<td align="right">21.1%</td>
<td align="right">22.6%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟢 Ultra</td>
<td align="right"><b>1511</b></td>
<td align="right">31.9%</td>
<td align="right">61.9%</td>
<td align="right">48.1%</td>
<td align="right">31.2%</td>
<td align="right">23.7%</td>
<td align="right">16.7%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟢 Psychic</td>
<td align="right"><b>1511</b></td>
<td align="right">26.6%</td>
<td align="right">53.3%</td>
<td align="right">35.6%</td>
<td align="right">21.6%</td>
<td align="right">23.1%</td>
<td align="right">18.8%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟢 Brotherhood</td>
<td align="right"><b>1511</b></td>
<td align="right">30.6%</td>
<td align="right">54.7%</td>
<td align="right">33.3%</td>
<td align="right">37.5%</td>
<td align="right">22.6%</td>
<td align="right">23.4%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟢 Masochist_Alt</td>
<td align="right"><b>1511</b></td>
<td align="right">31.1%</td>
<td align="right">69.2%</td>
<td align="right">42.3%</td>
<td align="right">28.7%</td>
<td align="right">28.8%</td>
<td align="right">17.6%</td>
<td align="right">486</td>
</tr>
<tr>
<td align="left">69</td>
<td align="left">🟢 Miner</td>
<td align="right"><b>1510</b></td>
<td align="right">27.8%</td>
<td align="right">50.0%</td>
<td align="right">43.5%</td>
<td align="right">23.9%</td>
<td align="right">22.6%</td>
<td align="right">19.0%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">70</td>
<td align="left">🟢 Nadir</td>
<td align="right"><b>1510</b></td>
<td align="right">29.1%</td>
<td align="right">69.4%</td>
<td align="right">43.1%</td>
<td align="right">29.5%</td>
<td align="right">17.9%</td>
<td align="right">15.5%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">71</td>
<td align="left">🟢 Sapient</td>
<td align="right"><b>1510</b></td>
<td align="right">28.4%</td>
<td align="right">52.4%</td>
<td align="right">45.9%</td>
<td align="right">26.7%</td>
<td align="right">29.6%</td>
<td align="right">12.0%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">72</td>
<td align="left">🟢 Kineticist</td>
<td align="right"><b>1510</b></td>
<td align="right">29.8%</td>
<td align="right">61.8%</td>
<td align="right">33.3%</td>
<td align="right">26.9%</td>
<td align="right">25.0%</td>
<td align="right">19.8%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">73</td>
<td align="left">🟢 Admiral</td>
<td align="right"><b>1510</b></td>
<td align="right">28.9%</td>
<td align="right">60.0%</td>
<td align="right">30.3%</td>
<td align="right">26.3%</td>
<td align="right">29.3%</td>
<td align="right">16.8%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">74</td>
<td align="left">🟢 Ruby</td>
<td align="right"><b>1510</b></td>
<td align="right">31.4%</td>
<td align="right">56.0%</td>
<td align="right">42.0%</td>
<td align="right">30.9%</td>
<td align="right">26.6%</td>
<td align="right">23.6%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">75</td>
<td align="left">🟢 Aristocrat</td>
<td align="right"><b>1510</b></td>
<td align="right">26.8%</td>
<td align="right">61.2%</td>
<td align="right">39.1%</td>
<td align="right">26.9%</td>
<td align="right">25.2%</td>
<td align="right">19.1%</td>
<td align="right">1832</td>
</tr>
<tr>
<td align="left">76</td>
<td align="left">🟢 Snowfall</td>
<td align="right"><b>1510</b></td>
<td align="right">40.0%</td>
<td align="right">45.5%</td>
<td align="right">69.2%</td>
<td align="right">28.6%</td>
<td align="right">31.6%</td>
<td align="right">30.8%</td>
<td align="right">70</td>
</tr>
<tr>
<td align="left">77</td>
<td align="left">🟢 Rival</td>
<td align="right"><b>1510</b></td>
<td align="right">40.0%</td>
<td align="right">57.1%</td>
<td align="right">63.6%</td>
<td align="right">45.5%</td>
<td align="right">38.9%</td>
<td align="right">21.7%</td>
<td align="right">70</td>
</tr>
<tr>
<td align="left">78</td>
<td align="left">🟢 Virus</td>
<td align="right"><b>1510</b></td>
<td align="right">26.9%</td>
<td align="right">80.6%</td>
<td align="right">41.1%</td>
<td align="right">26.0%</td>
<td align="right">25.3%</td>
<td align="right">19.4%</td>
<td align="right">2523</td>
</tr>
<tr>
<td align="left">79</td>
<td align="left">🟢 Flutist</td>
<td align="right"><b>1510</b></td>
<td align="right">28.7%</td>
<td align="right">61.7%</td>
<td align="right">38.2%</td>
<td align="right">30.3%</td>
<td align="right">21.7%</td>
<td align="right">17.2%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">80</td>
<td align="left">🟢 Ace</td>
<td align="right"><b>1510</b></td>
<td align="right">28.2%</td>
<td align="right">55.0%</td>
<td align="right">49.2%</td>
<td align="right">28.7%</td>
<td align="right">21.2%</td>
<td align="right">13.2%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">81</td>
<td align="left">🟢 Conductor</td>
<td align="right"><b>1510</b></td>
<td align="right">26.5%</td>
<td align="right">41.5%</td>
<td align="right">41.8%</td>
<td align="right">30.4%</td>
<td align="right">15.5%</td>
<td align="right">18.5%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">82</td>
<td align="left">🟢 Fighter</td>
<td align="right"><b>1510</b></td>
<td align="right">29.7%</td>
<td align="right">68.0%</td>
<td align="right">36.4%</td>
<td align="right">23.9%</td>
<td align="right">27.0%</td>
<td align="right">18.3%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">83</td>
<td align="left">🟢 Pretender_Alt</td>
<td align="right"><b>1510</b></td>
<td align="right">28.3%</td>
<td align="right">55.6%</td>
<td align="right">45.9%</td>
<td align="right">25.8%</td>
<td align="right">16.0%</td>
<td align="right">20.0%</td>
<td align="right">382</td>
</tr>
<tr>
<td align="left">84</td>
<td align="left">🟢 Entrepreneur</td>
<td align="right"><b>1510</b></td>
<td align="right">27.9%</td>
<td align="right">53.3%</td>
<td align="right">40.0%</td>
<td align="right">23.8%</td>
<td align="right">22.9%</td>
<td align="right">19.2%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">85</td>
<td align="left">🟢 Misfortune</td>
<td align="right"><b>1509</b></td>
<td align="right">28.5%</td>
<td align="right">47.8%</td>
<td align="right">37.3%</td>
<td align="right">31.0%</td>
<td align="right">24.7%</td>
<td align="right">20.7%</td>
<td align="right">386</td>
</tr>
<tr>
<td align="left">86</td>
<td align="left">🟢 Betrayer</td>
<td align="right"><b>1509</b></td>
<td align="right">28.7%</td>
<td align="right">49.0%</td>
<td align="right">43.1%</td>
<td align="right">19.3%</td>
<td align="right">27.8%</td>
<td align="right">20.0%</td>
<td align="right">397</td>
</tr>
<tr>
<td align="left">87</td>
<td align="left">🟢 Tentacle</td>
<td align="right"><b>1509</b></td>
<td align="right">26.5%</td>
<td align="right">55.9%</td>
<td align="right">33.7%</td>
<td align="right">27.6%</td>
<td align="right">16.5%</td>
<td align="right">20.8%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">88</td>
<td align="left">🟢 Spellcaster</td>
<td align="right"><b>1509</b></td>
<td align="right">38.8%</td>
<td align="right">71.4%</td>
<td align="right">46.2%</td>
<td align="right">50.0%</td>
<td align="right">35.3%</td>
<td align="right">24.1%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">89</td>
<td align="left">🟢 Guarantor</td>
<td align="right"><b>1509</b></td>
<td align="right">30.6%</td>
<td align="right">43.9%</td>
<td align="right">44.6%</td>
<td align="right">26.0%</td>
<td align="right">24.6%</td>
<td align="right">26.9%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">90</td>
<td align="left">🟢 Sorrow</td>
<td align="right"><b>1509</b></td>
<td align="right">28.2%</td>
<td align="right">61.5%</td>
<td align="right">38.7%</td>
<td align="right">27.1%</td>
<td align="right">19.3%</td>
<td align="right">17.8%</td>
<td align="right">390</td>
</tr>
<tr>
<td align="left">91</td>
<td align="left">🟢 Champion_Alt</td>
<td align="right"><b>1509</b></td>
<td align="right">28.5%</td>
<td align="right">41.3%</td>
<td align="right">53.7%</td>
<td align="right">25.0%</td>
<td align="right">24.0%</td>
<td align="right">19.1%</td>
<td align="right">396</td>
</tr>
<tr>
<td align="left">92</td>
<td align="left">🟢 Deja</td>
<td align="right"><b>1509</b></td>
<td align="right">38.4%</td>
<td align="right">75.0%</td>
<td align="right">36.4%</td>
<td align="right">28.6%</td>
<td align="right">52.6%</td>
<td align="right">28.0%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">93</td>
<td align="left">🟢 Dominator</td>
<td align="right"><b>1509</b></td>
<td align="right">27.7%</td>
<td align="right">47.7%</td>
<td align="right">36.4%</td>
<td align="right">29.7%</td>
<td align="right">23.5%</td>
<td align="right">17.2%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">94</td>
<td align="left">🟢 Sprinter</td>
<td align="right"><b>1509</b></td>
<td align="right">38.2%</td>
<td align="right">62.5%</td>
<td align="right">37.5%</td>
<td align="right">42.9%</td>
<td align="right">28.6%</td>
<td align="right">36.7%</td>
<td align="right">89</td>
</tr>
<tr>
<td align="left">95</td>
<td align="left">🟢 Shaman</td>
<td align="right"><b>1509</b></td>
<td align="right">27.5%</td>
<td align="right">54.3%</td>
<td align="right">30.3%</td>
<td align="right">29.4%</td>
<td align="right">23.4%</td>
<td align="right">18.9%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">96</td>
<td align="left">🟢 Higgs</td>
<td align="right"><b>1509</b></td>
<td align="right">29.2%</td>
<td align="right">63.0%</td>
<td align="right">41.8%</td>
<td align="right">26.7%</td>
<td align="right">20.4%</td>
<td align="right">21.1%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">97</td>
<td align="left">🟢 Calm</td>
<td align="right"><b>1509</b></td>
<td align="right">27.4%</td>
<td align="right">53.5%</td>
<td align="right">33.3%</td>
<td align="right">26.6%</td>
<td align="right">24.5%</td>
<td align="right">18.6%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">98</td>
<td align="left">🟢 Stormer</td>
<td align="right"><b>1509</b></td>
<td align="right">30.0%</td>
<td align="right">54.9%</td>
<td align="right">37.8%</td>
<td align="right">27.6%</td>
<td align="right">26.0%</td>
<td align="right">20.9%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">99</td>
<td align="left">🟢 Teacher</td>
<td align="right"><b>1509</b></td>
<td align="right">26.8%</td>
<td align="right">58.1%</td>
<td align="right">32.8%</td>
<td align="right">27.8%</td>
<td align="right">24.5%</td>
<td align="right">14.5%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">🟢 Bishop</td>
<td align="right"><b>1509</b></td>
<td align="right">38.0%</td>
<td align="right">83.3%</td>
<td align="right">85.7%</td>
<td align="right">27.3%</td>
<td align="right">22.7%</td>
<td align="right">19.2%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">101</td>
<td align="left">🟢 Shade</td>
<td align="right"><b>1509</b></td>
<td align="right">29.1%</td>
<td align="right">47.9%</td>
<td align="right">41.4%</td>
<td align="right">27.4%</td>
<td align="right">24.3%</td>
<td align="right">20.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">102</td>
<td align="left">🟢 Unpredictable</td>
<td align="right"><b>1509</b></td>
<td align="right">27.5%</td>
<td align="right">53.7%</td>
<td align="right">35.4%</td>
<td align="right">26.5%</td>
<td align="right">23.6%</td>
<td align="right">18.9%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">103</td>
<td align="left">🟢 Serendipity</td>
<td align="right"><b>1509</b></td>
<td align="right">30.0%</td>
<td align="right">57.7%</td>
<td align="right">40.3%</td>
<td align="right">30.6%</td>
<td align="right">29.6%</td>
<td align="right">16.0%</td>
<td align="right">477</td>
</tr>
<tr>
<td align="left">104</td>
<td align="left">🟢 Leaf</td>
<td align="right"><b>1509</b></td>
<td align="right">37.8%</td>
<td align="right">75.0%</td>
<td align="right">68.8%</td>
<td align="right">37.5%</td>
<td align="right">22.2%</td>
<td align="right">16.7%</td>
<td align="right">90</td>
</tr>
<tr>
<td align="left">105</td>
<td align="left">🟢 Infantry</td>
<td align="right"><b>1509</b></td>
<td align="right">28.0%</td>
<td align="right">65.7%</td>
<td align="right">31.5%</td>
<td align="right">29.7%</td>
<td align="right">30.2%</td>
<td align="right">14.9%</td>
<td align="right">400</td>
</tr>
<tr>
<td align="left">106</td>
<td align="left">🟢 Obliterator</td>
<td align="right"><b>1509</b></td>
<td align="right">28.1%</td>
<td align="right">65.5%</td>
<td align="right">29.2%</td>
<td align="right">28.0%</td>
<td align="right">23.5%</td>
<td align="right">16.7%</td>
<td align="right">509</td>
</tr>
<tr>
<td align="left">107</td>
<td align="left">🟢 Whisperer</td>
<td align="right"><b>1509</b></td>
<td align="right">27.6%</td>
<td align="right">61.0%</td>
<td align="right">46.9%</td>
<td align="right">27.7%</td>
<td align="right">14.5%</td>
<td align="right">19.1%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">108</td>
<td align="left">🟢 Plasma</td>
<td align="right"><b>1509</b></td>
<td align="right">26.3%</td>
<td align="right">56.8%</td>
<td align="right">37.2%</td>
<td align="right">27.6%</td>
<td align="right">22.0%</td>
<td align="right">15.0%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">109</td>
<td align="left">🟢 Ancient</td>
<td align="right"><b>1509</b></td>
<td align="right">26.7%</td>
<td align="right">44.0%</td>
<td align="right">40.6%</td>
<td align="right">32.8%</td>
<td align="right">13.4%</td>
<td align="right">22.0%</td>
<td align="right">270</td>
</tr>
<tr>
<td align="left">110</td>
<td align="left">🟢 Protector</td>
<td align="right"><b>1508</b></td>
<td align="right">28.3%</td>
<td align="right">59.6%</td>
<td align="right">36.4%</td>
<td align="right">31.5%</td>
<td align="right">23.8%</td>
<td align="right">15.3%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">111</td>
<td align="left">🟢 Prodigy</td>
<td align="right"><b>1508</b></td>
<td align="right">27.4%</td>
<td align="right">50.0%</td>
<td align="right">41.0%</td>
<td align="right">26.0%</td>
<td align="right">17.1%</td>
<td align="right">22.3%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">112</td>
<td align="left">🟢 Bolt</td>
<td align="right"><b>1508</b></td>
<td align="right">28.3%</td>
<td align="right">48.7%</td>
<td align="right">36.2%</td>
<td align="right">34.4%</td>
<td align="right">25.7%</td>
<td align="right">17.8%</td>
<td align="right">463</td>
</tr>
<tr>
<td align="left">113</td>
<td align="left">🟢 Werewolf</td>
<td align="right"><b>1508</b></td>
<td align="right">28.8%</td>
<td align="right">55.8%</td>
<td align="right">38.9%</td>
<td align="right">30.1%</td>
<td align="right">24.0%</td>
<td align="right">19.6%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">114</td>
<td align="left">🟢 Helper</td>
<td align="right"><b>1508</b></td>
<td align="right">27.5%</td>
<td align="right">53.5%</td>
<td align="right">25.7%</td>
<td align="right">35.9%</td>
<td align="right">22.9%</td>
<td align="right">18.4%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">115</td>
<td align="left">🟢 Chronos</td>
<td align="right"><b>1508</b></td>
<td align="right">23.8%</td>
<td align="right">54.4%</td>
<td align="right">31.9%</td>
<td align="right">26.9%</td>
<td align="right">20.1%</td>
<td align="right">18.3%</td>
<td align="right">2571</td>
</tr>
<tr>
<td align="left">116</td>
<td align="left">🟢 Fern</td>
<td align="right"><b>1508</b></td>
<td align="right">37.1%</td>
<td align="right">66.7%</td>
<td align="right">45.5%</td>
<td align="right">33.3%</td>
<td align="right">29.4%</td>
<td align="right">28.6%</td>
<td align="right">70</td>
</tr>
<tr>
<td align="left">117</td>
<td align="left">🟢 Hadron</td>
<td align="right"><b>1508</b></td>
<td align="right">28.3%</td>
<td align="right">71.1%</td>
<td align="right">31.1%</td>
<td align="right">33.0%</td>
<td align="right">18.2%</td>
<td align="right">18.4%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">118</td>
<td align="left">🟢 Bunker</td>
<td align="right"><b>1508</b></td>
<td align="right">27.4%</td>
<td align="right">42.6%</td>
<td align="right">38.5%</td>
<td align="right">32.4%</td>
<td align="right">22.9%</td>
<td align="right">15.3%</td>
<td align="right">475</td>
</tr>
<tr>
<td align="left">119</td>
<td align="left">🟢 Faker</td>
<td align="right"><b>1508</b></td>
<td align="right">26.0%</td>
<td align="right">61.9%</td>
<td align="right">26.9%</td>
<td align="right">27.0%</td>
<td align="right">19.3%</td>
<td align="right">19.2%</td>
<td align="right">412</td>
</tr>
<tr>
<td align="left">120</td>
<td align="left">🟢 Supporter</td>
<td align="right"><b>1508</b></td>
<td align="right">30.3%</td>
<td align="right">53.1%</td>
<td align="right">37.5%</td>
<td align="right">25.0%</td>
<td align="right">25.0%</td>
<td align="right">23.2%</td>
<td align="right">465</td>
</tr>
<tr>
<td align="left">121</td>
<td align="left">🟢 Liquidator</td>
<td align="right"><b>1508</b></td>
<td align="right">28.3%</td>
<td align="right">60.5%</td>
<td align="right">32.8%</td>
<td align="right">31.8%</td>
<td align="right">21.4%</td>
<td align="right">19.7%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">122</td>
<td align="left">🟢 Unmaker</td>
<td align="right"><b>1508</b></td>
<td align="right">28.3%</td>
<td align="right">52.3%</td>
<td align="right">36.4%</td>
<td align="right">29.4%</td>
<td align="right">22.6%</td>
<td align="right">18.8%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">123</td>
<td align="left">🟢 Assessor</td>
<td align="right"><b>1508</b></td>
<td align="right">25.9%</td>
<td align="right">41.5%</td>
<td align="right">32.3%</td>
<td align="right">25.3%</td>
<td align="right">23.7%</td>
<td align="right">20.8%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">124</td>
<td align="left">🟢 Juggernaut</td>
<td align="right"><b>1508</b></td>
<td align="right">27.3%</td>
<td align="right">57.9%</td>
<td align="right">46.8%</td>
<td align="right">27.1%</td>
<td align="right">18.8%</td>
<td align="right">15.7%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">125</td>
<td align="left">🟢 Mystic</td>
<td align="right"><b>1508</b></td>
<td align="right">29.4%</td>
<td align="right">55.1%</td>
<td align="right">33.8%</td>
<td align="right">29.2%</td>
<td align="right">24.8%</td>
<td align="right">21.3%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">126</td>
<td align="left">🟢 Princess</td>
<td align="right"><b>1508</b></td>
<td align="right">26.7%</td>
<td align="right">48.8%</td>
<td align="right">40.7%</td>
<td align="right">23.2%</td>
<td align="right">19.5%</td>
<td align="right">20.3%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">127</td>
<td align="left">🟢 Deity</td>
<td align="right"><b>1508</b></td>
<td align="right">27.0%</td>
<td align="right">53.8%</td>
<td align="right">37.7%</td>
<td align="right">24.7%</td>
<td align="right">24.3%</td>
<td align="right">15.6%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">128</td>
<td align="left">🟢 Fusion</td>
<td align="right"><b>1508</b></td>
<td align="right">27.8%</td>
<td align="right">47.4%</td>
<td align="right">25.4%</td>
<td align="right">31.9%</td>
<td align="right">25.9%</td>
<td align="right">18.9%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">129</td>
<td align="left">🟢 Trust</td>
<td align="right"><b>1508</b></td>
<td align="right">28.0%</td>
<td align="right">60.4%</td>
<td align="right">34.8%</td>
<td align="right">28.3%</td>
<td align="right">22.2%</td>
<td align="right">14.9%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">130</td>
<td align="left">🟢 Illusory</td>
<td align="right"><b>1508</b></td>
<td align="right">28.4%</td>
<td align="right">57.1%</td>
<td align="right">34.4%</td>
<td align="right">28.6%</td>
<td align="right">27.7%</td>
<td align="right">17.7%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">131</td>
<td align="left">🟢 YinYang</td>
<td align="right"><b>1508</b></td>
<td align="right">27.9%</td>
<td align="right">43.9%</td>
<td align="right">43.1%</td>
<td align="right">28.7%</td>
<td align="right">18.0%</td>
<td align="right">19.0%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">132</td>
<td align="left">🟢 Grumpus_Alt</td>
<td align="right"><b>1508</b></td>
<td align="right">28.9%</td>
<td align="right">61.4%</td>
<td align="right">34.3%</td>
<td align="right">21.1%</td>
<td align="right">25.9%</td>
<td align="right">21.4%</td>
<td align="right">412</td>
</tr>
<tr>
<td align="left">133</td>
<td align="left">🟢 Conqueror_Alt</td>
<td align="right"><b>1508</b></td>
<td align="right">28.2%</td>
<td align="right">59.5%</td>
<td align="right">38.5%</td>
<td align="right">20.0%</td>
<td align="right">28.7%</td>
<td align="right">20.7%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">134</td>
<td align="left">🟢 Generator</td>
<td align="right"><b>1508</b></td>
<td align="right">27.7%</td>
<td align="right">56.7%</td>
<td align="right">39.7%</td>
<td align="right">30.4%</td>
<td align="right">22.8%</td>
<td align="right">17.5%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">135</td>
<td align="left">🟢 Spark</td>
<td align="right"><b>1507</b></td>
<td align="right">26.0%</td>
<td align="right">67.4%</td>
<td align="right">28.6%</td>
<td align="right">19.1%</td>
<td align="right">21.9%</td>
<td align="right">18.1%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">136</td>
<td align="left">🟢 Folder</td>
<td align="right"><b>1507</b></td>
<td align="right">26.9%</td>
<td align="right">42.0%</td>
<td align="right">30.1%</td>
<td align="right">26.8%</td>
<td align="right">24.2%</td>
<td align="right">21.7%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">137</td>
<td align="left">🟢 Pacifier</td>
<td align="right"><b>1507</b></td>
<td align="right">28.8%</td>
<td align="right">52.5%</td>
<td align="right">43.3%</td>
<td align="right">24.4%</td>
<td align="right">23.9%</td>
<td align="right">20.7%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">138</td>
<td align="left">🟢 Rebel</td>
<td align="right"><b>1507</b></td>
<td align="right">26.0%</td>
<td align="right">55.4%</td>
<td align="right">38.1%</td>
<td align="right">19.7%</td>
<td align="right">17.4%</td>
<td align="right">19.2%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">139</td>
<td align="left">🟢 Anxiety</td>
<td align="right"><b>1507</b></td>
<td align="right">26.9%</td>
<td align="right">55.6%</td>
<td align="right">34.9%</td>
<td align="right">26.4%</td>
<td align="right">24.8%</td>
<td align="right">14.7%</td>
<td align="right">472</td>
</tr>
<tr>
<td align="left">140</td>
<td align="left">🟢 Snare</td>
<td align="right"><b>1507</b></td>
<td align="right">27.5%</td>
<td align="right">44.9%</td>
<td align="right">41.7%</td>
<td align="right">34.1%</td>
<td align="right">14.4%</td>
<td align="right">20.3%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">141</td>
<td align="left">🟢 DarkEnergy</td>
<td align="right"><b>1507</b></td>
<td align="right">28.6%</td>
<td align="right">62.5%</td>
<td align="right">38.1%</td>
<td align="right">29.3%</td>
<td align="right">21.2%</td>
<td align="right">19.2%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">142</td>
<td align="left">🟢 Cyclops</td>
<td align="right"><b>1507</b></td>
<td align="right">28.3%</td>
<td align="right">55.8%</td>
<td align="right">41.7%</td>
<td align="right">21.4%</td>
<td align="right">23.6%</td>
<td align="right">18.7%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">143</td>
<td align="left">🟢 Schemer</td>
<td align="right"><b>1507</b></td>
<td align="right">27.3%</td>
<td align="right">48.8%</td>
<td align="right">35.4%</td>
<td align="right">25.6%</td>
<td align="right">25.2%</td>
<td align="right">19.0%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">144</td>
<td align="left">🟢 Tomorrow</td>
<td align="right"><b>1507</b></td>
<td align="right">26.9%</td>
<td align="right">52.8%</td>
<td align="right">30.6%</td>
<td align="right">32.5%</td>
<td align="right">18.6%</td>
<td align="right">21.1%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">145</td>
<td align="left">🟢 Warhawk</td>
<td align="right"><b>1507</b></td>
<td align="right">26.6%</td>
<td align="right">53.5%</td>
<td align="right">37.9%</td>
<td align="right">26.1%</td>
<td align="right">22.7%</td>
<td align="right">15.9%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">146</td>
<td align="left">🟢 Hunter</td>
<td align="right"><b>1507</b></td>
<td align="right">27.1%</td>
<td align="right">47.4%</td>
<td align="right">33.8%</td>
<td align="right">27.7%</td>
<td align="right">22.9%</td>
<td align="right">19.3%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">147</td>
<td align="left">🟢 Impostor</td>
<td align="right"><b>1507</b></td>
<td align="right">27.2%</td>
<td align="right">45.0%</td>
<td align="right">38.5%</td>
<td align="right">27.3%</td>
<td align="right">25.0%</td>
<td align="right">18.9%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">148</td>
<td align="left">🟢 Homesteader</td>
<td align="right"><b>1507</b></td>
<td align="right">26.7%</td>
<td align="right">48.7%</td>
<td align="right">33.3%</td>
<td align="right">28.4%</td>
<td align="right">19.5%</td>
<td align="right">21.6%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">149</td>
<td align="left">🟢 Anchor</td>
<td align="right"><b>1507</b></td>
<td align="right">25.6%</td>
<td align="right">43.8%</td>
<td align="right">31.5%</td>
<td align="right">22.7%</td>
<td align="right">22.3%</td>
<td align="right">19.1%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">150</td>
<td align="left">🟢 Friend</td>
<td align="right"><b>1507</b></td>
<td align="right">27.5%</td>
<td align="right">57.4%</td>
<td align="right">42.5%</td>
<td align="right">30.1%</td>
<td align="right">13.2%</td>
<td align="right">16.9%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">151</td>
<td align="left">🟢 Rook</td>
<td align="right"><b>1507</b></td>
<td align="right">35.3%</td>
<td align="right">66.7%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">23.1%</td>
<td align="right">32.0%</td>
<td align="right">68</td>
</tr>
<tr>
<td align="left">152</td>
<td align="left">🟢 Boson</td>
<td align="right"><b>1507</b></td>
<td align="right">27.7%</td>
<td align="right">40.0%</td>
<td align="right">39.4%</td>
<td align="right">23.0%</td>
<td align="right">22.8%</td>
<td align="right">25.5%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">153</td>
<td align="left">🟢 Marine</td>
<td align="right"><b>1507</b></td>
<td align="right">30.0%</td>
<td align="right">60.0%</td>
<td align="right">33.3%</td>
<td align="right">31.2%</td>
<td align="right">22.3%</td>
<td align="right">23.0%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">154</td>
<td align="left">🟢 Void_Horror</td>
<td align="right"><b>1507</b></td>
<td align="right">28.0%</td>
<td align="right">53.3%</td>
<td align="right">37.5%</td>
<td align="right">26.9%</td>
<td align="right">17.0%</td>
<td align="right">20.0%</td>
<td align="right">250</td>
</tr>
<tr>
<td align="left">155</td>
<td align="left">🟢 Outpost</td>
<td align="right"><b>1507</b></td>
<td align="right">27.9%</td>
<td align="right">57.7%</td>
<td align="right">41.3%</td>
<td align="right">22.6%</td>
<td align="right">23.9%</td>
<td align="right">16.2%</td>
<td align="right">469</td>
</tr>
<tr>
<td align="left">156</td>
<td align="left">🟢 Sting</td>
<td align="right"><b>1507</b></td>
<td align="right">26.6%</td>
<td align="right">50.8%</td>
<td align="right">40.9%</td>
<td align="right">31.6%</td>
<td align="right">14.9%</td>
<td align="right">12.5%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">157</td>
<td align="left">🟢 Resonator</td>
<td align="right"><b>1507</b></td>
<td align="right">27.1%</td>
<td align="right">59.1%</td>
<td align="right">25.8%</td>
<td align="right">26.5%</td>
<td align="right">26.6%</td>
<td align="right">16.9%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">158</td>
<td align="left">🟢 Zenith</td>
<td align="right"><b>1507</b></td>
<td align="right">28.4%</td>
<td align="right">53.2%</td>
<td align="right">33.8%</td>
<td align="right">28.1%</td>
<td align="right">25.9%</td>
<td align="right">18.9%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">159</td>
<td align="left">🟢 Risk</td>
<td align="right"><b>1507</b></td>
<td align="right">26.2%</td>
<td align="right">43.8%</td>
<td align="right">42.1%</td>
<td align="right">34.9%</td>
<td align="right">19.5%</td>
<td align="right">13.5%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">160</td>
<td align="left">🟢 Forge</td>
<td align="right"><b>1507</b></td>
<td align="right">26.4%</td>
<td align="right">63.3%</td>
<td align="right">41.1%</td>
<td align="right">28.9%</td>
<td align="right">17.5%</td>
<td align="right">17.4%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">161</td>
<td align="left">🟢 Nova</td>
<td align="right"><b>1507</b></td>
<td align="right">28.1%</td>
<td align="right">66.0%</td>
<td align="right">39.4%</td>
<td align="right">24.5%</td>
<td align="right">25.0%</td>
<td align="right">14.4%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">162</td>
<td align="left">🟢 Queller</td>
<td align="right"><b>1507</b></td>
<td align="right">26.3%</td>
<td align="right">51.1%</td>
<td align="right">29.4%</td>
<td align="right">33.3%</td>
<td align="right">19.1%</td>
<td align="right">17.0%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">163</td>
<td align="left">🟢 Phaser</td>
<td align="right"><b>1507</b></td>
<td align="right">27.5%</td>
<td align="right">52.1%</td>
<td align="right">44.3%</td>
<td align="right">28.2%</td>
<td align="right">17.9%</td>
<td align="right">17.7%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">164</td>
<td align="left">🟢 Clouder</td>
<td align="right"><b>1507</b></td>
<td align="right">26.5%</td>
<td align="right">51.9%</td>
<td align="right">34.0%</td>
<td align="right">22.5%</td>
<td align="right">21.7%</td>
<td align="right">19.5%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">165</td>
<td align="left">🟢 Nibbler</td>
<td align="right"><b>1507</b></td>
<td align="right">28.7%</td>
<td align="right">43.2%</td>
<td align="right">35.1%</td>
<td align="right">34.3%</td>
<td align="right">25.0%</td>
<td align="right">18.7%</td>
<td align="right">244</td>
</tr>
<tr>
<td align="left">166</td>
<td align="left">🟢 Animal</td>
<td align="right"><b>1507</b></td>
<td align="right">28.1%</td>
<td align="right">50.0%</td>
<td align="right">34.7%</td>
<td align="right">33.8%</td>
<td align="right">22.6%</td>
<td align="right">20.1%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">167</td>
<td align="left">🟢 Nurturer</td>
<td align="right"><b>1507</b></td>
<td align="right">26.7%</td>
<td align="right">64.7%</td>
<td align="right">25.0%</td>
<td align="right">22.6%</td>
<td align="right">20.2%</td>
<td align="right">20.8%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">168</td>
<td align="left">🟢 Cricket</td>
<td align="right"><b>1507</b></td>
<td align="right">34.6%</td>
<td align="right">25.0%</td>
<td align="right">40.0%</td>
<td align="right">25.0%</td>
<td align="right">40.9%</td>
<td align="right">38.9%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">169</td>
<td align="left">🟢 Curator</td>
<td align="right"><b>1507</b></td>
<td align="right">26.2%</td>
<td align="right">41.7%</td>
<td align="right">30.5%</td>
<td align="right">34.1%</td>
<td align="right">17.8%</td>
<td align="right">19.1%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">170</td>
<td align="left">🟢 Shadow_Alt</td>
<td align="right"><b>1507</b></td>
<td align="right">28.2%</td>
<td align="right">51.7%</td>
<td align="right">39.6%</td>
<td align="right">24.7%</td>
<td align="right">29.2%</td>
<td align="right">18.6%</td>
<td align="right">394</td>
</tr>
<tr>
<td align="left">171</td>
<td align="left">🟢 Finale</td>
<td align="right"><b>1507</b></td>
<td align="right">26.0%</td>
<td align="right">42.9%</td>
<td align="right">40.0%</td>
<td align="right">21.6%</td>
<td align="right">24.8%</td>
<td align="right">18.3%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">172</td>
<td align="left">🟢 Prism</td>
<td align="right"><b>1507</b></td>
<td align="right">26.5%</td>
<td align="right">38.8%</td>
<td align="right">43.3%</td>
<td align="right">29.7%</td>
<td align="right">24.8%</td>
<td align="right">14.3%</td>
<td align="right">475</td>
</tr>
<tr>
<td align="left">173</td>
<td align="left">🟢 Cyclone</td>
<td align="right"><b>1507</b></td>
<td align="right">27.7%</td>
<td align="right">56.0%</td>
<td align="right">33.8%</td>
<td align="right">28.6%</td>
<td align="right">26.2%</td>
<td align="right">15.1%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">174</td>
<td align="left">🟢 Slowdown</td>
<td align="right"><b>1507</b></td>
<td align="right">27.1%</td>
<td align="right">40.0%</td>
<td align="right">41.7%</td>
<td align="right">25.3%</td>
<td align="right">22.4%</td>
<td align="right">19.9%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">175</td>
<td align="left">🟢 Whirligig</td>
<td align="right"><b>1506</b></td>
<td align="right">26.3%</td>
<td align="right">50.0%</td>
<td align="right">30.4%</td>
<td align="right">27.5%</td>
<td align="right">25.2%</td>
<td align="right">18.7%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">176</td>
<td align="left">🟢 Resistor</td>
<td align="right"><b>1506</b></td>
<td align="right">27.2%</td>
<td align="right">51.2%</td>
<td align="right">35.7%</td>
<td align="right">24.5%</td>
<td align="right">18.6%</td>
<td align="right">24.8%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">177</td>
<td align="left">🟢 Runner</td>
<td align="right"><b>1506</b></td>
<td align="right">27.3%</td>
<td align="right">55.8%</td>
<td align="right">37.3%</td>
<td align="right">23.7%</td>
<td align="right">21.6%</td>
<td align="right">17.7%</td>
<td align="right">406</td>
</tr>
<tr>
<td align="left">178</td>
<td align="left">🟢 Aura</td>
<td align="right"><b>1506</b></td>
<td align="right">28.8%</td>
<td align="right">47.2%</td>
<td align="right">50.0%</td>
<td align="right">28.1%</td>
<td align="right">28.0%</td>
<td align="right">17.3%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">179</td>
<td align="left">🟢 Wealthy</td>
<td align="right"><b>1506</b></td>
<td align="right">26.6%</td>
<td align="right">46.8%</td>
<td align="right">40.8%</td>
<td align="right">27.1%</td>
<td align="right">20.6%</td>
<td align="right">15.4%</td>
<td align="right">462</td>
</tr>
<tr>
<td align="left">180</td>
<td align="left">🟢 Elemental</td>
<td align="right"><b>1506</b></td>
<td align="right">29.5%</td>
<td align="right">55.1%</td>
<td align="right">34.3%</td>
<td align="right">29.8%</td>
<td align="right">24.5%</td>
<td align="right">20.7%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">181</td>
<td align="left">🟢 Basilisk</td>
<td align="right"><b>1506</b></td>
<td align="right">27.5%</td>
<td align="right">55.6%</td>
<td align="right">33.3%</td>
<td align="right">22.9%</td>
<td align="right">24.6%</td>
<td align="right">20.5%</td>
<td align="right">466</td>
</tr>
<tr>
<td align="left">182</td>
<td align="left">🟢 Mist_Alt2</td>
<td align="right"><b>1506</b></td>
<td align="right">34.2%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">47.1%</td>
<td align="right">35.3%</td>
<td align="right">15.8%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">183</td>
<td align="left">🟢 Blessed</td>
<td align="right"><b>1506</b></td>
<td align="right">29.3%</td>
<td align="right">60.0%</td>
<td align="right">33.3%</td>
<td align="right">36.6%</td>
<td align="right">21.3%</td>
<td align="right">21.0%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">184</td>
<td align="left">🟢 Processor</td>
<td align="right"><b>1506</b></td>
<td align="right">27.3%</td>
<td align="right">53.1%</td>
<td align="right">41.3%</td>
<td align="right">25.0%</td>
<td align="right">17.9%</td>
<td align="right">19.8%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">185</td>
<td align="left">🟢 Diamond</td>
<td align="right"><b>1506</b></td>
<td align="right">23.5%</td>
<td align="right">45.7%</td>
<td align="right">36.0%</td>
<td align="right">30.6%</td>
<td align="right">12.4%</td>
<td align="right">15.4%</td>
<td align="right">417</td>
</tr>
<tr>
<td align="left">186</td>
<td align="left">🟢 Virus_Alt</td>
<td align="right"><b>1506</b></td>
<td align="right">28.0%</td>
<td align="right">63.3%</td>
<td align="right">32.1%</td>
<td align="right">23.0%</td>
<td align="right">22.3%</td>
<td align="right">20.0%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">187</td>
<td align="left">🟢 Engineer_Alt</td>
<td align="right"><b>1506</b></td>
<td align="right">27.4%</td>
<td align="right">52.6%</td>
<td align="right">26.2%</td>
<td align="right">32.5%</td>
<td align="right">21.9%</td>
<td align="right">18.2%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">188</td>
<td align="left">🟢 Rewinder</td>
<td align="right"><b>1506</b></td>
<td align="right">26.1%</td>
<td align="right">42.1%</td>
<td align="right">39.7%</td>
<td align="right">26.7%</td>
<td align="right">18.9%</td>
<td align="right">20.4%</td>
<td align="right">476</td>
</tr>
<tr>
<td align="left">189</td>
<td align="left">🟢 Pride</td>
<td align="right"><b>1506</b></td>
<td align="right">28.0%</td>
<td align="right">68.6%</td>
<td align="right">32.8%</td>
<td align="right">31.2%</td>
<td align="right">21.7%</td>
<td align="right">18.0%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">190</td>
<td align="left">🟢 Ambassador</td>
<td align="right"><b>1506</b></td>
<td align="right">25.9%</td>
<td align="right">53.2%</td>
<td align="right">34.6%</td>
<td align="right">23.5%</td>
<td align="right">24.0%</td>
<td align="right">14.4%</td>
<td align="right">394</td>
</tr>
<tr>
<td align="left">191</td>
<td align="left">🟢 Broker</td>
<td align="right"><b>1506</b></td>
<td align="right">27.3%</td>
<td align="right">51.5%</td>
<td align="right">40.3%</td>
<td align="right">28.4%</td>
<td align="right">15.7%</td>
<td align="right">23.0%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">192</td>
<td align="left">🟢 Volcano</td>
<td align="right"><b>1506</b></td>
<td align="right">28.2%</td>
<td align="right">57.1%</td>
<td align="right">33.8%</td>
<td align="right">26.0%</td>
<td align="right">23.2%</td>
<td align="right">19.9%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">193</td>
<td align="left">🟢 Screamer</td>
<td align="right"><b>1506</b></td>
<td align="right">33.8%</td>
<td align="right">75.0%</td>
<td align="right">46.2%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">23.1%</td>
<td align="right">68</td>
</tr>
<tr>
<td align="left">194</td>
<td align="left">🟢 Blackhole</td>
<td align="right"><b>1506</b></td>
<td align="right">27.7%</td>
<td align="right">54.1%</td>
<td align="right">30.0%</td>
<td align="right">33.0%</td>
<td align="right">16.3%</td>
<td align="right">18.6%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">195</td>
<td align="left">🟢 Reconstructor</td>
<td align="right"><b>1506</b></td>
<td align="right">27.3%</td>
<td align="right">46.7%</td>
<td align="right">35.9%</td>
<td align="right">29.3%</td>
<td align="right">18.3%</td>
<td align="right">21.8%</td>
<td align="right">466</td>
</tr>
<tr>
<td align="left">196</td>
<td align="left">🟢 Monopolist</td>
<td align="right"><b>1506</b></td>
<td align="right">27.1%</td>
<td align="right">62.8%</td>
<td align="right">28.4%</td>
<td align="right">33.0%</td>
<td align="right">23.9%</td>
<td align="right">11.8%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">197</td>
<td align="left">🟢 Star</td>
<td align="right"><b>1506</b></td>
<td align="right">28.5%</td>
<td align="right">57.1%</td>
<td align="right">40.4%</td>
<td align="right">33.3%</td>
<td align="right">23.0%</td>
<td align="right">16.9%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">198</td>
<td align="left">🟢 Psychologist</td>
<td align="right"><b>1506</b></td>
<td align="right">33.7%</td>
<td align="right">56.2%</td>
<td align="right">50.0%</td>
<td align="right">22.7%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">83</td>
</tr>
<tr>
<td align="left">199</td>
<td align="left">🟢 Bee</td>
<td align="right"><b>1506</b></td>
<td align="right">33.7%</td>
<td align="right">43.8%</td>
<td align="right">58.3%</td>
<td align="right">33.3%</td>
<td align="right">8.3%</td>
<td align="right">28.0%</td>
<td align="right">86</td>
</tr>
<tr>
<td align="left">200</td>
<td align="left">🟢 Hide</td>
<td align="right"><b>1506</b></td>
<td align="right">26.8%</td>
<td align="right">47.2%</td>
<td align="right">39.1%</td>
<td align="right">28.4%</td>
<td align="right">16.3%</td>
<td align="right">21.8%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">201</td>
<td align="left">🟢 Gluon</td>
<td align="right"><b>1506</b></td>
<td align="right">24.8%</td>
<td align="right">41.7%</td>
<td align="right">38.5%</td>
<td align="right">28.0%</td>
<td align="right">19.8%</td>
<td align="right">16.3%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">202</td>
<td align="left">🟢 Cheater_Alt</td>
<td align="right"><b>1506</b></td>
<td align="right">26.7%</td>
<td align="right">46.2%</td>
<td align="right">41.9%</td>
<td align="right">26.6%</td>
<td align="right">23.7%</td>
<td align="right">16.5%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">203</td>
<td align="left">🟢 Radar</td>
<td align="right"><b>1506</b></td>
<td align="right">26.4%</td>
<td align="right">50.0%</td>
<td align="right">28.4%</td>
<td align="right">26.5%</td>
<td align="right">18.6%</td>
<td align="right">22.7%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">204</td>
<td align="left">🟢 Owl</td>
<td align="right"><b>1506</b></td>
<td align="right">26.2%</td>
<td align="right">51.0%</td>
<td align="right">30.4%</td>
<td align="right">19.3%</td>
<td align="right">23.7%</td>
<td align="right">21.1%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">205</td>
<td align="left">🟢 Keeper</td>
<td align="right"><b>1506</b></td>
<td align="right">26.5%</td>
<td align="right">45.9%</td>
<td align="right">45.3%</td>
<td align="right">27.7%</td>
<td align="right">17.5%</td>
<td align="right">21.2%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">206</td>
<td align="left">🟢 Vibrator</td>
<td align="right"><b>1506</b></td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">27.3%</td>
<td align="right">31.2%</td>
<td align="right">21.7%</td>
<td align="right">50.0%</td>
<td align="right">72</td>
</tr>
<tr>
<td align="left">207</td>
<td align="left">🟢 Eagle</td>
<td align="right"><b>1506</b></td>
<td align="right">26.6%</td>
<td align="right">47.9%</td>
<td align="right">38.9%</td>
<td align="right">20.7%</td>
<td align="right">19.8%</td>
<td align="right">22.2%</td>
<td align="right">463</td>
</tr>
<tr>
<td align="left">208</td>
<td align="left">🟢 Manticore</td>
<td align="right"><b>1506</b></td>
<td align="right">25.4%</td>
<td align="right">53.2%</td>
<td align="right">33.9%</td>
<td align="right">23.9%</td>
<td align="right">18.8%</td>
<td align="right">16.0%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">209</td>
<td align="left">🟢 Insect</td>
<td align="right"><b>1506</b></td>
<td align="right">25.8%</td>
<td align="right">62.8%</td>
<td align="right">37.5%</td>
<td align="right">25.5%</td>
<td align="right">23.2%</td>
<td align="right">18.8%</td>
<td align="right">1812</td>
</tr>
<tr>
<td align="left">210</td>
<td align="left">🟢 Shield_Alt</td>
<td align="right"><b>1506</b></td>
<td align="right">26.8%</td>
<td align="right">55.8%</td>
<td align="right">44.9%</td>
<td align="right">23.3%</td>
<td align="right">20.8%</td>
<td align="right">14.8%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">211</td>
<td align="left">🟢 Ghoul</td>
<td align="right"><b>1506</b></td>
<td align="right">27.8%</td>
<td align="right">66.0%</td>
<td align="right">43.3%</td>
<td align="right">34.5%</td>
<td align="right">23.1%</td>
<td align="right">17.3%</td>
<td align="right">2525</td>
</tr>
<tr>
<td align="left">212</td>
<td align="left">🟢 Quartz</td>
<td align="right"><b>1506</b></td>
<td align="right">27.1%</td>
<td align="right">51.2%</td>
<td align="right">25.7%</td>
<td align="right">24.5%</td>
<td align="right">21.3%</td>
<td align="right">26.2%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">213</td>
<td align="left">🟢 Cyborg</td>
<td align="right"><b>1506</b></td>
<td align="right">27.0%</td>
<td align="right">64.0%</td>
<td align="right">50.7%</td>
<td align="right">25.8%</td>
<td align="right">16.8%</td>
<td align="right">10.3%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">214</td>
<td align="left">🟢 Turquoise</td>
<td align="right"><b>1506</b></td>
<td align="right">27.6%</td>
<td align="right">57.1%</td>
<td align="right">29.6%</td>
<td align="right">30.3%</td>
<td align="right">24.1%</td>
<td align="right">16.8%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">215</td>
<td align="left">🟢 Clock</td>
<td align="right"><b>1506</b></td>
<td align="right">28.2%</td>
<td align="right">41.0%</td>
<td align="right">47.6%</td>
<td align="right">30.7%</td>
<td align="right">23.0%</td>
<td align="right">14.7%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">216</td>
<td align="left">🟢 Ethereal</td>
<td align="right"><b>1506</b></td>
<td align="right">27.9%</td>
<td align="right">50.0%</td>
<td align="right">39.1%</td>
<td align="right">25.8%</td>
<td align="right">19.0%</td>
<td align="right">24.8%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">217</td>
<td align="left">🟢 Rhythm</td>
<td align="right"><b>1506</b></td>
<td align="right">25.6%</td>
<td align="right">47.2%</td>
<td align="right">34.7%</td>
<td align="right">20.7%</td>
<td align="right">22.7%</td>
<td align="right">17.9%</td>
<td align="right">472</td>
</tr>
<tr>
<td align="left">218</td>
<td align="left">🟢 Theorist</td>
<td align="right"><b>1506</b></td>
<td align="right">32.9%</td>
<td align="right">38.5%</td>
<td align="right">54.5%</td>
<td align="right">42.9%</td>
<td align="right">35.3%</td>
<td align="right">14.8%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">219</td>
<td align="left">🟢 Leader</td>
<td align="right"><b>1505</b></td>
<td align="right">26.5%</td>
<td align="right">49.1%</td>
<td align="right">33.8%</td>
<td align="right">26.5%</td>
<td align="right">19.4%</td>
<td align="right">17.7%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">220</td>
<td align="left">🟢 Exchanger</td>
<td align="right"><b>1505</b></td>
<td align="right">27.1%</td>
<td align="right">51.0%</td>
<td align="right">41.0%</td>
<td align="right">22.5%</td>
<td align="right">21.5%</td>
<td align="right">15.9%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">221</td>
<td align="left">🟢 Dolphin</td>
<td align="right"><b>1505</b></td>
<td align="right">26.1%</td>
<td align="right">51.0%</td>
<td align="right">23.3%</td>
<td align="right">29.5%</td>
<td align="right">18.1%</td>
<td align="right">23.1%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">222</td>
<td align="left">🟢 Tank</td>
<td align="right"><b>1505</b></td>
<td align="right">28.5%</td>
<td align="right">44.9%</td>
<td align="right">37.1%</td>
<td align="right">30.9%</td>
<td align="right">25.5%</td>
<td align="right">18.5%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">223</td>
<td align="left">🟢 Regiment</td>
<td align="right"><b>1505</b></td>
<td align="right">26.8%</td>
<td align="right">70.4%</td>
<td align="right">35.4%</td>
<td align="right">28.8%</td>
<td align="right">21.8%</td>
<td align="right">15.9%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">224</td>
<td align="left">🟢 Finder</td>
<td align="right"><b>1505</b></td>
<td align="right">26.8%</td>
<td align="right">48.2%</td>
<td align="right">34.1%</td>
<td align="right">25.9%</td>
<td align="right">22.8%</td>
<td align="right">18.1%</td>
<td align="right">504</td>
</tr>
<tr>
<td align="left">225</td>
<td align="left">🟢 Avalanche</td>
<td align="right"><b>1505</b></td>
<td align="right">27.4%</td>
<td align="right">51.1%</td>
<td align="right">41.0%</td>
<td align="right">25.0%</td>
<td align="right">20.4%</td>
<td align="right">17.8%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">226</td>
<td align="left">🟢 Ninja</td>
<td align="right"><b>1505</b></td>
<td align="right">24.9%</td>
<td align="right">41.7%</td>
<td align="right">30.8%</td>
<td align="right">22.1%</td>
<td align="right">25.6%</td>
<td align="right">18.3%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">227</td>
<td align="left">🟢 Blocker</td>
<td align="right"><b>1505</b></td>
<td align="right">27.3%</td>
<td align="right">66.7%</td>
<td align="right">22.6%</td>
<td align="right">28.2%</td>
<td align="right">15.0%</td>
<td align="right">21.2%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">228</td>
<td align="left">🟢 Steam</td>
<td align="right"><b>1505</b></td>
<td align="right">26.0%</td>
<td align="right">38.7%</td>
<td align="right">36.2%</td>
<td align="right">30.0%</td>
<td align="right">20.0%</td>
<td align="right">20.0%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">229</td>
<td align="left">🟢 Minotaur</td>
<td align="right"><b>1505</b></td>
<td align="right">26.5%</td>
<td align="right">58.3%</td>
<td align="right">42.3%</td>
<td align="right">24.7%</td>
<td align="right">21.8%</td>
<td align="right">14.7%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">230</td>
<td align="left">🟢 Supermassive</td>
<td align="right"><b>1505</b></td>
<td align="right">25.7%</td>
<td align="right">56.8%</td>
<td align="right">38.6%</td>
<td align="right">24.4%</td>
<td align="right">19.0%</td>
<td align="right">17.1%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">231</td>
<td align="left">🟢 Mind</td>
<td align="right"><b>1505</b></td>
<td align="right">25.7%</td>
<td align="right">56.0%</td>
<td align="right">34.8%</td>
<td align="right">19.0%</td>
<td align="right">22.8%</td>
<td align="right">16.5%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">232</td>
<td align="left">🟢 Faction</td>
<td align="right"><b>1505</b></td>
<td align="right">26.2%</td>
<td align="right">51.2%</td>
<td align="right">38.8%</td>
<td align="right">24.7%</td>
<td align="right">19.1%</td>
<td align="right">16.8%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">233</td>
<td align="left">🟢 Wind</td>
<td align="right"><b>1505</b></td>
<td align="right">26.0%</td>
<td align="right">50.0%</td>
<td align="right">35.6%</td>
<td align="right">31.2%</td>
<td align="right">18.1%</td>
<td align="right">16.3%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">234</td>
<td align="left">🟢 Turret</td>
<td align="right"><b>1505</b></td>
<td align="right">26.5%</td>
<td align="right">48.8%</td>
<td align="right">33.8%</td>
<td align="right">26.9%</td>
<td align="right">19.2%</td>
<td align="right">22.6%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">235</td>
<td align="left">🟢 Hasty</td>
<td align="right"><b>1505</b></td>
<td align="right">25.8%</td>
<td align="right">60.0%</td>
<td align="right">26.4%</td>
<td align="right">25.3%</td>
<td align="right">21.2%</td>
<td align="right">19.1%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">236</td>
<td align="left">🟢 Ancestor</td>
<td align="right"><b>1505</b></td>
<td align="right">26.2%</td>
<td align="right">40.7%</td>
<td align="right">35.6%</td>
<td align="right">30.4%</td>
<td align="right">16.8%</td>
<td align="right">24.1%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">237</td>
<td align="left">🟢 Celestial</td>
<td align="right"><b>1505</b></td>
<td align="right">26.2%</td>
<td align="right">53.1%</td>
<td align="right">27.3%</td>
<td align="right">30.9%</td>
<td align="right">24.3%</td>
<td align="right">14.8%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">238</td>
<td align="left">🟢 Bronze</td>
<td align="right"><b>1505</b></td>
<td align="right">32.4%</td>
<td align="right">60.0%</td>
<td align="right">50.0%</td>
<td align="right">35.3%</td>
<td align="right">22.2%</td>
<td align="right">21.4%</td>
<td align="right">71</td>
</tr>
<tr>
<td align="left">239</td>
<td align="left">🟢 Conductor_Alt</td>
<td align="right"><b>1505</b></td>
<td align="right">27.4%</td>
<td align="right">54.3%</td>
<td align="right">25.4%</td>
<td align="right">26.6%</td>
<td align="right">25.5%</td>
<td align="right">20.5%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">240</td>
<td align="left">🟢 Infinite</td>
<td align="right"><b>1505</b></td>
<td align="right">26.2%</td>
<td align="right">50.9%</td>
<td align="right">32.2%</td>
<td align="right">35.2%</td>
<td align="right">13.4%</td>
<td align="right">16.3%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">241</td>
<td align="left">🟢 Seahorse</td>
<td align="right"><b>1505</b></td>
<td align="right">27.3%</td>
<td align="right">55.6%</td>
<td align="right">41.1%</td>
<td align="right">31.2%</td>
<td align="right">16.7%</td>
<td align="right">18.6%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">242</td>
<td align="left">🟢 Herald_Alt</td>
<td align="right"><b>1505</b></td>
<td align="right">25.5%</td>
<td align="right">60.0%</td>
<td align="right">36.5%</td>
<td align="right">22.7%</td>
<td align="right">16.3%</td>
<td align="right">15.4%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">243</td>
<td align="left">🟢 Fairy</td>
<td align="right"><b>1505</b></td>
<td align="right">28.4%</td>
<td align="right">66.7%</td>
<td align="right">51.5%</td>
<td align="right">31.3%</td>
<td align="right">18.0%</td>
<td align="right">11.3%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">244</td>
<td align="left">🟢 Engineer</td>
<td align="right"><b>1505</b></td>
<td align="right">25.6%</td>
<td align="right">57.1%</td>
<td align="right">34.1%</td>
<td align="right">25.1%</td>
<td align="right">25.9%</td>
<td align="right">19.2%</td>
<td align="right">1887</td>
</tr>
<tr>
<td align="left">245</td>
<td align="left">🟢 Immortal</td>
<td align="right"><b>1505</b></td>
<td align="right">26.5%</td>
<td align="right">43.9%</td>
<td align="right">29.0%</td>
<td align="right">30.1%</td>
<td align="right">22.8%</td>
<td align="right">19.8%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">246</td>
<td align="left">🟢 Lancer</td>
<td align="right"><b>1505</b></td>
<td align="right">28.4%</td>
<td align="right">53.7%</td>
<td align="right">37.0%</td>
<td align="right">26.6%</td>
<td align="right">24.5%</td>
<td align="right">19.8%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">247</td>
<td align="left">🟢 Decayer</td>
<td align="right"><b>1505</b></td>
<td align="right">26.2%</td>
<td align="right">45.5%</td>
<td align="right">46.7%</td>
<td align="right">21.4%</td>
<td align="right">22.5%</td>
<td align="right">15.4%</td>
<td align="right">473</td>
</tr>
<tr>
<td align="left">248</td>
<td align="left">🟢 Artillery</td>
<td align="right"><b>1505</b></td>
<td align="right">26.4%</td>
<td align="right">47.8%</td>
<td align="right">37.7%</td>
<td align="right">27.0%</td>
<td align="right">21.0%</td>
<td align="right">16.3%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">249</td>
<td align="left">🟢 Immunizer</td>
<td align="right"><b>1505</b></td>
<td align="right">28.4%</td>
<td align="right">54.5%</td>
<td align="right">33.3%</td>
<td align="right">32.5%</td>
<td align="right">20.9%</td>
<td align="right">20.3%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">250</td>
<td align="left">🟢 Weightless</td>
<td align="right"><b>1505</b></td>
<td align="right">32.1%</td>
<td align="right">42.9%</td>
<td align="right">23.1%</td>
<td align="right">50.0%</td>
<td align="right">35.7%</td>
<td align="right">20.0%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">251</td>
<td align="left">🟢 Spy_Alt</td>
<td align="right"><b>1505</b></td>
<td align="right">24.3%</td>
<td align="right">54.5%</td>
<td align="right">31.6%</td>
<td align="right">19.8%</td>
<td align="right">21.1%</td>
<td align="right">14.5%</td>
<td align="right">387</td>
</tr>
<tr>
<td align="left">252</td>
<td align="left">🟢 King</td>
<td align="right"><b>1505</b></td>
<td align="right">26.0%</td>
<td align="right">46.7%</td>
<td align="right">34.8%</td>
<td align="right">22.5%</td>
<td align="right">22.5%</td>
<td align="right">18.3%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">253</td>
<td align="left">🟢 Assistant</td>
<td align="right"><b>1505</b></td>
<td align="right">25.1%</td>
<td align="right">44.6%</td>
<td align="right">25.8%</td>
<td align="right">26.3%</td>
<td align="right">21.8%</td>
<td align="right">18.3%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">254</td>
<td align="left">🟢 Lurker</td>
<td align="right"><b>1505</b></td>
<td align="right">24.8%</td>
<td align="right">46.3%</td>
<td align="right">32.3%</td>
<td align="right">25.9%</td>
<td align="right">23.3%</td>
<td align="right">15.7%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">255</td>
<td align="left">🟢 Claimer</td>
<td align="right"><b>1505</b></td>
<td align="right">26.8%</td>
<td align="right">55.3%</td>
<td align="right">40.9%</td>
<td align="right">20.0%</td>
<td align="right">27.2%</td>
<td align="right">12.9%</td>
<td align="right">403</td>
</tr>
<tr>
<td align="left">256</td>
<td align="left">🟢 Skeptic</td>
<td align="right"><b>1505</b></td>
<td align="right">25.7%</td>
<td align="right">60.0%</td>
<td align="right">35.5%</td>
<td align="right">22.4%</td>
<td align="right">15.8%</td>
<td align="right">21.1%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">257</td>
<td align="left">🟢 Fermion</td>
<td align="right"><b>1505</b></td>
<td align="right">25.9%</td>
<td align="right">41.9%</td>
<td align="right">38.1%</td>
<td align="right">21.4%</td>
<td align="right">25.7%</td>
<td align="right">16.9%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">258</td>
<td align="left">🟢 Diceroller</td>
<td align="right"><b>1505</b></td>
<td align="right">31.9%</td>
<td align="right">61.5%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">31.2%</td>
<td align="right">13.0%</td>
<td align="right">72</td>
</tr>
<tr>
<td align="left">259</td>
<td align="left">🟢 Thaumaturge</td>
<td align="right"><b>1505</b></td>
<td align="right">27.0%</td>
<td align="right">51.5%</td>
<td align="right">39.7%</td>
<td align="right">28.3%</td>
<td align="right">17.9%</td>
<td align="right">18.8%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">260</td>
<td align="left">🟢 Undertaker</td>
<td align="right"><b>1505</b></td>
<td align="right">25.7%</td>
<td align="right">45.5%</td>
<td align="right">44.3%</td>
<td align="right">20.5%</td>
<td align="right">21.4%</td>
<td align="right">16.6%</td>
<td align="right">487</td>
</tr>
<tr>
<td align="left">261</td>
<td align="left">🟢 Blockade</td>
<td align="right"><b>1505</b></td>
<td align="right">26.2%</td>
<td align="right">47.5%</td>
<td align="right">39.4%</td>
<td align="right">23.7%</td>
<td align="right">17.8%</td>
<td align="right">16.9%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">262</td>
<td align="left">🟢 Telepath</td>
<td align="right"><b>1505</b></td>
<td align="right">25.3%</td>
<td align="right">54.1%</td>
<td align="right">35.6%</td>
<td align="right">19.7%</td>
<td align="right">22.7%</td>
<td align="right">16.3%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">263</td>
<td align="left">🟢 Tornado</td>
<td align="right"><b>1505</b></td>
<td align="right">27.7%</td>
<td align="right">63.4%</td>
<td align="right">33.3%</td>
<td align="right">25.5%</td>
<td align="right">23.3%</td>
<td align="right">19.6%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">264</td>
<td align="left">🟢 Scribe</td>
<td align="right"><b>1505</b></td>
<td align="right">31.8%</td>
<td align="right">60.0%</td>
<td align="right">30.0%</td>
<td align="right">46.7%</td>
<td align="right">10.5%</td>
<td align="right">25.0%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">265</td>
<td align="left">🟢 Formation</td>
<td align="right"><b>1505</b></td>
<td align="right">31.8%</td>
<td align="right">66.7%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">20.0%</td>
<td align="right">22.6%</td>
<td align="right">88</td>
</tr>
<tr>
<td align="left">266</td>
<td align="left">🟢 Vulch</td>
<td align="right"><b>1505</b></td>
<td align="right">27.0%</td>
<td align="right">40.0%</td>
<td align="right">35.7%</td>
<td align="right">36.2%</td>
<td align="right">20.7%</td>
<td align="right">16.9%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">267</td>
<td align="left">🟢 Bully</td>
<td align="right"><b>1505</b></td>
<td align="right">24.7%</td>
<td align="right">50.0%</td>
<td align="right">33.9%</td>
<td align="right">28.3%</td>
<td align="right">18.0%</td>
<td align="right">21.6%</td>
<td align="right">1808</td>
</tr>
<tr>
<td align="left">268</td>
<td align="left">🟢 Pitfall</td>
<td align="right"><b>1505</b></td>
<td align="right">26.0%</td>
<td align="right">50.0%</td>
<td align="right">27.3%</td>
<td align="right">28.6%</td>
<td align="right">22.9%</td>
<td align="right">15.0%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">269</td>
<td align="left">🟢 Geomancer</td>
<td align="right"><b>1505</b></td>
<td align="right">27.2%</td>
<td align="right">59.6%</td>
<td align="right">47.5%</td>
<td align="right">30.3%</td>
<td align="right">12.8%</td>
<td align="right">14.1%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">270</td>
<td align="left">🟢 Pioneer</td>
<td align="right"><b>1505</b></td>
<td align="right">24.5%</td>
<td align="right">42.5%</td>
<td align="right">25.0%</td>
<td align="right">32.6%</td>
<td align="right">18.9%</td>
<td align="right">17.8%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">271</td>
<td align="left">🟢 Liar</td>
<td align="right"><b>1505</b></td>
<td align="right">27.0%</td>
<td align="right">48.8%</td>
<td align="right">40.4%</td>
<td align="right">29.1%</td>
<td align="right">16.0%</td>
<td align="right">22.8%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">272</td>
<td align="left">🟢 Earthquake</td>
<td align="right"><b>1505</b></td>
<td align="right">28.3%</td>
<td align="right">65.0%</td>
<td align="right">30.3%</td>
<td align="right">27.3%</td>
<td align="right">22.5%</td>
<td align="right">21.3%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">273</td>
<td align="left">🟢 Fate</td>
<td align="right"><b>1505</b></td>
<td align="right">27.5%</td>
<td align="right">51.2%</td>
<td align="right">33.3%</td>
<td align="right">26.8%</td>
<td align="right">27.5%</td>
<td align="right">17.3%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">274</td>
<td align="left">🟢 Bluff</td>
<td align="right"><b>1505</b></td>
<td align="right">31.5%</td>
<td align="right">57.1%</td>
<td align="right">62.5%</td>
<td align="right">40.0%</td>
<td align="right">14.3%</td>
<td align="right">17.6%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">275</td>
<td align="left">🟢 Gamer</td>
<td align="right"><b>1505</b></td>
<td align="right">31.4%</td>
<td align="right">62.5%</td>
<td align="right">40.0%</td>
<td align="right">33.3%</td>
<td align="right">27.3%</td>
<td align="right">19.2%</td>
<td align="right">70</td>
</tr>
<tr>
<td align="left">276</td>
<td align="left">🟢 Porcupine</td>
<td align="right"><b>1505</b></td>
<td align="right">25.5%</td>
<td align="right">51.1%</td>
<td align="right">45.1%</td>
<td align="right">26.2%</td>
<td align="right">16.5%</td>
<td align="right">15.9%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">277</td>
<td align="left">🟢 Mapper</td>
<td align="right"><b>1505</b></td>
<td align="right">26.6%</td>
<td align="right">53.5%</td>
<td align="right">29.0%</td>
<td align="right">30.3%</td>
<td align="right">19.2%</td>
<td align="right">21.1%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">278</td>
<td align="left">🟢 Banshee</td>
<td align="right"><b>1505</b></td>
<td align="right">26.3%</td>
<td align="right">59.2%</td>
<td align="right">35.4%</td>
<td align="right">23.8%</td>
<td align="right">23.3%</td>
<td align="right">14.6%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">279</td>
<td align="left">🟢 Sniper</td>
<td align="right"><b>1505</b></td>
<td align="right">27.3%</td>
<td align="right">58.1%</td>
<td align="right">35.5%</td>
<td align="right">25.9%</td>
<td align="right">19.3%</td>
<td align="right">20.6%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">280</td>
<td align="left">🟢 Seer</td>
<td align="right"><b>1504</b></td>
<td align="right">25.1%</td>
<td align="right">46.9%</td>
<td align="right">37.8%</td>
<td align="right">23.7%</td>
<td align="right">15.4%</td>
<td align="right">15.7%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">281</td>
<td align="left">🟢 Feast</td>
<td align="right"><b>1504</b></td>
<td align="right">27.3%</td>
<td align="right">55.3%</td>
<td align="right">36.4%</td>
<td align="right">25.0%</td>
<td align="right">20.3%</td>
<td align="right">18.2%</td>
<td align="right">293</td>
</tr>
<tr>
<td align="left">282</td>
<td align="left">🟢 Vanisher</td>
<td align="right"><b>1504</b></td>
<td align="right">27.2%</td>
<td align="right">45.7%</td>
<td align="right">39.6%</td>
<td align="right">29.6%</td>
<td align="right">21.7%</td>
<td align="right">20.0%</td>
<td align="right">390</td>
</tr>
<tr>
<td align="left">283</td>
<td align="left">🟢 Metamorph</td>
<td align="right"><b>1504</b></td>
<td align="right">26.7%</td>
<td align="right">47.2%</td>
<td align="right">43.4%</td>
<td align="right">34.1%</td>
<td align="right">16.8%</td>
<td align="right">18.4%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">284</td>
<td align="left">🟢 Gambit</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">61.4%</td>
<td align="right">29.0%</td>
<td align="right">32.4%</td>
<td align="right">16.2%</td>
<td align="right">16.2%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">285</td>
<td align="left">🟢 Omnivore</td>
<td align="right"><b>1504</b></td>
<td align="right">27.4%</td>
<td align="right">52.2%</td>
<td align="right">34.0%</td>
<td align="right">41.2%</td>
<td align="right">11.9%</td>
<td align="right">17.6%</td>
<td align="right">248</td>
</tr>
<tr>
<td align="left">286</td>
<td align="left">🟢 Challenger</td>
<td align="right"><b>1504</b></td>
<td align="right">31.3%</td>
<td align="right">44.4%</td>
<td align="right">30.0%</td>
<td align="right">20.0%</td>
<td align="right">38.9%</td>
<td align="right">26.7%</td>
<td align="right">67</td>
</tr>
<tr>
<td align="left">287</td>
<td align="left">🟢 Duelist</td>
<td align="right"><b>1504</b></td>
<td align="right">25.6%</td>
<td align="right">51.0%</td>
<td align="right">34.4%</td>
<td align="right">27.9%</td>
<td align="right">16.8%</td>
<td align="right">16.5%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">288</td>
<td align="left">🟢 Crystal_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">26.6%</td>
<td align="right">38.5%</td>
<td align="right">31.0%</td>
<td align="right">28.6%</td>
<td align="right">24.8%</td>
<td align="right">21.1%</td>
<td align="right">488</td>
</tr>
<tr>
<td align="left">289</td>
<td align="left">🟢 Ant</td>
<td align="right"><b>1504</b></td>
<td align="right">31.3%</td>
<td align="right">20.0%</td>
<td align="right">60.0%</td>
<td align="right">33.3%</td>
<td align="right">24.1%</td>
<td align="right">29.2%</td>
<td align="right">83</td>
</tr>
<tr>
<td align="left">290</td>
<td align="left">🟢 Flood</td>
<td align="right"><b>1504</b></td>
<td align="right">26.4%</td>
<td align="right">40.5%</td>
<td align="right">43.1%</td>
<td align="right">27.2%</td>
<td align="right">23.7%</td>
<td align="right">16.9%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">291</td>
<td align="left">🟢 Crafter</td>
<td align="right"><b>1504</b></td>
<td align="right">25.6%</td>
<td align="right">56.8%</td>
<td align="right">27.9%</td>
<td align="right">17.9%</td>
<td align="right">24.5%</td>
<td align="right">19.4%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">292</td>
<td align="left">🟢 Gambler_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">31.2%</td>
<td align="right">85.7%</td>
<td align="right">28.6%</td>
<td align="right">53.3%</td>
<td align="right">21.4%</td>
<td align="right">13.3%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">293</td>
<td align="left">🟢 Lemming</td>
<td align="right"><b>1504</b></td>
<td align="right">25.9%</td>
<td align="right">52.4%</td>
<td align="right">32.2%</td>
<td align="right">23.9%</td>
<td align="right">23.1%</td>
<td align="right">18.8%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">294</td>
<td align="left">🟢 Doctor_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">25.3%</td>
<td align="right">48.2%</td>
<td align="right">24.6%</td>
<td align="right">27.5%</td>
<td align="right">22.9%</td>
<td align="right">17.8%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">295</td>
<td align="left">🟢 Gravitic</td>
<td align="right"><b>1504</b></td>
<td align="right">31.2%</td>
<td align="right">42.9%</td>
<td align="right">36.4%</td>
<td align="right">30.8%</td>
<td align="right">23.5%</td>
<td align="right">21.4%</td>
<td align="right">93</td>
</tr>
<tr>
<td align="left">296</td>
<td align="left">🟢 Bomber</td>
<td align="right"><b>1504</b></td>
<td align="right">26.3%</td>
<td align="right">61.1%</td>
<td align="right">32.7%</td>
<td align="right">18.0%</td>
<td align="right">23.3%</td>
<td align="right">22.0%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">297</td>
<td align="left">🟢 Overruler</td>
<td align="right"><b>1504</b></td>
<td align="right">25.9%</td>
<td align="right">50.0%</td>
<td align="right">37.7%</td>
<td align="right">33.3%</td>
<td align="right">13.8%</td>
<td align="right">16.1%</td>
<td align="right">483</td>
</tr>
<tr>
<td align="left">298</td>
<td align="left">🟢 Plant</td>
<td align="right"><b>1504</b></td>
<td align="right">26.8%</td>
<td align="right">44.6%</td>
<td align="right">37.7%</td>
<td align="right">30.2%</td>
<td align="right">20.4%</td>
<td align="right">16.7%</td>
<td align="right">478</td>
</tr>
<tr>
<td align="left">299</td>
<td align="left">🟢 Hologram</td>
<td align="right"><b>1504</b></td>
<td align="right">31.1%</td>
<td align="right">40.0%</td>
<td align="right">30.0%</td>
<td align="right">42.9%</td>
<td align="right">29.6%</td>
<td align="right">18.2%</td>
<td align="right">90</td>
</tr>
<tr>
<td align="left">300</td>
<td align="left">🟢 DarkMatter</td>
<td align="right"><b>1504</b></td>
<td align="right">26.0%</td>
<td align="right">57.4%</td>
<td align="right">34.8%</td>
<td align="right">22.2%</td>
<td align="right">20.3%</td>
<td align="right">18.3%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">301</td>
<td align="left">🟢 Venerable</td>
<td align="right"><b>1504</b></td>
<td align="right">26.7%</td>
<td align="right">54.8%</td>
<td align="right">21.9%</td>
<td align="right">25.7%</td>
<td align="right">25.9%</td>
<td align="right">16.5%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">302</td>
<td align="left">🟢 Spellbinder</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">58.5%</td>
<td align="right">44.2%</td>
<td align="right">25.3%</td>
<td align="right">17.4%</td>
<td align="right">16.4%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">303</td>
<td align="left">🟢 Tsar</td>
<td align="right"><b>1504</b></td>
<td align="right">26.4%</td>
<td align="right">48.7%</td>
<td align="right">31.0%</td>
<td align="right">28.6%</td>
<td align="right">23.8%</td>
<td align="right">18.5%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">304</td>
<td align="left">🟢 Trench</td>
<td align="right"><b>1504</b></td>
<td align="right">28.3%</td>
<td align="right">56.4%</td>
<td align="right">36.2%</td>
<td align="right">39.5%</td>
<td align="right">15.9%</td>
<td align="right">18.4%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">305</td>
<td align="left">🟢 Baron</td>
<td align="right"><b>1504</b></td>
<td align="right">27.3%</td>
<td align="right">55.8%</td>
<td align="right">38.5%</td>
<td align="right">25.3%</td>
<td align="right">21.0%</td>
<td align="right">16.9%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">306</td>
<td align="left">🟢 Parallax_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">25.3%</td>
<td align="right">52.0%</td>
<td align="right">29.5%</td>
<td align="right">23.3%</td>
<td align="right">25.7%</td>
<td align="right">15.3%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">307</td>
<td align="left">🟢 Hunger</td>
<td align="right"><b>1504</b></td>
<td align="right">27.2%</td>
<td align="right">55.1%</td>
<td align="right">37.5%</td>
<td align="right">29.1%</td>
<td align="right">19.4%</td>
<td align="right">18.1%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">308</td>
<td align="left">🟢 Zero</td>
<td align="right"><b>1504</b></td>
<td align="right">26.7%</td>
<td align="right">51.1%</td>
<td align="right">24.6%</td>
<td align="right">31.9%</td>
<td align="right">26.1%</td>
<td align="right">17.2%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">309</td>
<td align="left">🟢 Unicorn</td>
<td align="right"><b>1504</b></td>
<td align="right">26.7%</td>
<td align="right">55.6%</td>
<td align="right">31.4%</td>
<td align="right">24.2%</td>
<td align="right">27.8%</td>
<td align="right">14.8%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">310</td>
<td align="left">🟢 Visionary_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">25.9%</td>
<td align="right">46.3%</td>
<td align="right">32.9%</td>
<td align="right">14.4%</td>
<td align="right">26.6%</td>
<td align="right">20.0%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">311</td>
<td align="left">🟢 Puppeteer</td>
<td align="right"><b>1504</b></td>
<td align="right">25.0%</td>
<td align="right">38.3%</td>
<td align="right">20.8%</td>
<td align="right">22.3%</td>
<td align="right">28.3%</td>
<td align="right">21.1%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">312</td>
<td align="left">🟢 Dragonfly</td>
<td align="right"><b>1504</b></td>
<td align="right">30.8%</td>
<td align="right">60.0%</td>
<td align="right">30.0%</td>
<td align="right">30.0%</td>
<td align="right">25.0%</td>
<td align="right">21.7%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">313</td>
<td align="left">🟢 Echo</td>
<td align="right"><b>1504</b></td>
<td align="right">27.1%</td>
<td align="right">46.3%</td>
<td align="right">39.5%</td>
<td align="right">32.6%</td>
<td align="right">24.0%</td>
<td align="right">11.0%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">314</td>
<td align="left">🟢 Legend</td>
<td align="right"><b>1504</b></td>
<td align="right">26.5%</td>
<td align="right">40.9%</td>
<td align="right">29.7%</td>
<td align="right">28.4%</td>
<td align="right">25.2%</td>
<td align="right">20.1%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">315</td>
<td align="left">🟢 Overlord</td>
<td align="right"><b>1504</b></td>
<td align="right">26.6%</td>
<td align="right">37.5%</td>
<td align="right">36.1%</td>
<td align="right">33.3%</td>
<td align="right">21.4%</td>
<td align="right">19.6%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">316</td>
<td align="left">🟢 Sloth</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">52.2%</td>
<td align="right">34.6%</td>
<td align="right">25.6%</td>
<td align="right">21.7%</td>
<td align="right">16.7%</td>
<td align="right">406</td>
</tr>
<tr>
<td align="left">317</td>
<td align="left">🟢 Predator_Food</td>
<td align="right"><b>1504</b></td>
<td align="right">30.3%</td>
<td align="right">53.8%</td>
<td align="right">46.9%</td>
<td align="right">31.9%</td>
<td align="right">18.4%</td>
<td align="right">20.9%</td>
<td align="right">221</td>
</tr>
<tr>
<td align="left">318</td>
<td align="left">🟢 Predator</td>
<td align="right"><b>1504</b></td>
<td align="right">27.1%</td>
<td align="right">61.7%</td>
<td align="right">33.3%</td>
<td align="right">24.4%</td>
<td align="right">26.3%</td>
<td align="right">13.8%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">319</td>
<td align="left">🟢 Teammate</td>
<td align="right"><b>1504</b></td>
<td align="right">27.0%</td>
<td align="right">64.9%</td>
<td align="right">41.3%</td>
<td align="right">23.1%</td>
<td align="right">15.8%</td>
<td align="right">19.2%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">320</td>
<td align="left">🟢 Fortunate</td>
<td align="right"><b>1504</b></td>
<td align="right">25.6%</td>
<td align="right">43.2%</td>
<td align="right">41.7%</td>
<td align="right">18.9%</td>
<td align="right">19.4%</td>
<td align="right">23.5%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">321</td>
<td align="left">🟢 Recruiter</td>
<td align="right"><b>1504</b></td>
<td align="right">26.3%</td>
<td align="right">45.5%</td>
<td align="right">32.9%</td>
<td align="right">25.6%</td>
<td align="right">25.5%</td>
<td align="right">18.4%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">322</td>
<td align="left">🟢 Binder</td>
<td align="right"><b>1504</b></td>
<td align="right">26.6%</td>
<td align="right">38.6%</td>
<td align="right">40.6%</td>
<td align="right">26.7%</td>
<td align="right">21.4%</td>
<td align="right">19.3%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">323</td>
<td align="left">🟢 Steel</td>
<td align="right"><b>1504</b></td>
<td align="right">30.7%</td>
<td align="right">35.7%</td>
<td align="right">30.8%</td>
<td align="right">53.3%</td>
<td align="right">25.0%</td>
<td align="right">14.3%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">324</td>
<td align="left">🟢 Warrior_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">27.8%</td>
<td align="right">64.3%</td>
<td align="right">31.6%</td>
<td align="right">26.2%</td>
<td align="right">24.6%</td>
<td align="right">18.6%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">325</td>
<td align="left">🟢 Leprechaun</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">50.0%</td>
<td align="right">42.6%</td>
<td align="right">24.7%</td>
<td align="right">21.9%</td>
<td align="right">17.0%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">326</td>
<td align="left">🟢 Ambush</td>
<td align="right"><b>1504</b></td>
<td align="right">27.1%</td>
<td align="right">58.1%</td>
<td align="right">30.5%</td>
<td align="right">26.2%</td>
<td align="right">22.9%</td>
<td align="right">18.0%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">327</td>
<td align="left">🟢 Hastur</td>
<td align="right"><b>1504</b></td>
<td align="right">26.9%</td>
<td align="right">37.9%</td>
<td align="right">37.1%</td>
<td align="right">22.5%</td>
<td align="right">24.3%</td>
<td align="right">22.5%</td>
<td align="right">245</td>
</tr>
<tr>
<td align="left">328</td>
<td align="left">🟢 Salvager</td>
<td align="right"><b>1504</b></td>
<td align="right">27.3%</td>
<td align="right">60.0%</td>
<td align="right">43.4%</td>
<td align="right">24.0%</td>
<td align="right">14.1%</td>
<td align="right">21.4%</td>
<td align="right">498</td>
</tr>
<tr>
<td align="left">329</td>
<td align="left">🟢 Garnet</td>
<td align="right"><b>1504</b></td>
<td align="right">25.4%</td>
<td align="right">50.0%</td>
<td align="right">45.3%</td>
<td align="right">22.4%</td>
<td align="right">21.3%</td>
<td align="right">13.1%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">330</td>
<td align="left">🟢 Obstinate</td>
<td align="right"><b>1504</b></td>
<td align="right">24.3%</td>
<td align="right">53.2%</td>
<td align="right">30.8%</td>
<td align="right">23.0%</td>
<td align="right">19.4%</td>
<td align="right">16.7%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">331</td>
<td align="left">🟢 Pollinator</td>
<td align="right"><b>1504</b></td>
<td align="right">25.4%</td>
<td align="right">51.3%</td>
<td align="right">31.0%</td>
<td align="right">26.6%</td>
<td align="right">19.0%</td>
<td align="right">18.7%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">332</td>
<td align="left">🟢 Byakhee</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">50.0%</td>
<td align="right">27.8%</td>
<td align="right">27.7%</td>
<td align="right">18.8%</td>
<td align="right">22.1%</td>
<td align="right">257</td>
</tr>
<tr>
<td align="left">333</td>
<td align="left">🟢 Veto</td>
<td align="right"><b>1504</b></td>
<td align="right">26.6%</td>
<td align="right">36.0%</td>
<td align="right">45.8%</td>
<td align="right">27.8%</td>
<td align="right">16.3%</td>
<td align="right">19.2%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">334</td>
<td align="left">🟢 Jade</td>
<td align="right"><b>1504</b></td>
<td align="right">24.3%</td>
<td align="right">44.7%</td>
<td align="right">43.1%</td>
<td align="right">24.4%</td>
<td align="right">19.4%</td>
<td align="right">12.6%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">335</td>
<td align="left">🟢 Champion_Alt2</td>
<td align="right"><b>1504</b></td>
<td align="right">30.5%</td>
<td align="right">40.0%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">31.6%</td>
<td align="right">11.8%</td>
<td align="right">59</td>
</tr>
<tr>
<td align="left">336</td>
<td align="left">🟢 Marquis</td>
<td align="right"><b>1504</b></td>
<td align="right">26.8%</td>
<td align="right">59.6%</td>
<td align="right">35.4%</td>
<td align="right">27.0%</td>
<td align="right">23.1%</td>
<td align="right">13.0%</td>
<td align="right">463</td>
</tr>
<tr>
<td align="left">337</td>
<td align="left">🟢 Regent</td>
<td align="right"><b>1504</b></td>
<td align="right">25.3%</td>
<td align="right">52.9%</td>
<td align="right">31.7%</td>
<td align="right">32.9%</td>
<td align="right">13.9%</td>
<td align="right">16.7%</td>
<td align="right">474</td>
</tr>
<tr>
<td align="left">338</td>
<td align="left">🟢 Blaster</td>
<td align="right"><b>1504</b></td>
<td align="right">26.0%</td>
<td align="right">58.8%</td>
<td align="right">39.1%</td>
<td align="right">16.9%</td>
<td align="right">20.2%</td>
<td align="right">20.5%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">339</td>
<td align="left">🟢 Gold</td>
<td align="right"><b>1504</b></td>
<td align="right">30.5%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">28.6%</td>
<td align="right">33.3%</td>
<td align="right">22.2%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">340</td>
<td align="left">🟢 Yeti</td>
<td align="right"><b>1504</b></td>
<td align="right">24.3%</td>
<td align="right">45.2%</td>
<td align="right">42.2%</td>
<td align="right">26.0%</td>
<td align="right">16.3%</td>
<td align="right">14.7%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">341</td>
<td align="left">🟢 Nihilist</td>
<td align="right"><b>1504</b></td>
<td align="right">23.9%</td>
<td align="right">53.8%</td>
<td align="right">28.6%</td>
<td align="right">19.5%</td>
<td align="right">18.6%</td>
<td align="right">19.2%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">342</td>
<td align="left">🟢 Wrath</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">48.0%</td>
<td align="right">36.7%</td>
<td align="right">26.3%</td>
<td align="right">22.5%</td>
<td align="right">16.8%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">343</td>
<td align="left">🟢 Heavy</td>
<td align="right"><b>1504</b></td>
<td align="right">30.4%</td>
<td align="right">50.0%</td>
<td align="right">42.9%</td>
<td align="right">27.3%</td>
<td align="right">41.7%</td>
<td align="right">15.0%</td>
<td align="right">56</td>
</tr>
<tr>
<td align="left">344</td>
<td align="left">🟢 Berserker</td>
<td align="right"><b>1504</b></td>
<td align="right">26.0%</td>
<td align="right">55.6%</td>
<td align="right">30.9%</td>
<td align="right">30.1%</td>
<td align="right">16.5%</td>
<td align="right">16.0%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">345</td>
<td align="left">🟢 Handler</td>
<td align="right"><b>1504</b></td>
<td align="right">26.0%</td>
<td align="right">44.7%</td>
<td align="right">40.3%</td>
<td align="right">23.8%</td>
<td align="right">21.3%</td>
<td align="right">17.5%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">346</td>
<td align="left">🟢 Legion</td>
<td align="right"><b>1504</b></td>
<td align="right">27.5%</td>
<td align="right">51.1%</td>
<td align="right">30.6%</td>
<td align="right">30.5%</td>
<td align="right">22.4%</td>
<td align="right">20.0%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">347</td>
<td align="left">🟢 Captain</td>
<td align="right"><b>1504</b></td>
<td align="right">25.5%</td>
<td align="right">42.9%</td>
<td align="right">31.2%</td>
<td align="right">31.9%</td>
<td align="right">20.0%</td>
<td align="right">19.0%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">348</td>
<td align="left">🟢 Demolisher</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">51.2%</td>
<td align="right">35.2%</td>
<td align="right">23.3%</td>
<td align="right">23.9%</td>
<td align="right">18.2%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">349</td>
<td align="left">🟢 Militia</td>
<td align="right"><b>1504</b></td>
<td align="right">26.4%</td>
<td align="right">62.2%</td>
<td align="right">35.5%</td>
<td align="right">31.8%</td>
<td align="right">17.3%</td>
<td align="right">17.9%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">350</td>
<td align="left">🟢 Tide</td>
<td align="right"><b>1504</b></td>
<td align="right">26.4%</td>
<td align="right">54.3%</td>
<td align="right">27.1%</td>
<td align="right">28.7%</td>
<td align="right">20.2%</td>
<td align="right">20.5%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">351</td>
<td align="left">🟢 Demon_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">27.1%</td>
<td align="right">51.1%</td>
<td align="right">45.6%</td>
<td align="right">17.6%</td>
<td align="right">24.0%</td>
<td align="right">18.8%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">352</td>
<td align="left">🟢 Despair</td>
<td align="right"><b>1504</b></td>
<td align="right">27.6%</td>
<td align="right">64.3%</td>
<td align="right">40.9%</td>
<td align="right">31.5%</td>
<td align="right">15.8%</td>
<td align="right">16.4%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">353</td>
<td align="left">🟢 Graviton_Wave</td>
<td align="right"><b>1504</b></td>
<td align="right">24.7%</td>
<td align="right">45.7%</td>
<td align="right">28.8%</td>
<td align="right">26.0%</td>
<td align="right">25.2%</td>
<td align="right">13.4%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">354</td>
<td align="left">🟢 Amethyst</td>
<td align="right"><b>1504</b></td>
<td align="right">24.6%</td>
<td align="right">63.3%</td>
<td align="right">33.8%</td>
<td align="right">17.3%</td>
<td align="right">21.0%</td>
<td align="right">14.2%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">355</td>
<td align="left">🟢 Pokerface</td>
<td align="right"><b>1504</b></td>
<td align="right">30.1%</td>
<td align="right">66.7%</td>
<td align="right">31.2%</td>
<td align="right">45.5%</td>
<td align="right">31.2%</td>
<td align="right">12.5%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">356</td>
<td align="left">🟢 Dealer_Alt</td>
<td align="right"><b>1504</b></td>
<td align="right">30.1%</td>
<td align="right">57.1%</td>
<td align="right">56.2%</td>
<td align="right">46.2%</td>
<td align="right">5.6%</td>
<td align="right">17.2%</td>
<td align="right">83</td>
</tr>
<tr>
<td align="left">357</td>
<td align="left">🟢 Erasure</td>
<td align="right"><b>1504</b></td>
<td align="right">25.1%</td>
<td align="right">48.8%</td>
<td align="right">38.1%</td>
<td align="right">25.0%</td>
<td align="right">17.0%</td>
<td align="right">17.1%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">358</td>
<td align="left">🟢 Scaler</td>
<td align="right"><b>1504</b></td>
<td align="right">25.6%</td>
<td align="right">48.6%</td>
<td align="right">33.8%</td>
<td align="right">27.2%</td>
<td align="right">23.0%</td>
<td align="right">16.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">359</td>
<td align="left">🟢 Lens</td>
<td align="right"><b>1504</b></td>
<td align="right">28.9%</td>
<td align="right">65.3%</td>
<td align="right">38.3%</td>
<td align="right">29.2%</td>
<td align="right">19.6%</td>
<td align="right">18.4%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">360</td>
<td align="left">🟢 Moocher</td>
<td align="right"><b>1504</b></td>
<td align="right">26.1%</td>
<td align="right">57.5%</td>
<td align="right">33.3%</td>
<td align="right">26.8%</td>
<td align="right">26.7%</td>
<td align="right">11.1%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">361</td>
<td align="left">🟢 Force</td>
<td align="right"><b>1504</b></td>
<td align="right">25.8%</td>
<td align="right">55.9%</td>
<td align="right">32.8%</td>
<td align="right">29.9%</td>
<td align="right">22.9%</td>
<td align="right">13.6%</td>
<td align="right">392</td>
</tr>
<tr>
<td align="left">362</td>
<td align="left">🟢 Rhino</td>
<td align="right"><b>1504</b></td>
<td align="right">26.9%</td>
<td align="right">51.4%</td>
<td align="right">43.1%</td>
<td align="right">28.4%</td>
<td align="right">26.2%</td>
<td align="right">11.5%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">363</td>
<td align="left">🟢 Meteor</td>
<td align="right"><b>1504</b></td>
<td align="right">25.5%</td>
<td align="right">50.0%</td>
<td align="right">32.8%</td>
<td align="right">21.2%</td>
<td align="right">27.0%</td>
<td align="right">15.8%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">364</td>
<td align="left">🟢 Perfectionist</td>
<td align="right"><b>1504</b></td>
<td align="right">26.0%</td>
<td align="right">45.9%</td>
<td align="right">25.9%</td>
<td align="right">30.1%</td>
<td align="right">19.6%</td>
<td align="right">22.0%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">365</td>
<td align="left">🟢 Cursed</td>
<td align="right"><b>1504</b></td>
<td align="right">25.8%</td>
<td align="right">44.2%</td>
<td align="right">32.9%</td>
<td align="right">26.0%</td>
<td align="right">26.3%</td>
<td align="right">14.0%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">366</td>
<td align="left">🟢 Bettor</td>
<td align="right"><b>1504</b></td>
<td align="right">29.9%</td>
<td align="right">77.8%</td>
<td align="right">42.9%</td>
<td align="right">26.3%</td>
<td align="right">25.0%</td>
<td align="right">12.0%</td>
<td align="right">87</td>
</tr>
<tr>
<td align="left">367</td>
<td align="left">🟢 Ogre</td>
<td align="right"><b>1504</b></td>
<td align="right">25.0%</td>
<td align="right">44.2%</td>
<td align="right">41.5%</td>
<td align="right">27.4%</td>
<td align="right">15.5%</td>
<td align="right">16.2%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">368</td>
<td align="left">🟢 Corps</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">49.0%</td>
<td align="right">31.8%</td>
<td align="right">30.4%</td>
<td align="right">24.6%</td>
<td align="right">14.1%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">369</td>
<td align="left">🟢 Magma</td>
<td align="right"><b>1503</b></td>
<td align="right">26.5%</td>
<td align="right">51.3%</td>
<td align="right">33.3%</td>
<td align="right">28.0%</td>
<td align="right">25.0%</td>
<td align="right">16.4%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">370</td>
<td align="left">🟢 Voyager</td>
<td align="right"><b>1503</b></td>
<td align="right">25.9%</td>
<td align="right">52.5%</td>
<td align="right">31.9%</td>
<td align="right">20.7%</td>
<td align="right">22.6%</td>
<td align="right">21.3%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">371</td>
<td align="left">🟢 Joker</td>
<td align="right"><b>1503</b></td>
<td align="right">25.9%</td>
<td align="right">57.1%</td>
<td align="right">33.3%</td>
<td align="right">20.4%</td>
<td align="right">26.4%</td>
<td align="right">15.8%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">372</td>
<td align="left">🟢 Tycoon</td>
<td align="right"><b>1503</b></td>
<td align="right">26.8%</td>
<td align="right">54.4%</td>
<td align="right">46.3%</td>
<td align="right">19.5%</td>
<td align="right">22.5%</td>
<td align="right">14.3%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">373</td>
<td align="left">🟢 Fox</td>
<td align="right"><b>1503</b></td>
<td align="right">24.5%</td>
<td align="right">39.0%</td>
<td align="right">38.5%</td>
<td align="right">26.4%</td>
<td align="right">22.0%</td>
<td align="right">10.4%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">374</td>
<td align="left">🟢 Phoenix</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">38.3%</td>
<td align="right">38.0%</td>
<td align="right">23.9%</td>
<td align="right">17.9%</td>
<td align="right">23.6%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">375</td>
<td align="left">🟢 Thunder</td>
<td align="right"><b>1503</b></td>
<td align="right">25.1%</td>
<td align="right">62.2%</td>
<td align="right">29.2%</td>
<td align="right">19.3%</td>
<td align="right">21.2%</td>
<td align="right">17.7%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">376</td>
<td align="left">🟢 Quanta</td>
<td align="right"><b>1503</b></td>
<td align="right">29.8%</td>
<td align="right">60.0%</td>
<td align="right">45.5%</td>
<td align="right">21.1%</td>
<td align="right">31.8%</td>
<td align="right">22.2%</td>
<td align="right">84</td>
</tr>
<tr>
<td align="left">377</td>
<td align="left">🟢 Tortoise</td>
<td align="right"><b>1503</b></td>
<td align="right">24.5%</td>
<td align="right">52.1%</td>
<td align="right">32.4%</td>
<td align="right">21.0%</td>
<td align="right">19.8%</td>
<td align="right">16.0%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">378</td>
<td align="left">🟢 Merchant_Alt</td>
<td align="right"><b>1503</b></td>
<td align="right">25.2%</td>
<td align="right">57.1%</td>
<td align="right">36.0%</td>
<td align="right">21.0%</td>
<td align="right">15.7%</td>
<td align="right">19.5%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">379</td>
<td align="left">🟢 Humming</td>
<td align="right"><b>1503</b></td>
<td align="right">29.7%</td>
<td align="right">50.0%</td>
<td align="right">22.2%</td>
<td align="right">35.7%</td>
<td align="right">21.1%</td>
<td align="right">27.3%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">380</td>
<td align="left">🟢 Centaur</td>
<td align="right"><b>1503</b></td>
<td align="right">25.2%</td>
<td align="right">43.9%</td>
<td align="right">28.8%</td>
<td align="right">26.9%</td>
<td align="right">19.6%</td>
<td align="right">20.3%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">381</td>
<td align="left">🟢 Recon</td>
<td align="right"><b>1503</b></td>
<td align="right">25.5%</td>
<td align="right">57.1%</td>
<td align="right">26.3%</td>
<td align="right">28.4%</td>
<td align="right">23.5%</td>
<td align="right">17.1%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">382</td>
<td align="left">🟢 Mindflayer</td>
<td align="right"><b>1503</b></td>
<td align="right">26.0%</td>
<td align="right">68.0%</td>
<td align="right">22.2%</td>
<td align="right">28.9%</td>
<td align="right">17.2%</td>
<td align="right">20.2%</td>
<td align="right">254</td>
</tr>
<tr>
<td align="left">383</td>
<td align="left">🟢 Kraken</td>
<td align="right"><b>1503</b></td>
<td align="right">26.5%</td>
<td align="right">64.7%</td>
<td align="right">22.5%</td>
<td align="right">20.2%</td>
<td align="right">26.1%</td>
<td align="right">18.8%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">384</td>
<td align="left">🟢 Nickel</td>
<td align="right"><b>1503</b></td>
<td align="right">29.7%</td>
<td align="right">80.0%</td>
<td align="right">41.7%</td>
<td align="right">37.5%</td>
<td align="right">17.6%</td>
<td align="right">7.1%</td>
<td align="right">64</td>
</tr>
<tr>
<td align="left">385</td>
<td align="left">🟢 Pollen</td>
<td align="right"><b>1503</b></td>
<td align="right">29.7%</td>
<td align="right">25.0%</td>
<td align="right">41.2%</td>
<td align="right">36.8%</td>
<td align="right">25.0%</td>
<td align="right">22.2%</td>
<td align="right">91</td>
</tr>
<tr>
<td align="left">386</td>
<td align="left">🟢 Sunshine</td>
<td align="right"><b>1503</b></td>
<td align="right">24.9%</td>
<td align="right">39.6%</td>
<td align="right">41.2%</td>
<td align="right">19.5%</td>
<td align="right">23.6%</td>
<td align="right">17.2%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">387</td>
<td align="left">🟢 Fog</td>
<td align="right"><b>1503</b></td>
<td align="right">26.8%</td>
<td align="right">43.1%</td>
<td align="right">32.8%</td>
<td align="right">35.0%</td>
<td align="right">14.4%</td>
<td align="right">19.1%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">388</td>
<td align="left">🟢 PackRat</td>
<td align="right"><b>1503</b></td>
<td align="right">26.9%</td>
<td align="right">47.1%</td>
<td align="right">43.9%</td>
<td align="right">26.8%</td>
<td align="right">22.4%</td>
<td align="right">17.7%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">389</td>
<td align="left">🟢 Armorer</td>
<td align="right"><b>1503</b></td>
<td align="right">25.0%</td>
<td align="right">43.8%</td>
<td align="right">36.5%</td>
<td align="right">27.0%</td>
<td align="right">21.2%</td>
<td align="right">17.4%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">390</td>
<td align="left">🟢 Cellist</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">44.2%</td>
<td align="right">37.9%</td>
<td align="right">22.5%</td>
<td align="right">24.6%</td>
<td align="right">18.4%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">391</td>
<td align="left">🟢 Climate</td>
<td align="right"><b>1503</b></td>
<td align="right">29.6%</td>
<td align="right">66.7%</td>
<td align="right">63.6%</td>
<td align="right">23.1%</td>
<td align="right">16.0%</td>
<td align="right">18.8%</td>
<td align="right">71</td>
</tr>
<tr>
<td align="left">392</td>
<td align="left">🟢 Commander_Alt</td>
<td align="right"><b>1503</b></td>
<td align="right">25.8%</td>
<td align="right">50.0%</td>
<td align="right">32.8%</td>
<td align="right">26.4%</td>
<td align="right">22.0%</td>
<td align="right">15.1%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">393</td>
<td align="left">🟢 Executioner</td>
<td align="right"><b>1503</b></td>
<td align="right">25.7%</td>
<td align="right">62.5%</td>
<td align="right">34.8%</td>
<td align="right">21.3%</td>
<td align="right">25.0%</td>
<td align="right">13.7%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">394</td>
<td align="left">🟢 Winner</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">48.9%</td>
<td align="right">41.2%</td>
<td align="right">19.4%</td>
<td align="right">24.7%</td>
<td align="right">16.4%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">395</td>
<td align="left">🟢 Tinker</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">52.3%</td>
<td align="right">34.8%</td>
<td align="right">27.0%</td>
<td align="right">22.5%</td>
<td align="right">16.3%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">396</td>
<td align="left">🟢 Bulwark</td>
<td align="right"><b>1503</b></td>
<td align="right">24.7%</td>
<td align="right">60.0%</td>
<td align="right">37.2%</td>
<td align="right">27.3%</td>
<td align="right">21.6%</td>
<td align="right">15.2%</td>
<td align="right">1798</td>
</tr>
<tr>
<td align="left">397</td>
<td align="left">🟢 Breeze</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">48.5%</td>
<td align="right">38.3%</td>
<td align="right">27.1%</td>
<td align="right">21.1%</td>
<td align="right">19.4%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">398</td>
<td align="left">🟢 Ghost</td>
<td align="right"><b>1503</b></td>
<td align="right">25.1%</td>
<td align="right">42.4%</td>
<td align="right">28.2%</td>
<td align="right">31.2%</td>
<td align="right">20.6%</td>
<td align="right">17.9%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">399</td>
<td align="left">🟢 Memorizer</td>
<td align="right"><b>1503</b></td>
<td align="right">29.5%</td>
<td align="right">55.6%</td>
<td align="right">27.3%</td>
<td align="right">21.1%</td>
<td align="right">21.4%</td>
<td align="right">32.0%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">400</td>
<td align="left">🟢 Chemist</td>
<td align="right"><b>1503</b></td>
<td align="right">29.5%</td>
<td align="right">60.0%</td>
<td align="right">21.4%</td>
<td align="right">35.3%</td>
<td align="right">17.6%</td>
<td align="right">27.0%</td>
<td align="right">95</td>
</tr>
<tr>
<td align="left">401</td>
<td align="left">🟢 Emerald</td>
<td align="right"><b>1503</b></td>
<td align="right">25.0%</td>
<td align="right">43.6%</td>
<td align="right">33.9%</td>
<td align="right">30.3%</td>
<td align="right">20.7%</td>
<td align="right">15.8%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">402</td>
<td align="left">🟢 Mindlink</td>
<td align="right"><b>1503</b></td>
<td align="right">25.4%</td>
<td align="right">48.8%</td>
<td align="right">27.1%</td>
<td align="right">25.9%</td>
<td align="right">24.2%</td>
<td align="right">18.1%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">403</td>
<td align="left">🟢 Camouflage</td>
<td align="right"><b>1503</b></td>
<td align="right">27.1%</td>
<td align="right">41.2%</td>
<td align="right">38.6%</td>
<td align="right">24.5%</td>
<td align="right">28.2%</td>
<td align="right">17.1%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">404</td>
<td align="left">🟢 Igniter</td>
<td align="right"><b>1503</b></td>
<td align="right">26.3%</td>
<td align="right">62.8%</td>
<td align="right">42.3%</td>
<td align="right">23.0%</td>
<td align="right">16.9%</td>
<td align="right">17.2%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">405</td>
<td align="left">🟢 Queen_Strategy</td>
<td align="right"><b>1503</b></td>
<td align="right">29.4%</td>
<td align="right">60.0%</td>
<td align="right">30.8%</td>
<td align="right">38.5%</td>
<td align="right">25.9%</td>
<td align="right">13.6%</td>
<td align="right">85</td>
</tr>
<tr>
<td align="left">406</td>
<td align="left">🟢 Astronomer</td>
<td align="right"><b>1503</b></td>
<td align="right">29.4%</td>
<td align="right">75.0%</td>
<td align="right">58.3%</td>
<td align="right">21.4%</td>
<td align="right">22.7%</td>
<td align="right">12.5%</td>
<td align="right">68</td>
</tr>
<tr>
<td align="left">407</td>
<td align="left">🟢 Manipulator</td>
<td align="right"><b>1503</b></td>
<td align="right">26.9%</td>
<td align="right">44.0%</td>
<td align="right">36.0%</td>
<td align="right">20.4%</td>
<td align="right">25.2%</td>
<td align="right">21.5%</td>
<td align="right">476</td>
</tr>
<tr>
<td align="left">408</td>
<td align="left">🟢 Octopus</td>
<td align="right"><b>1503</b></td>
<td align="right">26.0%</td>
<td align="right">54.1%</td>
<td align="right">36.8%</td>
<td align="right">21.6%</td>
<td align="right">26.6%</td>
<td align="right">15.4%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">409</td>
<td align="left">🟢 Hurricane</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">60.9%</td>
<td align="right">28.1%</td>
<td align="right">28.7%</td>
<td align="right">23.3%</td>
<td align="right">13.7%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">410</td>
<td align="left">🟢 Mantis</td>
<td align="right"><b>1503</b></td>
<td align="right">29.3%</td>
<td align="right">57.1%</td>
<td align="right">50.0%</td>
<td align="right">14.3%</td>
<td align="right">22.7%</td>
<td align="right">22.2%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">411</td>
<td align="left">🟢 Polymorph</td>
<td align="right"><b>1503</b></td>
<td align="right">25.7%</td>
<td align="right">54.0%</td>
<td align="right">35.8%</td>
<td align="right">27.8%</td>
<td align="right">14.7%</td>
<td align="right">18.8%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">412</td>
<td align="left">🟢 Lurker_Alt</td>
<td align="right"><b>1503</b></td>
<td align="right">27.4%</td>
<td align="right">54.5%</td>
<td align="right">30.5%</td>
<td align="right">26.9%</td>
<td align="right">28.9%</td>
<td align="right">15.7%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">413</td>
<td align="left">🟢 Archer</td>
<td align="right"><b>1503</b></td>
<td align="right">29.3%</td>
<td align="right">63.6%</td>
<td align="right">50.0%</td>
<td align="right">24.0%</td>
<td align="right">19.2%</td>
<td align="right">14.3%</td>
<td align="right">99</td>
</tr>
<tr>
<td align="left">414</td>
<td align="left">🟢 Forager</td>
<td align="right"><b>1503</b></td>
<td align="right">28.5%</td>
<td align="right">48.4%</td>
<td align="right">39.0%</td>
<td align="right">30.4%</td>
<td align="right">21.2%</td>
<td align="right">17.4%</td>
<td align="right">239</td>
</tr>
<tr>
<td align="left">415</td>
<td align="left">🟢 Reborn</td>
<td align="right"><b>1503</b></td>
<td align="right">25.5%</td>
<td align="right">51.4%</td>
<td align="right">40.8%</td>
<td align="right">23.7%</td>
<td align="right">14.3%</td>
<td align="right">20.1%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">416</td>
<td align="left">🟢 Drought</td>
<td align="right"><b>1503</b></td>
<td align="right">25.8%</td>
<td align="right">53.3%</td>
<td align="right">32.2%</td>
<td align="right">23.5%</td>
<td align="right">24.6%</td>
<td align="right">16.4%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">417</td>
<td align="left">🟢 Charmed</td>
<td align="right"><b>1503</b></td>
<td align="right">25.6%</td>
<td align="right">54.4%</td>
<td align="right">26.1%</td>
<td align="right">25.8%</td>
<td align="right">20.8%</td>
<td align="right">16.2%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">418</td>
<td align="left">🟢 Necromancer</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">49.0%</td>
<td align="right">28.3%</td>
<td align="right">21.6%</td>
<td align="right">27.1%</td>
<td align="right">19.0%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">419</td>
<td align="left">🟢 Transposer</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">46.7%</td>
<td align="right">38.8%</td>
<td align="right">23.2%</td>
<td align="right">25.2%</td>
<td align="right">12.9%</td>
<td align="right">485</td>
</tr>
<tr>
<td align="left">420</td>
<td align="left">🟢 Eraser</td>
<td align="right"><b>1503</b></td>
<td align="right">29.2%</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
<td align="right">46.2%</td>
<td align="right">28.6%</td>
<td align="right">31.2%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">421</td>
<td align="left">🟢 Emissary</td>
<td align="right"><b>1503</b></td>
<td align="right">26.9%</td>
<td align="right">51.2%</td>
<td align="right">31.1%</td>
<td align="right">21.5%</td>
<td align="right">30.4%</td>
<td align="right">16.5%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">422</td>
<td align="left">🟢 Sultan</td>
<td align="right"><b>1503</b></td>
<td align="right">25.1%</td>
<td align="right">60.9%</td>
<td align="right">30.0%</td>
<td align="right">24.4%</td>
<td align="right">15.6%</td>
<td align="right">17.5%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">423</td>
<td align="left">🟢 Smith</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">54.5%</td>
<td align="right">36.0%</td>
<td align="right">31.0%</td>
<td align="right">16.7%</td>
<td align="right">15.6%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">424</td>
<td align="left">🟢 Miser</td>
<td align="right"><b>1503</b></td>
<td align="right">26.1%</td>
<td align="right">69.6%</td>
<td align="right">34.6%</td>
<td align="right">30.8%</td>
<td align="right">22.3%</td>
<td align="right">18.2%</td>
<td align="right">1777</td>
</tr>
<tr>
<td align="left">425</td>
<td align="left">🟢 Shatterer</td>
<td align="right"><b>1503</b></td>
<td align="right">24.8%</td>
<td align="right">54.3%</td>
<td align="right">29.6%</td>
<td align="right">26.2%</td>
<td align="right">22.2%</td>
<td align="right">13.0%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">426</td>
<td align="left">🟢 Mercury</td>
<td align="right"><b>1503</b></td>
<td align="right">29.1%</td>
<td align="right">50.0%</td>
<td align="right">23.1%</td>
<td align="right">21.4%</td>
<td align="right">21.7%</td>
<td align="right">36.8%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">427</td>
<td align="left">🟢 Jinxed</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">53.5%</td>
<td align="right">45.5%</td>
<td align="right">23.5%</td>
<td align="right">14.4%</td>
<td align="right">20.0%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">428</td>
<td align="left">🟢 Eldritch</td>
<td align="right"><b>1503</b></td>
<td align="right">27.1%</td>
<td align="right">57.7%</td>
<td align="right">39.5%</td>
<td align="right">29.2%</td>
<td align="right">15.0%</td>
<td align="right">17.6%</td>
<td align="right">251</td>
</tr>
<tr>
<td align="left">429</td>
<td align="left">🟢 Expander</td>
<td align="right"><b>1503</b></td>
<td align="right">23.4%</td>
<td align="right">60.4%</td>
<td align="right">33.3%</td>
<td align="right">20.2%</td>
<td align="right">20.0%</td>
<td align="right">8.1%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">430</td>
<td align="left">🟢 Medusa</td>
<td align="right"><b>1503</b></td>
<td align="right">26.0%</td>
<td align="right">50.0%</td>
<td align="right">41.8%</td>
<td align="right">29.6%</td>
<td align="right">12.6%</td>
<td align="right">16.7%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">431</td>
<td align="left">🟢 Ambusher</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">58.7%</td>
<td align="right">25.4%</td>
<td align="right">25.0%</td>
<td align="right">25.9%</td>
<td align="right">16.7%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">432</td>
<td align="left">🟢 Cosmic_Entity</td>
<td align="right"><b>1503</b></td>
<td align="right">27.8%</td>
<td align="right">53.6%</td>
<td align="right">39.4%</td>
<td align="right">27.7%</td>
<td align="right">22.2%</td>
<td align="right">11.5%</td>
<td align="right">399</td>
</tr>
<tr>
<td align="left">433</td>
<td align="left">🟢 Boomer</td>
<td align="right"><b>1503</b></td>
<td align="right">29.0%</td>
<td align="right">66.7%</td>
<td align="right">45.5%</td>
<td align="right">8.3%</td>
<td align="right">35.3%</td>
<td align="right">10.0%</td>
<td align="right">69</td>
</tr>
<tr>
<td align="left">434</td>
<td align="left">🟢 Caterpillar</td>
<td align="right"><b>1503</b></td>
<td align="right">28.9%</td>
<td align="right">28.6%</td>
<td align="right">33.3%</td>
<td align="right">35.3%</td>
<td align="right">19.0%</td>
<td align="right">31.8%</td>
<td align="right">76</td>
</tr>
<tr>
<td align="left">435</td>
<td align="left">🟢 Lepton</td>
<td align="right"><b>1503</b></td>
<td align="right">25.5%</td>
<td align="right">51.2%</td>
<td align="right">42.6%</td>
<td align="right">21.4%</td>
<td align="right">20.2%</td>
<td align="right">14.0%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">436</td>
<td align="left">🟢 Gale</td>
<td align="right"><b>1503</b></td>
<td align="right">24.9%</td>
<td align="right">57.9%</td>
<td align="right">40.3%</td>
<td align="right">18.8%</td>
<td align="right">15.0%</td>
<td align="right">12.4%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">437</td>
<td align="left">🟢 Warper</td>
<td align="right"><b>1503</b></td>
<td align="right">26.3%</td>
<td align="right">47.8%</td>
<td align="right">35.5%</td>
<td align="right">26.2%</td>
<td align="right">21.5%</td>
<td align="right">18.8%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">438</td>
<td align="left">🟢 Runaway</td>
<td align="right"><b>1503</b></td>
<td align="right">25.9%</td>
<td align="right">49.0%</td>
<td align="right">30.0%</td>
<td align="right">27.5%</td>
<td align="right">22.0%</td>
<td align="right">17.2%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">439</td>
<td align="left">🟢 Soloist</td>
<td align="right"><b>1503</b></td>
<td align="right">26.1%</td>
<td align="right">40.5%</td>
<td align="right">44.3%</td>
<td align="right">25.8%</td>
<td align="right">17.8%</td>
<td align="right">18.3%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">440</td>
<td align="left">🟢 Ally</td>
<td align="right"><b>1503</b></td>
<td align="right">25.7%</td>
<td align="right">44.7%</td>
<td align="right">32.7%</td>
<td align="right">23.7%</td>
<td align="right">24.8%</td>
<td align="right">18.1%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">441</td>
<td align="left">🟢 Fear_Alt</td>
<td align="right"><b>1503</b></td>
<td align="right">24.7%</td>
<td align="right">56.6%</td>
<td align="right">25.0%</td>
<td align="right">21.8%</td>
<td align="right">20.8%</td>
<td align="right">16.3%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">442</td>
<td align="left">🟢 Pawn</td>
<td align="right"><b>1503</b></td>
<td align="right">28.8%</td>
<td align="right">20.0%</td>
<td align="right">50.0%</td>
<td align="right">30.8%</td>
<td align="right">25.0%</td>
<td align="right">25.0%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">443</td>
<td align="left">🟢 Tin</td>
<td align="right"><b>1503</b></td>
<td align="right">28.7%</td>
<td align="right">80.0%</td>
<td align="right">40.0%</td>
<td align="right">28.6%</td>
<td align="right">17.4%</td>
<td align="right">17.9%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">444</td>
<td align="left">🟢 Obsidian</td>
<td align="right"><b>1503</b></td>
<td align="right">26.3%</td>
<td align="right">58.3%</td>
<td align="right">45.0%</td>
<td align="right">26.6%</td>
<td align="right">16.0%</td>
<td align="right">17.7%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">445</td>
<td align="left">🟢 Navigator</td>
<td align="right"><b>1503</b></td>
<td align="right">25.2%</td>
<td align="right">57.5%</td>
<td align="right">30.2%</td>
<td align="right">23.7%</td>
<td align="right">18.7%</td>
<td align="right">19.5%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">446</td>
<td align="left">🟢 Destined</td>
<td align="right"><b>1503</b></td>
<td align="right">25.7%</td>
<td align="right">46.2%</td>
<td align="right">35.3%</td>
<td align="right">39.5%</td>
<td align="right">22.9%</td>
<td align="right">9.0%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">447</td>
<td align="left">🟢 Victor</td>
<td align="right"><b>1503</b></td>
<td align="right">24.6%</td>
<td align="right">45.5%</td>
<td align="right">29.8%</td>
<td align="right">26.9%</td>
<td align="right">19.4%</td>
<td align="right">15.4%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">448</td>
<td align="left">🟢 Connoisseur</td>
<td align="right"><b>1503</b></td>
<td align="right">23.5%</td>
<td align="right">50.0%</td>
<td align="right">37.7%</td>
<td align="right">24.8%</td>
<td align="right">20.5%</td>
<td align="right">15.3%</td>
<td align="right">1828</td>
</tr>
<tr>
<td align="left">449</td>
<td align="left">🟢 Biologist</td>
<td align="right"><b>1503</b></td>
<td align="right">28.7%</td>
<td align="right">46.2%</td>
<td align="right">22.2%</td>
<td align="right">27.3%</td>
<td align="right">18.2%</td>
<td align="right">31.2%</td>
<td align="right">87</td>
</tr>
<tr>
<td align="left">450</td>
<td align="left">🟢 Silver</td>
<td align="right"><b>1503</b></td>
<td align="right">28.7%</td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">32.0%</td>
<td align="right">12.5%</td>
<td align="right">87</td>
</tr>
<tr>
<td align="left">451</td>
<td align="left">🟢 Factorial</td>
<td align="right"><b>1503</b></td>
<td align="right">28.7%</td>
<td align="right">50.0%</td>
<td align="right">13.3%</td>
<td align="right">27.3%</td>
<td align="right">30.0%</td>
<td align="right">25.9%</td>
<td align="right">87</td>
</tr>
<tr>
<td align="left">452</td>
<td align="left">🟢 Patrol</td>
<td align="right"><b>1503</b></td>
<td align="right">25.8%</td>
<td align="right">52.2%</td>
<td align="right">38.1%</td>
<td align="right">18.9%</td>
<td align="right">23.4%</td>
<td align="right">13.8%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">453</td>
<td align="left">🟢 Singer</td>
<td align="right"><b>1503</b></td>
<td align="right">25.3%</td>
<td align="right">40.0%</td>
<td align="right">44.4%</td>
<td align="right">22.6%</td>
<td align="right">13.5%</td>
<td align="right">18.7%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">454</td>
<td align="left">🟢 Transcendent</td>
<td align="right"><b>1503</b></td>
<td align="right">26.2%</td>
<td align="right">52.6%</td>
<td align="right">32.9%</td>
<td align="right">30.1%</td>
<td align="right">18.7%</td>
<td align="right">18.0%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">455</td>
<td align="left">🟢 Memory</td>
<td align="right"><b>1503</b></td>
<td align="right">25.6%</td>
<td align="right">50.0%</td>
<td align="right">30.7%</td>
<td align="right">22.7%</td>
<td align="right">20.0%</td>
<td align="right">21.1%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">456</td>
<td align="left">🟢 Sovereign</td>
<td align="right"><b>1503</b></td>
<td align="right">24.6%</td>
<td align="right">53.2%</td>
<td align="right">40.0%</td>
<td align="right">24.3%</td>
<td align="right">19.4%</td>
<td align="right">13.0%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">457</td>
<td align="left">🟢 Yogi</td>
<td align="right"><b>1503</b></td>
<td align="right">26.0%</td>
<td align="right">60.8%</td>
<td align="right">37.3%</td>
<td align="right">25.7%</td>
<td align="right">17.8%</td>
<td align="right">12.8%</td>
<td align="right">470</td>
</tr>
<tr>
<td align="left">458</td>
<td align="left">🟢 Deflector</td>
<td align="right"><b>1503</b></td>
<td align="right">26.4%</td>
<td align="right">42.9%</td>
<td align="right">37.3%</td>
<td align="right">27.3%</td>
<td align="right">21.2%</td>
<td align="right">18.9%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">459</td>
<td align="left">🟢 Whale</td>
<td align="right"><b>1503</b></td>
<td align="right">26.5%</td>
<td align="right">38.9%</td>
<td align="right">37.8%</td>
<td align="right">27.4%</td>
<td align="right">20.7%</td>
<td align="right">19.9%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">460</td>
<td align="left">🟢 Subjugator</td>
<td align="right"><b>1503</b></td>
<td align="right">24.4%</td>
<td align="right">60.0%</td>
<td align="right">35.1%</td>
<td align="right">26.1%</td>
<td align="right">15.8%</td>
<td align="right">12.1%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">461</td>
<td align="left">🟢 Thunder_Alt</td>
<td align="right"><b>1503</b></td>
<td align="right">28.6%</td>
<td align="right">50.0%</td>
<td align="right">18.2%</td>
<td align="right">34.8%</td>
<td align="right">31.8%</td>
<td align="right">20.7%</td>
<td align="right">91</td>
</tr>
<tr>
<td align="left">462</td>
<td align="left">🟢 Copper</td>
<td align="right"><b>1503</b></td>
<td align="right">28.6%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">10.5%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">463</td>
<td align="left">🟢 Barrier</td>
<td align="right"><b>1503</b></td>
<td align="right">25.8%</td>
<td align="right">58.5%</td>
<td align="right">39.4%</td>
<td align="right">26.2%</td>
<td align="right">21.7%</td>
<td align="right">12.0%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">464</td>
<td align="left">🟢 Destroyer</td>
<td align="right"><b>1503</b></td>
<td align="right">24.9%</td>
<td align="right">50.0%</td>
<td align="right">35.2%</td>
<td align="right">25.4%</td>
<td align="right">20.2%</td>
<td align="right">16.4%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">465</td>
<td align="left">🟢 Enchanter</td>
<td align="right"><b>1503</b></td>
<td align="right">26.1%</td>
<td align="right">40.0%</td>
<td align="right">29.7%</td>
<td align="right">30.4%</td>
<td align="right">22.1%</td>
<td align="right">20.0%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">466</td>
<td align="left">🟢 Skulker</td>
<td align="right"><b>1503</b></td>
<td align="right">25.1%</td>
<td align="right">44.7%</td>
<td align="right">37.3%</td>
<td align="right">24.1%</td>
<td align="right">19.4%</td>
<td align="right">19.2%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">467</td>
<td align="left">🟢 Shifter</td>
<td align="right"><b>1503</b></td>
<td align="right">24.9%</td>
<td align="right">55.3%</td>
<td align="right">31.6%</td>
<td align="right">23.3%</td>
<td align="right">18.5%</td>
<td align="right">18.1%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">468</td>
<td align="left">🟢 Mushroom</td>
<td align="right"><b>1503</b></td>
<td align="right">28.4%</td>
<td align="right">75.0%</td>
<td align="right">54.5%</td>
<td align="right">22.2%</td>
<td align="right">13.0%</td>
<td align="right">21.4%</td>
<td align="right">88</td>
</tr>
<tr>
<td align="left">469</td>
<td align="left">🟢 Quark</td>
<td align="right"><b>1503</b></td>
<td align="right">26.3%</td>
<td align="right">56.4%</td>
<td align="right">31.7%</td>
<td align="right">25.7%</td>
<td align="right">26.9%</td>
<td align="right">15.2%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">470</td>
<td align="left">🟢 Nyarlathotep</td>
<td align="right"><b>1503</b></td>
<td align="right">25.8%</td>
<td align="right">42.3%</td>
<td align="right">38.5%</td>
<td align="right">31.7%</td>
<td align="right">19.0%</td>
<td align="right">13.5%</td>
<td align="right">260</td>
</tr>
<tr>
<td align="left">471</td>
<td align="left">🟢 Uncertain</td>
<td align="right"><b>1503</b></td>
<td align="right">28.4%</td>
<td align="right">55.6%</td>
<td align="right">43.8%</td>
<td align="right">23.1%</td>
<td align="right">18.8%</td>
<td align="right">15.0%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">472</td>
<td align="left">🟢 Attractor</td>
<td align="right"><b>1503</b></td>
<td align="right">28.4%</td>
<td align="right">44.4%</td>
<td align="right">55.6%</td>
<td align="right">20.0%</td>
<td align="right">26.3%</td>
<td align="right">18.2%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">473</td>
<td align="left">🟢 Nanny</td>
<td align="right"><b>1503</b></td>
<td align="right">25.7%</td>
<td align="right">51.6%</td>
<td align="right">36.4%</td>
<td align="right">19.8%</td>
<td align="right">21.6%</td>
<td align="right">18.0%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">474</td>
<td align="left">🟢 Quartermaster</td>
<td align="right"><b>1503</b></td>
<td align="right">23.6%</td>
<td align="right">47.4%</td>
<td align="right">33.3%</td>
<td align="right">20.6%</td>
<td align="right">23.5%</td>
<td align="right">14.9%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">475</td>
<td align="left">🟢 Governor</td>
<td align="right"><b>1503</b></td>
<td align="right">24.9%</td>
<td align="right">64.1%</td>
<td align="right">37.5%</td>
<td align="right">21.6%</td>
<td align="right">18.3%</td>
<td align="right">15.2%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">476</td>
<td align="left">🟢 Whirlwind</td>
<td align="right"><b>1502</b></td>
<td align="right">25.8%</td>
<td align="right">48.8%</td>
<td align="right">33.3%</td>
<td align="right">30.6%</td>
<td align="right">18.2%</td>
<td align="right">17.8%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">477</td>
<td align="left">🟢 Star_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">24.7%</td>
<td align="right">67.6%</td>
<td align="right">30.8%</td>
<td align="right">21.4%</td>
<td align="right">23.5%</td>
<td align="right">13.7%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">478</td>
<td align="left">🟢 Prime</td>
<td align="right"><b>1502</b></td>
<td align="right">28.3%</td>
<td align="right">46.2%</td>
<td align="right">21.1%</td>
<td align="right">11.1%</td>
<td align="right">36.0%</td>
<td align="right">23.1%</td>
<td align="right">92</td>
</tr>
<tr>
<td align="left">479</td>
<td align="left">🟢 Competitor</td>
<td align="right"><b>1502</b></td>
<td align="right">28.2%</td>
<td align="right">71.4%</td>
<td align="right">29.4%</td>
<td align="right">42.1%</td>
<td align="right">15.0%</td>
<td align="right">13.6%</td>
<td align="right">85</td>
</tr>
<tr>
<td align="left">480</td>
<td align="left">🟢 Fortifier</td>
<td align="right"><b>1502</b></td>
<td align="right">26.1%</td>
<td align="right">48.8%</td>
<td align="right">38.9%</td>
<td align="right">22.1%</td>
<td align="right">25.7%</td>
<td align="right">14.3%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">481</td>
<td align="left">🟢 Flourisher</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">58.6%</td>
<td align="right">31.1%</td>
<td align="right">25.0%</td>
<td align="right">17.4%</td>
<td align="right">18.3%</td>
<td align="right">494</td>
</tr>
<tr>
<td align="left">482</td>
<td align="left">🟢 Reminiscer</td>
<td align="right"><b>1502</b></td>
<td align="right">28.2%</td>
<td align="right">60.0%</td>
<td align="right">20.0%</td>
<td align="right">20.0%</td>
<td align="right">31.6%</td>
<td align="right">20.8%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">483</td>
<td align="left">🟢 Season</td>
<td align="right"><b>1502</b></td>
<td align="right">28.2%</td>
<td align="right">69.2%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">6.2%</td>
<td align="right">20.0%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">484</td>
<td align="left">🟢 Fader</td>
<td align="right"><b>1502</b></td>
<td align="right">25.2%</td>
<td align="right">41.0%</td>
<td align="right">42.9%</td>
<td align="right">26.0%</td>
<td align="right">20.2%</td>
<td align="right">13.3%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">485</td>
<td align="left">🟢 Cthonic</td>
<td align="right"><b>1502</b></td>
<td align="right">27.0%</td>
<td align="right">69.6%</td>
<td align="right">27.0%</td>
<td align="right">30.8%</td>
<td align="right">17.2%</td>
<td align="right">19.2%</td>
<td align="right">248</td>
</tr>
<tr>
<td align="left">486</td>
<td align="left">🟢 Consensus</td>
<td align="right"><b>1502</b></td>
<td align="right">25.9%</td>
<td align="right">40.7%</td>
<td align="right">30.4%</td>
<td align="right">33.8%</td>
<td align="right">17.1%</td>
<td align="right">19.1%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">487</td>
<td align="left">🟢 Will</td>
<td align="right"><b>1502</b></td>
<td align="right">24.2%</td>
<td align="right">45.8%</td>
<td align="right">46.2%</td>
<td align="right">12.5%</td>
<td align="right">24.3%</td>
<td align="right">12.8%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">488</td>
<td align="left">🟢 Seal</td>
<td align="right"><b>1502</b></td>
<td align="right">24.8%</td>
<td align="right">57.1%</td>
<td align="right">32.9%</td>
<td align="right">21.7%</td>
<td align="right">23.8%</td>
<td align="right">13.8%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">489</td>
<td align="left">🟢 Page</td>
<td align="right"><b>1502</b></td>
<td align="right">25.3%</td>
<td align="right">39.4%</td>
<td align="right">30.0%</td>
<td align="right">32.6%</td>
<td align="right">20.3%</td>
<td align="right">14.9%</td>
<td align="right">466</td>
</tr>
<tr>
<td align="left">490</td>
<td align="left">🟢 Coordinator</td>
<td align="right"><b>1502</b></td>
<td align="right">28.5%</td>
<td align="right">54.2%</td>
<td align="right">38.2%</td>
<td align="right">26.2%</td>
<td align="right">27.0%</td>
<td align="right">16.2%</td>
<td align="right">396</td>
</tr>
<tr>
<td align="left">491</td>
<td align="left">🟢 Cosmic_Ray</td>
<td align="right"><b>1502</b></td>
<td align="right">25.9%</td>
<td align="right">48.0%</td>
<td align="right">40.0%</td>
<td align="right">22.3%</td>
<td align="right">23.9%</td>
<td align="right">16.4%</td>
<td align="right">498</td>
</tr>
<tr>
<td align="left">492</td>
<td align="left">🟢 Evolver_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">24.1%</td>
<td align="right">36.8%</td>
<td align="right">44.8%</td>
<td align="right">17.0%</td>
<td align="right">24.5%</td>
<td align="right">14.9%</td>
<td align="right">406</td>
</tr>
<tr>
<td align="left">493</td>
<td align="left">🟢 Historian_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">28.0%</td>
<td align="right">71.4%</td>
<td align="right">37.5%</td>
<td align="right">31.2%</td>
<td align="right">26.1%</td>
<td align="right">5.0%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">494</td>
<td align="left">🟢 Void_Entity</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">39.5%</td>
<td align="right">35.4%</td>
<td align="right">23.9%</td>
<td align="right">25.6%</td>
<td align="right">17.9%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">495</td>
<td align="left">🟢 Filth</td>
<td align="right"><b>1502</b></td>
<td align="right">24.8%</td>
<td align="right">35.7%</td>
<td align="right">44.6%</td>
<td align="right">22.5%</td>
<td align="right">16.5%</td>
<td align="right">19.3%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">496</td>
<td align="left">🟢 Crystalline</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">56.8%</td>
<td align="right">41.2%</td>
<td align="right">22.3%</td>
<td align="right">15.8%</td>
<td align="right">18.1%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">497</td>
<td align="left">🟢 Deluge</td>
<td align="right"><b>1502</b></td>
<td align="right">28.0%</td>
<td align="right">75.0%</td>
<td align="right">36.4%</td>
<td align="right">30.0%</td>
<td align="right">6.7%</td>
<td align="right">19.0%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">498</td>
<td align="left">🟢 Sprint</td>
<td align="right"><b>1502</b></td>
<td align="right">24.5%</td>
<td align="right">50.0%</td>
<td align="right">44.4%</td>
<td align="right">23.2%</td>
<td align="right">18.6%</td>
<td align="right">12.2%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">499</td>
<td align="left">🟢 Photon</td>
<td align="right"><b>1502</b></td>
<td align="right">26.2%</td>
<td align="right">51.2%</td>
<td align="right">30.5%</td>
<td align="right">23.3%</td>
<td align="right">24.6%</td>
<td align="right">19.8%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">500</td>
<td align="left">🟢 Cannibal</td>
<td align="right"><b>1502</b></td>
<td align="right">27.1%</td>
<td align="right">61.5%</td>
<td align="right">36.1%</td>
<td align="right">26.9%</td>
<td align="right">17.0%</td>
<td align="right">19.0%</td>
<td align="right">251</td>
</tr>
<tr>
<td align="left">501</td>
<td align="left">🟢 Shelter</td>
<td align="right"><b>1502</b></td>
<td align="right">26.5%</td>
<td align="right">47.2%</td>
<td align="right">33.9%</td>
<td align="right">27.2%</td>
<td align="right">17.4%</td>
<td align="right">22.1%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">502</td>
<td align="left">🟢 Micron</td>
<td align="right"><b>1502</b></td>
<td align="right">26.1%</td>
<td align="right">53.7%</td>
<td align="right">37.1%</td>
<td align="right">34.2%</td>
<td align="right">14.9%</td>
<td align="right">17.1%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">503</td>
<td align="left">🟢 Platoon</td>
<td align="right"><b>1502</b></td>
<td align="right">25.1%</td>
<td align="right">47.1%</td>
<td align="right">33.3%</td>
<td align="right">22.3%</td>
<td align="right">23.7%</td>
<td align="right">18.6%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">504</td>
<td align="left">🟢 Zealot</td>
<td align="right"><b>1502</b></td>
<td align="right">26.1%</td>
<td align="right">51.4%</td>
<td align="right">41.4%</td>
<td align="right">31.2%</td>
<td align="right">16.5%</td>
<td align="right">17.6%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">505</td>
<td align="left">🟢 Transmitter</td>
<td align="right"><b>1502</b></td>
<td align="right">24.9%</td>
<td align="right">48.5%</td>
<td align="right">26.2%</td>
<td align="right">27.3%</td>
<td align="right">23.1%</td>
<td align="right">18.5%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">506</td>
<td align="left">🟢 Scavenger_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">25.3%</td>
<td align="right">57.1%</td>
<td align="right">35.6%</td>
<td align="right">21.1%</td>
<td align="right">16.0%</td>
<td align="right">19.1%</td>
<td align="right">470</td>
</tr>
<tr>
<td align="left">507</td>
<td align="left">🟢 Lore</td>
<td align="right"><b>1502</b></td>
<td align="right">24.7%</td>
<td align="right">52.7%</td>
<td align="right">31.7%</td>
<td align="right">29.3%</td>
<td align="right">18.8%</td>
<td align="right">11.9%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">508</td>
<td align="left">🟢 Orbit</td>
<td align="right"><b>1502</b></td>
<td align="right">25.4%</td>
<td align="right">46.2%</td>
<td align="right">29.5%</td>
<td align="right">25.6%</td>
<td align="right">23.1%</td>
<td align="right">16.1%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">509</td>
<td align="left">🟢 Cinder</td>
<td align="right"><b>1502</b></td>
<td align="right">25.4%</td>
<td align="right">37.8%</td>
<td align="right">33.3%</td>
<td align="right">25.9%</td>
<td align="right">22.8%</td>
<td align="right">20.5%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">510</td>
<td align="left">🟢 Hexer</td>
<td align="right"><b>1502</b></td>
<td align="right">26.1%</td>
<td align="right">45.5%</td>
<td align="right">30.3%</td>
<td align="right">29.8%</td>
<td align="right">19.4%</td>
<td align="right">18.9%</td>
<td align="right">476</td>
</tr>
<tr>
<td align="left">511</td>
<td align="left">🟢 Federation</td>
<td align="right"><b>1502</b></td>
<td align="right">27.3%</td>
<td align="right">60.5%</td>
<td align="right">37.3%</td>
<td align="right">27.7%</td>
<td align="right">19.5%</td>
<td align="right">18.9%</td>
<td align="right">417</td>
</tr>
<tr>
<td align="left">512</td>
<td align="left">🟢 Prowler</td>
<td align="right"><b>1502</b></td>
<td align="right">24.6%</td>
<td align="right">57.9%</td>
<td align="right">33.3%</td>
<td align="right">22.5%</td>
<td align="right">20.7%</td>
<td align="right">11.0%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">513</td>
<td align="left">🟢 Fortune</td>
<td align="right"><b>1502</b></td>
<td align="right">24.9%</td>
<td align="right">55.3%</td>
<td align="right">22.2%</td>
<td align="right">23.9%</td>
<td align="right">24.3%</td>
<td align="right">18.8%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">514</td>
<td align="left">🟢 Chronicler</td>
<td align="right"><b>1502</b></td>
<td align="right">24.6%</td>
<td align="right">43.8%</td>
<td align="right">31.2%</td>
<td align="right">25.8%</td>
<td align="right">25.0%</td>
<td align="right">12.9%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">515</td>
<td align="left">🟢 Grudge</td>
<td align="right"><b>1502</b></td>
<td align="right">22.5%</td>
<td align="right">44.4%</td>
<td align="right">32.7%</td>
<td align="right">24.4%</td>
<td align="right">20.7%</td>
<td align="right">16.5%</td>
<td align="right">2595</td>
</tr>
<tr>
<td align="left">516</td>
<td align="left">🟢 Compressor</td>
<td align="right"><b>1502</b></td>
<td align="right">27.6%</td>
<td align="right">36.4%</td>
<td align="right">41.7%</td>
<td align="right">8.3%</td>
<td align="right">42.1%</td>
<td align="right">13.6%</td>
<td align="right">76</td>
</tr>
<tr>
<td align="left">517</td>
<td align="left">🟢 Tyrant</td>
<td align="right"><b>1502</b></td>
<td align="right">23.6%</td>
<td align="right">44.4%</td>
<td align="right">35.7%</td>
<td align="right">23.6%</td>
<td align="right">19.0%</td>
<td align="right">20.8%</td>
<td align="right">2445</td>
</tr>
<tr>
<td align="left">518</td>
<td align="left">🟢 Squee</td>
<td align="right"><b>1502</b></td>
<td align="right">23.5%</td>
<td align="right">41.3%</td>
<td align="right">37.1%</td>
<td align="right">20.4%</td>
<td align="right">23.2%</td>
<td align="right">12.3%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">519</td>
<td align="left">🟢 Interface</td>
<td align="right"><b>1502</b></td>
<td align="right">23.8%</td>
<td align="right">51.2%</td>
<td align="right">29.3%</td>
<td align="right">22.9%</td>
<td align="right">22.8%</td>
<td align="right">16.1%</td>
<td align="right">479</td>
</tr>
<tr>
<td align="left">520</td>
<td align="left">🟢 Moon_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">23.3%</td>
<td align="right">52.4%</td>
<td align="right">23.5%</td>
<td align="right">23.1%</td>
<td align="right">19.8%</td>
<td align="right">13.9%</td>
<td align="right">477</td>
</tr>
<tr>
<td align="left">521</td>
<td align="left">🟢 Coalition</td>
<td align="right"><b>1502</b></td>
<td align="right">23.2%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">24.4%</td>
<td align="right">17.9%</td>
<td align="right">18.0%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">522</td>
<td align="left">🟢 Turtle</td>
<td align="right"><b>1502</b></td>
<td align="right">24.9%</td>
<td align="right">51.1%</td>
<td align="right">30.5%</td>
<td align="right">33.3%</td>
<td align="right">15.7%</td>
<td align="right">14.9%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">523</td>
<td align="left">🟢 Sneak</td>
<td align="right"><b>1502</b></td>
<td align="right">24.5%</td>
<td align="right">48.8%</td>
<td align="right">40.3%</td>
<td align="right">27.2%</td>
<td align="right">10.1%</td>
<td align="right">16.0%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">524</td>
<td align="left">🟢 Bloomer</td>
<td align="right"><b>1502</b></td>
<td align="right">25.6%</td>
<td align="right">61.5%</td>
<td align="right">28.4%</td>
<td align="right">22.1%</td>
<td align="right">25.0%</td>
<td align="right">17.5%</td>
<td align="right">484</td>
</tr>
<tr>
<td align="left">525</td>
<td align="left">🟢 Melody</td>
<td align="right"><b>1502</b></td>
<td align="right">26.0%</td>
<td align="right">65.0%</td>
<td align="right">37.1%</td>
<td align="right">27.6%</td>
<td align="right">17.3%</td>
<td align="right">16.8%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">526</td>
<td align="left">🟢 Storm_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">25.6%</td>
<td align="right">47.9%</td>
<td align="right">30.8%</td>
<td align="right">22.0%</td>
<td align="right">21.3%</td>
<td align="right">20.8%</td>
<td align="right">406</td>
</tr>
<tr>
<td align="left">527</td>
<td align="left">🟢 Pandemonium</td>
<td align="right"><b>1502</b></td>
<td align="right">25.3%</td>
<td align="right">55.8%</td>
<td align="right">33.3%</td>
<td align="right">19.0%</td>
<td align="right">21.3%</td>
<td align="right">15.8%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">528</td>
<td align="left">🟢 Retreat</td>
<td align="right"><b>1502</b></td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
<td align="right">43.8%</td>
<td align="right">23.5%</td>
<td align="right">28.6%</td>
<td align="right">20.0%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">529</td>
<td align="left">🟢 Automaton</td>
<td align="right"><b>1502</b></td>
<td align="right">26.7%</td>
<td align="right">54.1%</td>
<td align="right">32.8%</td>
<td align="right">29.5%</td>
<td align="right">18.1%</td>
<td align="right">21.7%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">530</td>
<td align="left">🟢 Developer</td>
<td align="right"><b>1502</b></td>
<td align="right">24.1%</td>
<td align="right">45.0%</td>
<td align="right">35.4%</td>
<td align="right">20.8%</td>
<td align="right">19.5%</td>
<td align="right">17.8%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">531</td>
<td align="left">🟢 Wall</td>
<td align="right"><b>1502</b></td>
<td align="right">26.5%</td>
<td align="right">54.2%</td>
<td align="right">41.0%</td>
<td align="right">23.8%</td>
<td align="right">19.6%</td>
<td align="right">15.4%</td>
<td align="right">407</td>
</tr>
<tr>
<td align="left">532</td>
<td align="left">🟢 Hunter_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">25.0%</td>
<td align="right">53.2%</td>
<td align="right">26.0%</td>
<td align="right">27.1%</td>
<td align="right">17.6%</td>
<td align="right">18.9%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">533</td>
<td align="left">🟢 Invader</td>
<td align="right"><b>1502</b></td>
<td align="right">23.8%</td>
<td align="right">65.7%</td>
<td align="right">36.8%</td>
<td align="right">24.2%</td>
<td align="right">18.3%</td>
<td align="right">18.9%</td>
<td align="right">1861</td>
</tr>
<tr>
<td align="left">534</td>
<td align="left">🟢 Taskmaster</td>
<td align="right"><b>1502</b></td>
<td align="right">24.6%</td>
<td align="right">55.3%</td>
<td align="right">38.3%</td>
<td align="right">17.8%</td>
<td align="right">22.1%</td>
<td align="right">15.4%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">535</td>
<td align="left">🟢 Shock</td>
<td align="right"><b>1502</b></td>
<td align="right">25.0%</td>
<td align="right">47.5%</td>
<td align="right">27.7%</td>
<td align="right">27.2%</td>
<td align="right">18.9%</td>
<td align="right">21.4%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">536</td>
<td align="left">🟢 Pretender</td>
<td align="right"><b>1502</b></td>
<td align="right">23.9%</td>
<td align="right">48.8%</td>
<td align="right">31.0%</td>
<td align="right">23.3%</td>
<td align="right">14.6%</td>
<td align="right">20.0%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">537</td>
<td align="left">🟢 Division</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">53.8%</td>
<td align="right">40.8%</td>
<td align="right">15.9%</td>
<td align="right">21.5%</td>
<td align="right">14.9%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">538</td>
<td align="left">🟢 Spider</td>
<td align="right"><b>1502</b></td>
<td align="right">22.6%</td>
<td align="right">52.6%</td>
<td align="right">28.2%</td>
<td align="right">24.8%</td>
<td align="right">19.6%</td>
<td align="right">12.2%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">539</td>
<td align="left">🟢 Multiplier_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">27.2%</td>
<td align="right">55.6%</td>
<td align="right">50.0%</td>
<td align="right">18.8%</td>
<td align="right">21.1%</td>
<td align="right">16.0%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">540</td>
<td align="left">🟢 Capitalist</td>
<td align="right"><b>1502</b></td>
<td align="right">23.8%</td>
<td align="right">50.0%</td>
<td align="right">32.5%</td>
<td align="right">20.0%</td>
<td align="right">17.8%</td>
<td align="right">16.7%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">541</td>
<td align="left">🟢 Primordial</td>
<td align="right"><b>1502</b></td>
<td align="right">24.5%</td>
<td align="right">47.6%</td>
<td align="right">29.0%</td>
<td align="right">26.3%</td>
<td align="right">21.0%</td>
<td align="right">16.9%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">542</td>
<td align="left">🟢 Cloak</td>
<td align="right"><b>1502</b></td>
<td align="right">26.8%</td>
<td align="right">57.6%</td>
<td align="right">38.7%</td>
<td align="right">25.0%</td>
<td align="right">23.3%</td>
<td align="right">17.2%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">543</td>
<td align="left">🟢 Conscript</td>
<td align="right"><b>1502</b></td>
<td align="right">23.3%</td>
<td align="right">41.3%</td>
<td align="right">27.1%</td>
<td align="right">20.2%</td>
<td align="right">20.9%</td>
<td align="right">19.7%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">544</td>
<td align="left">🟢 Lightning</td>
<td align="right"><b>1502</b></td>
<td align="right">26.1%</td>
<td align="right">39.6%</td>
<td align="right">29.2%</td>
<td align="right">36.4%</td>
<td align="right">20.5%</td>
<td align="right">17.7%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">545</td>
<td align="left">🟢 Sonar</td>
<td align="right"><b>1502</b></td>
<td align="right">27.1%</td>
<td align="right">40.0%</td>
<td align="right">36.8%</td>
<td align="right">42.9%</td>
<td align="right">19.0%</td>
<td align="right">15.4%</td>
<td align="right">85</td>
</tr>
<tr>
<td align="left">546</td>
<td align="left">🟢 Weasel</td>
<td align="right"><b>1502</b></td>
<td align="right">25.2%</td>
<td align="right">52.6%</td>
<td align="right">30.3%</td>
<td align="right">23.9%</td>
<td align="right">20.5%</td>
<td align="right">18.2%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">547</td>
<td align="left">🟢 Trapper</td>
<td align="right"><b>1502</b></td>
<td align="right">26.6%</td>
<td align="right">54.5%</td>
<td align="right">37.5%</td>
<td align="right">20.3%</td>
<td align="right">23.3%</td>
<td align="right">18.3%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">548</td>
<td align="left">🟢 Symphony</td>
<td align="right"><b>1502</b></td>
<td align="right">24.5%</td>
<td align="right">47.4%</td>
<td align="right">36.4%</td>
<td align="right">16.7%</td>
<td align="right">23.5%</td>
<td align="right">15.0%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">549</td>
<td align="left">🟢 Dimension</td>
<td align="right"><b>1502</b></td>
<td align="right">26.4%</td>
<td align="right">47.1%</td>
<td align="right">41.9%</td>
<td align="right">30.1%</td>
<td align="right">17.6%</td>
<td align="right">17.0%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">550</td>
<td align="left">🟢 Electron</td>
<td align="right"><b>1502</b></td>
<td align="right">24.8%</td>
<td align="right">52.8%</td>
<td align="right">35.8%</td>
<td align="right">25.1%</td>
<td align="right">21.6%</td>
<td align="right">19.4%</td>
<td align="right">1869</td>
</tr>
<tr>
<td align="left">551</td>
<td align="left">🟢 Regenerator</td>
<td align="right"><b>1502</b></td>
<td align="right">24.8%</td>
<td align="right">61.9%</td>
<td align="right">38.9%</td>
<td align="right">25.6%</td>
<td align="right">17.3%</td>
<td align="right">13.1%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">552</td>
<td align="left">🟢 Swift</td>
<td align="right"><b>1502</b></td>
<td align="right">24.4%</td>
<td align="right">48.6%</td>
<td align="right">26.8%</td>
<td align="right">29.1%</td>
<td align="right">19.8%</td>
<td align="right">16.7%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">553</td>
<td align="left">🟢 Highroller</td>
<td align="right"><b>1502</b></td>
<td align="right">27.0%</td>
<td align="right">62.5%</td>
<td align="right">37.5%</td>
<td align="right">33.3%</td>
<td align="right">24.0%</td>
<td align="right">11.1%</td>
<td align="right">89</td>
</tr>
<tr>
<td align="left">554</td>
<td align="left">🟢 Creeper</td>
<td align="right"><b>1502</b></td>
<td align="right">23.4%</td>
<td align="right">48.6%</td>
<td align="right">27.7%</td>
<td align="right">25.0%</td>
<td align="right">15.9%</td>
<td align="right">19.8%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">555</td>
<td align="left">🟢 Mayhem</td>
<td align="right"><b>1502</b></td>
<td align="right">25.3%</td>
<td align="right">51.2%</td>
<td align="right">39.3%</td>
<td align="right">27.5%</td>
<td align="right">19.6%</td>
<td align="right">14.3%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">556</td>
<td align="left">🟢 Factory</td>
<td align="right"><b>1502</b></td>
<td align="right">25.2%</td>
<td align="right">41.4%</td>
<td align="right">26.2%</td>
<td align="right">25.0%</td>
<td align="right">24.0%</td>
<td align="right">18.8%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">557</td>
<td align="left">🟢 Catalyst</td>
<td align="right"><b>1502</b></td>
<td align="right">25.2%</td>
<td align="right">53.1%</td>
<td align="right">31.7%</td>
<td align="right">25.0%</td>
<td align="right">17.5%</td>
<td align="right">17.4%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">558</td>
<td align="left">🟢 Fencer</td>
<td align="right"><b>1502</b></td>
<td align="right">26.9%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">8.3%</td>
<td align="right">20.0%</td>
<td align="right">18.5%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">559</td>
<td align="left">🟢 Divider</td>
<td align="right"><b>1502</b></td>
<td align="right">26.9%</td>
<td align="right">28.6%</td>
<td align="right">28.6%</td>
<td align="right">33.3%</td>
<td align="right">30.4%</td>
<td align="right">15.8%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">560</td>
<td align="left">🟢 Flashback</td>
<td align="right"><b>1502</b></td>
<td align="right">26.9%</td>
<td align="right">40.0%</td>
<td align="right">29.4%</td>
<td align="right">27.8%</td>
<td align="right">33.3%</td>
<td align="right">11.8%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">561</td>
<td align="left">🟢 Quarantine</td>
<td align="right"><b>1502</b></td>
<td align="right">24.0%</td>
<td align="right">45.2%</td>
<td align="right">34.8%</td>
<td align="right">17.9%</td>
<td align="right">23.6%</td>
<td align="right">16.7%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">562</td>
<td align="left">🟢 Queen</td>
<td align="right"><b>1502</b></td>
<td align="right">24.0%</td>
<td align="right">59.6%</td>
<td align="right">32.3%</td>
<td align="right">16.0%</td>
<td align="right">16.8%</td>
<td align="right">16.9%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">563</td>
<td align="left">🟢 Void_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">25.3%</td>
<td align="right">42.6%</td>
<td align="right">31.0%</td>
<td align="right">30.9%</td>
<td align="right">17.4%</td>
<td align="right">17.6%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">564</td>
<td align="left">🟢 Discharge</td>
<td align="right"><b>1502</b></td>
<td align="right">25.8%</td>
<td align="right">48.8%</td>
<td align="right">37.3%</td>
<td align="right">31.5%</td>
<td align="right">13.9%</td>
<td align="right">18.4%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">565</td>
<td align="left">🟢 Radiation</td>
<td align="right"><b>1502</b></td>
<td align="right">26.4%</td>
<td align="right">48.6%</td>
<td align="right">35.4%</td>
<td align="right">37.1%</td>
<td align="right">16.9%</td>
<td align="right">15.4%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">566</td>
<td align="left">🟢 Eternal</td>
<td align="right"><b>1502</b></td>
<td align="right">25.5%</td>
<td align="right">57.5%</td>
<td align="right">26.2%</td>
<td align="right">28.6%</td>
<td align="right">22.1%</td>
<td align="right">15.6%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">567</td>
<td align="left">🟢 YogSothoth</td>
<td align="right"><b>1502</b></td>
<td align="right">24.6%</td>
<td align="right">40.7%</td>
<td align="right">33.3%</td>
<td align="right">30.2%</td>
<td align="right">25.8%</td>
<td align="right">10.7%</td>
<td align="right">240</td>
</tr>
<tr>
<td align="left">568</td>
<td align="left">🟢 Adder</td>
<td align="right"><b>1502</b></td>
<td align="right">26.8%</td>
<td align="right">54.5%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">23.1%</td>
<td align="right">17.4%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">569</td>
<td align="left">🟢 Sadist_Alt</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">53.3%</td>
<td align="right">32.3%</td>
<td align="right">28.9%</td>
<td align="right">15.6%</td>
<td align="right">18.4%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">570</td>
<td align="left">🟢 Enslaver</td>
<td align="right"><b>1501</b></td>
<td align="right">25.2%</td>
<td align="right">46.2%</td>
<td align="right">28.7%</td>
<td align="right">22.4%</td>
<td align="right">27.6%</td>
<td align="right">13.8%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">571</td>
<td align="left">🟢 Despot</td>
<td align="right"><b>1501</b></td>
<td align="right">25.1%</td>
<td align="right">42.1%</td>
<td align="right">40.3%</td>
<td align="right">33.0%</td>
<td align="right">20.2%</td>
<td align="right">11.9%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">572</td>
<td align="left">🟢 Yesterday</td>
<td align="right"><b>1501</b></td>
<td align="right">23.4%</td>
<td align="right">41.1%</td>
<td align="right">35.6%</td>
<td align="right">22.0%</td>
<td align="right">16.5%</td>
<td align="right">16.2%</td>
<td align="right">462</td>
</tr>
<tr>
<td align="left">573</td>
<td align="left">🟢 Patriarch</td>
<td align="right"><b>1501</b></td>
<td align="right">24.3%</td>
<td align="right">47.5%</td>
<td align="right">29.1%</td>
<td align="right">29.1%</td>
<td align="right">20.9%</td>
<td align="right">14.6%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">574</td>
<td align="left">🟢 Morpher</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">56.5%</td>
<td align="right">36.8%</td>
<td align="right">25.0%</td>
<td align="right">18.3%</td>
<td align="right">15.4%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">575</td>
<td align="left">🟢 DeepOne</td>
<td align="right"><b>1501</b></td>
<td align="right">25.3%</td>
<td align="right">36.0%</td>
<td align="right">31.4%</td>
<td align="right">29.3%</td>
<td align="right">21.4%</td>
<td align="right">19.4%</td>
<td align="right">233</td>
</tr>
<tr>
<td align="left">576</td>
<td align="left">🟢 Emperor</td>
<td align="right"><b>1501</b></td>
<td align="right">24.6%</td>
<td align="right">41.9%</td>
<td align="right">33.3%</td>
<td align="right">27.2%</td>
<td align="right">22.2%</td>
<td align="right">13.8%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">577</td>
<td align="left">🟢 Schizoid_Alt</td>
<td align="right"><b>1501</b></td>
<td align="right">23.9%</td>
<td align="right">37.8%</td>
<td align="right">32.1%</td>
<td align="right">29.7%</td>
<td align="right">18.7%</td>
<td align="right">16.3%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">578</td>
<td align="left">🟢 Cloud</td>
<td align="right"><b>1501</b></td>
<td align="right">24.2%</td>
<td align="right">50.0%</td>
<td align="right">33.8%</td>
<td align="right">26.2%</td>
<td align="right">18.1%</td>
<td align="right">14.3%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">579</td>
<td align="left">🟢 Jammer</td>
<td align="right"><b>1501</b></td>
<td align="right">23.1%</td>
<td align="right">51.1%</td>
<td align="right">25.8%</td>
<td align="right">26.3%</td>
<td align="right">18.8%</td>
<td align="right">13.7%</td>
<td align="right">476</td>
</tr>
<tr>
<td align="left">580</td>
<td align="left">🟢 Harvester</td>
<td align="right"><b>1501</b></td>
<td align="right">23.5%</td>
<td align="right">43.2%</td>
<td align="right">32.7%</td>
<td align="right">27.2%</td>
<td align="right">16.4%</td>
<td align="right">15.9%</td>
<td align="right">408</td>
</tr>
<tr>
<td align="left">581</td>
<td align="left">🟢 Absorber</td>
<td align="right"><b>1501</b></td>
<td align="right">23.8%</td>
<td align="right">47.4%</td>
<td align="right">34.7%</td>
<td align="right">22.9%</td>
<td align="right">20.0%</td>
<td align="right">13.6%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">582</td>
<td align="left">🟢 Collapser</td>
<td align="right"><b>1501</b></td>
<td align="right">26.7%</td>
<td align="right">71.4%</td>
<td align="right">12.5%</td>
<td align="right">43.8%</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
<td align="right">60</td>
</tr>
<tr>
<td align="left">583</td>
<td align="left">🟢 Coach</td>
<td align="right"><b>1501</b></td>
<td align="right">26.7%</td>
<td align="right">100.0%</td>
<td align="right">11.1%</td>
<td align="right">26.7%</td>
<td align="right">33.3%</td>
<td align="right">11.8%</td>
<td align="right">60</td>
</tr>
<tr>
<td align="left">584</td>
<td align="left">🟢 Ghast</td>
<td align="right"><b>1501</b></td>
<td align="right">23.0%</td>
<td align="right">56.0%</td>
<td align="right">34.0%</td>
<td align="right">25.8%</td>
<td align="right">20.1%</td>
<td align="right">15.5%</td>
<td align="right">1843</td>
</tr>
<tr>
<td align="left">585</td>
<td align="left">🟢 Joy</td>
<td align="right"><b>1501</b></td>
<td align="right">25.5%</td>
<td align="right">53.3%</td>
<td align="right">29.9%</td>
<td align="right">23.9%</td>
<td align="right">19.8%</td>
<td align="right">18.2%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">586</td>
<td align="left">🟢 Sphinx</td>
<td align="right"><b>1501</b></td>
<td align="right">25.1%</td>
<td align="right">66.7%</td>
<td align="right">35.2%</td>
<td align="right">31.9%</td>
<td align="right">16.8%</td>
<td align="right">12.5%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">587</td>
<td align="left">🟢 Influence</td>
<td align="right"><b>1501</b></td>
<td align="right">27.5%</td>
<td align="right">51.2%</td>
<td align="right">30.0%</td>
<td align="right">35.5%</td>
<td align="right">19.8%</td>
<td align="right">19.4%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">588</td>
<td align="left">🟢 Hibernator</td>
<td align="right"><b>1501</b></td>
<td align="right">26.9%</td>
<td align="right">64.3%</td>
<td align="right">30.7%</td>
<td align="right">30.1%</td>
<td align="right">19.1%</td>
<td align="right">16.4%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">589</td>
<td align="left">🟢 Gambler</td>
<td align="right"><b>1501</b></td>
<td align="right">22.5%</td>
<td align="right">37.8%</td>
<td align="right">32.5%</td>
<td align="right">23.6%</td>
<td align="right">20.7%</td>
<td align="right">17.3%</td>
<td align="right">2593</td>
</tr>
<tr>
<td align="left">590</td>
<td align="left">🟢 Armor</td>
<td align="right"><b>1501</b></td>
<td align="right">24.9%</td>
<td align="right">51.2%</td>
<td align="right">36.5%</td>
<td align="right">24.7%</td>
<td align="right">22.2%</td>
<td align="right">15.1%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">591</td>
<td align="left">🟢 BleedingHeart</td>
<td align="right"><b>1501</b></td>
<td align="right">23.3%</td>
<td align="right">45.2%</td>
<td align="right">30.5%</td>
<td align="right">25.8%</td>
<td align="right">20.3%</td>
<td align="right">15.9%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">592</td>
<td align="left">🟢 Xenophile</td>
<td align="right"><b>1501</b></td>
<td align="right">24.9%</td>
<td align="right">47.5%</td>
<td align="right">39.7%</td>
<td align="right">24.7%</td>
<td align="right">18.3%</td>
<td align="right">15.0%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">593</td>
<td align="left">🟢 Spokesman</td>
<td align="right"><b>1501</b></td>
<td align="right">25.5%</td>
<td align="right">50.0%</td>
<td align="right">32.4%</td>
<td align="right">22.0%</td>
<td align="right">21.0%</td>
<td align="right">19.8%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">594</td>
<td align="left">🟢 Poltergeist</td>
<td align="right"><b>1501</b></td>
<td align="right">25.6%</td>
<td align="right">51.4%</td>
<td align="right">35.9%</td>
<td align="right">25.9%</td>
<td align="right">19.3%</td>
<td align="right">18.5%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">595</td>
<td align="left">🟢 Mesmer</td>
<td align="right"><b>1501</b></td>
<td align="right">25.8%</td>
<td align="right">42.1%</td>
<td align="right">40.8%</td>
<td align="right">28.9%</td>
<td align="right">25.0%</td>
<td align="right">12.2%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">596</td>
<td align="left">🟢 Dasher</td>
<td align="right"><b>1501</b></td>
<td align="right">24.1%</td>
<td align="right">50.0%</td>
<td align="right">35.6%</td>
<td align="right">19.8%</td>
<td align="right">22.5%</td>
<td align="right">16.3%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">597</td>
<td align="left">🟢 Kamikaze</td>
<td align="right"><b>1501</b></td>
<td align="right">23.1%</td>
<td align="right">51.3%</td>
<td align="right">31.7%</td>
<td align="right">24.7%</td>
<td align="right">18.0%</td>
<td align="right">12.3%</td>
<td align="right">412</td>
</tr>
<tr>
<td align="left">598</td>
<td align="left">🟢 Nexus</td>
<td align="right"><b>1501</b></td>
<td align="right">22.1%</td>
<td align="right">41.5%</td>
<td align="right">34.6%</td>
<td align="right">22.1%</td>
<td align="right">14.9%</td>
<td align="right">17.7%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">599</td>
<td align="left">🟢 Prestidigitator</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">40.6%</td>
<td align="right">33.9%</td>
<td align="right">24.5%</td>
<td align="right">22.0%</td>
<td align="right">15.2%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">600</td>
<td align="left">🟢 Hail</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">41.7%</td>
<td align="right">45.6%</td>
<td align="right">24.3%</td>
<td align="right">20.9%</td>
<td align="right">15.7%</td>
<td align="right">385</td>
</tr>
<tr>
<td align="left">601</td>
<td align="left">🟢 Twister</td>
<td align="right"><b>1501</b></td>
<td align="right">23.9%</td>
<td align="right">47.5%</td>
<td align="right">42.9%</td>
<td align="right">28.7%</td>
<td align="right">19.8%</td>
<td align="right">8.6%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">602</td>
<td align="left">🟢 Cactus</td>
<td align="right"><b>1501</b></td>
<td align="right">26.3%</td>
<td align="right">50.0%</td>
<td align="right">46.7%</td>
<td align="right">31.2%</td>
<td align="right">25.0%</td>
<td align="right">4.3%</td>
<td align="right">76</td>
</tr>
<tr>
<td align="left">603</td>
<td align="left">🟢 Sunset</td>
<td align="right"><b>1501</b></td>
<td align="right">24.5%</td>
<td align="right">53.1%</td>
<td align="right">23.0%</td>
<td align="right">29.8%</td>
<td align="right">19.0%</td>
<td align="right">19.2%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">604</td>
<td align="left">🟢 Titanium</td>
<td align="right"><b>1501</b></td>
<td align="right">26.2%</td>
<td align="right">75.0%</td>
<td align="right">42.9%</td>
<td align="right">13.3%</td>
<td align="right">21.7%</td>
<td align="right">8.7%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">605</td>
<td align="left">🟢 Pyromancer</td>
<td align="right"><b>1501</b></td>
<td align="right">23.6%</td>
<td align="right">50.0%</td>
<td align="right">29.2%</td>
<td align="right">26.4%</td>
<td align="right">16.7%</td>
<td align="right">16.5%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">606</td>
<td align="left">🟢 Geneticist</td>
<td align="right"><b>1501</b></td>
<td align="right">26.2%</td>
<td align="right">33.3%</td>
<td align="right">41.7%</td>
<td align="right">20.0%</td>
<td align="right">23.5%</td>
<td align="right">21.1%</td>
<td align="right">61</td>
</tr>
<tr>
<td align="left">607</td>
<td align="left">🟢 Ravager</td>
<td align="right"><b>1501</b></td>
<td align="right">23.0%</td>
<td align="right">53.8%</td>
<td align="right">39.1%</td>
<td align="right">18.6%</td>
<td align="right">14.1%</td>
<td align="right">15.4%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">608</td>
<td align="left">🟢 Neutrino</td>
<td align="right"><b>1501</b></td>
<td align="right">24.2%</td>
<td align="right">55.8%</td>
<td align="right">33.3%</td>
<td align="right">17.0%</td>
<td align="right">21.6%</td>
<td align="right">16.9%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">609</td>
<td align="left">🟢 Tidal</td>
<td align="right"><b>1501</b></td>
<td align="right">26.2%</td>
<td align="right">66.7%</td>
<td align="right">38.9%</td>
<td align="right">25.0%</td>
<td align="right">13.6%</td>
<td align="right">21.2%</td>
<td align="right">103</td>
</tr>
<tr>
<td align="left">610</td>
<td align="left">🟢 Subtractor</td>
<td align="right"><b>1501</b></td>
<td align="right">26.2%</td>
<td align="right">25.0%</td>
<td align="right">28.6%</td>
<td align="right">36.4%</td>
<td align="right">35.7%</td>
<td align="right">13.6%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">611</td>
<td align="left">🟢 Random</td>
<td align="right"><b>1501</b></td>
<td align="right">26.6%</td>
<td align="right">52.0%</td>
<td align="right">34.8%</td>
<td align="right">36.3%</td>
<td align="right">20.8%</td>
<td align="right">12.6%</td>
<td align="right">478</td>
</tr>
<tr>
<td align="left">612</td>
<td align="left">🟢 Herbivore</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">63.2%</td>
<td align="right">53.3%</td>
<td align="right">26.8%</td>
<td align="right">13.6%</td>
<td align="right">13.8%</td>
<td align="right">244</td>
</tr>
<tr>
<td align="left">613</td>
<td align="left">🟢 Pianist</td>
<td align="right"><b>1501</b></td>
<td align="right">24.2%</td>
<td align="right">47.2%</td>
<td align="right">30.4%</td>
<td align="right">26.6%</td>
<td align="right">23.3%</td>
<td align="right">15.1%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">614</td>
<td align="left">🟢 Sleet</td>
<td align="right"><b>1501</b></td>
<td align="right">26.1%</td>
<td align="right">28.6%</td>
<td align="right">62.5%</td>
<td align="right">31.2%</td>
<td align="right">23.5%</td>
<td align="right">9.5%</td>
<td align="right">69</td>
</tr>
<tr>
<td align="left">615</td>
<td align="left">🟢 Rookie</td>
<td align="right"><b>1501</b></td>
<td align="right">26.1%</td>
<td align="right">22.2%</td>
<td align="right">43.8%</td>
<td align="right">20.0%</td>
<td align="right">26.7%</td>
<td align="right">15.8%</td>
<td align="right">69</td>
</tr>
<tr>
<td align="left">616</td>
<td align="left">🟢 Beacon</td>
<td align="right"><b>1501</b></td>
<td align="right">25.3%</td>
<td align="right">47.5%</td>
<td align="right">29.0%</td>
<td align="right">22.9%</td>
<td align="right">28.3%</td>
<td align="right">17.0%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">617</td>
<td align="left">🟢 Authority</td>
<td align="right"><b>1501</b></td>
<td align="right">22.9%</td>
<td align="right">30.8%</td>
<td align="right">36.7%</td>
<td align="right">28.2%</td>
<td align="right">20.6%</td>
<td align="right">13.6%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">618</td>
<td align="left">🟢 Hexcaster</td>
<td align="right"><b>1501</b></td>
<td align="right">24.9%</td>
<td align="right">31.8%</td>
<td align="right">41.5%</td>
<td align="right">28.0%</td>
<td align="right">22.2%</td>
<td align="right">15.1%</td>
<td align="right">474</td>
</tr>
<tr>
<td align="left">619</td>
<td align="left">🟢 Puller</td>
<td align="right"><b>1501</b></td>
<td align="right">26.0%</td>
<td align="right">50.0%</td>
<td align="right">42.9%</td>
<td align="right">20.0%</td>
<td align="right">10.0%</td>
<td align="right">30.0%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">620</td>
<td align="left">🟢 Heretic</td>
<td align="right"><b>1501</b></td>
<td align="right">25.5%</td>
<td align="right">55.8%</td>
<td align="right">30.8%</td>
<td align="right">20.7%</td>
<td align="right">23.6%</td>
<td align="right">16.4%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">621</td>
<td align="left">🟢 Battlemaster</td>
<td align="right"><b>1501</b></td>
<td align="right">24.6%</td>
<td align="right">51.0%</td>
<td align="right">38.9%</td>
<td align="right">27.7%</td>
<td align="right">19.9%</td>
<td align="right">16.6%</td>
<td align="right">1780</td>
</tr>
<tr>
<td align="left">622</td>
<td align="left">🟢 Demon</td>
<td align="right"><b>1501</b></td>
<td align="right">24.5%</td>
<td align="right">43.6%</td>
<td align="right">39.0%</td>
<td align="right">22.0%</td>
<td align="right">17.4%</td>
<td align="right">20.3%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">623</td>
<td align="left">🟢 Magnate</td>
<td align="right"><b>1501</b></td>
<td align="right">24.8%</td>
<td align="right">39.6%</td>
<td align="right">37.1%</td>
<td align="right">23.7%</td>
<td align="right">22.0%</td>
<td align="right">17.3%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">624</td>
<td align="left">🟢 Forecaster</td>
<td align="right"><b>1501</b></td>
<td align="right">24.7%</td>
<td align="right">55.8%</td>
<td align="right">36.5%</td>
<td align="right">26.5%</td>
<td align="right">18.5%</td>
<td align="right">12.2%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">625</td>
<td align="left">🟢 Spectrum</td>
<td align="right"><b>1501</b></td>
<td align="right">24.7%</td>
<td align="right">48.7%</td>
<td align="right">36.2%</td>
<td align="right">30.8%</td>
<td align="right">20.3%</td>
<td align="right">12.6%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">626</td>
<td align="left">🟢 Ghostly</td>
<td align="right"><b>1501</b></td>
<td align="right">24.2%</td>
<td align="right">52.2%</td>
<td align="right">26.3%</td>
<td align="right">24.0%</td>
<td align="right">24.0%</td>
<td align="right">12.8%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">627</td>
<td align="left">🟢 Tempest</td>
<td align="right"><b>1501</b></td>
<td align="right">24.8%</td>
<td align="right">51.2%</td>
<td align="right">34.2%</td>
<td align="right">29.1%</td>
<td align="right">18.3%</td>
<td align="right">14.6%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">628</td>
<td align="left">🟢 Void</td>
<td align="right"><b>1501</b></td>
<td align="right">22.4%</td>
<td align="right">38.9%</td>
<td align="right">34.6%</td>
<td align="right">23.6%</td>
<td align="right">18.8%</td>
<td align="right">17.9%</td>
<td align="right">2550</td>
</tr>
<tr>
<td align="left">629</td>
<td align="left">🟢 Envy</td>
<td align="right"><b>1501</b></td>
<td align="right">25.6%</td>
<td align="right">63.6%</td>
<td align="right">32.8%</td>
<td align="right">28.3%</td>
<td align="right">15.0%</td>
<td align="right">16.5%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">630</td>
<td align="left">🟢 Hope</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">47.1%</td>
<td align="right">32.3%</td>
<td align="right">23.2%</td>
<td align="right">19.7%</td>
<td align="right">18.4%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">631</td>
<td align="left">🟢 Entropy</td>
<td align="right"><b>1501</b></td>
<td align="right">25.5%</td>
<td align="right">52.8%</td>
<td align="right">43.3%</td>
<td align="right">21.1%</td>
<td align="right">20.5%</td>
<td align="right">16.8%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">632</td>
<td align="left">🟢 Hurtz</td>
<td align="right"><b>1501</b></td>
<td align="right">25.1%</td>
<td align="right">44.2%</td>
<td align="right">39.7%</td>
<td align="right">22.1%</td>
<td align="right">18.9%</td>
<td align="right">17.6%</td>
<td align="right">471</td>
</tr>
<tr>
<td align="left">633</td>
<td align="left">🟢 Grumpus</td>
<td align="right"><b>1501</b></td>
<td align="right">23.5%</td>
<td align="right">42.0%</td>
<td align="right">30.8%</td>
<td align="right">17.2%</td>
<td align="right">15.4%</td>
<td align="right">23.9%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">634</td>
<td align="left">🟢 Wasp</td>
<td align="right"><b>1501</b></td>
<td align="right">25.8%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">28.6%</td>
<td align="right">26.1%</td>
<td align="right">8.3%</td>
<td align="right">62</td>
</tr>
<tr>
<td align="left">635</td>
<td align="left">🟢 Bluffer</td>
<td align="right"><b>1501</b></td>
<td align="right">22.6%</td>
<td align="right">47.5%</td>
<td align="right">19.4%</td>
<td align="right">24.7%</td>
<td align="right">17.1%</td>
<td align="right">20.0%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">636</td>
<td align="left">🟢 Deceiver</td>
<td align="right"><b>1501</b></td>
<td align="right">25.6%</td>
<td align="right">55.1%</td>
<td align="right">26.7%</td>
<td align="right">24.7%</td>
<td align="right">22.0%</td>
<td align="right">17.7%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">637</td>
<td align="left">🟢 Tunneler</td>
<td align="right"><b>1501</b></td>
<td align="right">25.8%</td>
<td align="right">22.2%</td>
<td align="right">50.0%</td>
<td align="right">21.4%</td>
<td align="right">25.0%</td>
<td align="right">15.4%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">638</td>
<td align="left">🟢 Nostalgic</td>
<td align="right"><b>1501</b></td>
<td align="right">25.8%</td>
<td align="right">25.0%</td>
<td align="right">30.0%</td>
<td align="right">25.0%</td>
<td align="right">36.8%</td>
<td align="right">11.8%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">639</td>
<td align="left">🟢 Specter</td>
<td align="right"><b>1501</b></td>
<td align="right">26.4%</td>
<td align="right">60.0%</td>
<td align="right">30.5%</td>
<td align="right">29.9%</td>
<td align="right">10.8%</td>
<td align="right">18.8%</td>
<td align="right">417</td>
</tr>
<tr>
<td align="left">640</td>
<td align="left">🟢 Tangler</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">48.9%</td>
<td align="right">28.6%</td>
<td align="right">20.2%</td>
<td align="right">22.2%</td>
<td align="right">17.3%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">641</td>
<td align="left">🟢 Ripple</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">42.3%</td>
<td align="right">43.9%</td>
<td align="right">29.5%</td>
<td align="right">21.4%</td>
<td align="right">16.2%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">642</td>
<td align="left">🟢 Settler_Alt</td>
<td align="right"><b>1501</b></td>
<td align="right">23.9%</td>
<td align="right">39.3%</td>
<td align="right">35.4%</td>
<td align="right">31.0%</td>
<td align="right">21.4%</td>
<td align="right">14.0%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">643</td>
<td align="left">🟢 Whisper</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
<td align="right">35.7%</td>
<td align="right">29.4%</td>
<td align="right">4.3%</td>
<td align="right">70</td>
</tr>
<tr>
<td align="left">644</td>
<td align="left">🟢 Squire</td>
<td align="right"><b>1501</b></td>
<td align="right">23.6%</td>
<td align="right">47.8%</td>
<td align="right">28.3%</td>
<td align="right">22.7%</td>
<td align="right">19.2%</td>
<td align="right">16.7%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">645</td>
<td align="left">🟢 Hourglass</td>
<td align="right"><b>1501</b></td>
<td align="right">25.6%</td>
<td align="right">46.9%</td>
<td align="right">37.1%</td>
<td align="right">18.0%</td>
<td align="right">26.3%</td>
<td align="right">15.1%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">646</td>
<td align="left">🟢 Weightlifter</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">20.0%</td>
<td align="right">37.5%</td>
<td align="right">18.2%</td>
<td align="right">27.6%</td>
<td align="right">23.8%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">647</td>
<td align="left">🟢 Recycler</td>
<td align="right"><b>1501</b></td>
<td align="right">25.2%</td>
<td align="right">57.1%</td>
<td align="right">31.1%</td>
<td align="right">28.1%</td>
<td align="right">18.8%</td>
<td align="right">15.6%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">648</td>
<td align="left">🟢 Evoker</td>
<td align="right"><b>1501</b></td>
<td align="right">25.6%</td>
<td align="right">44.4%</td>
<td align="right">33.3%</td>
<td align="right">14.3%</td>
<td align="right">22.7%</td>
<td align="right">23.8%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">649</td>
<td align="left">🟢 Rainbow</td>
<td align="right"><b>1501</b></td>
<td align="right">24.7%</td>
<td align="right">51.2%</td>
<td align="right">30.8%</td>
<td align="right">21.9%</td>
<td align="right">22.4%</td>
<td align="right">17.0%</td>
<td align="right">474</td>
</tr>
<tr>
<td align="left">650</td>
<td align="left">🟢 Peacekeeper</td>
<td align="right"><b>1501</b></td>
<td align="right">24.9%</td>
<td align="right">39.1%</td>
<td align="right">39.4%</td>
<td align="right">25.3%</td>
<td align="right">21.2%</td>
<td align="right">15.0%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">651</td>
<td align="left">🟢 Coward</td>
<td align="right"><b>1501</b></td>
<td align="right">23.7%</td>
<td align="right">45.9%</td>
<td align="right">29.9%</td>
<td align="right">15.5%</td>
<td align="right">26.2%</td>
<td align="right">17.7%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">652</td>
<td align="left">🟢 Reader</td>
<td align="right"><b>1501</b></td>
<td align="right">23.2%</td>
<td align="right">54.0%</td>
<td align="right">27.5%</td>
<td align="right">13.5%</td>
<td align="right">22.8%</td>
<td align="right">16.2%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">653</td>
<td align="left">🟢 Stone</td>
<td align="right"><b>1501</b></td>
<td align="right">25.0%</td>
<td align="right">42.5%</td>
<td align="right">33.8%</td>
<td align="right">24.4%</td>
<td align="right">26.6%</td>
<td align="right">12.7%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">654</td>
<td align="left">🟢 Compeller</td>
<td align="right"><b>1501</b></td>
<td align="right">23.6%</td>
<td align="right">43.6%</td>
<td align="right">32.1%</td>
<td align="right">23.5%</td>
<td align="right">22.6%</td>
<td align="right">15.2%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">655</td>
<td align="left">🟢 Obscurer</td>
<td align="right"><b>1501</b></td>
<td align="right">25.2%</td>
<td align="right">40.4%</td>
<td align="right">28.8%</td>
<td align="right">31.8%</td>
<td align="right">16.7%</td>
<td align="right">19.8%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">656</td>
<td align="left">🟢 Haunt</td>
<td align="right"><b>1501</b></td>
<td align="right">24.6%</td>
<td align="right">52.1%</td>
<td align="right">35.5%</td>
<td align="right">17.8%</td>
<td align="right">18.0%</td>
<td align="right">20.0%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">657</td>
<td align="left">🟢 Mercenary</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">48.0%</td>
<td align="right">29.9%</td>
<td align="right">32.2%</td>
<td align="right">17.9%</td>
<td align="right">17.8%</td>
<td align="right">476</td>
</tr>
<tr>
<td align="left">658</td>
<td align="left">🟢 Brute_Alt</td>
<td align="right"><b>1501</b></td>
<td align="right">22.8%</td>
<td align="right">59.5%</td>
<td align="right">30.0%</td>
<td align="right">12.5%</td>
<td align="right">18.5%</td>
<td align="right">19.1%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">659</td>
<td align="left">🟢 Deflect</td>
<td align="right"><b>1501</b></td>
<td align="right">24.6%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">23.2%</td>
<td align="right">21.2%</td>
<td align="right">13.7%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">660</td>
<td align="left">🟢 Maven</td>
<td align="right"><b>1501</b></td>
<td align="right">24.8%</td>
<td align="right">56.5%</td>
<td align="right">32.3%</td>
<td align="right">21.1%</td>
<td align="right">20.8%</td>
<td align="right">15.0%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">661</td>
<td align="left">🟢 Oligarch</td>
<td align="right"><b>1501</b></td>
<td align="right">24.4%</td>
<td align="right">43.2%</td>
<td align="right">37.3%</td>
<td align="right">24.4%</td>
<td align="right">17.1%</td>
<td align="right">19.6%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">662</td>
<td align="left">🟢 Pouncer</td>
<td align="right"><b>1501</b></td>
<td align="right">25.9%</td>
<td align="right">47.1%</td>
<td align="right">44.3%</td>
<td align="right">27.9%</td>
<td align="right">14.8%</td>
<td align="right">20.7%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">663</td>
<td align="left">🟢 Ruler_Alt</td>
<td align="right"><b>1501</b></td>
<td align="right">23.1%</td>
<td align="right">60.5%</td>
<td align="right">25.0%</td>
<td align="right">30.9%</td>
<td align="right">13.0%</td>
<td align="right">13.6%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">664</td>
<td align="left">🟢 Buffer</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">52.6%</td>
<td align="right">36.7%</td>
<td align="right">23.7%</td>
<td align="right">20.0%</td>
<td align="right">18.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">665</td>
<td align="left">🟢 Grasshopper</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">60.0%</td>
<td align="right">21.4%</td>
<td align="right">33.3%</td>
<td align="right">6.2%</td>
<td align="right">22.2%</td>
<td align="right">67</td>
</tr>
<tr>
<td align="left">666</td>
<td align="left">🟢 Smoke</td>
<td align="right"><b>1501</b></td>
<td align="right">25.5%</td>
<td align="right">51.0%</td>
<td align="right">20.0%</td>
<td align="right">27.5%</td>
<td align="right">27.8%</td>
<td align="right">15.4%</td>
<td align="right">462</td>
</tr>
<tr>
<td align="left">667</td>
<td align="left">🟢 Phantom_Alt</td>
<td align="right"><b>1501</b></td>
<td align="right">23.9%</td>
<td align="right">52.4%</td>
<td align="right">34.4%</td>
<td align="right">26.5%</td>
<td align="right">18.3%</td>
<td align="right">12.8%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">668</td>
<td align="left">🟢 Jackpot</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">60.0%</td>
<td align="right">33.3%</td>
<td align="right">27.3%</td>
<td align="right">5.6%</td>
<td align="right">21.7%</td>
<td align="right">71</td>
</tr>
<tr>
<td align="left">669</td>
<td align="left">🟢 Bluffer_Alt</td>
<td align="right"><b>1501</b></td>
<td align="right">25.4%</td>
<td align="right">40.0%</td>
<td align="right">36.4%</td>
<td align="right">23.1%</td>
<td align="right">35.7%</td>
<td align="right">14.3%</td>
<td align="right">71</td>
</tr>
<tr>
<td align="left">670</td>
<td align="left">🟢 Eradicator</td>
<td align="right"><b>1501</b></td>
<td align="right">26.1%</td>
<td align="right">55.8%</td>
<td align="right">31.6%</td>
<td align="right">27.8%</td>
<td align="right">20.8%</td>
<td align="right">16.1%</td>
<td align="right">403</td>
</tr>
<tr>
<td align="left">671</td>
<td align="left">🟢 Dynamo</td>
<td align="right"><b>1501</b></td>
<td align="right">26.6%</td>
<td align="right">59.1%</td>
<td align="right">34.4%</td>
<td align="right">23.3%</td>
<td align="right">16.4%</td>
<td align="right">21.6%</td>
<td align="right">394</td>
</tr>
<tr>
<td align="left">672</td>
<td align="left">🟢 Projector</td>
<td align="right"><b>1501</b></td>
<td align="right">25.3%</td>
<td align="right">46.8%</td>
<td align="right">40.0%</td>
<td align="right">27.3%</td>
<td align="right">18.2%</td>
<td align="right">14.0%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">673</td>
<td align="left">🟢 Composer</td>
<td align="right"><b>1501</b></td>
<td align="right">25.2%</td>
<td align="right">44.7%</td>
<td align="right">36.7%</td>
<td align="right">30.4%</td>
<td align="right">22.0%</td>
<td align="right">12.4%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">674</td>
<td align="left">🟢 Mage</td>
<td align="right"><b>1501</b></td>
<td align="right">25.3%</td>
<td align="right">50.0%</td>
<td align="right">31.2%</td>
<td align="right">20.0%</td>
<td align="right">21.1%</td>
<td align="right">19.0%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">675</td>
<td align="left">🟢 Veteran</td>
<td align="right"><b>1501</b></td>
<td align="right">24.6%</td>
<td align="right">52.3%</td>
<td align="right">32.8%</td>
<td align="right">27.4%</td>
<td align="right">18.7%</td>
<td align="right">15.0%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">676</td>
<td align="left">🟢 Grief</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">43.5%</td>
<td align="right">36.2%</td>
<td align="right">28.1%</td>
<td align="right">20.9%</td>
<td align="right">15.9%</td>
<td align="right">1812</td>
</tr>
<tr>
<td align="left">677</td>
<td align="left">🟢 Wind_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">26.4%</td>
<td align="right">51.0%</td>
<td align="right">26.9%</td>
<td align="right">24.4%</td>
<td align="right">25.0%</td>
<td align="right">18.8%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">678</td>
<td align="left">🟢 Charmer</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">38.8%</td>
<td align="right">46.2%</td>
<td align="right">24.7%</td>
<td align="right">21.3%</td>
<td align="right">10.2%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">679</td>
<td align="left">🟢 Stopper</td>
<td align="right"><b>1500</b></td>
<td align="right">25.2%</td>
<td align="right">56.4%</td>
<td align="right">33.9%</td>
<td align="right">25.8%</td>
<td align="right">21.6%</td>
<td align="right">12.0%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">680</td>
<td align="left">🟢 Infiltrate</td>
<td align="right"><b>1500</b></td>
<td align="right">24.2%</td>
<td align="right">52.2%</td>
<td align="right">32.8%</td>
<td align="right">32.1%</td>
<td align="right">18.2%</td>
<td align="right">11.6%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">681</td>
<td align="left">🟢 Occupier</td>
<td align="right"><b>1500</b></td>
<td align="right">26.8%</td>
<td align="right">50.0%</td>
<td align="right">48.5%</td>
<td align="right">25.0%</td>
<td align="right">21.1%</td>
<td align="right">13.5%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">682</td>
<td align="left">🟢 Announcer</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">45.9%</td>
<td align="right">32.0%</td>
<td align="right">39.5%</td>
<td align="right">12.1%</td>
<td align="right">18.3%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">683</td>
<td align="left">🟢 Parallax</td>
<td align="right"><b>1500</b></td>
<td align="right">26.2%</td>
<td align="right">66.0%</td>
<td align="right">45.8%</td>
<td align="right">14.8%</td>
<td align="right">15.1%</td>
<td align="right">19.3%</td>
<td align="right">469</td>
</tr>
<tr>
<td align="left">684</td>
<td align="left">🟢 Scrambler</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">44.4%</td>
<td align="right">35.4%</td>
<td align="right">23.5%</td>
<td align="right">21.7%</td>
<td align="right">14.3%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">685</td>
<td align="left">🟢 Delegator</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">50.0%</td>
<td align="right">36.6%</td>
<td align="right">25.5%</td>
<td align="right">21.2%</td>
<td align="right">16.0%</td>
<td align="right">1816</td>
</tr>
<tr>
<td align="left">686</td>
<td align="left">🟢 Abyss</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">53.7%</td>
<td align="right">28.8%</td>
<td align="right">29.7%</td>
<td align="right">16.4%</td>
<td align="right">19.5%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">687</td>
<td align="left">🟢 Starvation</td>
<td align="right"><b>1500</b></td>
<td align="right">23.1%</td>
<td align="right">35.7%</td>
<td align="right">26.5%</td>
<td align="right">23.2%</td>
<td align="right">21.3%</td>
<td align="right">16.9%</td>
<td align="right">238</td>
</tr>
<tr>
<td align="left">688</td>
<td align="left">🟢 Cultivator</td>
<td align="right"><b>1500</b></td>
<td align="right">25.6%</td>
<td align="right">45.0%</td>
<td align="right">38.2%</td>
<td align="right">20.2%</td>
<td align="right">25.2%</td>
<td align="right">17.9%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">689</td>
<td align="left">🟢 Mosquito</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">60.0%</td>
<td align="right">22.2%</td>
<td align="right">23.1%</td>
<td align="right">15.4%</td>
<td align="right">15.8%</td>
<td align="right">64</td>
</tr>
<tr>
<td align="left">690</td>
<td align="left">🟢 Flower</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">18.2%</td>
<td align="right">37.5%</td>
<td align="right">22.2%</td>
<td align="right">20.0%</td>
<td align="right">76</td>
</tr>
<tr>
<td align="left">691</td>
<td align="left">🟢 Captain_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">66.7%</td>
<td align="right">54.5%</td>
<td align="right">18.2%</td>
<td align="right">8.7%</td>
<td align="right">19.0%</td>
<td align="right">72</td>
</tr>
<tr>
<td align="left">692</td>
<td align="left">🟢 Seed</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">70.0%</td>
<td align="right">28.6%</td>
<td align="right">23.5%</td>
<td align="right">19.2%</td>
<td align="right">14.3%</td>
<td align="right">88</td>
</tr>
<tr>
<td align="left">693</td>
<td align="left">🟢 Wolf</td>
<td align="right"><b>1500</b></td>
<td align="right">25.6%</td>
<td align="right">58.3%</td>
<td align="right">31.6%</td>
<td align="right">26.6%</td>
<td align="right">21.8%</td>
<td align="right">17.4%</td>
<td align="right">477</td>
</tr>
<tr>
<td align="left">694</td>
<td align="left">🟢 Amoeba</td>
<td align="right"><b>1500</b></td>
<td align="right">22.2%</td>
<td align="right">35.1%</td>
<td align="right">36.2%</td>
<td align="right">25.1%</td>
<td align="right">19.3%</td>
<td align="right">15.1%</td>
<td align="right">2486</td>
</tr>
<tr>
<td align="left">695</td>
<td align="left">🟢 Love</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">47.1%</td>
<td align="right">42.6%</td>
<td align="right">25.6%</td>
<td align="right">16.8%</td>
<td align="right">16.0%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">696</td>
<td align="left">🟢 Meteor_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">24.9%</td>
<td align="right">37.8%</td>
<td align="right">28.6%</td>
<td align="right">33.7%</td>
<td align="right">26.9%</td>
<td align="right">11.8%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">697</td>
<td align="left">🟢 Hoaxer</td>
<td align="right"><b>1500</b></td>
<td align="right">23.4%</td>
<td align="right">53.8%</td>
<td align="right">31.0%</td>
<td align="right">24.0%</td>
<td align="right">20.6%</td>
<td align="right">12.1%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">698</td>
<td align="left">🟢 Terminal</td>
<td align="right"><b>1500</b></td>
<td align="right">23.4%</td>
<td align="right">41.0%</td>
<td align="right">33.9%</td>
<td align="right">21.1%</td>
<td align="right">24.0%</td>
<td align="right">14.7%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">699</td>
<td align="left">🟢 Judge</td>
<td align="right"><b>1500</b></td>
<td align="right">26.8%</td>
<td align="right">45.2%</td>
<td align="right">33.9%</td>
<td align="right">33.3%</td>
<td align="right">24.7%</td>
<td align="right">16.6%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">700</td>
<td align="left">🟢 Peddler</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">45.1%</td>
<td align="right">33.3%</td>
<td align="right">20.8%</td>
<td align="right">20.7%</td>
<td align="right">18.4%</td>
<td align="right">507</td>
</tr>
<tr>
<td align="left">701</td>
<td align="left">🟢 Erosion</td>
<td align="right"><b>1500</b></td>
<td align="right">26.8%</td>
<td align="right">67.5%</td>
<td align="right">31.6%</td>
<td align="right">30.7%</td>
<td align="right">17.8%</td>
<td align="right">18.2%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">702</td>
<td align="left">🟢 Cosmos</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">54.1%</td>
<td align="right">29.6%</td>
<td align="right">20.2%</td>
<td align="right">20.7%</td>
<td align="right">16.5%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">703</td>
<td align="left">🟢 Outlaw</td>
<td align="right"><b>1500</b></td>
<td align="right">24.3%</td>
<td align="right">49.0%</td>
<td align="right">36.8%</td>
<td align="right">28.0%</td>
<td align="right">16.4%</td>
<td align="right">14.4%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">704</td>
<td align="left">🟢 Mirror_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">53.7%</td>
<td align="right">38.5%</td>
<td align="right">19.0%</td>
<td align="right">18.9%</td>
<td align="right">14.9%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">705</td>
<td align="left">🟢 Permafrost</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">54.8%</td>
<td align="right">38.6%</td>
<td align="right">27.6%</td>
<td align="right">14.2%</td>
<td align="right">14.3%</td>
<td align="right">465</td>
</tr>
<tr>
<td align="left">706</td>
<td align="left">🟢 Bear</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">65.6%</td>
<td align="right">37.1%</td>
<td align="right">20.0%</td>
<td align="right">18.3%</td>
<td align="right">19.0%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">707</td>
<td align="left">🟢 Squadron</td>
<td align="right"><b>1500</b></td>
<td align="right">24.3%</td>
<td align="right">54.5%</td>
<td align="right">27.1%</td>
<td align="right">25.0%</td>
<td align="right">17.0%</td>
<td align="right">15.7%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">708</td>
<td align="left">🟢 Oracle</td>
<td align="right"><b>1500</b></td>
<td align="right">22.4%</td>
<td align="right">56.1%</td>
<td align="right">36.9%</td>
<td align="right">23.0%</td>
<td align="right">19.1%</td>
<td align="right">15.7%</td>
<td align="right">2549</td>
</tr>
<tr>
<td align="left">709</td>
<td align="left">🟢 Oppressor</td>
<td align="right"><b>1500</b></td>
<td align="right">23.1%</td>
<td align="right">43.4%</td>
<td align="right">32.4%</td>
<td align="right">25.6%</td>
<td align="right">19.0%</td>
<td align="right">11.1%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">710</td>
<td align="left">🟢 Moss</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">62.5%</td>
<td align="right">36.4%</td>
<td align="right">13.6%</td>
<td align="right">22.7%</td>
<td align="right">18.2%</td>
<td align="right">85</td>
</tr>
<tr>
<td align="left">711</td>
<td align="left">🟢 Dew</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">57.1%</td>
<td align="right">36.8%</td>
<td align="right">27.3%</td>
<td align="right">12.0%</td>
<td align="right">17.4%</td>
<td align="right">85</td>
</tr>
<tr>
<td align="left">712</td>
<td align="left">🟢 Collector_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">24.2%</td>
<td align="right">48.9%</td>
<td align="right">32.3%</td>
<td align="right">26.4%</td>
<td align="right">19.2%</td>
<td align="right">15.2%</td>
<td align="right">479</td>
</tr>
<tr>
<td align="left">713</td>
<td align="left">🟢 Bandit</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">42.9%</td>
<td align="right">29.6%</td>
<td align="right">25.6%</td>
<td align="right">22.0%</td>
<td align="right">17.6%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">714</td>
<td align="left">🟢 Gymnast</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">30.0%</td>
<td align="right">15.8%</td>
<td align="right">22.2%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">715</td>
<td align="left">🟢 Fury</td>
<td align="right"><b>1500</b></td>
<td align="right">21.8%</td>
<td align="right">46.3%</td>
<td align="right">30.6%</td>
<td align="right">26.6%</td>
<td align="right">17.9%</td>
<td align="right">16.2%</td>
<td align="right">2588</td>
</tr>
<tr>
<td align="left">716</td>
<td align="left">🟢 Fated</td>
<td align="right"><b>1500</b></td>
<td align="right">25.1%</td>
<td align="right">48.1%</td>
<td align="right">28.3%</td>
<td align="right">29.0%</td>
<td align="right">20.2%</td>
<td align="right">17.3%</td>
<td align="right">479</td>
</tr>
<tr>
<td align="left">717</td>
<td align="left">🟢 Channeler</td>
<td align="right"><b>1500</b></td>
<td align="right">24.0%</td>
<td align="right">52.5%</td>
<td align="right">30.9%</td>
<td align="right">32.1%</td>
<td align="right">12.2%</td>
<td align="right">14.8%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">718</td>
<td align="left">🟢 Goalie</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">42.9%</td>
<td align="right">27.3%</td>
<td align="right">25.0%</td>
<td align="right">16.7%</td>
<td align="right">23.8%</td>
<td align="right">69</td>
</tr>
<tr>
<td align="left">719</td>
<td align="left">🟢 Illusioner</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">54.5%</td>
<td align="right">33.3%</td>
<td align="right">46.7%</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
<td align="right">69</td>
</tr>
<tr>
<td align="left">720</td>
<td align="left">🟢 Wrestler</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">80.0%</td>
<td align="right">20.0%</td>
<td align="right">16.7%</td>
<td align="right">23.1%</td>
<td align="right">21.4%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">721</td>
<td align="left">🟢 Referee</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">0.0%</td>
<td align="right">61.5%</td>
<td align="right">50.0%</td>
<td align="right">7.7%</td>
<td align="right">7.7%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">722</td>
<td align="left">🟢 Taxman</td>
<td align="right"><b>1500</b></td>
<td align="right">25.8%</td>
<td align="right">45.0%</td>
<td align="right">41.7%</td>
<td align="right">23.4%</td>
<td align="right">28.0%</td>
<td align="right">13.0%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">723</td>
<td align="left">🟢 Illusory_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">23.5%</td>
<td align="right">48.9%</td>
<td align="right">36.2%</td>
<td align="right">27.7%</td>
<td align="right">15.3%</td>
<td align="right">10.2%</td>
<td align="right">391</td>
</tr>
<tr>
<td align="left">724</td>
<td align="left">🟢 Network</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">40.5%</td>
<td align="right">34.7%</td>
<td align="right">24.4%</td>
<td align="right">19.4%</td>
<td align="right">16.3%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">725</td>
<td align="left">🟢 Archaeologist</td>
<td align="right"><b>1500</b></td>
<td align="right">24.0%</td>
<td align="right">41.7%</td>
<td align="right">36.8%</td>
<td align="right">21.8%</td>
<td align="right">20.2%</td>
<td align="right">12.9%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">726</td>
<td align="left">🟢 Confusion</td>
<td align="right"><b>1500</b></td>
<td align="right">22.9%</td>
<td align="right">48.8%</td>
<td align="right">35.2%</td>
<td align="right">19.6%</td>
<td align="right">20.2%</td>
<td align="right">12.3%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">727</td>
<td align="left">🟢 Gremlin</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">42.5%</td>
<td align="right">37.5%</td>
<td align="right">30.4%</td>
<td align="right">18.8%</td>
<td align="right">16.3%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">728</td>
<td align="left">🟢 Jinx</td>
<td align="right"><b>1500</b></td>
<td align="right">24.0%</td>
<td align="right">48.6%</td>
<td align="right">29.0%</td>
<td align="right">22.2%</td>
<td align="right">22.0%</td>
<td align="right">18.4%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">729</td>
<td align="left">🟢 Universal</td>
<td align="right"><b>1500</b></td>
<td align="right">23.5%</td>
<td align="right">46.2%</td>
<td align="right">30.9%</td>
<td align="right">28.9%</td>
<td align="right">19.0%</td>
<td align="right">14.6%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">730</td>
<td align="left">🟢 Drummer</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">51.0%</td>
<td align="right">25.8%</td>
<td align="right">27.1%</td>
<td align="right">19.2%</td>
<td align="right">17.9%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">731</td>
<td align="left">🟡 Occultist</td>
<td align="right"><b>1500</b></td>
<td align="right">25.6%</td>
<td align="right">60.9%</td>
<td align="right">37.7%</td>
<td align="right">20.2%</td>
<td align="right">20.7%</td>
<td align="right">15.8%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">732</td>
<td align="left">🟡 Analyst</td>
<td align="right"><b>1500</b></td>
<td align="right">23.3%</td>
<td align="right">47.5%</td>
<td align="right">33.3%</td>
<td align="right">21.0%</td>
<td align="right">20.5%</td>
<td align="right">11.5%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">733</td>
<td align="left">🟡 Trumpeter</td>
<td align="right"><b>1500</b></td>
<td align="right">23.6%</td>
<td align="right">41.5%</td>
<td align="right">40.0%</td>
<td align="right">18.7%</td>
<td align="right">20.0%</td>
<td align="right">14.2%</td>
<td align="right">479</td>
</tr>
<tr>
<td align="left">734</td>
<td align="left">🟡 Dense</td>
<td align="right"><b>1500</b></td>
<td align="right">24.5%</td>
<td align="right">44.4%</td>
<td align="right">26.3%</td>
<td align="right">33.3%</td>
<td align="right">15.0%</td>
<td align="right">19.4%</td>
<td align="right">94</td>
</tr>
<tr>
<td align="left">735</td>
<td align="left">🟡 Oblivion</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">48.7%</td>
<td align="right">28.1%</td>
<td align="right">40.3%</td>
<td align="right">22.5%</td>
<td align="right">11.4%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">736</td>
<td align="left">🟡 Provocateur</td>
<td align="right"><b>1500</b></td>
<td align="right">22.6%</td>
<td align="right">41.7%</td>
<td align="right">33.3%</td>
<td align="right">23.2%</td>
<td align="right">21.3%</td>
<td align="right">12.9%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">737</td>
<td align="left">🟡 Apparition</td>
<td align="right"><b>1500</b></td>
<td align="right">23.9%</td>
<td align="right">40.5%</td>
<td align="right">30.9%</td>
<td align="right">21.7%</td>
<td align="right">18.5%</td>
<td align="right">21.1%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">738</td>
<td align="left">🟡 Fanatic</td>
<td align="right"><b>1500</b></td>
<td align="right">26.3%</td>
<td align="right">36.0%</td>
<td align="right">35.8%</td>
<td align="right">22.5%</td>
<td align="right">28.2%</td>
<td align="right">18.0%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">739</td>
<td align="left">🟡 Guard</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">45.9%</td>
<td align="right">29.0%</td>
<td align="right">35.0%</td>
<td align="right">14.6%</td>
<td align="right">17.0%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">740</td>
<td align="left">🟡 Pincer</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">30.0%</td>
<td align="right">53.8%</td>
<td align="right">21.1%</td>
<td align="right">15.8%</td>
<td align="right">14.3%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">741</td>
<td align="left">🟡 Deafener</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">66.7%</td>
<td align="right">45.5%</td>
<td align="right">21.4%</td>
<td align="right">17.4%</td>
<td align="right">14.3%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">742</td>
<td align="left">🟡 Bright</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">40.0%</td>
<td align="right">47.1%</td>
<td align="right">16.7%</td>
<td align="right">24.0%</td>
<td align="right">10.3%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">743</td>
<td align="left">🟡 Feint</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">0.0%</td>
<td align="right">30.8%</td>
<td align="right">29.2%</td>
<td align="right">9.5%</td>
<td align="right">31.8%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">744</td>
<td align="left">🟡 Racer</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">56.8%</td>
<td align="right">31.6%</td>
<td align="right">17.3%</td>
<td align="right">25.3%</td>
<td align="right">12.9%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">745</td>
<td align="left">🟡 Conjurer</td>
<td align="right"><b>1500</b></td>
<td align="right">26.6%</td>
<td align="right">55.3%</td>
<td align="right">36.1%</td>
<td align="right">18.5%</td>
<td align="right">21.4%</td>
<td align="right">23.3%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">746</td>
<td align="left">🟡 AllIn</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">22.2%</td>
<td align="right">41.7%</td>
<td align="right">14.3%</td>
<td align="right">26.1%</td>
<td align="right">20.0%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">747</td>
<td align="left">🟡 Flare_Entity</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">38.5%</td>
<td align="right">31.3%</td>
<td align="right">24.7%</td>
<td align="right">19.4%</td>
<td align="right">20.1%</td>
<td align="right">475</td>
</tr>
<tr>
<td align="left">748</td>
<td align="left">🟡 Rift</td>
<td align="right"><b>1500</b></td>
<td align="right">25.1%</td>
<td align="right">37.0%</td>
<td align="right">32.9%</td>
<td align="right">22.7%</td>
<td align="right">21.5%</td>
<td align="right">20.2%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">749</td>
<td align="left">🟡 Siege</td>
<td align="right"><b>1500</b></td>
<td align="right">23.5%</td>
<td align="right">48.9%</td>
<td align="right">41.4%</td>
<td align="right">30.7%</td>
<td align="right">14.9%</td>
<td align="right">10.9%</td>
<td align="right">480</td>
</tr>
<tr>
<td align="left">750</td>
<td align="left">🟡 Rapid</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">42.1%</td>
<td align="right">40.7%</td>
<td align="right">20.4%</td>
<td align="right">25.4%</td>
<td align="right">14.6%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">751</td>
<td align="left">🟡 Parry</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">50.0%</td>
<td align="right">28.8%</td>
<td align="right">29.4%</td>
<td align="right">15.6%</td>
<td align="right">20.2%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">752</td>
<td align="left">🟡 Klutz</td>
<td align="right"><b>1500</b></td>
<td align="right">23.5%</td>
<td align="right">51.2%</td>
<td align="right">25.6%</td>
<td align="right">27.6%</td>
<td align="right">21.4%</td>
<td align="right">11.6%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">753</td>
<td align="left">🟡 Diviner</td>
<td align="right"><b>1500</b></td>
<td align="right">23.4%</td>
<td align="right">51.0%</td>
<td align="right">29.3%</td>
<td align="right">22.0%</td>
<td align="right">18.7%</td>
<td align="right">15.4%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">754</td>
<td align="left">🟡 Historian</td>
<td align="right"><b>1500</b></td>
<td align="right">24.2%</td>
<td align="right">42.9%</td>
<td align="right">50.0%</td>
<td align="right">27.3%</td>
<td align="right">10.0%</td>
<td align="right">22.2%</td>
<td align="right">62</td>
</tr>
<tr>
<td align="left">755</td>
<td align="left">🟡 Fission</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">51.1%</td>
<td align="right">39.7%</td>
<td align="right">29.2%</td>
<td align="right">18.6%</td>
<td align="right">15.2%</td>
<td align="right">491</td>
</tr>
<tr>
<td align="left">756</td>
<td align="left">🟡 Shoggoth</td>
<td align="right"><b>1500</b></td>
<td align="right">22.6%</td>
<td align="right">38.9%</td>
<td align="right">24.3%</td>
<td align="right">32.2%</td>
<td align="right">17.9%</td>
<td align="right">13.7%</td>
<td align="right">243</td>
</tr>
<tr>
<td align="left">757</td>
<td align="left">🟡 Lord</td>
<td align="right"><b>1500</b></td>
<td align="right">24.3%</td>
<td align="right">59.1%</td>
<td align="right">32.5%</td>
<td align="right">28.1%</td>
<td align="right">15.2%</td>
<td align="right">14.7%</td>
<td align="right">481</td>
</tr>
<tr>
<td align="left">758</td>
<td align="left">🟡 Unifier</td>
<td align="right"><b>1500</b></td>
<td align="right">25.1%</td>
<td align="right">51.4%</td>
<td align="right">41.0%</td>
<td align="right">23.2%</td>
<td align="right">18.3%</td>
<td align="right">17.2%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">759</td>
<td align="left">🟡 Summoner</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">42.2%</td>
<td align="right">34.7%</td>
<td align="right">26.8%</td>
<td align="right">17.0%</td>
<td align="right">19.0%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">760</td>
<td align="left">🟡 Perceiver</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">54.8%</td>
<td align="right">30.4%</td>
<td align="right">25.6%</td>
<td align="right">20.7%</td>
<td align="right">14.5%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">761</td>
<td align="left">🟡 Entangler_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">55.6%</td>
<td align="right">30.8%</td>
<td align="right">23.8%</td>
<td align="right">22.2%</td>
<td align="right">5.6%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">762</td>
<td align="left">🟡 Casino</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">0.0%</td>
<td align="right">38.9%</td>
<td align="right">27.8%</td>
<td align="right">37.5%</td>
<td align="right">5.0%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">763</td>
<td align="left">🟡 Enchanter_Alt</td>
<td align="right"><b>1500</b></td>
<td align="right">24.1%</td>
<td align="right">46.2%</td>
<td align="right">26.7%</td>
<td align="right">20.0%</td>
<td align="right">5.6%</td>
<td align="right">27.8%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">764</td>
<td align="left">🟡 Escape</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">51.5%</td>
<td align="right">30.5%</td>
<td align="right">24.7%</td>
<td align="right">15.7%</td>
<td align="right">22.5%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">765</td>
<td align="left">🟡 Server</td>
<td align="right"><b>1500</b></td>
<td align="right">24.5%</td>
<td align="right">39.5%</td>
<td align="right">34.4%</td>
<td align="right">21.6%</td>
<td align="right">17.9%</td>
<td align="right">22.3%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">766</td>
<td align="left">🟡 Guardian</td>
<td align="right"><b>1500</b></td>
<td align="right">23.6%</td>
<td align="right">64.3%</td>
<td align="right">32.4%</td>
<td align="right">26.5%</td>
<td align="right">20.0%</td>
<td align="right">15.6%</td>
<td align="right">1877</td>
</tr>
<tr>
<td align="left">767</td>
<td align="left">🟡 Madness</td>
<td align="right"><b>1500</b></td>
<td align="right">23.6%</td>
<td align="right">42.0%</td>
<td align="right">25.0%</td>
<td align="right">23.0%</td>
<td align="right">19.4%</td>
<td align="right">20.8%</td>
<td align="right">496</td>
</tr>
<tr>
<td align="left">768</td>
<td align="left">🟡 Dispeller</td>
<td align="right"><b>1500</b></td>
<td align="right">24.0%</td>
<td align="right">60.0%</td>
<td align="right">11.1%</td>
<td align="right">30.8%</td>
<td align="right">17.4%</td>
<td align="right">15.0%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">769</td>
<td align="left">🟡 Bamboo</td>
<td align="right"><b>1500</b></td>
<td align="right">24.0%</td>
<td align="right">50.0%</td>
<td align="right">55.6%</td>
<td align="right">18.2%</td>
<td align="right">23.1%</td>
<td align="right">12.0%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">770</td>
<td align="left">🟡 Elder</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">41.5%</td>
<td align="right">30.2%</td>
<td align="right">28.4%</td>
<td align="right">22.6%</td>
<td align="right">17.2%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">771</td>
<td align="left">🟡 Filch</td>
<td align="right"><b>1500</b></td>
<td align="right">22.5%</td>
<td align="right">51.6%</td>
<td align="right">34.3%</td>
<td align="right">25.2%</td>
<td align="right">19.2%</td>
<td align="right">16.5%</td>
<td align="right">2534</td>
</tr>
<tr>
<td align="left">772</td>
<td align="left">🟡 Noble</td>
<td align="right"><b>1500</b></td>
<td align="right">26.5%</td>
<td align="right">56.4%</td>
<td align="right">37.7%</td>
<td align="right">23.9%</td>
<td align="right">19.0%</td>
<td align="right">19.9%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">773</td>
<td align="left">🟡 Interpreter</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">58.5%</td>
<td align="right">25.3%</td>
<td align="right">24.7%</td>
<td align="right">21.4%</td>
<td align="right">17.3%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">774</td>
<td align="left">🟡 Xeno</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">54.9%</td>
<td align="right">28.1%</td>
<td align="right">29.3%</td>
<td align="right">19.8%</td>
<td align="right">14.9%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">775</td>
<td align="left">🟡 Glutton_Food</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">39.1%</td>
<td align="right">29.7%</td>
<td align="right">29.8%</td>
<td align="right">20.0%</td>
<td align="right">17.9%</td>
<td align="right">266</td>
</tr>
<tr>
<td align="left">776</td>
<td align="left">🟡 Collector</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">58.1%</td>
<td align="right">36.4%</td>
<td align="right">28.2%</td>
<td align="right">19.3%</td>
<td align="right">8.3%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">777</td>
<td align="left">🟡 Dreamer</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">34.4%</td>
<td align="right">36.2%</td>
<td align="right">35.5%</td>
<td align="right">17.7%</td>
<td align="right">17.6%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">778</td>
<td align="left">🟡 Slayer</td>
<td align="right"><b>1500</b></td>
<td align="right">24.8%</td>
<td align="right">43.2%</td>
<td align="right">35.2%</td>
<td align="right">24.4%</td>
<td align="right">15.5%</td>
<td align="right">21.4%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">779</td>
<td align="left">🟡 Jellyfish</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">57.9%</td>
<td align="right">25.4%</td>
<td align="right">27.5%</td>
<td align="right">17.9%</td>
<td align="right">19.3%</td>
<td align="right">392</td>
</tr>
<tr>
<td align="left">780</td>
<td align="left">🟡 Cryo</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">46.9%</td>
<td align="right">33.8%</td>
<td align="right">28.3%</td>
<td align="right">16.8%</td>
<td align="right">16.4%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">781</td>
<td align="left">🟡 Leech</td>
<td align="right"><b>1500</b></td>
<td align="right">23.6%</td>
<td align="right">41.9%</td>
<td align="right">30.2%</td>
<td align="right">30.5%</td>
<td align="right">18.3%</td>
<td align="right">15.7%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">782</td>
<td align="left">🟡 Blitz</td>
<td align="right"><b>1500</b></td>
<td align="right">23.9%</td>
<td align="right">41.2%</td>
<td align="right">32.3%</td>
<td align="right">24.0%</td>
<td align="right">20.8%</td>
<td align="right">15.9%</td>
<td align="right">472</td>
</tr>
<tr>
<td align="left">783</td>
<td align="left">🟡 Lead</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">50.0%</td>
<td align="right">30.8%</td>
<td align="right">18.2%</td>
<td align="right">13.0%</td>
<td align="right">19.0%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">784</td>
<td align="left">🟡 Chromium</td>
<td align="right"><b>1500</b></td>
<td align="right">23.8%</td>
<td align="right">41.7%</td>
<td align="right">26.7%</td>
<td align="right">36.4%</td>
<td align="right">10.0%</td>
<td align="right">18.2%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">785</td>
<td align="left">🟡 Courtier</td>
<td align="right"><b>1500</b></td>
<td align="right">25.1%</td>
<td align="right">53.2%</td>
<td align="right">31.2%</td>
<td align="right">26.3%</td>
<td align="right">21.2%</td>
<td align="right">15.4%</td>
<td align="right">478</td>
</tr>
<tr>
<td align="left">786</td>
<td align="left">🟡 Dust</td>
<td align="right"><b>1500</b></td>
<td align="right">23.4%</td>
<td align="right">46.5%</td>
<td align="right">28.6%</td>
<td align="right">22.9%</td>
<td align="right">23.1%</td>
<td align="right">14.1%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">787</td>
<td align="left">🟡 Diplomat</td>
<td align="right"><b>1499</b></td>
<td align="right">22.1%</td>
<td align="right">27.0%</td>
<td align="right">33.1%</td>
<td align="right">25.6%</td>
<td align="right">19.5%</td>
<td align="right">16.0%</td>
<td align="right">1765</td>
</tr>
<tr>
<td align="left">788</td>
<td align="left">🟡 Shuffler</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">37.5%</td>
<td align="right">37.5%</td>
<td align="right">23.5%</td>
<td align="right">16.7%</td>
<td align="right">18.8%</td>
<td align="right">97</td>
</tr>
<tr>
<td align="left">789</td>
<td align="left">🟡 Harmonist</td>
<td align="right"><b>1499</b></td>
<td align="right">25.7%</td>
<td align="right">56.5%</td>
<td align="right">39.4%</td>
<td align="right">19.4%</td>
<td align="right">22.5%</td>
<td align="right">14.0%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">790</td>
<td align="left">🟡 Marathoner</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">58.3%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">16.7%</td>
<td align="right">8.3%</td>
<td align="right">76</td>
</tr>
<tr>
<td align="left">791</td>
<td align="left">🟡 Explorer</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">43.8%</td>
<td align="right">31.8%</td>
<td align="right">29.0%</td>
<td align="right">17.9%</td>
<td align="right">15.5%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">792</td>
<td align="left">🟡 Resilient</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">39.6%</td>
<td align="right">35.9%</td>
<td align="right">24.3%</td>
<td align="right">21.5%</td>
<td align="right">17.2%</td>
<td align="right">463</td>
</tr>
<tr>
<td align="left">793</td>
<td align="left">🟡 Strategist</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">50.0%</td>
<td align="right">22.2%</td>
<td align="right">33.3%</td>
<td align="right">6.2%</td>
<td align="right">23.1%</td>
<td align="right">72</td>
</tr>
<tr>
<td align="left">794</td>
<td align="left">🟡 Daredevil</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">50.0%</td>
<td align="right">28.1%</td>
<td align="right">26.7%</td>
<td align="right">18.3%</td>
<td align="right">16.7%</td>
<td align="right">408</td>
</tr>
<tr>
<td align="left">795</td>
<td align="left">🟡 Butterfly</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">36.4%</td>
<td align="right">31.2%</td>
<td align="right">18.2%</td>
<td align="right">19.0%</td>
<td align="right">20.0%</td>
<td align="right">89</td>
</tr>
<tr>
<td align="left">796</td>
<td align="left">🟡 Chancy</td>
<td align="right"><b>1499</b></td>
<td align="right">22.2%</td>
<td align="right">37.1%</td>
<td align="right">38.5%</td>
<td align="right">25.5%</td>
<td align="right">15.5%</td>
<td align="right">13.0%</td>
<td align="right">473</td>
</tr>
<tr>
<td align="left">797</td>
<td align="left">🟡 Guerrilla</td>
<td align="right"><b>1499</b></td>
<td align="right">24.9%</td>
<td align="right">48.7%</td>
<td align="right">27.7%</td>
<td align="right">27.8%</td>
<td align="right">22.1%</td>
<td align="right">17.1%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">798</td>
<td align="left">🟡 Savage</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">40.9%</td>
<td align="right">40.0%</td>
<td align="right">26.7%</td>
<td align="right">14.4%</td>
<td align="right">17.0%</td>
<td align="right">462</td>
</tr>
<tr>
<td align="left">799</td>
<td align="left">🟡 Levitator</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">28.6%</td>
<td align="right">37.5%</td>
<td align="right">13.6%</td>
<td align="right">19.4%</td>
<td align="right">26.9%</td>
<td align="right">102</td>
</tr>
<tr>
<td align="left">800</td>
<td align="left">🟡 Fungus</td>
<td align="right"><b>1499</b></td>
<td align="right">22.8%</td>
<td align="right">61.5%</td>
<td align="right">36.4%</td>
<td align="right">24.9%</td>
<td align="right">17.0%</td>
<td align="right">17.0%</td>
<td align="right">1886</td>
</tr>
<tr>
<td align="left">801</td>
<td align="left">🟡 Charlatan</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">42.9%</td>
<td align="right">32.1%</td>
<td align="right">27.7%</td>
<td align="right">16.7%</td>
<td align="right">17.2%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">802</td>
<td align="left">🟡 Omen</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">65.3%</td>
<td align="right">35.9%</td>
<td align="right">23.6%</td>
<td align="right">20.4%</td>
<td align="right">5.6%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">803</td>
<td align="left">🟡 Formless</td>
<td align="right"><b>1499</b></td>
<td align="right">24.6%</td>
<td align="right">55.0%</td>
<td align="right">51.6%</td>
<td align="right">29.6%</td>
<td align="right">14.5%</td>
<td align="right">11.1%</td>
<td align="right">248</td>
</tr>
<tr>
<td align="left">804</td>
<td align="left">🟡 Masked</td>
<td align="right"><b>1499</b></td>
<td align="right">23.4%</td>
<td align="right">55.9%</td>
<td align="right">20.3%</td>
<td align="right">24.7%</td>
<td align="right">14.3%</td>
<td align="right">23.6%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">805</td>
<td align="left">🟡 Scorpion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">54.5%</td>
<td align="right">40.8%</td>
<td align="right">23.7%</td>
<td align="right">15.1%</td>
<td align="right">8.4%</td>
<td align="right">477</td>
</tr>
<tr>
<td align="left">806</td>
<td align="left">🟡 Asteroid</td>
<td align="right"><b>1499</b></td>
<td align="right">25.2%</td>
<td align="right">47.6%</td>
<td align="right">25.7%</td>
<td align="right">20.0%</td>
<td align="right">26.5%</td>
<td align="right">16.5%</td>
<td align="right">469</td>
</tr>
<tr>
<td align="left">807</td>
<td align="left">🟡 Marshal</td>
<td align="right"><b>1499</b></td>
<td align="right">26.5%</td>
<td align="right">53.3%</td>
<td align="right">40.9%</td>
<td align="right">24.4%</td>
<td align="right">19.7%</td>
<td align="right">16.7%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">808</td>
<td align="left">🟡 Faster</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">51.3%</td>
<td align="right">31.0%</td>
<td align="right">23.9%</td>
<td align="right">20.5%</td>
<td align="right">14.8%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">809</td>
<td align="left">🟡 Maximizer</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">27.3%</td>
<td align="right">21.7%</td>
<td align="right">18.2%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">810</td>
<td align="left">🟡 Abomination</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">37.9%</td>
<td align="right">40.5%</td>
<td align="right">20.0%</td>
<td align="right">20.8%</td>
<td align="right">15.5%</td>
<td align="right">269</td>
</tr>
<tr>
<td align="left">811</td>
<td align="left">🟡 Potentate</td>
<td align="right"><b>1499</b></td>
<td align="right">23.4%</td>
<td align="right">57.5%</td>
<td align="right">40.7%</td>
<td align="right">24.2%</td>
<td align="right">10.7%</td>
<td align="right">16.0%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">812</td>
<td align="left">🟡 Amplify</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">50.0%</td>
<td align="right">47.0%</td>
<td align="right">20.2%</td>
<td align="right">23.8%</td>
<td align="right">7.5%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">813</td>
<td align="left">🟡 Analyst_Alt</td>
<td align="right"><b>1499</b></td>
<td align="right">23.4%</td>
<td align="right">44.4%</td>
<td align="right">37.5%</td>
<td align="right">16.7%</td>
<td align="right">23.8%</td>
<td align="right">14.8%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">814</td>
<td align="left">🟡 Squall</td>
<td align="right"><b>1499</b></td>
<td align="right">23.4%</td>
<td align="right">33.3%</td>
<td align="right">38.9%</td>
<td align="right">44.4%</td>
<td align="right">10.0%</td>
<td align="right">9.5%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">815</td>
<td align="left">🟡 Vampire</td>
<td align="right"><b>1499</b></td>
<td align="right">24.0%</td>
<td align="right">45.8%</td>
<td align="right">36.9%</td>
<td align="right">22.7%</td>
<td align="right">23.5%</td>
<td align="right">10.8%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">816</td>
<td align="left">🟡 Rainbow_Alt</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">50.0%</td>
<td align="right">10.0%</td>
<td align="right">27.3%</td>
<td align="right">23.5%</td>
<td align="right">25.0%</td>
<td align="right">60</td>
</tr>
<tr>
<td align="left">817</td>
<td align="left">🟡 Schizoid</td>
<td align="right"><b>1499</b></td>
<td align="right">22.5%</td>
<td align="right">47.9%</td>
<td align="right">34.3%</td>
<td align="right">22.1%</td>
<td align="right">20.7%</td>
<td align="right">15.9%</td>
<td align="right">1804</td>
</tr>
<tr>
<td align="left">818</td>
<td align="left">🟡 Serpent</td>
<td align="right"><b>1499</b></td>
<td align="right">23.2%</td>
<td align="right">45.3%</td>
<td align="right">32.4%</td>
<td align="right">22.9%</td>
<td align="right">16.5%</td>
<td align="right">13.6%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">819</td>
<td align="left">🟡 Statistician</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">50.0%</td>
<td align="right">18.2%</td>
<td align="right">37.5%</td>
<td align="right">15.0%</td>
<td align="right">16.7%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">820</td>
<td align="left">🟡 Amnesiac</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">75.0%</td>
<td align="right">25.0%</td>
<td align="right">20.8%</td>
<td align="right">16.7%</td>
<td align="right">21.1%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">821</td>
<td align="left">🟡 Desolator</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">55.0%</td>
<td align="right">23.5%</td>
<td align="right">21.6%</td>
<td align="right">24.6%</td>
<td align="right">17.3%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">822</td>
<td align="left">🟡 Anarchy</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">47.6%</td>
<td align="right">25.7%</td>
<td align="right">25.0%</td>
<td align="right">19.3%</td>
<td align="right">17.4%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">823</td>
<td align="left">🟡 Warrior</td>
<td align="right"><b>1499</b></td>
<td align="right">23.4%</td>
<td align="right">66.7%</td>
<td align="right">37.4%</td>
<td align="right">26.0%</td>
<td align="right">19.7%</td>
<td align="right">15.6%</td>
<td align="right">2575</td>
</tr>
<tr>
<td align="left">824</td>
<td align="left">🟡 Database</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">52.1%</td>
<td align="right">27.6%</td>
<td align="right">33.7%</td>
<td align="right">12.2%</td>
<td align="right">15.5%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">825</td>
<td align="left">🟡 Broadcaster</td>
<td align="right"><b>1499</b></td>
<td align="right">24.9%</td>
<td align="right">47.2%</td>
<td align="right">28.2%</td>
<td align="right">24.5%</td>
<td align="right">23.9%</td>
<td align="right">14.8%</td>
<td align="right">485</td>
</tr>
<tr>
<td align="left">826</td>
<td align="left">🟡 Clam</td>
<td align="right"><b>1499</b></td>
<td align="right">22.3%</td>
<td align="right">38.6%</td>
<td align="right">31.3%</td>
<td align="right">18.2%</td>
<td align="right">19.4%</td>
<td align="right">17.5%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">827</td>
<td align="left">🟡 Spiff</td>
<td align="right"><b>1499</b></td>
<td align="right">21.9%</td>
<td align="right">55.0%</td>
<td align="right">32.1%</td>
<td align="right">27.5%</td>
<td align="right">19.2%</td>
<td align="right">13.5%</td>
<td align="right">2579</td>
</tr>
<tr>
<td align="left">828</td>
<td align="left">🟡 Garrison</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">44.7%</td>
<td align="right">32.9%</td>
<td align="right">29.3%</td>
<td align="right">16.4%</td>
<td align="right">15.6%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">829</td>
<td align="left">🟡 Caller</td>
<td align="right"><b>1499</b></td>
<td align="right">25.0%</td>
<td align="right">60.0%</td>
<td align="right">35.9%</td>
<td align="right">20.9%</td>
<td align="right">19.8%</td>
<td align="right">15.9%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">830</td>
<td align="left">🟡 Fogger</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">61.9%</td>
<td align="right">32.9%</td>
<td align="right">23.7%</td>
<td align="right">14.2%</td>
<td align="right">16.3%</td>
<td align="right">472</td>
</tr>
<tr>
<td align="left">831</td>
<td align="left">🟡 Inventor</td>
<td align="right"><b>1499</b></td>
<td align="right">22.9%</td>
<td align="right">31.7%</td>
<td align="right">31.3%</td>
<td align="right">24.6%</td>
<td align="right">21.0%</td>
<td align="right">15.7%</td>
<td align="right">388</td>
</tr>
<tr>
<td align="left">832</td>
<td align="left">🟡 Pusher</td>
<td align="right"><b>1499</b></td>
<td align="right">23.2%</td>
<td align="right">42.9%</td>
<td align="right">29.4%</td>
<td align="right">13.3%</td>
<td align="right">17.4%</td>
<td align="right">25.0%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">833</td>
<td align="left">🟡 TheCult</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">52.2%</td>
<td align="right">20.0%</td>
<td align="right">31.2%</td>
<td align="right">20.5%</td>
<td align="right">17.8%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">834</td>
<td align="left">🟡 Saprophyte</td>
<td align="right"><b>1499</b></td>
<td align="right">22.8%</td>
<td align="right">45.5%</td>
<td align="right">32.1%</td>
<td align="right">29.4%</td>
<td align="right">14.5%</td>
<td align="right">17.4%</td>
<td align="right">263</td>
</tr>
<tr>
<td align="left">835</td>
<td align="left">🟡 Landlord</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">59.1%</td>
<td align="right">26.8%</td>
<td align="right">28.6%</td>
<td align="right">22.5%</td>
<td align="right">12.6%</td>
<td align="right">469</td>
</tr>
<tr>
<td align="left">836</td>
<td align="left">🟡 Spirit</td>
<td align="right"><b>1499</b></td>
<td align="right">24.7%</td>
<td align="right">55.0%</td>
<td align="right">27.1%</td>
<td align="right">22.9%</td>
<td align="right">20.0%</td>
<td align="right">18.5%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">837</td>
<td align="left">🟡 Concealer</td>
<td align="right"><b>1499</b></td>
<td align="right">22.4%</td>
<td align="right">53.1%</td>
<td align="right">29.9%</td>
<td align="right">19.8%</td>
<td align="right">14.7%</td>
<td align="right">19.7%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">838</td>
<td align="left">🟡 Importer</td>
<td align="right"><b>1499</b></td>
<td align="right">25.4%</td>
<td align="right">45.9%</td>
<td align="right">27.4%</td>
<td align="right">30.9%</td>
<td align="right">13.7%</td>
<td align="right">23.9%</td>
<td align="right">406</td>
</tr>
<tr>
<td align="left">839</td>
<td align="left">🟡 Schrodinger</td>
<td align="right"><b>1499</b></td>
<td align="right">23.1%</td>
<td align="right">40.0%</td>
<td align="right">36.4%</td>
<td align="right">14.3%</td>
<td align="right">20.0%</td>
<td align="right">18.5%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">840</td>
<td align="left">🟡 Sentinel</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">60.5%</td>
<td align="right">26.7%</td>
<td align="right">28.1%</td>
<td align="right">20.0%</td>
<td align="right">12.4%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">841</td>
<td align="left">🟡 Bonder</td>
<td align="right"><b>1499</b></td>
<td align="right">27.0%</td>
<td align="right">42.0%</td>
<td align="right">44.7%</td>
<td align="right">21.1%</td>
<td align="right">22.5%</td>
<td align="right">18.6%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">842</td>
<td align="left">🟡 Solar</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">49.1%</td>
<td align="right">36.7%</td>
<td align="right">19.4%</td>
<td align="right">19.5%</td>
<td align="right">16.7%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">843</td>
<td align="left">🟡 Null</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">45.5%</td>
<td align="right">30.6%</td>
<td align="right">25.9%</td>
<td align="right">17.4%</td>
<td align="right">17.9%</td>
<td align="right">477</td>
</tr>
<tr>
<td align="left">844</td>
<td align="left">🟡 Absorb</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">49.0%</td>
<td align="right">28.6%</td>
<td align="right">28.0%</td>
<td align="right">14.6%</td>
<td align="right">18.8%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">845</td>
<td align="left">🟡 Bender</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">58.1%</td>
<td align="right">25.0%</td>
<td align="right">19.7%</td>
<td align="right">24.5%</td>
<td align="right">16.8%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">846</td>
<td align="left">🟡 Dictator</td>
<td align="right"><b>1499</b></td>
<td align="right">21.7%</td>
<td align="right">50.0%</td>
<td align="right">33.0%</td>
<td align="right">23.3%</td>
<td align="right">18.5%</td>
<td align="right">16.5%</td>
<td align="right">2433</td>
</tr>
<tr>
<td align="left">847</td>
<td align="left">🟡 Platinum</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">23.8%</td>
<td align="right">31.6%</td>
<td align="right">8.3%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">848</td>
<td align="left">🟡 Tsunami</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">56.0%</td>
<td align="right">32.1%</td>
<td align="right">21.1%</td>
<td align="right">23.9%</td>
<td align="right">13.1%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">849</td>
<td align="left">🟡 Diplomat_Alt</td>
<td align="right"><b>1499</b></td>
<td align="right">22.6%</td>
<td align="right">37.0%</td>
<td align="right">22.4%</td>
<td align="right">23.7%</td>
<td align="right">20.5%</td>
<td align="right">18.5%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">850</td>
<td align="left">🟡 Crow</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">40.4%</td>
<td align="right">27.8%</td>
<td align="right">25.3%</td>
<td align="right">25.9%</td>
<td align="right">11.2%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">851</td>
<td align="left">🟡 Chameleon</td>
<td align="right"><b>1499</b></td>
<td align="right">22.1%</td>
<td align="right">40.5%</td>
<td align="right">32.7%</td>
<td align="right">25.8%</td>
<td align="right">14.7%</td>
<td align="right">17.4%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">852</td>
<td align="left">🟡 Adapter</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">33.3%</td>
<td align="right">38.1%</td>
<td align="right">28.3%</td>
<td align="right">20.5%</td>
<td align="right">12.7%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">853</td>
<td align="left">🟡 Vortex</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">42.9%</td>
<td align="right">35.6%</td>
<td align="right">26.7%</td>
<td align="right">18.0%</td>
<td align="right">15.1%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">854</td>
<td align="left">🟡 Lighter</td>
<td align="right"><b>1499</b></td>
<td align="right">22.8%</td>
<td align="right">42.9%</td>
<td align="right">46.2%</td>
<td align="right">23.5%</td>
<td align="right">9.5%</td>
<td align="right">14.3%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">855</td>
<td align="left">🟡 Transformer</td>
<td align="right"><b>1499</b></td>
<td align="right">25.2%</td>
<td align="right">61.7%</td>
<td align="right">32.8%</td>
<td align="right">27.6%</td>
<td align="right">11.2%</td>
<td align="right">16.2%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">856</td>
<td align="left">🟡 AI</td>
<td align="right"><b>1499</b></td>
<td align="right">24.7%</td>
<td align="right">36.1%</td>
<td align="right">34.2%</td>
<td align="right">23.7%</td>
<td align="right">21.6%</td>
<td align="right">18.8%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">857</td>
<td align="left">🟡 Gorgon</td>
<td align="right"><b>1499</b></td>
<td align="right">23.2%</td>
<td align="right">46.3%</td>
<td align="right">40.6%</td>
<td align="right">25.3%</td>
<td align="right">15.7%</td>
<td align="right">12.8%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">858</td>
<td align="left">🟡 Inferno</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">51.1%</td>
<td align="right">36.1%</td>
<td align="right">17.5%</td>
<td align="right">23.6%</td>
<td align="right">13.2%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">859</td>
<td align="left">🟡 Locust_Alt</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">57.9%</td>
<td align="right">35.5%</td>
<td align="right">27.3%</td>
<td align="right">20.6%</td>
<td align="right">11.1%</td>
<td align="right">423</td>
</tr>
<tr>
<td align="left">860</td>
<td align="left">🟡 Worm</td>
<td align="right"><b>1499</b></td>
<td align="right">22.5%</td>
<td align="right">50.0%</td>
<td align="right">26.0%</td>
<td align="right">26.7%</td>
<td align="right">15.9%</td>
<td align="right">13.5%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">861</td>
<td align="left">🟡 Scavenger</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">46.8%</td>
<td align="right">25.0%</td>
<td align="right">21.6%</td>
<td align="right">16.4%</td>
<td align="right">24.0%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">862</td>
<td align="left">🟡 Probabilist</td>
<td align="right"><b>1499</b></td>
<td align="right">22.7%</td>
<td align="right">75.0%</td>
<td align="right">22.2%</td>
<td align="right">15.8%</td>
<td align="right">18.8%</td>
<td align="right">7.1%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">863</td>
<td align="left">🟡 Scholar</td>
<td align="right"><b>1499</b></td>
<td align="right">22.7%</td>
<td align="right">71.4%</td>
<td align="right">20.0%</td>
<td align="right">26.7%</td>
<td align="right">15.8%</td>
<td align="right">12.5%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">864</td>
<td align="left">🟡 Tree</td>
<td align="right"><b>1499</b></td>
<td align="right">22.6%</td>
<td align="right">40.0%</td>
<td align="right">25.0%</td>
<td align="right">22.2%</td>
<td align="right">7.1%</td>
<td align="right">23.3%</td>
<td align="right">84</td>
</tr>
<tr>
<td align="left">865</td>
<td align="left">🟡 Mathematician</td>
<td align="right"><b>1499</b></td>
<td align="right">22.6%</td>
<td align="right">75.0%</td>
<td align="right">30.8%</td>
<td align="right">16.7%</td>
<td align="right">14.3%</td>
<td align="right">12.0%</td>
<td align="right">84</td>
</tr>
<tr>
<td align="left">866</td>
<td align="left">🟡 Reactor</td>
<td align="right"><b>1499</b></td>
<td align="right">22.8%</td>
<td align="right">57.5%</td>
<td align="right">27.0%</td>
<td align="right">22.1%</td>
<td align="right">18.8%</td>
<td align="right">13.3%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">867</td>
<td align="left">🟡 Current</td>
<td align="right"><b>1499</b></td>
<td align="right">25.4%</td>
<td align="right">40.0%</td>
<td align="right">35.9%</td>
<td align="right">37.8%</td>
<td align="right">16.8%</td>
<td align="right">12.6%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">868</td>
<td align="left">🟡 Luminary</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">38.6%</td>
<td align="right">28.1%</td>
<td align="right">22.8%</td>
<td align="right">20.2%</td>
<td align="right">19.5%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">869</td>
<td align="left">🟡 Abjurer</td>
<td align="right"><b>1499</b></td>
<td align="right">22.5%</td>
<td align="right">83.3%</td>
<td align="right">30.0%</td>
<td align="right">14.3%</td>
<td align="right">16.7%</td>
<td align="right">12.5%</td>
<td align="right">71</td>
</tr>
<tr>
<td align="left">870</td>
<td align="left">🟡 Griffin</td>
<td align="right"><b>1499</b></td>
<td align="right">23.2%</td>
<td align="right">43.8%</td>
<td align="right">20.4%</td>
<td align="right">27.8%</td>
<td align="right">16.4%</td>
<td align="right">19.2%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">871</td>
<td align="left">🟡 Changeling</td>
<td align="right"><b>1499</b></td>
<td align="right">21.2%</td>
<td align="right">33.3%</td>
<td align="right">25.3%</td>
<td align="right">27.6%</td>
<td align="right">18.2%</td>
<td align="right">16.5%</td>
<td align="right">2591</td>
</tr>
<tr>
<td align="left">872</td>
<td align="left">🟡 Quantum</td>
<td align="right"><b>1499</b></td>
<td align="right">22.5%</td>
<td align="right">40.0%</td>
<td align="right">50.0%</td>
<td align="right">17.4%</td>
<td align="right">23.5%</td>
<td align="right">8.7%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">873</td>
<td align="left">🟡 Streaker</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">44.7%</td>
<td align="right">33.8%</td>
<td align="right">16.5%</td>
<td align="right">18.9%</td>
<td align="right">19.1%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">874</td>
<td align="left">🟡 Illusionist</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">35.9%</td>
<td align="right">34.4%</td>
<td align="right">23.4%</td>
<td align="right">20.8%</td>
<td align="right">18.5%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">875</td>
<td align="left">🟡 Warlock</td>
<td align="right"><b>1499</b></td>
<td align="right">21.7%</td>
<td align="right">44.2%</td>
<td align="right">30.1%</td>
<td align="right">27.3%</td>
<td align="right">18.7%</td>
<td align="right">15.7%</td>
<td align="right">2458</td>
</tr>
<tr>
<td align="left">876</td>
<td align="left">🟡 Mimic_Alt</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">45.5%</td>
<td align="right">31.2%</td>
<td align="right">31.0%</td>
<td align="right">14.8%</td>
<td align="right">13.5%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">877</td>
<td align="left">🟡 Relic</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">60.0%</td>
<td align="right">29.0%</td>
<td align="right">20.2%</td>
<td align="right">15.7%</td>
<td align="right">20.6%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">878</td>
<td align="left">🟡 Gnome</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">51.1%</td>
<td align="right">42.4%</td>
<td align="right">21.9%</td>
<td align="right">21.7%</td>
<td align="right">13.2%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">879</td>
<td align="left">🟡 Gourmand</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">41.7%</td>
<td align="right">29.4%</td>
<td align="right">41.2%</td>
<td align="right">16.7%</td>
<td align="right">13.3%</td>
<td align="right">258</td>
</tr>
<tr>
<td align="left">880</td>
<td align="left">🟡 Mentor</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">54.3%</td>
<td align="right">32.1%</td>
<td align="right">30.1%</td>
<td align="right">15.3%</td>
<td align="right">14.6%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">881</td>
<td align="left">🟡 Alien</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">45.9%</td>
<td align="right">39.0%</td>
<td align="right">20.3%</td>
<td align="right">19.6%</td>
<td align="right">16.8%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">882</td>
<td align="left">🟡 Pulse</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">32.8%</td>
<td align="right">41.4%</td>
<td align="right">16.2%</td>
<td align="right">17.7%</td>
<td align="right">17.5%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">883</td>
<td align="left">🟡 Battalion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">47.9%</td>
<td align="right">26.6%</td>
<td align="right">26.4%</td>
<td align="right">16.8%</td>
<td align="right">17.5%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">884</td>
<td align="left">🟡 Angler</td>
<td align="right"><b>1499</b></td>
<td align="right">22.8%</td>
<td align="right">48.9%</td>
<td align="right">33.3%</td>
<td align="right">27.8%</td>
<td align="right">15.6%</td>
<td align="right">10.6%</td>
<td align="right">470</td>
</tr>
<tr>
<td align="left">885</td>
<td align="left">🟡 General</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">60.0%</td>
<td align="right">27.9%</td>
<td align="right">26.0%</td>
<td align="right">20.5%</td>
<td align="right">13.4%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">886</td>
<td align="left">🟡 Ember</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">31.9%</td>
<td align="right">31.3%</td>
<td align="right">19.4%</td>
<td align="right">21.4%</td>
<td align="right">18.1%</td>
<td align="right">400</td>
</tr>
<tr>
<td align="left">887</td>
<td align="left">🟡 Battery</td>
<td align="right"><b>1499</b></td>
<td align="right">22.1%</td>
<td align="right">39.3%</td>
<td align="right">34.2%</td>
<td align="right">19.3%</td>
<td align="right">15.9%</td>
<td align="right">14.4%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">888</td>
<td align="left">🟡 Forger</td>
<td align="right"><b>1499</b></td>
<td align="right">22.7%</td>
<td align="right">47.5%</td>
<td align="right">34.8%</td>
<td align="right">27.5%</td>
<td align="right">14.3%</td>
<td align="right">13.1%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">889</td>
<td align="left">🟡 Suppressor</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">60.9%</td>
<td align="right">28.1%</td>
<td align="right">24.6%</td>
<td align="right">19.8%</td>
<td align="right">12.4%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">890</td>
<td align="left">🟡 Lawyer</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">59.5%</td>
<td align="right">25.0%</td>
<td align="right">27.7%</td>
<td align="right">16.9%</td>
<td align="right">13.4%</td>
<td align="right">403</td>
</tr>
<tr>
<td align="left">891</td>
<td align="left">🟡 Blinder</td>
<td align="right"><b>1499</b></td>
<td align="right">22.2%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">21.1%</td>
<td align="right">24.0%</td>
<td align="right">21.7%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">892</td>
<td align="left">🟡 Tempest_Alt2</td>
<td align="right"><b>1499</b></td>
<td align="right">22.2%</td>
<td align="right">28.6%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">30.0%</td>
<td align="right">7.4%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">893</td>
<td align="left">🟡 Radiant</td>
<td align="right"><b>1499</b></td>
<td align="right">22.2%</td>
<td align="right">42.9%</td>
<td align="right">33.3%</td>
<td align="right">38.5%</td>
<td align="right">15.8%</td>
<td align="right">4.8%</td>
<td align="right">72</td>
</tr>
<tr>
<td align="left">894</td>
<td align="left">🟡 Gust</td>
<td align="right"><b>1499</b></td>
<td align="right">22.2%</td>
<td align="right">50.0%</td>
<td align="right">12.5%</td>
<td align="right">18.8%</td>
<td align="right">19.0%</td>
<td align="right">21.4%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">895</td>
<td align="left">🟡 Tenacious</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">50.0%</td>
<td align="right">35.2%</td>
<td align="right">22.0%</td>
<td align="right">21.8%</td>
<td align="right">11.2%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">896</td>
<td align="left">🟡 Frontier</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">50.0%</td>
<td align="right">33.8%</td>
<td align="right">29.2%</td>
<td align="right">19.6%</td>
<td align="right">8.3%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">897</td>
<td align="left">🟡 Overclocked</td>
<td align="right"><b>1498</b></td>
<td align="right">24.1%</td>
<td align="right">60.8%</td>
<td align="right">28.8%</td>
<td align="right">26.0%</td>
<td align="right">16.4%</td>
<td align="right">12.5%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">898</td>
<td align="left">🟡 Breeder</td>
<td align="right"><b>1498</b></td>
<td align="right">23.3%</td>
<td align="right">55.3%</td>
<td align="right">30.9%</td>
<td align="right">25.4%</td>
<td align="right">12.7%</td>
<td align="right">18.4%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">899</td>
<td align="left">🟡 Reformer</td>
<td align="right"><b>1498</b></td>
<td align="right">24.5%</td>
<td align="right">50.0%</td>
<td align="right">41.1%</td>
<td align="right">23.5%</td>
<td align="right">19.1%</td>
<td align="right">10.7%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">900</td>
<td align="left">🟡 Evolver</td>
<td align="right"><b>1498</b></td>
<td align="right">23.2%</td>
<td align="right">65.7%</td>
<td align="right">29.4%</td>
<td align="right">18.8%</td>
<td align="right">19.8%</td>
<td align="right">16.0%</td>
<td align="right">475</td>
</tr>
<tr>
<td align="left">901</td>
<td align="left">🟡 Squatter</td>
<td align="right"><b>1498</b></td>
<td align="right">22.3%</td>
<td align="right">38.1%</td>
<td align="right">30.0%</td>
<td align="right">17.4%</td>
<td align="right">19.8%</td>
<td align="right">17.5%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">902</td>
<td align="left">🟡 Doubler</td>
<td align="right"><b>1498</b></td>
<td align="right">23.4%</td>
<td align="right">42.2%</td>
<td align="right">32.3%</td>
<td align="right">21.8%</td>
<td align="right">22.6%</td>
<td align="right">13.0%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">903</td>
<td align="left">🟡 Particle</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">43.2%</td>
<td align="right">37.8%</td>
<td align="right">24.5%</td>
<td align="right">14.3%</td>
<td align="right">14.8%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">904</td>
<td align="left">🟡 Thorn</td>
<td align="right"><b>1498</b></td>
<td align="right">22.1%</td>
<td align="right">50.0%</td>
<td align="right">18.2%</td>
<td align="right">9.1%</td>
<td align="right">15.8%</td>
<td align="right">26.7%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">905</td>
<td align="left">🟡 Galaxy</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">43.5%</td>
<td align="right">40.0%</td>
<td align="right">20.5%</td>
<td align="right">20.0%</td>
<td align="right">11.8%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">906</td>
<td align="left">🟡 Nymph</td>
<td align="right"><b>1498</b></td>
<td align="right">25.1%</td>
<td align="right">66.7%</td>
<td align="right">24.6%</td>
<td align="right">24.7%</td>
<td align="right">23.3%</td>
<td align="right">9.3%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">907</td>
<td align="left">🟡 Minimizer</td>
<td align="right"><b>1498</b></td>
<td align="right">22.1%</td>
<td align="right">71.4%</td>
<td align="right">22.2%</td>
<td align="right">25.0%</td>
<td align="right">8.7%</td>
<td align="right">17.6%</td>
<td align="right">68</td>
</tr>
<tr>
<td align="left">908</td>
<td align="left">🟡 Distorter</td>
<td align="right"><b>1498</b></td>
<td align="right">24.0%</td>
<td align="right">42.0%</td>
<td align="right">40.4%</td>
<td align="right">25.7%</td>
<td align="right">20.0%</td>
<td align="right">14.5%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">909</td>
<td align="left">🟡 Autocrat</td>
<td align="right"><b>1498</b></td>
<td align="right">22.6%</td>
<td align="right">45.2%</td>
<td align="right">27.4%</td>
<td align="right">32.2%</td>
<td align="right">14.2%</td>
<td align="right">13.8%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">910</td>
<td align="left">🟡 Earl</td>
<td align="right"><b>1498</b></td>
<td align="right">24.5%</td>
<td align="right">50.0%</td>
<td align="right">27.9%</td>
<td align="right">25.3%</td>
<td align="right">18.0%</td>
<td align="right">18.4%</td>
<td align="right">473</td>
</tr>
<tr>
<td align="left">911</td>
<td align="left">🟡 Grifter</td>
<td align="right"><b>1498</b></td>
<td align="right">24.2%</td>
<td align="right">44.0%</td>
<td align="right">33.8%</td>
<td align="right">29.1%</td>
<td align="right">15.5%</td>
<td align="right">13.4%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">912</td>
<td align="left">🟡 Wager</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">37.0%</td>
<td align="right">29.9%</td>
<td align="right">24.0%</td>
<td align="right">18.3%</td>
<td align="right">15.7%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">913</td>
<td align="left">🟡 Commando</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">51.1%</td>
<td align="right">26.9%</td>
<td align="right">30.7%</td>
<td align="right">17.9%</td>
<td align="right">7.5%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">914</td>
<td align="left">🟡 Spartan</td>
<td align="right"><b>1498</b></td>
<td align="right">23.3%</td>
<td align="right">52.1%</td>
<td align="right">27.9%</td>
<td align="right">23.5%</td>
<td align="right">18.1%</td>
<td align="right">14.4%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">915</td>
<td align="left">🟡 Equalizer</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">43.8%</td>
<td align="right">36.7%</td>
<td align="right">20.0%</td>
<td align="right">23.1%</td>
<td align="right">11.1%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">916</td>
<td align="left">🟡 Expander_Alt</td>
<td align="right"><b>1498</b></td>
<td align="right">22.1%</td>
<td align="right">46.8%</td>
<td align="right">21.7%</td>
<td align="right">26.5%</td>
<td align="right">20.6%</td>
<td align="right">11.7%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">917</td>
<td align="left">🟡 Empath_Alt</td>
<td align="right"><b>1498</b></td>
<td align="right">24.2%</td>
<td align="right">44.7%</td>
<td align="right">33.3%</td>
<td align="right">27.1%</td>
<td align="right">18.3%</td>
<td align="right">16.2%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">918</td>
<td align="left">🟡 Magnet</td>
<td align="right"><b>1498</b></td>
<td align="right">21.8%</td>
<td align="right">45.7%</td>
<td align="right">25.0%</td>
<td align="right">24.0%</td>
<td align="right">19.1%</td>
<td align="right">12.9%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">919</td>
<td align="left">🟡 Multiplier</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">51.9%</td>
<td align="right">27.6%</td>
<td align="right">24.6%</td>
<td align="right">14.9%</td>
<td align="right">16.2%</td>
<td align="right">462</td>
</tr>
<tr>
<td align="left">920</td>
<td align="left">🟡 Arcade</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">43.9%</td>
<td align="right">33.3%</td>
<td align="right">28.2%</td>
<td align="right">20.6%</td>
<td align="right">13.5%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">921</td>
<td align="left">🟡 Messenger</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">47.8%</td>
<td align="right">36.0%</td>
<td align="right">28.6%</td>
<td align="right">20.0%</td>
<td align="right">16.7%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">922</td>
<td align="left">🟡 Djinn</td>
<td align="right"><b>1498</b></td>
<td align="right">22.6%</td>
<td align="right">38.6%</td>
<td align="right">27.0%</td>
<td align="right">23.0%</td>
<td align="right">18.1%</td>
<td align="right">19.0%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">923</td>
<td align="left">🟡 Lunatic</td>
<td align="right"><b>1498</b></td>
<td align="right">23.1%</td>
<td align="right">61.4%</td>
<td align="right">28.4%</td>
<td align="right">21.4%</td>
<td align="right">20.0%</td>
<td align="right">12.3%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">924</td>
<td align="left">🟡 Vandal</td>
<td align="right"><b>1498</b></td>
<td align="right">22.5%</td>
<td align="right">55.3%</td>
<td align="right">20.0%</td>
<td align="right">28.0%</td>
<td align="right">15.7%</td>
<td align="right">13.8%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">925</td>
<td align="left">🟡 Overload</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">54.0%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">17.9%</td>
<td align="right">14.4%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">926</td>
<td align="left">🟡 Constellation</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">43.1%</td>
<td align="right">23.6%</td>
<td align="right">29.1%</td>
<td align="right">20.2%</td>
<td align="right">13.9%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">927</td>
<td align="left">🟡 Disorder</td>
<td align="right"><b>1498</b></td>
<td align="right">23.4%</td>
<td align="right">45.9%</td>
<td align="right">21.7%</td>
<td align="right">27.8%</td>
<td align="right">19.4%</td>
<td align="right">18.8%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">928</td>
<td align="left">🟡 Profiteer</td>
<td align="right"><b>1498</b></td>
<td align="right">23.7%</td>
<td align="right">49.1%</td>
<td align="right">34.0%</td>
<td align="right">27.6%</td>
<td align="right">18.1%</td>
<td align="right">12.7%</td>
<td align="right">448</td>
</tr>
<tr>
<td align="left">929</td>
<td align="left">🟡 Embargo</td>
<td align="right"><b>1498</b></td>
<td align="right">24.6%</td>
<td align="right">45.5%</td>
<td align="right">32.6%</td>
<td align="right">28.9%</td>
<td align="right">21.9%</td>
<td align="right">14.9%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">930</td>
<td align="left">🟡 Economist</td>
<td align="right"><b>1498</b></td>
<td align="right">21.6%</td>
<td align="right">83.3%</td>
<td align="right">42.9%</td>
<td align="right">20.0%</td>
<td align="right">5.9%</td>
<td align="right">13.8%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">931</td>
<td align="left">🟡 Primal</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">55.6%</td>
<td align="right">34.5%</td>
<td align="right">23.6%</td>
<td align="right">11.5%</td>
<td align="right">14.5%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">932</td>
<td align="left">🟡 Stealthy</td>
<td align="right"><b>1498</b></td>
<td align="right">24.4%</td>
<td align="right">55.0%</td>
<td align="right">36.2%</td>
<td align="right">22.4%</td>
<td align="right">21.2%</td>
<td align="right">14.8%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">933</td>
<td align="left">🟡 Jester</td>
<td align="right"><b>1498</b></td>
<td align="right">23.3%</td>
<td align="right">60.0%</td>
<td align="right">34.2%</td>
<td align="right">27.0%</td>
<td align="right">17.3%</td>
<td align="right">17.2%</td>
<td align="right">1855</td>
</tr>
<tr>
<td align="left">934</td>
<td align="left">🟡 Glutton</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">60.4%</td>
<td align="right">30.5%</td>
<td align="right">25.5%</td>
<td align="right">20.0%</td>
<td align="right">16.3%</td>
<td align="right">1832</td>
</tr>
<tr>
<td align="left">935</td>
<td align="left">🟡 Seedling</td>
<td align="right"><b>1498</b></td>
<td align="right">22.9%</td>
<td align="right">50.0%</td>
<td align="right">38.2%</td>
<td align="right">22.8%</td>
<td align="right">13.8%</td>
<td align="right">14.4%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">936</td>
<td align="left">🟡 Robot</td>
<td align="right"><b>1498</b></td>
<td align="right">24.6%</td>
<td align="right">42.9%</td>
<td align="right">39.5%</td>
<td align="right">23.2%</td>
<td align="right">20.4%</td>
<td align="right">14.0%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">937</td>
<td align="left">🟡 Odds</td>
<td align="right"><b>1498</b></td>
<td align="right">23.3%</td>
<td align="right">54.3%</td>
<td align="right">38.8%</td>
<td align="right">18.5%</td>
<td align="right">17.8%</td>
<td align="right">13.9%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">938</td>
<td align="left">🟡 Dealer</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">45.9%</td>
<td align="right">21.1%</td>
<td align="right">26.9%</td>
<td align="right">20.6%</td>
<td align="right">22.5%</td>
<td align="right">417</td>
</tr>
<tr>
<td align="left">939</td>
<td align="left">🟡 Blizzard</td>
<td align="right"><b>1498</b></td>
<td align="right">23.4%</td>
<td align="right">48.9%</td>
<td align="right">20.0%</td>
<td align="right">20.4%</td>
<td align="right">19.8%</td>
<td align="right">20.2%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">940</td>
<td align="left">🟡 Augur</td>
<td align="right"><b>1498</b></td>
<td align="right">24.1%</td>
<td align="right">56.9%</td>
<td align="right">28.4%</td>
<td align="right">18.3%</td>
<td align="right">20.7%</td>
<td align="right">15.3%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">941</td>
<td align="left">🟡 Piercer</td>
<td align="right"><b>1498</b></td>
<td align="right">21.0%</td>
<td align="right">48.9%</td>
<td align="right">25.8%</td>
<td align="right">22.1%</td>
<td align="right">19.0%</td>
<td align="right">10.5%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">942</td>
<td align="left">🟡 Quorum</td>
<td align="right"><b>1498</b></td>
<td align="right">24.3%</td>
<td align="right">48.6%</td>
<td align="right">36.8%</td>
<td align="right">24.5%</td>
<td align="right">19.4%</td>
<td align="right">15.2%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">943</td>
<td align="left">🟡 Throwback</td>
<td align="right"><b>1498</b></td>
<td align="right">23.0%</td>
<td align="right">31.2%</td>
<td align="right">36.6%</td>
<td align="right">28.7%</td>
<td align="right">18.2%</td>
<td align="right">13.9%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">944</td>
<td align="left">🟡 Gatherer</td>
<td align="right"><b>1498</b></td>
<td align="right">22.5%</td>
<td align="right">42.5%</td>
<td align="right">37.1%</td>
<td align="right">25.6%</td>
<td align="right">18.3%</td>
<td align="right">13.0%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">945</td>
<td align="left">🟡 Anglerfish</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">36.2%</td>
<td align="right">36.4%</td>
<td align="right">30.6%</td>
<td align="right">16.7%</td>
<td align="right">10.7%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">946</td>
<td align="left">🟡 Recall</td>
<td align="right"><b>1498</b></td>
<td align="right">21.3%</td>
<td align="right">71.4%</td>
<td align="right">28.6%</td>
<td align="right">21.4%</td>
<td align="right">9.1%</td>
<td align="right">10.3%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">947</td>
<td align="left">🟡 Onyx</td>
<td align="right"><b>1498</b></td>
<td align="right">23.0%</td>
<td align="right">50.0%</td>
<td align="right">29.7%</td>
<td align="right">21.1%</td>
<td align="right">14.7%</td>
<td align="right">18.4%</td>
<td align="right">404</td>
</tr>
<tr>
<td align="left">948</td>
<td align="left">🟡 Swimmer</td>
<td align="right"><b>1498</b></td>
<td align="right">21.3%</td>
<td align="right">16.7%</td>
<td align="right">40.0%</td>
<td align="right">31.2%</td>
<td align="right">0.0%</td>
<td align="right">26.3%</td>
<td align="right">61</td>
</tr>
<tr>
<td align="left">949</td>
<td align="left">🟡 Starfish</td>
<td align="right"><b>1498</b></td>
<td align="right">23.2%</td>
<td align="right">41.0%</td>
<td align="right">31.1%</td>
<td align="right">23.5%</td>
<td align="right">20.2%</td>
<td align="right">16.0%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">950</td>
<td align="left">🟡 Spreader</td>
<td align="right"><b>1498</b></td>
<td align="right">23.0%</td>
<td align="right">48.7%</td>
<td align="right">31.8%</td>
<td align="right">23.2%</td>
<td align="right">19.2%</td>
<td align="right">14.7%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">951</td>
<td align="left">🟡 Mentalist</td>
<td align="right"><b>1498</b></td>
<td align="right">23.0%</td>
<td align="right">36.0%</td>
<td align="right">39.2%</td>
<td align="right">22.9%</td>
<td align="right">13.5%</td>
<td align="right">18.1%</td>
<td align="right">473</td>
</tr>
<tr>
<td align="left">952</td>
<td align="left">🟡 Violinist</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">26.5%</td>
<td align="right">30.4%</td>
<td align="right">31.2%</td>
<td align="right">18.3%</td>
<td align="right">16.2%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">953</td>
<td align="left">🟡 Arcane</td>
<td align="right"><b>1498</b></td>
<td align="right">23.0%</td>
<td align="right">46.3%</td>
<td align="right">25.4%</td>
<td align="right">26.4%</td>
<td align="right">19.0%</td>
<td align="right">15.6%</td>
<td align="right">409</td>
</tr>
<tr>
<td align="left">954</td>
<td align="left">🟡 Clockwork</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">53.8%</td>
<td align="right">35.4%</td>
<td align="right">17.4%</td>
<td align="right">16.5%</td>
<td align="right">13.8%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">955</td>
<td align="left">🟡 Eidolon</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">47.9%</td>
<td align="right">38.6%</td>
<td align="right">16.4%</td>
<td align="right">20.0%</td>
<td align="right">16.9%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">956</td>
<td align="left">🟡 Researcher</td>
<td align="right"><b>1498</b></td>
<td align="right">21.2%</td>
<td align="right">66.7%</td>
<td align="right">50.0%</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
<td align="right">10.5%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">957</td>
<td align="left">🟡 Lullaby</td>
<td align="right"><b>1498</b></td>
<td align="right">21.2%</td>
<td align="right">28.6%</td>
<td align="right">28.6%</td>
<td align="right">54.5%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">958</td>
<td align="left">🟡 Chaser</td>
<td align="right"><b>1498</b></td>
<td align="right">22.6%</td>
<td align="right">44.2%</td>
<td align="right">24.6%</td>
<td align="right">23.8%</td>
<td align="right">19.8%</td>
<td align="right">16.9%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">959</td>
<td align="left">🟡 Swindler</td>
<td align="right"><b>1498</b></td>
<td align="right">23.3%</td>
<td align="right">48.6%</td>
<td align="right">34.0%</td>
<td align="right">15.4%</td>
<td align="right">21.1%</td>
<td align="right">19.5%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">960</td>
<td align="left">🟡 Pawnbroker</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">62.9%</td>
<td align="right">32.7%</td>
<td align="right">24.5%</td>
<td align="right">19.6%</td>
<td align="right">8.0%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">961</td>
<td align="left">🟡 Breeze_Alt</td>
<td align="right"><b>1498</b></td>
<td align="right">21.2%</td>
<td align="right">20.0%</td>
<td align="right">40.0%</td>
<td align="right">12.5%</td>
<td align="right">24.0%</td>
<td align="right">17.2%</td>
<td align="right">85</td>
</tr>
<tr>
<td align="left">962</td>
<td align="left">🟡 Uniter</td>
<td align="right"><b>1498</b></td>
<td align="right">25.0%</td>
<td align="right">60.0%</td>
<td align="right">38.7%</td>
<td align="right">27.7%</td>
<td align="right">12.7%</td>
<td align="right">18.1%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">963</td>
<td align="left">🟡 Supplier</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">47.6%</td>
<td align="right">31.9%</td>
<td align="right">25.6%</td>
<td align="right">17.5%</td>
<td align="right">15.4%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">964</td>
<td align="left">🟡 Supernova</td>
<td align="right"><b>1498</b></td>
<td align="right">24.2%</td>
<td align="right">45.0%</td>
<td align="right">37.7%</td>
<td align="right">21.1%</td>
<td align="right">16.8%</td>
<td align="right">17.8%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">965</td>
<td align="left">🟡 Persist</td>
<td align="right"><b>1498</b></td>
<td align="right">21.6%</td>
<td align="right">48.8%</td>
<td align="right">25.9%</td>
<td align="right">23.0%</td>
<td align="right">13.3%</td>
<td align="right">16.1%</td>
<td align="right">398</td>
</tr>
<tr>
<td align="left">966</td>
<td align="left">🟡 FireDancer</td>
<td align="right"><b>1498</b></td>
<td align="right">22.4%</td>
<td align="right">54.5%</td>
<td align="right">30.0%</td>
<td align="right">19.4%</td>
<td align="right">18.9%</td>
<td align="right">11.3%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">967</td>
<td align="left">🟡 Clairvoyant</td>
<td align="right"><b>1498</b></td>
<td align="right">23.2%</td>
<td align="right">55.6%</td>
<td align="right">36.1%</td>
<td align="right">19.8%</td>
<td align="right">15.7%</td>
<td align="right">13.2%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">968</td>
<td align="left">🟡 Yardmaster</td>
<td align="right"><b>1498</b></td>
<td align="right">23.2%</td>
<td align="right">48.9%</td>
<td align="right">29.7%</td>
<td align="right">16.9%</td>
<td align="right">21.8%</td>
<td align="right">16.2%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">969</td>
<td align="left">🟡 Iron</td>
<td align="right"><b>1498</b></td>
<td align="right">21.0%</td>
<td align="right">55.6%</td>
<td align="right">22.2%</td>
<td align="right">28.6%</td>
<td align="right">18.2%</td>
<td align="right">7.4%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">970</td>
<td align="left">🟡 Wormhole</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">40.4%</td>
<td align="right">34.3%</td>
<td align="right">16.2%</td>
<td align="right">22.0%</td>
<td align="right">17.8%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">971</td>
<td align="left">🟡 Greenhorn</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">61.5%</td>
<td align="right">24.6%</td>
<td align="right">21.6%</td>
<td align="right">21.4%</td>
<td align="right">13.6%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">972</td>
<td align="left">🟡 Entangler</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">52.5%</td>
<td align="right">21.9%</td>
<td align="right">22.5%</td>
<td align="right">20.6%</td>
<td align="right">19.5%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">973</td>
<td align="left">🟡 Scientist_Alt</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">46.3%</td>
<td align="right">28.0%</td>
<td align="right">31.4%</td>
<td align="right">24.0%</td>
<td align="right">7.6%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">974</td>
<td align="left">🟡 Artist</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">53.1%</td>
<td align="right">32.8%</td>
<td align="right">17.1%</td>
<td align="right">20.0%</td>
<td align="right">13.3%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">975</td>
<td align="left">🟡 Shade_Alt</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">54.3%</td>
<td align="right">37.1%</td>
<td align="right">27.7%</td>
<td align="right">18.4%</td>
<td align="right">12.1%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">976</td>
<td align="left">🟡 Comet</td>
<td align="right"><b>1498</b></td>
<td align="right">23.0%</td>
<td align="right">53.1%</td>
<td align="right">30.3%</td>
<td align="right">26.2%</td>
<td align="right">18.0%</td>
<td align="right">10.4%</td>
<td align="right">474</td>
</tr>
<tr>
<td align="left">977</td>
<td align="left">🟡 Glow</td>
<td align="right"><b>1498</b></td>
<td align="right">20.9%</td>
<td align="right">37.5%</td>
<td align="right">46.7%</td>
<td align="right">23.1%</td>
<td align="right">4.8%</td>
<td align="right">14.7%</td>
<td align="right">91</td>
</tr>
<tr>
<td align="left">978</td>
<td align="left">🟡 Draft</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">35.1%</td>
<td align="right">30.8%</td>
<td align="right">18.3%</td>
<td align="right">24.8%</td>
<td align="right">14.8%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">979</td>
<td align="left">🟡 Devourer</td>
<td align="right"><b>1498</b></td>
<td align="right">22.9%</td>
<td align="right">50.0%</td>
<td align="right">31.4%</td>
<td align="right">25.3%</td>
<td align="right">18.4%</td>
<td align="right">11.2%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">980</td>
<td align="left">🟡 Mesmerist</td>
<td align="right"><b>1498</b></td>
<td align="right">23.6%</td>
<td align="right">43.9%</td>
<td align="right">43.8%</td>
<td align="right">18.7%</td>
<td align="right">16.1%</td>
<td align="right">17.4%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">981</td>
<td align="left">🟡 Shielder</td>
<td align="right"><b>1498</b></td>
<td align="right">21.1%</td>
<td align="right">44.7%</td>
<td align="right">30.8%</td>
<td align="right">19.0%</td>
<td align="right">20.8%</td>
<td align="right">12.6%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">982</td>
<td align="left">🟡 Sprout</td>
<td align="right"><b>1498</b></td>
<td align="right">20.8%</td>
<td align="right">80.0%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">9.5%</td>
<td align="right">9.1%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">983</td>
<td align="left">🟡 Reflector</td>
<td align="right"><b>1498</b></td>
<td align="right">23.7%</td>
<td align="right">29.3%</td>
<td align="right">30.0%</td>
<td align="right">21.7%</td>
<td align="right">19.4%</td>
<td align="right">23.0%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">984</td>
<td align="left">🟡 Wielder</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">40.7%</td>
<td align="right">26.4%</td>
<td align="right">28.7%</td>
<td align="right">16.4%</td>
<td align="right">14.4%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">985</td>
<td align="left">🟡 Monarch</td>
<td align="right"><b>1498</b></td>
<td align="right">22.4%</td>
<td align="right">46.2%</td>
<td align="right">36.1%</td>
<td align="right">25.0%</td>
<td align="right">14.3%</td>
<td align="right">12.3%</td>
<td align="right">392</td>
</tr>
<tr>
<td align="left">986</td>
<td align="left">🟡 Sparkle</td>
<td align="right"><b>1498</b></td>
<td align="right">20.7%</td>
<td align="right">33.3%</td>
<td align="right">21.4%</td>
<td align="right">5.3%</td>
<td align="right">31.6%</td>
<td align="right">20.8%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">987</td>
<td align="left">🟡 Mirage</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">44.7%</td>
<td align="right">29.4%</td>
<td align="right">28.2%</td>
<td align="right">17.3%</td>
<td align="right">15.5%</td>
<td align="right">461</td>
</tr>
<tr>
<td align="left">988</td>
<td align="left">🟡 Crab</td>
<td align="right"><b>1498</b></td>
<td align="right">24.1%</td>
<td align="right">42.2%</td>
<td align="right">35.1%</td>
<td align="right">24.3%</td>
<td align="right">20.7%</td>
<td align="right">13.0%</td>
<td align="right">399</td>
</tr>
<tr>
<td align="left">989</td>
<td align="left">🟡 Tripwire</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">43.5%</td>
<td align="right">33.3%</td>
<td align="right">15.8%</td>
<td align="right">23.1%</td>
<td align="right">12.9%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">990</td>
<td align="left">🟡 Barbarian</td>
<td align="right"><b>1497</b></td>
<td align="right">22.4%</td>
<td align="right">37.5%</td>
<td align="right">29.4%</td>
<td align="right">25.8%</td>
<td align="right">21.2%</td>
<td align="right">16.7%</td>
<td align="right">2411</td>
</tr>
<tr>
<td align="left">991</td>
<td align="left">🟡 Mi_Go</td>
<td align="right"><b>1497</b></td>
<td align="right">23.8%</td>
<td align="right">60.0%</td>
<td align="right">29.5%</td>
<td align="right">21.9%</td>
<td align="right">19.4%</td>
<td align="right">15.5%</td>
<td align="right">261</td>
</tr>
<tr>
<td align="left">992</td>
<td align="left">🟡 Sapphire</td>
<td align="right"><b>1497</b></td>
<td align="right">24.4%</td>
<td align="right">52.8%</td>
<td align="right">23.4%</td>
<td align="right">25.3%</td>
<td align="right">22.1%</td>
<td align="right">15.2%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">993</td>
<td align="left">🟡 Storm</td>
<td align="right"><b>1497</b></td>
<td align="right">23.5%</td>
<td align="right">53.2%</td>
<td align="right">19.4%</td>
<td align="right">24.0%</td>
<td align="right">19.5%</td>
<td align="right">18.2%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">994</td>
<td align="left">🟡 Master_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">22.8%</td>
<td align="right">46.7%</td>
<td align="right">41.9%</td>
<td align="right">19.6%</td>
<td align="right">15.0%</td>
<td align="right">13.7%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">995</td>
<td align="left">🟡 Grass</td>
<td align="right"><b>1497</b></td>
<td align="right">20.5%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">11.8%</td>
<td align="right">73</td>
</tr>
<tr>
<td align="left">996</td>
<td align="left">🟡 Imperator</td>
<td align="right"><b>1497</b></td>
<td align="right">24.4%</td>
<td align="right">42.0%</td>
<td align="right">33.3%</td>
<td align="right">30.8%</td>
<td align="right">18.0%</td>
<td align="right">12.5%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">997</td>
<td align="left">🟡 Pirate</td>
<td align="right"><b>1497</b></td>
<td align="right">22.3%</td>
<td align="right">52.4%</td>
<td align="right">32.1%</td>
<td align="right">21.3%</td>
<td align="right">20.8%</td>
<td align="right">17.8%</td>
<td align="right">2457</td>
</tr>
<tr>
<td align="left">998</td>
<td align="left">🟡 Swarm_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">47.6%</td>
<td align="right">26.2%</td>
<td align="right">24.1%</td>
<td align="right">15.8%</td>
<td align="right">16.9%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">999</td>
<td align="left">🟡 Mimic</td>
<td align="right"><b>1497</b></td>
<td align="right">22.8%</td>
<td align="right">45.5%</td>
<td align="right">34.5%</td>
<td align="right">25.4%</td>
<td align="right">20.7%</td>
<td align="right">15.6%</td>
<td align="right">2471</td>
</tr>
<tr>
<td align="left">1000</td>
<td align="left">🟡 Survivor_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">23.9%</td>
<td align="right">45.8%</td>
<td align="right">31.2%</td>
<td align="right">19.0%</td>
<td align="right">18.9%</td>
<td align="right">19.3%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">1001</td>
<td align="left">🟡 Fraud</td>
<td align="right"><b>1497</b></td>
<td align="right">24.0%</td>
<td align="right">36.7%</td>
<td align="right">36.6%</td>
<td align="right">28.1%</td>
<td align="right">19.0%</td>
<td align="right">16.4%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">1002</td>
<td align="left">🟡 Doppelganger</td>
<td align="right"><b>1497</b></td>
<td align="right">21.8%</td>
<td align="right">42.6%</td>
<td align="right">26.9%</td>
<td align="right">27.1%</td>
<td align="right">21.0%</td>
<td align="right">14.9%</td>
<td align="right">1845</td>
</tr>
<tr>
<td align="left">1003</td>
<td align="left">🟡 Evade</td>
<td align="right"><b>1497</b></td>
<td align="right">22.0%</td>
<td align="right">51.0%</td>
<td align="right">38.1%</td>
<td align="right">17.3%</td>
<td align="right">16.4%</td>
<td align="right">12.3%</td>
<td align="right">469</td>
</tr>
<tr>
<td align="left">1004</td>
<td align="left">🟡 Chaos_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">25.2%</td>
<td align="right">47.5%</td>
<td align="right">29.7%</td>
<td align="right">30.3%</td>
<td align="right">20.0%</td>
<td align="right">17.3%</td>
<td align="right">408</td>
</tr>
<tr>
<td align="left">1005</td>
<td align="left">🟡 Sender</td>
<td align="right"><b>1497</b></td>
<td align="right">23.2%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">24.2%</td>
<td align="right">24.3%</td>
<td align="right">14.9%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">1006</td>
<td align="left">🟡 Rusher</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">51.1%</td>
<td align="right">26.2%</td>
<td align="right">22.7%</td>
<td align="right">19.7%</td>
<td align="right">12.9%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">1007</td>
<td align="left">🟡 Viceroy</td>
<td align="right"><b>1497</b></td>
<td align="right">22.1%</td>
<td align="right">51.2%</td>
<td align="right">25.4%</td>
<td align="right">20.6%</td>
<td align="right">17.2%</td>
<td align="right">16.3%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">1008</td>
<td align="left">🟡 Miner_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">23.7%</td>
<td align="right">47.1%</td>
<td align="right">20.7%</td>
<td align="right">27.5%</td>
<td align="right">20.2%</td>
<td align="right">17.3%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">1009</td>
<td align="left">🟡 Grandmaster</td>
<td align="right"><b>1497</b></td>
<td align="right">20.3%</td>
<td align="right">25.0%</td>
<td align="right">42.9%</td>
<td align="right">16.7%</td>
<td align="right">28.6%</td>
<td align="right">7.7%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">1010</td>
<td align="left">🟡 Boxer</td>
<td align="right"><b>1497</b></td>
<td align="right">20.3%</td>
<td align="right">28.6%</td>
<td align="right">28.6%</td>
<td align="right">25.0%</td>
<td align="right">11.8%</td>
<td align="right">12.5%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">1011</td>
<td align="left">🟡 Encircle</td>
<td align="right"><b>1497</b></td>
<td align="right">20.3%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">1012</td>
<td align="left">🟡 Howler</td>
<td align="right"><b>1497</b></td>
<td align="right">20.3%</td>
<td align="right">66.7%</td>
<td align="right">38.5%</td>
<td align="right">18.8%</td>
<td align="right">14.8%</td>
<td align="right">10.0%</td>
<td align="right">79</td>
</tr>
<tr>
<td align="left">1013</td>
<td align="left">🟡 Blocker_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">21.5%</td>
<td align="right">51.9%</td>
<td align="right">23.8%</td>
<td align="right">19.8%</td>
<td align="right">21.2%</td>
<td align="right">10.1%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">1014</td>
<td align="left">🟡 Dragon</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">48.0%</td>
<td align="right">33.3%</td>
<td align="right">20.3%</td>
<td align="right">20.8%</td>
<td align="right">18.1%</td>
<td align="right">2474</td>
</tr>
<tr>
<td align="left">1015</td>
<td align="left">🟡 Eternity</td>
<td align="right"><b>1497</b></td>
<td align="right">22.2%</td>
<td align="right">53.7%</td>
<td align="right">30.9%</td>
<td align="right">14.3%</td>
<td align="right">18.3%</td>
<td align="right">14.4%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">1016</td>
<td align="left">🟡 Seller</td>
<td align="right"><b>1497</b></td>
<td align="right">23.1%</td>
<td align="right">32.5%</td>
<td align="right">32.1%</td>
<td align="right">26.1%</td>
<td align="right">24.2%</td>
<td align="right">13.3%</td>
<td align="right">412</td>
</tr>
<tr>
<td align="left">1017</td>
<td align="left">🟡 Multitude</td>
<td align="right"><b>1497</b></td>
<td align="right">23.7%</td>
<td align="right">44.2%</td>
<td align="right">40.8%</td>
<td align="right">21.1%</td>
<td align="right">16.4%</td>
<td align="right">15.9%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">1018</td>
<td align="left">🟡 Mermaid</td>
<td align="right"><b>1497</b></td>
<td align="right">22.1%</td>
<td align="right">37.5%</td>
<td align="right">31.6%</td>
<td align="right">27.4%</td>
<td align="right">17.0%</td>
<td align="right">11.7%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">1019</td>
<td align="left">🟡 Eavesdropper</td>
<td align="right"><b>1497</b></td>
<td align="right">23.0%</td>
<td align="right">46.5%</td>
<td align="right">32.7%</td>
<td align="right">25.9%</td>
<td align="right">18.5%</td>
<td align="right">13.4%</td>
<td align="right">408</td>
</tr>
<tr>
<td align="left">1020</td>
<td align="left">🟡 Wildcard</td>
<td align="right"><b>1497</b></td>
<td align="right">22.4%</td>
<td align="right">38.1%</td>
<td align="right">39.7%</td>
<td align="right">20.7%</td>
<td align="right">19.6%</td>
<td align="right">14.0%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">1021</td>
<td align="left">🟡 Saboteur</td>
<td align="right"><b>1497</b></td>
<td align="right">23.2%</td>
<td align="right">41.9%</td>
<td align="right">38.5%</td>
<td align="right">33.3%</td>
<td align="right">15.7%</td>
<td align="right">11.2%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">1022</td>
<td align="left">🟡 Quake</td>
<td align="right"><b>1497</b></td>
<td align="right">23.7%</td>
<td align="right">50.0%</td>
<td align="right">36.4%</td>
<td align="right">18.9%</td>
<td align="right">16.4%</td>
<td align="right">20.2%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">1023</td>
<td align="left">🟡 Cloaker</td>
<td align="right"><b>1497</b></td>
<td align="right">23.3%</td>
<td align="right">57.9%</td>
<td align="right">32.0%</td>
<td align="right">19.8%</td>
<td align="right">15.1%</td>
<td align="right">17.1%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">1024</td>
<td align="left">🟡 Mainframe</td>
<td align="right"><b>1497</b></td>
<td align="right">22.5%</td>
<td align="right">43.2%</td>
<td align="right">33.9%</td>
<td align="right">21.6%</td>
<td align="right">17.3%</td>
<td align="right">15.6%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">1025</td>
<td align="left">🟡 Jeweler</td>
<td align="right"><b>1497</b></td>
<td align="right">21.9%</td>
<td align="right">50.0%</td>
<td align="right">22.2%</td>
<td align="right">27.5%</td>
<td align="right">16.5%</td>
<td align="right">15.3%</td>
<td align="right">466</td>
</tr>
<tr>
<td align="left">1026</td>
<td align="left">🟡 Zinc</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">30.0%</td>
<td align="right">25.0%</td>
<td align="right">10.0%</td>
<td align="right">5.9%</td>
<td align="right">26.9%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">1027</td>
<td align="left">🟡 Vine</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">22.2%</td>
<td align="right">14.3%</td>
<td align="right">14.3%</td>
<td align="right">90</td>
</tr>
<tr>
<td align="left">1028</td>
<td align="left">🟡 Spotlight</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">66.7%</td>
<td align="right">21.4%</td>
<td align="right">25.0%</td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">1029</td>
<td align="left">🟡 Choir</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">60.0%</td>
<td align="right">25.0%</td>
<td align="right">12.5%</td>
<td align="right">16.7%</td>
<td align="right">17.4%</td>
<td align="right">70</td>
</tr>
<tr>
<td align="left">1030</td>
<td align="left">🟡 Aluminum</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">42.9%</td>
<td align="right">25.0%</td>
<td align="right">14.3%</td>
<td align="right">18.8%</td>
<td align="right">16.7%</td>
<td align="right">65</td>
</tr>
<tr>
<td align="left">1031</td>
<td align="left">🟡 Cardsharp</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">66.7%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">13.0%</td>
<td align="right">4.2%</td>
<td align="right">80</td>
</tr>
<tr>
<td align="left">1032</td>
<td align="left">🟡 Firewall</td>
<td align="right"><b>1497</b></td>
<td align="right">23.7%</td>
<td align="right">42.6%</td>
<td align="right">29.8%</td>
<td align="right">25.0%</td>
<td align="right">20.0%</td>
<td align="right">17.4%</td>
<td align="right">465</td>
</tr>
<tr>
<td align="left">1033</td>
<td align="left">🟡 Bubble</td>
<td align="right"><b>1497</b></td>
<td align="right">23.5%</td>
<td align="right">55.3%</td>
<td align="right">24.3%</td>
<td align="right">21.8%</td>
<td align="right">22.1%</td>
<td align="right">16.7%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">1034</td>
<td align="left">🟡 Gladiator</td>
<td align="right"><b>1497</b></td>
<td align="right">22.5%</td>
<td align="right">67.6%</td>
<td align="right">35.0%</td>
<td align="right">19.1%</td>
<td align="right">16.5%</td>
<td align="right">13.8%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">1035</td>
<td align="left">🟡 Chance</td>
<td align="right"><b>1497</b></td>
<td align="right">22.6%</td>
<td align="right">39.1%</td>
<td align="right">28.4%</td>
<td align="right">19.8%</td>
<td align="right">19.7%</td>
<td align="right">17.4%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1036</td>
<td align="left">🟡 Detective</td>
<td align="right"><b>1497</b></td>
<td align="right">23.1%</td>
<td align="right">50.0%</td>
<td align="right">30.4%</td>
<td align="right">23.7%</td>
<td align="right">20.2%</td>
<td align="right">14.9%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">1037</td>
<td align="left">🟡 Breaker</td>
<td align="right"><b>1497</b></td>
<td align="right">24.9%</td>
<td align="right">48.9%</td>
<td align="right">35.6%</td>
<td align="right">28.4%</td>
<td align="right">14.6%</td>
<td align="right">15.6%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">1038</td>
<td align="left">🟡 Prophet</td>
<td align="right"><b>1497</b></td>
<td align="right">23.3%</td>
<td align="right">53.3%</td>
<td align="right">37.0%</td>
<td align="right">22.8%</td>
<td align="right">23.2%</td>
<td align="right">15.4%</td>
<td align="right">1810</td>
</tr>
<tr>
<td align="left">1039</td>
<td align="left">🟡 Grower</td>
<td align="right"><b>1497</b></td>
<td align="right">23.4%</td>
<td align="right">46.9%</td>
<td align="right">36.2%</td>
<td align="right">26.0%</td>
<td align="right">8.9%</td>
<td align="right">17.5%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">1040</td>
<td align="left">🟡 Duke</td>
<td align="right"><b>1497</b></td>
<td align="right">23.0%</td>
<td align="right">52.8%</td>
<td align="right">28.1%</td>
<td align="right">25.0%</td>
<td align="right">19.2%</td>
<td align="right">15.5%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">1041</td>
<td align="left">🟡 Linguist</td>
<td align="right"><b>1497</b></td>
<td align="right">22.2%</td>
<td align="right">42.9%</td>
<td align="right">27.1%</td>
<td align="right">22.4%</td>
<td align="right">23.5%</td>
<td align="right">10.9%</td>
<td align="right">469</td>
</tr>
<tr>
<td align="left">1042</td>
<td align="left">🟡 Cavalry</td>
<td align="right"><b>1497</b></td>
<td align="right">23.4%</td>
<td align="right">60.8%</td>
<td align="right">31.6%</td>
<td align="right">26.4%</td>
<td align="right">21.2%</td>
<td align="right">16.1%</td>
<td align="right">1884</td>
</tr>
<tr>
<td align="left">1043</td>
<td align="left">🟡 Troll</td>
<td align="right"><b>1497</b></td>
<td align="right">23.0%</td>
<td align="right">44.7%</td>
<td align="right">27.7%</td>
<td align="right">19.5%</td>
<td align="right">21.7%</td>
<td align="right">16.3%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">1044</td>
<td align="left">🟡 Portal</td>
<td align="right"><b>1497</b></td>
<td align="right">22.1%</td>
<td align="right">47.7%</td>
<td align="right">34.4%</td>
<td align="right">25.0%</td>
<td align="right">15.4%</td>
<td align="right">12.7%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">1045</td>
<td align="left">🟡 Hoarder</td>
<td align="right"><b>1497</b></td>
<td align="right">22.9%</td>
<td align="right">55.8%</td>
<td align="right">29.3%</td>
<td align="right">22.7%</td>
<td align="right">14.0%</td>
<td align="right">15.2%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">1046</td>
<td align="left">🟡 Astrologer</td>
<td align="right"><b>1497</b></td>
<td align="right">21.6%</td>
<td align="right">41.3%</td>
<td align="right">27.0%</td>
<td align="right">25.3%</td>
<td align="right">17.1%</td>
<td align="right">13.2%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">1047</td>
<td align="left">🟡 Darkness</td>
<td align="right"><b>1497</b></td>
<td align="right">21.8%</td>
<td align="right">48.8%</td>
<td align="right">33.3%</td>
<td align="right">25.5%</td>
<td align="right">12.8%</td>
<td align="right">13.1%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">1048</td>
<td align="left">🟡 Endurer</td>
<td align="right"><b>1497</b></td>
<td align="right">24.2%</td>
<td align="right">44.7%</td>
<td align="right">31.6%</td>
<td align="right">28.4%</td>
<td align="right">19.2%</td>
<td align="right">13.9%</td>
<td align="right">392</td>
</tr>
<tr>
<td align="left">1049</td>
<td align="left">🟡 Leviathan</td>
<td align="right"><b>1497</b></td>
<td align="right">21.8%</td>
<td align="right">62.2%</td>
<td align="right">35.4%</td>
<td align="right">23.8%</td>
<td align="right">17.2%</td>
<td align="right">15.6%</td>
<td align="right">2575</td>
</tr>
<tr>
<td align="left">1050</td>
<td align="left">🟡 Opportunist</td>
<td align="right"><b>1497</b></td>
<td align="right">23.6%</td>
<td align="right">40.0%</td>
<td align="right">31.9%</td>
<td align="right">28.4%</td>
<td align="right">22.2%</td>
<td align="right">11.3%</td>
<td align="right">484</td>
</tr>
<tr>
<td align="left">1051</td>
<td align="left">🟡 Counterattack</td>
<td align="right"><b>1497</b></td>
<td align="right">19.5%</td>
<td align="right">66.7%</td>
<td align="right">38.5%</td>
<td align="right">23.5%</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
<td align="right">82</td>
</tr>
<tr>
<td align="left">1052</td>
<td align="left">🟡 Ordnance</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">40.9%</td>
<td align="right">46.3%</td>
<td align="right">18.4%</td>
<td align="right">18.4%</td>
<td align="right">11.5%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">1053</td>
<td align="left">🟡 Exorcist</td>
<td align="right"><b>1497</b></td>
<td align="right">23.0%</td>
<td align="right">41.5%</td>
<td align="right">40.7%</td>
<td align="right">18.3%</td>
<td align="right">17.4%</td>
<td align="right">16.9%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">1054</td>
<td align="left">🟡 Lloyd</td>
<td align="right"><b>1497</b></td>
<td align="right">22.6%</td>
<td align="right">47.1%</td>
<td align="right">32.1%</td>
<td align="right">17.2%</td>
<td align="right">16.5%</td>
<td align="right">17.1%</td>
<td align="right">393</td>
</tr>
<tr>
<td align="left">1055</td>
<td align="left">🟡 Moth</td>
<td align="right"><b>1497</b></td>
<td align="right">19.4%</td>
<td align="right">50.0%</td>
<td align="right">29.4%</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
<td align="right">7.7%</td>
<td align="right">72</td>
</tr>
<tr>
<td align="left">1056</td>
<td align="left">🟡 Soul</td>
<td align="right"><b>1497</b></td>
<td align="right">22.4%</td>
<td align="right">41.0%</td>
<td align="right">29.5%</td>
<td align="right">21.2%</td>
<td align="right">21.4%</td>
<td align="right">15.9%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">1057</td>
<td align="left">🟡 Ravager_Alt</td>
<td align="right"><b>1497</b></td>
<td align="right">22.5%</td>
<td align="right">51.2%</td>
<td align="right">44.1%</td>
<td align="right">17.5%</td>
<td align="right">14.9%</td>
<td align="right">12.1%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">1058</td>
<td align="left">🟡 Pauser</td>
<td align="right"><b>1497</b></td>
<td align="right">23.1%</td>
<td align="right">58.5%</td>
<td align="right">26.0%</td>
<td align="right">26.1%</td>
<td align="right">15.8%</td>
<td align="right">14.6%</td>
<td align="right">450</td>
</tr>
<tr>
<td align="left">1059</td>
<td align="left">🟡 Controller</td>
<td align="right"><b>1497</b></td>
<td align="right">22.8%</td>
<td align="right">48.9%</td>
<td align="right">34.8%</td>
<td align="right">28.2%</td>
<td align="right">14.9%</td>
<td align="right">10.0%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">1060</td>
<td align="left">🟡 Omniscient</td>
<td align="right"><b>1497</b></td>
<td align="right">22.8%</td>
<td align="right">26.9%</td>
<td align="right">38.7%</td>
<td align="right">24.8%</td>
<td align="right">18.3%</td>
<td align="right">16.0%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">1061</td>
<td align="left">🟡 Poison</td>
<td align="right"><b>1497</b></td>
<td align="right">21.7%</td>
<td align="right">44.8%</td>
<td align="right">29.2%</td>
<td align="right">24.7%</td>
<td align="right">19.4%</td>
<td align="right">17.3%</td>
<td align="right">2443</td>
</tr>
<tr>
<td align="left">1062</td>
<td align="left">🟡 Bride</td>
<td align="right"><b>1497</b></td>
<td align="right">21.7%</td>
<td align="right">50.0%</td>
<td align="right">32.3%</td>
<td align="right">20.0%</td>
<td align="right">14.5%</td>
<td align="right">13.5%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">1063</td>
<td align="left">🟡 WaveFunction</td>
<td align="right"><b>1497</b></td>
<td align="right">22.4%</td>
<td align="right">40.5%</td>
<td align="right">25.4%</td>
<td align="right">27.6%</td>
<td align="right">20.4%</td>
<td align="right">14.0%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">1064</td>
<td align="left">🟡 Prince</td>
<td align="right"><b>1497</b></td>
<td align="right">22.2%</td>
<td align="right">45.8%</td>
<td align="right">22.6%</td>
<td align="right">23.2%</td>
<td align="right">20.3%</td>
<td align="right">14.5%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">1065</td>
<td align="left">🟡 Patriot</td>
<td align="right"><b>1497</b></td>
<td align="right">23.7%</td>
<td align="right">58.3%</td>
<td align="right">40.7%</td>
<td align="right">24.7%</td>
<td align="right">19.7%</td>
<td align="right">16.1%</td>
<td align="right">2442</td>
</tr>
<tr>
<td align="left">1066</td>
<td align="left">🟡 Zilch</td>
<td align="right"><b>1497</b></td>
<td align="right">23.8%</td>
<td align="right">39.1%</td>
<td align="right">35.5%</td>
<td align="right">25.5%</td>
<td align="right">20.8%</td>
<td align="right">14.0%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">1067</td>
<td align="left">🟡 Vacuum</td>
<td align="right"><b>1497</b></td>
<td align="right">22.9%</td>
<td align="right">52.5%</td>
<td align="right">35.6%</td>
<td align="right">24.4%</td>
<td align="right">18.6%</td>
<td align="right">17.5%</td>
<td align="right">2558</td>
</tr>
<tr>
<td align="left">1068</td>
<td align="left">🟡 Geek</td>
<td align="right"><b>1497</b></td>
<td align="right">23.0%</td>
<td align="right">42.9%</td>
<td align="right">28.3%</td>
<td align="right">23.7%</td>
<td align="right">17.2%</td>
<td align="right">18.9%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1069</td>
<td align="left">🟡 Disguiser</td>
<td align="right"><b>1496</b></td>
<td align="right">22.1%</td>
<td align="right">50.0%</td>
<td align="right">24.6%</td>
<td align="right">25.9%</td>
<td align="right">17.9%</td>
<td align="right">13.4%</td>
<td align="right">407</td>
</tr>
<tr>
<td align="left">1070</td>
<td align="left">🟡 Hawk</td>
<td align="right"><b>1496</b></td>
<td align="right">23.8%</td>
<td align="right">51.7%</td>
<td align="right">30.6%</td>
<td align="right">29.3%</td>
<td align="right">13.5%</td>
<td align="right">14.8%</td>
<td align="right">505</td>
</tr>
<tr>
<td align="left">1071</td>
<td align="left">🟡 Floater</td>
<td align="right"><b>1496</b></td>
<td align="right">19.0%</td>
<td align="right">33.3%</td>
<td align="right">28.6%</td>
<td align="right">14.3%</td>
<td align="right">11.8%</td>
<td align="right">19.2%</td>
<td align="right">63</td>
</tr>
<tr>
<td align="left">1072</td>
<td align="left">🟡 Shark</td>
<td align="right"><b>1496</b></td>
<td align="right">22.7%</td>
<td align="right">48.8%</td>
<td align="right">25.0%</td>
<td align="right">18.8%</td>
<td align="right">19.8%</td>
<td align="right">18.5%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">1073</td>
<td align="left">🟡 Fortress_Alt</td>
<td align="right"><b>1496</b></td>
<td align="right">23.0%</td>
<td align="right">42.9%</td>
<td align="right">25.0%</td>
<td align="right">32.4%</td>
<td align="right">17.9%</td>
<td align="right">14.0%</td>
<td align="right">396</td>
</tr>
<tr>
<td align="left">1074</td>
<td align="left">🟡 Crusher</td>
<td align="right"><b>1496</b></td>
<td align="right">22.4%</td>
<td align="right">44.7%</td>
<td align="right">31.6%</td>
<td align="right">22.6%</td>
<td align="right">15.5%</td>
<td align="right">15.4%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">1075</td>
<td align="left">🟡 Nightmare</td>
<td align="right"><b>1496</b></td>
<td align="right">20.9%</td>
<td align="right">45.0%</td>
<td align="right">29.8%</td>
<td align="right">20.3%</td>
<td align="right">18.9%</td>
<td align="right">17.0%</td>
<td align="right">2391</td>
</tr>
<tr>
<td align="left">1076</td>
<td align="left">🟡 Timewarp</td>
<td align="right"><b>1496</b></td>
<td align="right">22.7%</td>
<td align="right">45.9%</td>
<td align="right">34.9%</td>
<td align="right">25.5%</td>
<td align="right">14.6%</td>
<td align="right">14.6%</td>
<td align="right">431</td>
</tr>
<tr>
<td align="left">1077</td>
<td align="left">🟡 Eclipse</td>
<td align="right"><b>1496</b></td>
<td align="right">23.0%</td>
<td align="right">45.0%</td>
<td align="right">40.0%</td>
<td align="right">21.1%</td>
<td align="right">18.4%</td>
<td align="right">9.2%</td>
<td align="right">408</td>
</tr>
<tr>
<td align="left">1078</td>
<td align="left">🟡 Vox</td>
<td align="right"><b>1496</b></td>
<td align="right">22.0%</td>
<td align="right">62.7%</td>
<td align="right">32.0%</td>
<td align="right">24.3%</td>
<td align="right">17.9%</td>
<td align="right">16.3%</td>
<td align="right">2452</td>
</tr>
<tr>
<td align="left">1079</td>
<td align="left">🟡 Sadist</td>
<td align="right"><b>1496</b></td>
<td align="right">22.2%</td>
<td align="right">49.0%</td>
<td align="right">26.8%</td>
<td align="right">22.3%</td>
<td align="right">16.3%</td>
<td align="right">14.3%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">1080</td>
<td align="left">🟡 Venus</td>
<td align="right"><b>1496</b></td>
<td align="right">22.6%</td>
<td align="right">54.5%</td>
<td align="right">26.0%</td>
<td align="right">28.6%</td>
<td align="right">15.0%</td>
<td align="right">14.4%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">1081</td>
<td align="left">🟡 Beetle</td>
<td align="right"><b>1496</b></td>
<td align="right">18.9%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">18.8%</td>
<td align="right">12.5%</td>
<td align="right">17.9%</td>
<td align="right">74</td>
</tr>
<tr>
<td align="left">1082</td>
<td align="left">🟡 Kamikazee</td>
<td align="right"><b>1496</b></td>
<td align="right">24.1%</td>
<td align="right">54.1%</td>
<td align="right">35.9%</td>
<td align="right">27.9%</td>
<td align="right">19.5%</td>
<td align="right">17.9%</td>
<td align="right">2538</td>
</tr>
<tr>
<td align="left">1083</td>
<td align="left">🟡 Firefly</td>
<td align="right"><b>1496</b></td>
<td align="right">18.9%</td>
<td align="right">50.0%</td>
<td align="right">55.6%</td>
<td align="right">16.7%</td>
<td align="right">18.2%</td>
<td align="right">7.3%</td>
<td align="right">90</td>
</tr>
<tr>
<td align="left">1084</td>
<td align="left">🟡 Skinwalker</td>
<td align="right"><b>1496</b></td>
<td align="right">22.9%</td>
<td align="right">41.9%</td>
<td align="right">22.2%</td>
<td align="right">25.0%</td>
<td align="right">20.7%</td>
<td align="right">18.0%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">1085</td>
<td align="left">🟡 Count</td>
<td align="right"><b>1496</b></td>
<td align="right">22.1%</td>
<td align="right">40.0%</td>
<td align="right">29.3%</td>
<td align="right">18.7%</td>
<td align="right">23.0%</td>
<td align="right">13.4%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">1086</td>
<td align="left">🟡 Vanguard</td>
<td align="right"><b>1496</b></td>
<td align="right">24.4%</td>
<td align="right">60.0%</td>
<td align="right">38.9%</td>
<td align="right">19.1%</td>
<td align="right">19.4%</td>
<td align="right">12.5%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">1087</td>
<td align="left">🟡 Viscount</td>
<td align="right"><b>1496</b></td>
<td align="right">23.2%</td>
<td align="right">44.7%</td>
<td align="right">28.6%</td>
<td align="right">25.8%</td>
<td align="right">15.5%</td>
<td align="right">18.9%</td>
<td align="right">462</td>
</tr>
<tr>
<td align="left">1088</td>
<td align="left">🟡 Teleporter</td>
<td align="right"><b>1496</b></td>
<td align="right">18.8%</td>
<td align="right">28.6%</td>
<td align="right">38.5%</td>
<td align="right">22.2%</td>
<td align="right">0.0%</td>
<td align="right">15.0%</td>
<td align="right">64</td>
</tr>
<tr>
<td align="left">1089</td>
<td align="left">🟡 Cudgel</td>
<td align="right"><b>1496</b></td>
<td align="right">22.3%</td>
<td align="right">65.8%</td>
<td align="right">37.9%</td>
<td align="right">26.2%</td>
<td align="right">17.0%</td>
<td align="right">14.1%</td>
<td align="right">2507</td>
</tr>
<tr>
<td align="left">1090</td>
<td align="left">🟡 Netter</td>
<td align="right"><b>1496</b></td>
<td align="right">22.9%</td>
<td align="right">50.0%</td>
<td align="right">32.9%</td>
<td align="right">18.8%</td>
<td align="right">20.0%</td>
<td align="right">16.3%</td>
<td align="right">411</td>
</tr>
<tr>
<td align="left">1091</td>
<td align="left">🟡 Viper</td>
<td align="right"><b>1496</b></td>
<td align="right">22.2%</td>
<td align="right">41.9%</td>
<td align="right">29.7%</td>
<td align="right">26.4%</td>
<td align="right">12.8%</td>
<td align="right">15.0%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">1092</td>
<td align="left">🟡 Signaler</td>
<td align="right"><b>1496</b></td>
<td align="right">24.4%</td>
<td align="right">54.2%</td>
<td align="right">30.9%</td>
<td align="right">19.7%</td>
<td align="right">20.9%</td>
<td align="right">16.9%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1093</td>
<td align="left">🟡 Capacitor</td>
<td align="right"><b>1496</b></td>
<td align="right">22.6%</td>
<td align="right">44.2%</td>
<td align="right">27.7%</td>
<td align="right">28.3%</td>
<td align="right">18.8%</td>
<td align="right">12.6%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1094</td>
<td align="left">🟡 Propagator</td>
<td align="right"><b>1496</b></td>
<td align="right">21.6%</td>
<td align="right">57.5%</td>
<td align="right">27.7%</td>
<td align="right">24.3%</td>
<td align="right">14.4%</td>
<td align="right">14.0%</td>
<td align="right">490</td>
</tr>
<tr>
<td align="left">1095</td>
<td align="left">🟡 Greed_Alt</td>
<td align="right"><b>1496</b></td>
<td align="right">22.0%</td>
<td align="right">41.5%</td>
<td align="right">25.4%</td>
<td align="right">20.0%</td>
<td align="right">15.3%</td>
<td align="right">19.4%</td>
<td align="right">455</td>
</tr>
<tr>
<td align="left">1096</td>
<td align="left">🟡 Splitter</td>
<td align="right"><b>1496</b></td>
<td align="right">23.4%</td>
<td align="right">48.9%</td>
<td align="right">34.9%</td>
<td align="right">17.5%</td>
<td align="right">15.9%</td>
<td align="right">19.4%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">1097</td>
<td align="left">🟡 Nebula</td>
<td align="right"><b>1496</b></td>
<td align="right">23.1%</td>
<td align="right">50.0%</td>
<td align="right">25.4%</td>
<td align="right">24.1%</td>
<td align="right">21.3%</td>
<td align="right">14.8%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">1098</td>
<td align="left">🟡 Wrecker</td>
<td align="right"><b>1496</b></td>
<td align="right">22.6%</td>
<td align="right">38.3%</td>
<td align="right">35.2%</td>
<td align="right">16.3%</td>
<td align="right">20.6%</td>
<td align="right">18.8%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">1099</td>
<td align="left">🟡 Speculator</td>
<td align="right"><b>1496</b></td>
<td align="right">22.9%</td>
<td align="right">41.9%</td>
<td align="right">30.1%</td>
<td align="right">28.7%</td>
<td align="right">14.7%</td>
<td align="right">16.0%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">1100</td>
<td align="left">🟡 Drone</td>
<td align="right"><b>1496</b></td>
<td align="right">21.6%</td>
<td align="right">50.0%</td>
<td align="right">21.2%</td>
<td align="right">27.9%</td>
<td align="right">16.1%</td>
<td align="right">12.2%</td>
<td align="right">459</td>
</tr>
<tr>
<td align="left">1101</td>
<td align="left">🟡 Transmuter</td>
<td align="right"><b>1496</b></td>
<td align="right">21.5%</td>
<td align="right">46.0%</td>
<td align="right">36.4%</td>
<td align="right">16.3%</td>
<td align="right">14.3%</td>
<td align="right">16.6%</td>
<td align="right">460</td>
</tr>
<tr>
<td align="left">1102</td>
<td align="left">🟡 Hardener</td>
<td align="right"><b>1496</b></td>
<td align="right">22.3%</td>
<td align="right">53.1%</td>
<td align="right">24.4%</td>
<td align="right">24.4%</td>
<td align="right">11.8%</td>
<td align="right">17.8%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">1103</td>
<td align="left">🟡 Collaborator</td>
<td align="right"><b>1496</b></td>
<td align="right">23.1%</td>
<td align="right">52.0%</td>
<td align="right">27.8%</td>
<td align="right">20.7%</td>
<td align="right">22.1%</td>
<td align="right">14.1%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">1104</td>
<td align="left">🟡 Temporal</td>
<td align="right"><b>1496</b></td>
<td align="right">24.5%</td>
<td align="right">51.2%</td>
<td align="right">31.0%</td>
<td align="right">24.7%</td>
<td align="right">17.8%</td>
<td align="right">18.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">1105</td>
<td align="left">🟡 EvilTwin</td>
<td align="right"><b>1496</b></td>
<td align="right">23.2%</td>
<td align="right">44.7%</td>
<td align="right">36.4%</td>
<td align="right">28.9%</td>
<td align="right">16.7%</td>
<td align="right">12.6%</td>
<td align="right">396</td>
</tr>
<tr>
<td align="left">1106</td>
<td align="left">🟡 Telekinetic</td>
<td align="right"><b>1496</b></td>
<td align="right">22.7%</td>
<td align="right">51.0%</td>
<td align="right">30.3%</td>
<td align="right">16.7%</td>
<td align="right">19.8%</td>
<td align="right">15.3%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">1107</td>
<td align="left">🟡 Invisible</td>
<td align="right"><b>1496</b></td>
<td align="right">21.8%</td>
<td align="right">52.8%</td>
<td align="right">27.0%</td>
<td align="right">17.2%</td>
<td align="right">21.2%</td>
<td align="right">15.1%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">1108</td>
<td align="left">🟡 Probability</td>
<td align="right"><b>1496</b></td>
<td align="right">22.7%</td>
<td align="right">57.1%</td>
<td align="right">25.4%</td>
<td align="right">15.4%</td>
<td align="right">21.5%</td>
<td align="right">16.4%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">1109</td>
<td align="left">🟡 Necro</td>
<td align="right"><b>1496</b></td>
<td align="right">18.2%</td>
<td align="right">42.9%</td>
<td align="right">11.1%</td>
<td align="right">11.1%</td>
<td align="right">16.7%</td>
<td align="right">20.0%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">1110</td>
<td align="left">🟡 Roach</td>
<td align="right"><b>1496</b></td>
<td align="right">22.0%</td>
<td align="right">48.9%</td>
<td align="right">30.7%</td>
<td align="right">27.4%</td>
<td align="right">18.6%</td>
<td align="right">15.3%</td>
<td align="right">1827</td>
</tr>
<tr>
<td align="left">1111</td>
<td align="left">🟡 Frost</td>
<td align="right"><b>1496</b></td>
<td align="right">21.8%</td>
<td align="right">43.1%</td>
<td align="right">28.8%</td>
<td align="right">17.0%</td>
<td align="right">18.0%</td>
<td align="right">15.5%</td>
<td align="right">463</td>
</tr>
<tr>
<td align="left">1112</td>
<td align="left">🟡 Wraith</td>
<td align="right"><b>1496</b></td>
<td align="right">21.9%</td>
<td align="right">48.9%</td>
<td align="right">27.1%</td>
<td align="right">26.7%</td>
<td align="right">15.5%</td>
<td align="right">11.6%</td>
<td align="right">407</td>
</tr>
<tr>
<td align="left">1113</td>
<td align="left">🟡 Zealotry</td>
<td align="right"><b>1496</b></td>
<td align="right">24.2%</td>
<td align="right">42.5%</td>
<td align="right">39.3%</td>
<td align="right">19.5%</td>
<td align="right">24.1%</td>
<td align="right">13.5%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">1114</td>
<td align="left">🟡 Fido</td>
<td align="right"><b>1496</b></td>
<td align="right">22.7%</td>
<td align="right">60.0%</td>
<td align="right">35.7%</td>
<td align="right">24.4%</td>
<td align="right">19.0%</td>
<td align="right">16.6%</td>
<td align="right">2635</td>
</tr>
<tr>
<td align="left">1115</td>
<td align="left">🟡 Locksmith</td>
<td align="right"><b>1496</b></td>
<td align="right">21.5%</td>
<td align="right">37.5%</td>
<td align="right">33.9%</td>
<td align="right">19.3%</td>
<td align="right">18.4%</td>
<td align="right">15.8%</td>
<td align="right">405</td>
</tr>
<tr>
<td align="left">1116</td>
<td align="left">🟡 Striker</td>
<td align="right"><b>1496</b></td>
<td align="right">22.4%</td>
<td align="right">50.0%</td>
<td align="right">31.1%</td>
<td align="right">24.5%</td>
<td align="right">15.3%</td>
<td align="right">15.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">1117</td>
<td align="left">🟡 Courage</td>
<td align="right"><b>1496</b></td>
<td align="right">23.8%</td>
<td align="right">46.0%</td>
<td align="right">26.1%</td>
<td align="right">23.1%</td>
<td align="right">19.1%</td>
<td align="right">18.3%</td>
<td align="right">412</td>
</tr>
<tr>
<td align="left">1118</td>
<td align="left">🟡 Reproducer</td>
<td align="right"><b>1496</b></td>
<td align="right">22.2%</td>
<td align="right">46.3%</td>
<td align="right">34.7%</td>
<td align="right">18.3%</td>
<td align="right">16.5%</td>
<td align="right">15.0%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">1119</td>
<td align="left">🟡 Chef</td>
<td align="right"><b>1496</b></td>
<td align="right">20.3%</td>
<td align="right">39.3%</td>
<td align="right">24.3%</td>
<td align="right">20.5%</td>
<td align="right">19.1%</td>
<td align="right">14.4%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">1120</td>
<td align="left">🟡 Tourist</td>
<td align="right"><b>1496</b></td>
<td align="right">22.3%</td>
<td align="right">39.0%</td>
<td align="right">35.7%</td>
<td align="right">23.9%</td>
<td align="right">19.4%</td>
<td align="right">12.6%</td>
<td align="right">453</td>
</tr>
<tr>
<td align="left">1121</td>
<td align="left">🟡 Flanker</td>
<td align="right"><b>1496</b></td>
<td align="right">21.3%</td>
<td align="right">38.8%</td>
<td align="right">28.3%</td>
<td align="right">22.9%</td>
<td align="right">16.0%</td>
<td align="right">15.2%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">1122</td>
<td align="left">🟡 Mechanic</td>
<td align="right"><b>1496</b></td>
<td align="right">20.2%</td>
<td align="right">26.7%</td>
<td align="right">23.4%</td>
<td align="right">15.9%</td>
<td align="right">18.0%</td>
<td align="right">20.4%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1123</td>
<td align="left">🟡 Outcast</td>
<td align="right"><b>1496</b></td>
<td align="right">23.2%</td>
<td align="right">45.1%</td>
<td align="right">32.8%</td>
<td align="right">16.4%</td>
<td align="right">16.9%</td>
<td align="right">18.6%</td>
<td align="right">414</td>
</tr>
<tr>
<td align="left">1124</td>
<td align="left">🟡 Wrack</td>
<td align="right"><b>1496</b></td>
<td align="right">21.9%</td>
<td align="right">42.3%</td>
<td align="right">26.9%</td>
<td align="right">26.0%</td>
<td align="right">16.1%</td>
<td align="right">13.2%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">1125</td>
<td align="left">🟡 Perfectionist_Alt</td>
<td align="right"><b>1496</b></td>
<td align="right">22.9%</td>
<td align="right">35.4%</td>
<td align="right">34.3%</td>
<td align="right">30.1%</td>
<td align="right">17.6%</td>
<td align="right">10.9%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">1126</td>
<td align="left">🟡 Tactician</td>
<td align="right"><b>1496</b></td>
<td align="right">23.0%</td>
<td align="right">55.6%</td>
<td align="right">34.9%</td>
<td align="right">27.3%</td>
<td align="right">15.8%</td>
<td align="right">11.8%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">1127</td>
<td align="left">🟡 Charger</td>
<td align="right"><b>1496</b></td>
<td align="right">23.0%</td>
<td align="right">53.7%</td>
<td align="right">35.6%</td>
<td align="right">25.6%</td>
<td align="right">14.0%</td>
<td align="right">13.4%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">1128</td>
<td align="left">🟡 Apex</td>
<td align="right"><b>1496</b></td>
<td align="right">23.4%</td>
<td align="right">61.3%</td>
<td align="right">25.7%</td>
<td align="right">19.3%</td>
<td align="right">22.2%</td>
<td align="right">15.5%</td>
<td align="right">389</td>
</tr>
<tr>
<td align="left">1129</td>
<td align="left">🟡 Raven</td>
<td align="right"><b>1496</b></td>
<td align="right">21.6%</td>
<td align="right">45.7%</td>
<td align="right">31.1%</td>
<td align="right">15.8%</td>
<td align="right">19.8%</td>
<td align="right">14.3%</td>
<td align="right">407</td>
</tr>
<tr>
<td align="left">1130</td>
<td align="left">🟡 Pilot</td>
<td align="right"><b>1496</b></td>
<td align="right">21.8%</td>
<td align="right">61.4%</td>
<td align="right">22.6%</td>
<td align="right">24.5%</td>
<td align="right">12.0%</td>
<td align="right">14.0%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">1131</td>
<td align="left">🟡 Sacrifice</td>
<td align="right"><b>1496</b></td>
<td align="right">17.6%</td>
<td align="right">25.0%</td>
<td align="right">20.0%</td>
<td align="right">27.8%</td>
<td align="right">14.3%</td>
<td align="right">9.1%</td>
<td align="right">68</td>
</tr>
<tr>
<td align="left">1132</td>
<td align="left">🟡 Extortionist</td>
<td align="right"><b>1496</b></td>
<td align="right">20.8%</td>
<td align="right">51.2%</td>
<td align="right">31.0%</td>
<td align="right">21.1%</td>
<td align="right">17.6%</td>
<td align="right">16.3%</td>
<td align="right">1910</td>
</tr>
<tr>
<td align="left">1133</td>
<td align="left">🟡 Muckraker</td>
<td align="right"><b>1495</b></td>
<td align="right">21.9%</td>
<td align="right">36.7%</td>
<td align="right">26.8%</td>
<td align="right">21.5%</td>
<td align="right">19.2%</td>
<td align="right">18.4%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">1134</td>
<td align="left">🟡 Wave</td>
<td align="right"><b>1495</b></td>
<td align="right">22.5%</td>
<td align="right">44.1%</td>
<td align="right">27.8%</td>
<td align="right">27.1%</td>
<td align="right">17.2%</td>
<td align="right">16.7%</td>
<td align="right">457</td>
</tr>
<tr>
<td align="left">1135</td>
<td align="left">🟡 Keeper_Alt</td>
<td align="right"><b>1495</b></td>
<td align="right">20.2%</td>
<td align="right">43.9%</td>
<td align="right">29.9%</td>
<td align="right">20.5%</td>
<td align="right">13.7%</td>
<td align="right">13.5%</td>
<td align="right">441</td>
</tr>
<tr>
<td align="left">1136</td>
<td align="left">🟡 Prominence</td>
<td align="right"><b>1495</b></td>
<td align="right">22.7%</td>
<td align="right">65.9%</td>
<td align="right">23.5%</td>
<td align="right">28.4%</td>
<td align="right">16.1%</td>
<td align="right">8.6%</td>
<td align="right">396</td>
</tr>
<tr>
<td align="left">1137</td>
<td align="left">🟡 Famine</td>
<td align="right"><b>1495</b></td>
<td align="right">20.9%</td>
<td align="right">39.1%</td>
<td align="right">31.6%</td>
<td align="right">22.6%</td>
<td align="right">18.3%</td>
<td align="right">12.0%</td>
<td align="right">268</td>
</tr>
<tr>
<td align="left">1138</td>
<td align="left">🟡 Looter</td>
<td align="right"><b>1495</b></td>
<td align="right">22.7%</td>
<td align="right">47.8%</td>
<td align="right">30.7%</td>
<td align="right">24.5%</td>
<td align="right">15.6%</td>
<td align="right">11.1%</td>
<td align="right">449</td>
</tr>
<tr>
<td align="left">1139</td>
<td align="left">🟡 Reincarnator</td>
<td align="right"><b>1495</b></td>
<td align="right">20.8%</td>
<td align="right">57.1%</td>
<td align="right">31.0%</td>
<td align="right">23.3%</td>
<td align="right">17.6%</td>
<td align="right">15.3%</td>
<td align="right">2555</td>
</tr>
<tr>
<td align="left">1140</td>
<td align="left">🟡 Exponential</td>
<td align="right"><b>1495</b></td>
<td align="right">17.4%</td>
<td align="right">25.0%</td>
<td align="right">12.5%</td>
<td align="right">31.2%</td>
<td align="right">10.5%</td>
<td align="right">13.6%</td>
<td align="right">69</td>
</tr>
<tr>
<td align="left">1141</td>
<td align="left">🟡 Annihilator</td>
<td align="right"><b>1495</b></td>
<td align="right">21.4%</td>
<td align="right">45.9%</td>
<td align="right">35.8%</td>
<td align="right">27.5%</td>
<td align="right">11.8%</td>
<td align="right">10.7%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">1142</td>
<td align="left">🟡 Director</td>
<td align="right"><b>1495</b></td>
<td align="right">21.1%</td>
<td align="right">40.0%</td>
<td align="right">17.7%</td>
<td align="right">23.6%</td>
<td align="right">17.8%</td>
<td align="right">17.8%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">1143</td>
<td align="left">🟡 Champion_Gaming</td>
<td align="right"><b>1495</b></td>
<td align="right">17.2%</td>
<td align="right">50.0%</td>
<td align="right">14.3%</td>
<td align="right">16.7%</td>
<td align="right">18.2%</td>
<td align="right">10.5%</td>
<td align="right">64</td>
</tr>
<tr>
<td align="left">1144</td>
<td align="left">🟡 Tachyon</td>
<td align="right"><b>1495</b></td>
<td align="right">23.0%</td>
<td align="right">50.0%</td>
<td align="right">26.2%</td>
<td align="right">23.7%</td>
<td align="right">13.2%</td>
<td align="right">16.7%</td>
<td align="right">417</td>
</tr>
<tr>
<td align="left">1145</td>
<td align="left">🟡 Conman</td>
<td align="right"><b>1495</b></td>
<td align="right">23.9%</td>
<td align="right">41.7%</td>
<td align="right">27.6%</td>
<td align="right">21.2%</td>
<td align="right">21.9%</td>
<td align="right">19.4%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">1146</td>
<td align="left">🟡 Lotto</td>
<td align="right"><b>1495</b></td>
<td align="right">22.9%</td>
<td align="right">41.2%</td>
<td align="right">35.4%</td>
<td align="right">23.4%</td>
<td align="right">16.8%</td>
<td align="right">17.6%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">1147</td>
<td align="left">🟡 Comrade</td>
<td align="right"><b>1495</b></td>
<td align="right">22.4%</td>
<td align="right">48.8%</td>
<td align="right">31.0%</td>
<td align="right">16.9%</td>
<td align="right">21.5%</td>
<td align="right">11.7%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1148</td>
<td align="left">🟡 Hider</td>
<td align="right"><b>1495</b></td>
<td align="right">21.4%</td>
<td align="right">44.1%</td>
<td align="right">26.5%</td>
<td align="right">23.7%</td>
<td align="right">16.5%</td>
<td align="right">11.8%</td>
<td align="right">471</td>
</tr>
<tr>
<td align="left">1149</td>
<td align="left">🟡 Android</td>
<td align="right"><b>1495</b></td>
<td align="right">21.5%</td>
<td align="right">38.1%</td>
<td align="right">28.6%</td>
<td align="right">18.2%</td>
<td align="right">19.1%</td>
<td align="right">17.4%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1150</td>
<td align="left">🟡 Root</td>
<td align="right"><b>1495</b></td>
<td align="right">17.1%</td>
<td align="right">27.3%</td>
<td align="right">22.2%</td>
<td align="right">20.0%</td>
<td align="right">10.0%</td>
<td align="right">15.4%</td>
<td align="right">76</td>
</tr>
<tr>
<td align="left">1151</td>
<td align="left">🟡 Foam</td>
<td align="right"><b>1495</b></td>
<td align="right">22.4%</td>
<td align="right">43.8%</td>
<td align="right">29.7%</td>
<td align="right">24.4%</td>
<td align="right">21.2%</td>
<td align="right">17.3%</td>
<td align="right">1786</td>
</tr>
<tr>
<td align="left">1152</td>
<td align="left">🟡 Revenant</td>
<td align="right"><b>1495</b></td>
<td align="right">22.5%</td>
<td align="right">42.9%</td>
<td align="right">26.2%</td>
<td align="right">22.9%</td>
<td align="right">17.9%</td>
<td align="right">17.3%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">1153</td>
<td align="left">🟡 Jailer</td>
<td align="right"><b>1495</b></td>
<td align="right">21.2%</td>
<td align="right">57.4%</td>
<td align="right">27.9%</td>
<td align="right">22.5%</td>
<td align="right">14.3%</td>
<td align="right">11.6%</td>
<td align="right">467</td>
</tr>
<tr>
<td align="left">1154</td>
<td align="left">🟡 Thoughter</td>
<td align="right"><b>1495</b></td>
<td align="right">19.9%</td>
<td align="right">38.2%</td>
<td align="right">25.9%</td>
<td align="right">20.2%</td>
<td align="right">18.5%</td>
<td align="right">13.4%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">1155</td>
<td align="left">🟡 Trickster</td>
<td align="right"><b>1495</b></td>
<td align="right">21.2%</td>
<td align="right">44.7%</td>
<td align="right">32.8%</td>
<td align="right">23.7%</td>
<td align="right">14.7%</td>
<td align="right">12.3%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">1156</td>
<td align="left">🟡 Arbiter</td>
<td align="right"><b>1495</b></td>
<td align="right">22.2%</td>
<td align="right">53.1%</td>
<td align="right">24.6%</td>
<td align="right">23.0%</td>
<td align="right">17.0%</td>
<td align="right">17.6%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">1157</td>
<td align="left">🟡 Chimera</td>
<td align="right"><b>1495</b></td>
<td align="right">22.0%</td>
<td align="right">37.3%</td>
<td align="right">25.8%</td>
<td align="right">21.1%</td>
<td align="right">24.4%</td>
<td align="right">11.9%</td>
<td align="right">478</td>
</tr>
<tr>
<td align="left">1158</td>
<td align="left">🟡 Decoy</td>
<td align="right"><b>1495</b></td>
<td align="right">23.1%</td>
<td align="right">53.7%</td>
<td align="right">29.8%</td>
<td align="right">26.7%</td>
<td align="right">14.2%</td>
<td align="right">12.6%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">1159</td>
<td align="left">🟡 Observer</td>
<td align="right"><b>1495</b></td>
<td align="right">22.5%</td>
<td align="right">48.5%</td>
<td align="right">36.1%</td>
<td align="right">26.5%</td>
<td align="right">16.7%</td>
<td align="right">17.1%</td>
<td align="right">2607</td>
</tr>
<tr>
<td align="left">1160</td>
<td align="left">🟡 Harmonic</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">18.8%</td>
<td align="right">12.0%</td>
<td align="right">66</td>
</tr>
<tr>
<td align="left">1161</td>
<td align="left">🟡 Fly</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">45.5%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">15.4%</td>
<td align="right">78</td>
</tr>
<tr>
<td align="left">1162</td>
<td align="left">🟡 Antimatter_Cosmic</td>
<td align="right"><b>1495</b></td>
<td align="right">21.3%</td>
<td align="right">47.2%</td>
<td align="right">25.7%</td>
<td align="right">28.3%</td>
<td align="right">14.4%</td>
<td align="right">12.6%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">1163</td>
<td align="left">🟡 Stalker</td>
<td align="right"><b>1495</b></td>
<td align="right">20.2%</td>
<td align="right">56.0%</td>
<td align="right">16.7%</td>
<td align="right">23.7%</td>
<td align="right">21.7%</td>
<td align="right">12.3%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">1164</td>
<td align="left">🟡 Crystal</td>
<td align="right"><b>1495</b></td>
<td align="right">21.3%</td>
<td align="right">60.0%</td>
<td align="right">26.8%</td>
<td align="right">23.2%</td>
<td align="right">18.0%</td>
<td align="right">17.8%</td>
<td align="right">2491</td>
</tr>
<tr>
<td align="left">1165</td>
<td align="left">🟡 Hydra</td>
<td align="right"><b>1495</b></td>
<td align="right">22.1%</td>
<td align="right">51.2%</td>
<td align="right">29.0%</td>
<td align="right">17.6%</td>
<td align="right">19.3%</td>
<td align="right">14.9%</td>
<td align="right">458</td>
</tr>
<tr>
<td align="left">1166</td>
<td align="left">🟡 Remote</td>
<td align="right"><b>1495</b></td>
<td align="right">20.4%</td>
<td align="right">41.7%</td>
<td align="right">28.8%</td>
<td align="right">24.2%</td>
<td align="right">7.5%</td>
<td align="right">15.6%</td>
<td align="right">445</td>
</tr>
<tr>
<td align="left">1167</td>
<td align="left">🟡 Reflector_Alt</td>
<td align="right"><b>1495</b></td>
<td align="right">16.5%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">22.2%</td>
<td align="right">7.7%</td>
<td align="right">15.0%</td>
<td align="right">91</td>
</tr>
<tr>
<td align="left">1168</td>
<td align="left">🟡 Surge</td>
<td align="right"><b>1495</b></td>
<td align="right">21.4%</td>
<td align="right">53.1%</td>
<td align="right">33.2%</td>
<td align="right">24.4%</td>
<td align="right">18.9%</td>
<td align="right">13.9%</td>
<td align="right">2592</td>
</tr>
<tr>
<td align="left">1169</td>
<td align="left">🟡 Colonizer</td>
<td align="right"><b>1495</b></td>
<td align="right">21.1%</td>
<td align="right">51.4%</td>
<td align="right">29.0%</td>
<td align="right">21.2%</td>
<td align="right">18.9%</td>
<td align="right">10.3%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">1170</td>
<td align="left">🟡 Giver</td>
<td align="right"><b>1495</b></td>
<td align="right">22.3%</td>
<td align="right">52.1%</td>
<td align="right">31.2%</td>
<td align="right">24.0%</td>
<td align="right">20.3%</td>
<td align="right">16.9%</td>
<td align="right">2670</td>
</tr>
<tr>
<td align="left">1171</td>
<td align="left">🟡 Quicken</td>
<td align="right"><b>1495</b></td>
<td align="right">22.4%</td>
<td align="right">37.7%</td>
<td align="right">29.9%</td>
<td align="right">15.4%</td>
<td align="right">18.3%</td>
<td align="right">18.9%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">1172</td>
<td align="left">🟡 Lightning_Alt</td>
<td align="right"><b>1495</b></td>
<td align="right">21.7%</td>
<td align="right">46.3%</td>
<td align="right">29.1%</td>
<td align="right">23.0%</td>
<td align="right">21.4%</td>
<td align="right">10.2%</td>
<td align="right">415</td>
</tr>
<tr>
<td align="left">1173</td>
<td align="left">🟡 Remora</td>
<td align="right"><b>1495</b></td>
<td align="right">22.8%</td>
<td align="right">59.0%</td>
<td align="right">30.6%</td>
<td align="right">24.3%</td>
<td align="right">23.2%</td>
<td align="right">15.2%</td>
<td align="right">2477</td>
</tr>
<tr>
<td align="left">1174</td>
<td align="left">🟡 Receiver</td>
<td align="right"><b>1495</b></td>
<td align="right">24.0%</td>
<td align="right">46.0%</td>
<td align="right">23.9%</td>
<td align="right">25.3%</td>
<td align="right">23.6%</td>
<td align="right">14.5%</td>
<td align="right">438</td>
</tr>
<tr>
<td align="left">1175</td>
<td align="left">🟡 Witch</td>
<td align="right"><b>1495</b></td>
<td align="right">22.2%</td>
<td align="right">41.4%</td>
<td align="right">35.9%</td>
<td align="right">22.1%</td>
<td align="right">17.7%</td>
<td align="right">17.7%</td>
<td align="right">1882</td>
</tr>
<tr>
<td align="left">1176</td>
<td align="left">🟡 Architect</td>
<td align="right"><b>1495</b></td>
<td align="right">21.9%</td>
<td align="right">55.3%</td>
<td align="right">35.8%</td>
<td align="right">21.9%</td>
<td align="right">20.8%</td>
<td align="right">14.3%</td>
<td align="right">1849</td>
</tr>
<tr>
<td align="left">1177</td>
<td align="left">🟡 Liaison</td>
<td align="right"><b>1495</b></td>
<td align="right">21.5%</td>
<td align="right">42.5%</td>
<td align="right">28.0%</td>
<td align="right">22.7%</td>
<td align="right">18.2%</td>
<td align="right">15.1%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">1178</td>
<td align="left">🟡 Physicist</td>
<td align="right"><b>1494</b></td>
<td align="right">16.0%</td>
<td align="right">36.4%</td>
<td align="right">23.1%</td>
<td align="right">13.3%</td>
<td align="right">8.0%</td>
<td align="right">11.8%</td>
<td align="right">81</td>
</tr>
<tr>
<td align="left">1179</td>
<td align="left">🟡 Pegasus</td>
<td align="right"><b>1494</b></td>
<td align="right">21.3%</td>
<td align="right">50.0%</td>
<td align="right">39.7%</td>
<td align="right">17.6%</td>
<td align="right">13.9%</td>
<td align="right">11.5%</td>
<td align="right">418</td>
</tr>
<tr>
<td align="left">1180</td>
<td align="left">🟡 Shimmer</td>
<td align="right"><b>1494</b></td>
<td align="right">16.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">8.3%</td>
<td align="right">15.0%</td>
<td align="right">17.2%</td>
<td align="right">75</td>
</tr>
<tr>
<td align="left">1181</td>
<td align="left">🟡 Extractor</td>
<td align="right"><b>1494</b></td>
<td align="right">20.6%</td>
<td align="right">45.9%</td>
<td align="right">32.9%</td>
<td align="right">16.0%</td>
<td align="right">18.5%</td>
<td align="right">12.2%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1182</td>
<td align="left">🟡 Hypochondriac</td>
<td align="right"><b>1494</b></td>
<td align="right">21.9%</td>
<td align="right">42.0%</td>
<td align="right">34.8%</td>
<td align="right">19.0%</td>
<td align="right">18.0%</td>
<td align="right">12.1%</td>
<td align="right">430</td>
</tr>
<tr>
<td align="left">1183</td>
<td align="left">🟡 Mouth</td>
<td align="right"><b>1494</b></td>
<td align="right">22.4%</td>
<td align="right">49.0%</td>
<td align="right">31.9%</td>
<td align="right">23.9%</td>
<td align="right">16.8%</td>
<td align="right">12.4%</td>
<td align="right">478</td>
</tr>
<tr>
<td align="left">1184</td>
<td align="left">🟡 Telepath_Alt</td>
<td align="right"><b>1494</b></td>
<td align="right">23.8%</td>
<td align="right">43.4%</td>
<td align="right">33.9%</td>
<td align="right">25.0%</td>
<td align="right">14.8%</td>
<td align="right">18.3%</td>
<td align="right">454</td>
</tr>
<tr>
<td align="left">1185</td>
<td align="left">🟡 Kibitzer</td>
<td align="right"><b>1494</b></td>
<td align="right">21.7%</td>
<td align="right">47.4%</td>
<td align="right">27.6%</td>
<td align="right">17.5%</td>
<td align="right">26.4%</td>
<td align="right">9.1%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">1186</td>
<td align="left">🟡 Nomad_Alt</td>
<td align="right"><b>1494</b></td>
<td align="right">22.7%</td>
<td align="right">42.5%</td>
<td align="right">37.0%</td>
<td align="right">21.1%</td>
<td align="right">17.9%</td>
<td align="right">12.3%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">1187</td>
<td align="left">🟡 Hollow</td>
<td align="right"><b>1494</b></td>
<td align="right">21.5%</td>
<td align="right">35.4%</td>
<td align="right">30.4%</td>
<td align="right">20.3%</td>
<td align="right">17.2%</td>
<td align="right">16.1%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">1188</td>
<td align="left">🟡 Mist</td>
<td align="right"><b>1494</b></td>
<td align="right">22.0%</td>
<td align="right">42.1%</td>
<td align="right">35.1%</td>
<td align="right">14.6%</td>
<td align="right">14.7%</td>
<td align="right">19.6%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">1189</td>
<td align="left">🟡 Crone</td>
<td align="right"><b>1494</b></td>
<td align="right">22.4%</td>
<td align="right">53.8%</td>
<td align="right">28.5%</td>
<td align="right">23.8%</td>
<td align="right">21.8%</td>
<td align="right">16.9%</td>
<td align="right">2577</td>
</tr>
<tr>
<td align="left">1190</td>
<td align="left">🟡 Titan</td>
<td align="right"><b>1494</b></td>
<td align="right">22.1%</td>
<td align="right">47.6%</td>
<td align="right">22.7%</td>
<td align="right">25.6%</td>
<td align="right">18.7%</td>
<td align="right">14.6%</td>
<td align="right">452</td>
</tr>
<tr>
<td align="left">1191</td>
<td align="left">🟡 Haze</td>
<td align="right"><b>1494</b></td>
<td align="right">22.4%</td>
<td align="right">54.5%</td>
<td align="right">21.3%</td>
<td align="right">24.4%</td>
<td align="right">18.4%</td>
<td align="right">16.4%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">1192</td>
<td align="left">🟡 Moment</td>
<td align="right"><b>1494</b></td>
<td align="right">21.4%</td>
<td align="right">42.9%</td>
<td align="right">25.8%</td>
<td align="right">15.1%</td>
<td align="right">21.6%</td>
<td align="right">14.0%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">1193</td>
<td align="left">🟡 Philanthropist</td>
<td align="right"><b>1494</b></td>
<td align="right">21.8%</td>
<td align="right">36.7%</td>
<td align="right">31.9%</td>
<td align="right">26.9%</td>
<td align="right">18.3%</td>
<td align="right">15.9%</td>
<td align="right">2602</td>
</tr>
<tr>
<td align="left">1194</td>
<td align="left">🟡 Herald</td>
<td align="right"><b>1494</b></td>
<td align="right">21.0%</td>
<td align="right">30.0%</td>
<td align="right">35.4%</td>
<td align="right">22.8%</td>
<td align="right">17.1%</td>
<td align="right">14.2%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">1195</td>
<td align="left">🟡 Topaz</td>
<td align="right"><b>1494</b></td>
<td align="right">20.6%</td>
<td align="right">52.8%</td>
<td align="right">21.9%</td>
<td align="right">19.7%</td>
<td align="right">16.2%</td>
<td align="right">15.3%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">1196</td>
<td align="left">🟡 Recursive</td>
<td align="right"><b>1494</b></td>
<td align="right">22.3%</td>
<td align="right">45.2%</td>
<td align="right">29.2%</td>
<td align="right">22.5%</td>
<td align="right">17.1%</td>
<td align="right">15.4%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">1197</td>
<td align="left">🟡 Climber</td>
<td align="right"><b>1494</b></td>
<td align="right">21.2%</td>
<td align="right">50.0%</td>
<td align="right">25.4%</td>
<td align="right">15.2%</td>
<td align="right">22.0%</td>
<td align="right">14.1%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">1198</td>
<td align="left">🟡 Usurper</td>
<td align="right"><b>1494</b></td>
<td align="right">21.4%</td>
<td align="right">46.5%</td>
<td align="right">27.9%</td>
<td align="right">19.8%</td>
<td align="right">19.8%</td>
<td align="right">12.5%</td>
<td align="right">429</td>
</tr>
<tr>
<td align="left">1199</td>
<td align="left">🟡 Phantasm</td>
<td align="right"><b>1494</b></td>
<td align="right">21.1%</td>
<td align="right">43.3%</td>
<td align="right">32.2%</td>
<td align="right">21.5%</td>
<td align="right">20.4%</td>
<td align="right">10.1%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">1200</td>
<td align="left">🟡 Blaze</td>
<td align="right"><b>1494</b></td>
<td align="right">21.1%</td>
<td align="right">51.4%</td>
<td align="right">29.6%</td>
<td align="right">13.3%</td>
<td align="right">22.8%</td>
<td align="right">13.4%</td>
<td align="right">437</td>
</tr>
<tr>
<td align="left">1201</td>
<td align="left">🟡 Laser</td>
<td align="right"><b>1494</b></td>
<td align="right">22.2%</td>
<td align="right">55.8%</td>
<td align="right">32.6%</td>
<td align="right">23.3%</td>
<td align="right">19.1%</td>
<td align="right">16.9%</td>
<td align="right">2395</td>
</tr>
<tr>
<td align="left">1202</td>
<td align="left">🟡 Eel</td>
<td align="right"><b>1494</b></td>
<td align="right">22.0%</td>
<td align="right">39.1%</td>
<td align="right">30.4%</td>
<td align="right">20.5%</td>
<td align="right">21.8%</td>
<td align="right">14.5%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">1203</td>
<td align="left">🟡 Vector</td>
<td align="right"><b>1494</b></td>
<td align="right">21.5%</td>
<td align="right">50.0%</td>
<td align="right">36.6%</td>
<td align="right">22.0%</td>
<td align="right">10.5%</td>
<td align="right">12.7%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1204</td>
<td align="left">🟡 Border</td>
<td align="right"><b>1494</b></td>
<td align="right">21.7%</td>
<td align="right">39.0%</td>
<td align="right">33.9%</td>
<td align="right">19.6%</td>
<td align="right">18.1%</td>
<td align="right">14.0%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">1205</td>
<td align="left">🟡 Boomerang</td>
<td align="right"><b>1494</b></td>
<td align="right">22.9%</td>
<td align="right">45.2%</td>
<td align="right">39.6%</td>
<td align="right">24.1%</td>
<td align="right">18.7%</td>
<td align="right">16.2%</td>
<td align="right">2443</td>
</tr>
<tr>
<td align="left">1206</td>
<td align="left">🟡 Amplifier</td>
<td align="right"><b>1494</b></td>
<td align="right">23.1%</td>
<td align="right">46.9%</td>
<td align="right">22.2%</td>
<td align="right">18.5%</td>
<td align="right">24.7%</td>
<td align="right">19.5%</td>
<td align="right">402</td>
</tr>
<tr>
<td align="left">1207</td>
<td align="left">🟡 Harbinger</td>
<td align="right"><b>1494</b></td>
<td align="right">20.9%</td>
<td align="right">53.3%</td>
<td align="right">27.1%</td>
<td align="right">24.2%</td>
<td align="right">15.9%</td>
<td align="right">17.4%</td>
<td align="right">1877</td>
</tr>
<tr>
<td align="left">1208</td>
<td align="left">🟡 Archivist</td>
<td align="right"><b>1494</b></td>
<td align="right">14.9%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">23.5%</td>
<td align="right">12.5%</td>
<td align="right">4.5%</td>
<td align="right">67</td>
</tr>
<tr>
<td align="left">1209</td>
<td align="left">🟡 Feline</td>
<td align="right"><b>1494</b></td>
<td align="right">23.0%</td>
<td align="right">51.5%</td>
<td align="right">34.5%</td>
<td align="right">22.4%</td>
<td align="right">19.7%</td>
<td align="right">18.5%</td>
<td align="right">1773</td>
</tr>
<tr>
<td align="left">1210</td>
<td align="left">🟡 Lion</td>
<td align="right"><b>1494</b></td>
<td align="right">20.9%</td>
<td align="right">46.9%</td>
<td align="right">19.5%</td>
<td align="right">25.9%</td>
<td align="right">18.8%</td>
<td align="right">13.2%</td>
<td align="right">416</td>
</tr>
<tr>
<td align="left">1211</td>
<td align="left">🟡 Pragmatist</td>
<td align="right"><b>1494</b></td>
<td align="right">21.5%</td>
<td align="right">63.6%</td>
<td align="right">33.9%</td>
<td align="right">20.0%</td>
<td align="right">14.4%</td>
<td align="right">9.3%</td>
<td align="right">432</td>
</tr>
<tr>
<td align="left">1212</td>
<td align="left">🟡 Visionary</td>
<td align="right"><b>1494</b></td>
<td align="right">20.8%</td>
<td align="right">53.8%</td>
<td align="right">32.4%</td>
<td align="right">20.6%</td>
<td align="right">19.8%</td>
<td align="right">14.6%</td>
<td align="right">2578</td>
</tr>
<tr>
<td align="left">1213</td>
<td align="left">🟡 Zombie_Alt</td>
<td align="right"><b>1494</b></td>
<td align="right">21.1%</td>
<td align="right">50.0%</td>
<td align="right">35.2%</td>
<td align="right">19.3%</td>
<td align="right">17.9%</td>
<td align="right">10.5%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">1214</td>
<td align="left">🟡 Vulture</td>
<td align="right"><b>1494</b></td>
<td align="right">21.5%</td>
<td align="right">36.6%</td>
<td align="right">34.0%</td>
<td align="right">25.2%</td>
<td align="right">18.2%</td>
<td align="right">14.5%</td>
<td align="right">1818</td>
</tr>
<tr>
<td align="left">1215</td>
<td align="left">🟡 Sycophant</td>
<td align="right"><b>1494</b></td>
<td align="right">21.9%</td>
<td align="right">46.2%</td>
<td align="right">27.3%</td>
<td align="right">18.9%</td>
<td align="right">14.3%</td>
<td align="right">20.3%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">1216</td>
<td align="left">🟡 Hypnotist</td>
<td align="right"><b>1493</b></td>
<td align="right">21.1%</td>
<td align="right">45.7%</td>
<td align="right">21.3%</td>
<td align="right">28.6%</td>
<td align="right">16.2%</td>
<td align="right">12.2%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">1217</td>
<td align="left">🟡 Host</td>
<td align="right"><b>1493</b></td>
<td align="right">22.1%</td>
<td align="right">37.5%</td>
<td align="right">36.4%</td>
<td align="right">21.8%</td>
<td align="right">20.0%</td>
<td align="right">11.8%</td>
<td align="right">480</td>
</tr>
<tr>
<td align="left">1218</td>
<td align="left">🟡 Hate</td>
<td align="right"><b>1493</b></td>
<td align="right">22.4%</td>
<td align="right">52.5%</td>
<td align="right">33.1%</td>
<td align="right">25.9%</td>
<td align="right">21.6%</td>
<td align="right">14.2%</td>
<td align="right">2393</td>
</tr>
<tr>
<td align="left">1219</td>
<td align="left">🟡 Lucky_Alt</td>
<td align="right"><b>1493</b></td>
<td align="right">22.3%</td>
<td align="right">47.1%</td>
<td align="right">39.1%</td>
<td align="right">29.7%</td>
<td align="right">13.3%</td>
<td align="right">6.8%</td>
<td align="right">440</td>
</tr>
<tr>
<td align="left">1220</td>
<td align="left">🟡 Recorder</td>
<td align="right"><b>1493</b></td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
<td align="right">16.7%</td>
<td align="right">9.1%</td>
<td align="right">13.0%</td>
<td align="right">77</td>
</tr>
<tr>
<td align="left">1221</td>
<td align="left">🟡 Lurer</td>
<td align="right"><b>1493</b></td>
<td align="right">20.6%</td>
<td align="right">50.0%</td>
<td align="right">32.0%</td>
<td align="right">19.2%</td>
<td align="right">15.1%</td>
<td align="right">11.3%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">1222</td>
<td align="left">🟡 Treasurer</td>
<td align="right"><b>1493</b></td>
<td align="right">20.6%</td>
<td align="right">42.6%</td>
<td align="right">32.8%</td>
<td align="right">21.3%</td>
<td align="right">9.7%</td>
<td align="right">17.1%</td>
<td align="right">446</td>
</tr>
<tr>
<td align="left">1223</td>
<td align="left">🟡 Genius</td>
<td align="right"><b>1493</b></td>
<td align="right">22.4%</td>
<td align="right">54.3%</td>
<td align="right">35.5%</td>
<td align="right">25.1%</td>
<td align="right">20.0%</td>
<td align="right">15.2%</td>
<td align="right">2529</td>
</tr>
<tr>
<td align="left">1224</td>
<td align="left">🟡 Buyer</td>
<td align="right"><b>1493</b></td>
<td align="right">20.7%</td>
<td align="right">40.0%</td>
<td align="right">17.1%</td>
<td align="right">23.8%</td>
<td align="right">19.4%</td>
<td align="right">14.3%</td>
<td align="right">420</td>
</tr>
<tr>
<td align="left">1225</td>
<td align="left">🟡 Seeker</td>
<td align="right"><b>1493</b></td>
<td align="right">20.6%</td>
<td align="right">42.9%</td>
<td align="right">28.8%</td>
<td align="right">23.7%</td>
<td align="right">18.0%</td>
<td align="right">15.5%</td>
<td align="right">2679</td>
</tr>
<tr>
<td align="left">1226</td>
<td align="left">🟡 Warden</td>
<td align="right"><b>1493</b></td>
<td align="right">21.7%</td>
<td align="right">40.9%</td>
<td align="right">16.9%</td>
<td align="right">24.8%</td>
<td align="right">18.7%</td>
<td align="right">18.0%</td>
<td align="right">451</td>
</tr>
<tr>
<td align="left">1227</td>
<td align="left">🟡 Daredevil_Alt</td>
<td align="right"><b>1493</b></td>
<td align="right">21.3%</td>
<td align="right">46.9%</td>
<td align="right">22.5%</td>
<td align="right">20.8%</td>
<td align="right">20.9%</td>
<td align="right">14.8%</td>
<td align="right">442</td>
</tr>
<tr>
<td align="left">1228</td>
<td align="left">🟡 Politician</td>
<td align="right"><b>1493</b></td>
<td align="right">22.6%</td>
<td align="right">50.0%</td>
<td align="right">28.0%</td>
<td align="right">17.2%</td>
<td align="right">19.4%</td>
<td align="right">18.1%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">1229</td>
<td align="left">🟡 Moneylender</td>
<td align="right"><b>1493</b></td>
<td align="right">22.1%</td>
<td align="right">57.9%</td>
<td align="right">24.7%</td>
<td align="right">23.4%</td>
<td align="right">15.5%</td>
<td align="right">13.8%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">1230</td>
<td align="left">🟡 Express</td>
<td align="right"><b>1493</b></td>
<td align="right">21.1%</td>
<td align="right">43.8%</td>
<td align="right">32.1%</td>
<td align="right">20.5%</td>
<td align="right">16.0%</td>
<td align="right">12.9%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">1231</td>
<td align="left">🟡 Brute</td>
<td align="right"><b>1493</b></td>
<td align="right">21.6%</td>
<td align="right">48.7%</td>
<td align="right">31.8%</td>
<td align="right">23.4%</td>
<td align="right">19.1%</td>
<td align="right">15.7%</td>
<td align="right">2501</td>
</tr>
<tr>
<td align="left">1232</td>
<td align="left">🟡 Empty</td>
<td align="right"><b>1493</b></td>
<td align="right">21.8%</td>
<td align="right">27.5%</td>
<td align="right">33.8%</td>
<td align="right">23.5%</td>
<td align="right">18.5%</td>
<td align="right">14.8%</td>
<td align="right">417</td>
</tr>
<tr>
<td align="left">1233</td>
<td align="left">🟡 Overseer</td>
<td align="right"><b>1493</b></td>
<td align="right">19.6%</td>
<td align="right">47.5%</td>
<td align="right">18.0%</td>
<td align="right">23.7%</td>
<td align="right">13.8%</td>
<td align="right">14.0%</td>
<td align="right">428</td>
</tr>
<tr>
<td align="left">1234</td>
<td align="left">🟡 Web</td>
<td align="right"><b>1493</b></td>
<td align="right">21.4%</td>
<td align="right">50.0%</td>
<td align="right">31.2%</td>
<td align="right">17.7%</td>
<td align="right">17.8%</td>
<td align="right">14.6%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1235</td>
<td align="left">🟡 Sage</td>
<td align="right"><b>1493</b></td>
<td align="right">21.4%</td>
<td align="right">63.6%</td>
<td align="right">31.9%</td>
<td align="right">23.6%</td>
<td align="right">18.0%</td>
<td align="right">16.1%</td>
<td align="right">2423</td>
</tr>
<tr>
<td align="left">1236</td>
<td align="left">🟡 Bouncer</td>
<td align="right"><b>1493</b></td>
<td align="right">20.7%</td>
<td align="right">45.9%</td>
<td align="right">30.3%</td>
<td align="right">16.3%</td>
<td align="right">20.8%</td>
<td align="right">11.5%</td>
<td align="right">425</td>
</tr>
<tr>
<td align="left">1237</td>
<td align="left">🟡 Hero</td>
<td align="right"><b>1493</b></td>
<td align="right">22.0%</td>
<td align="right">46.2%</td>
<td align="right">29.2%</td>
<td align="right">15.6%</td>
<td align="right">19.2%</td>
<td align="right">17.3%</td>
<td align="right">427</td>
</tr>
<tr>
<td align="left">1238</td>
<td align="left">🟡 Clone</td>
<td align="right"><b>1493</b></td>
<td align="right">21.7%</td>
<td align="right">50.0%</td>
<td align="right">29.8%</td>
<td align="right">23.2%</td>
<td align="right">18.8%</td>
<td align="right">17.9%</td>
<td align="right">2567</td>
</tr>
<tr>
<td align="left">1239</td>
<td align="left">🟡 Sheriff</td>
<td align="right"><b>1493</b></td>
<td align="right">21.7%</td>
<td align="right">43.6%</td>
<td align="right">32.2%</td>
<td align="right">25.4%</td>
<td align="right">17.8%</td>
<td align="right">16.9%</td>
<td align="right">2639</td>
</tr>
<tr>
<td align="left">1240</td>
<td align="left">🟡 Sensor</td>
<td align="right"><b>1493</b></td>
<td align="right">20.2%</td>
<td align="right">43.6%</td>
<td align="right">30.6%</td>
<td align="right">20.5%</td>
<td align="right">15.1%</td>
<td align="right">13.3%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">1241</td>
<td align="left">🟡 Singularity</td>
<td align="right"><b>1493</b></td>
<td align="right">20.4%</td>
<td align="right">55.0%</td>
<td align="right">29.4%</td>
<td align="right">17.6%</td>
<td align="right">13.5%</td>
<td align="right">13.7%</td>
<td align="right">401</td>
</tr>
<tr>
<td align="left">1242</td>
<td align="left">🟡 Altruist</td>
<td align="right"><b>1493</b></td>
<td align="right">20.9%</td>
<td align="right">41.5%</td>
<td align="right">34.0%</td>
<td align="right">23.3%</td>
<td align="right">16.8%</td>
<td align="right">14.5%</td>
<td align="right">2526</td>
</tr>
<tr>
<td align="left">1243</td>
<td align="left">🟡 Mediator</td>
<td align="right"><b>1493</b></td>
<td align="right">21.2%</td>
<td align="right">38.6%</td>
<td align="right">31.7%</td>
<td align="right">17.9%</td>
<td align="right">17.5%</td>
<td align="right">15.7%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">1244</td>
<td align="left">🟡 Fodder</td>
<td align="right"><b>1493</b></td>
<td align="right">20.0%</td>
<td align="right">36.8%</td>
<td align="right">31.5%</td>
<td align="right">22.3%</td>
<td align="right">17.4%</td>
<td align="right">14.0%</td>
<td align="right">1881</td>
</tr>
<tr>
<td align="left">1245</td>
<td align="left">🟡 Flash</td>
<td align="right"><b>1493</b></td>
<td align="right">20.9%</td>
<td align="right">39.0%</td>
<td align="right">28.3%</td>
<td align="right">21.7%</td>
<td align="right">20.2%</td>
<td align="right">11.4%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">1246</td>
<td align="left">🟡 Harpy</td>
<td align="right"><b>1492</b></td>
<td align="right">22.2%</td>
<td align="right">48.8%</td>
<td align="right">41.7%</td>
<td align="right">21.6%</td>
<td align="right">11.8%</td>
<td align="right">14.3%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">1247</td>
<td align="left">🟡 Zombie</td>
<td align="right"><b>1492</b></td>
<td align="right">22.5%</td>
<td align="right">55.3%</td>
<td align="right">30.2%</td>
<td align="right">27.1%</td>
<td align="right">20.3%</td>
<td align="right">15.5%</td>
<td align="right">2517</td>
</tr>
<tr>
<td align="left">1248</td>
<td align="left">🟡 Phoenix_Alt</td>
<td align="right"><b>1492</b></td>
<td align="right">21.1%</td>
<td align="right">53.7%</td>
<td align="right">18.9%</td>
<td align="right">25.0%</td>
<td align="right">12.1%</td>
<td align="right">16.2%</td>
<td align="right">421</td>
</tr>
<tr>
<td align="left">1249</td>
<td align="left">🟡 Magician</td>
<td align="right"><b>1492</b></td>
<td align="right">20.5%</td>
<td align="right">40.0%</td>
<td align="right">29.2%</td>
<td align="right">21.4%</td>
<td align="right">21.2%</td>
<td align="right">14.1%</td>
<td align="right">1763</td>
</tr>
<tr>
<td align="left">1250</td>
<td align="left">🟡 Past</td>
<td align="right"><b>1492</b></td>
<td align="right">22.4%</td>
<td align="right">51.1%</td>
<td align="right">26.2%</td>
<td align="right">26.9%</td>
<td align="right">15.7%</td>
<td align="right">14.1%</td>
<td align="right">434</td>
</tr>
<tr>
<td align="left">1251</td>
<td align="left">🟡 Speeder</td>
<td align="right"><b>1492</b></td>
<td align="right">20.6%</td>
<td align="right">51.1%</td>
<td align="right">29.1%</td>
<td align="right">21.8%</td>
<td align="right">16.0%</td>
<td align="right">10.8%</td>
<td align="right">447</td>
</tr>
<tr>
<td align="left">1252</td>
<td align="left">🟡 Catcher</td>
<td align="right"><b>1492</b></td>
<td align="right">20.7%</td>
<td align="right">32.5%</td>
<td align="right">26.4%</td>
<td align="right">22.6%</td>
<td align="right">20.0%</td>
<td align="right">13.3%</td>
<td align="right">444</td>
</tr>
<tr>
<td align="left">1253</td>
<td align="left">🟡 Bard</td>
<td align="right"><b>1492</b></td>
<td align="right">21.0%</td>
<td align="right">45.9%</td>
<td align="right">19.2%</td>
<td align="right">25.3%</td>
<td align="right">20.0%</td>
<td align="right">13.7%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">1254</td>
<td align="left">🟡 Ethic</td>
<td align="right"><b>1492</b></td>
<td align="right">22.7%</td>
<td align="right">47.9%</td>
<td align="right">34.4%</td>
<td align="right">27.3%</td>
<td align="right">20.6%</td>
<td align="right">14.3%</td>
<td align="right">2545</td>
</tr>
<tr>
<td align="left">1255</td>
<td align="left">🟡 Opal</td>
<td align="right"><b>1492</b></td>
<td align="right">21.7%</td>
<td align="right">31.0%</td>
<td align="right">35.8%</td>
<td align="right">21.5%</td>
<td align="right">17.7%</td>
<td align="right">13.1%</td>
<td align="right">391</td>
</tr>
<tr>
<td align="left">1256</td>
<td align="left">🟡 Insider</td>
<td align="right"><b>1492</b></td>
<td align="right">21.8%</td>
<td align="right">44.2%</td>
<td align="right">33.8%</td>
<td align="right">22.7%</td>
<td align="right">17.1%</td>
<td align="right">14.2%</td>
<td align="right">481</td>
</tr>
<tr>
<td align="left">1257</td>
<td align="left">🟡 Scanner</td>
<td align="right"><b>1492</b></td>
<td align="right">21.2%</td>
<td align="right">40.0%</td>
<td align="right">30.8%</td>
<td align="right">19.0%</td>
<td align="right">14.7%</td>
<td align="right">15.8%</td>
<td align="right">410</td>
</tr>
<tr>
<td align="left">1258</td>
<td align="left">🟡 Jumper</td>
<td align="right"><b>1492</b></td>
<td align="right">21.3%</td>
<td align="right">43.2%</td>
<td align="right">28.8%</td>
<td align="right">17.5%</td>
<td align="right">20.5%</td>
<td align="right">14.5%</td>
<td align="right">456</td>
</tr>
<tr>
<td align="left">1259</td>
<td align="left">🟡 Legacy</td>
<td align="right"><b>1492</b></td>
<td align="right">21.0%</td>
<td align="right">58.8%</td>
<td align="right">38.0%</td>
<td align="right">22.8%</td>
<td align="right">14.5%</td>
<td align="right">8.2%</td>
<td align="right">395</td>
</tr>
<tr>
<td align="left">1260</td>
<td align="left">🟡 Cockroach</td>
<td align="right"><b>1492</b></td>
<td align="right">19.1%</td>
<td align="right">41.9%</td>
<td align="right">22.1%</td>
<td align="right">11.8%</td>
<td align="right">17.0%</td>
<td align="right">16.5%</td>
<td align="right">435</td>
</tr>
<tr>
<td align="left">1261</td>
<td align="left">🟡 Surgeon</td>
<td align="right"><b>1491</b></td>
<td align="right">20.5%</td>
<td align="right">53.1%</td>
<td align="right">23.1%</td>
<td align="right">20.2%</td>
<td align="right">11.5%</td>
<td align="right">14.6%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">1262</td>
<td align="left">🟡 Thief</td>
<td align="right"><b>1491</b></td>
<td align="right">21.0%</td>
<td align="right">53.6%</td>
<td align="right">30.6%</td>
<td align="right">23.1%</td>
<td align="right">18.3%</td>
<td align="right">16.0%</td>
<td align="right">2428</td>
</tr>
<tr>
<td align="left">1263</td>
<td align="left">🟡 Alchemist</td>
<td align="right"><b>1491</b></td>
<td align="right">19.4%</td>
<td align="right">25.5%</td>
<td align="right">38.9%</td>
<td align="right">18.4%</td>
<td align="right">13.6%</td>
<td align="right">12.1%</td>
<td align="right">474</td>
</tr>
<tr>
<td align="left">1264</td>
<td align="left">🟡 Turbulence</td>
<td align="right"><b>1491</b></td>
<td align="right">21.9%</td>
<td align="right">39.5%</td>
<td align="right">38.5%</td>
<td align="right">13.0%</td>
<td align="right">18.8%</td>
<td align="right">15.6%</td>
<td align="right">424</td>
</tr>
<tr>
<td align="left">1265</td>
<td align="left">🟡 Wizard</td>
<td align="right"><b>1491</b></td>
<td align="right">20.9%</td>
<td align="right">34.1%</td>
<td align="right">32.8%</td>
<td align="right">23.2%</td>
<td align="right">18.3%</td>
<td align="right">10.2%</td>
<td align="right">426</td>
</tr>
<tr>
<td align="left">1266</td>
<td align="left">🟡 Airborne</td>
<td align="right"><b>1491</b></td>
<td align="right">20.3%</td>
<td align="right">41.3%</td>
<td align="right">26.6%</td>
<td align="right">20.3%</td>
<td align="right">16.2%</td>
<td align="right">13.0%</td>
<td align="right">413</td>
</tr>
<tr>
<td align="left">1267</td>
<td align="left">🟡 Converter</td>
<td align="right"><b>1491</b></td>
<td align="right">20.7%</td>
<td align="right">42.9%</td>
<td align="right">30.4%</td>
<td align="right">25.2%</td>
<td align="right">15.7%</td>
<td align="right">14.9%</td>
<td align="right">1801</td>
</tr>
<tr>
<td align="left">1268</td>
<td align="left">🟡 Watcher</td>
<td align="right"><b>1491</b></td>
<td align="right">21.2%</td>
<td align="right">45.2%</td>
<td align="right">27.9%</td>
<td align="right">20.8%</td>
<td align="right">16.8%</td>
<td align="right">14.2%</td>
<td align="right">433</td>
</tr>
<tr>
<td align="left">1269</td>
<td align="left">🟡 Satellite</td>
<td align="right"><b>1491</b></td>
<td align="right">20.5%</td>
<td align="right">39.4%</td>
<td align="right">31.5%</td>
<td align="right">17.3%</td>
<td align="right">14.4%</td>
<td align="right">17.2%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1270</td>
<td align="left">🟡 Horde</td>
<td align="right"><b>1491</b></td>
<td align="right">21.3%</td>
<td align="right">48.7%</td>
<td align="right">30.5%</td>
<td align="right">23.9%</td>
<td align="right">18.6%</td>
<td align="right">16.1%</td>
<td align="right">1862</td>
</tr>
<tr>
<td align="left">1271</td>
<td align="left">🟡 Healer</td>
<td align="right"><b>1491</b></td>
<td align="right">22.7%</td>
<td align="right">63.4%</td>
<td align="right">33.0%</td>
<td align="right">24.7%</td>
<td align="right">20.4%</td>
<td align="right">16.5%</td>
<td align="right">2473</td>
</tr>
<tr>
<td align="left">1272</td>
<td align="left">🟡 Decimator</td>
<td align="right"><b>1491</b></td>
<td align="right">19.8%</td>
<td align="right">44.7%</td>
<td align="right">30.1%</td>
<td align="right">23.9%</td>
<td align="right">10.0%</td>
<td align="right">12.2%</td>
<td align="right">464</td>
</tr>
<tr>
<td align="left">1273</td>
<td align="left">🟡 Rage</td>
<td align="right"><b>1491</b></td>
<td align="right">21.7%</td>
<td align="right">47.2%</td>
<td align="right">32.3%</td>
<td align="right">23.7%</td>
<td align="right">19.7%</td>
<td align="right">15.7%</td>
<td align="right">2466</td>
</tr>
<tr>
<td align="left">1274</td>
<td align="left">🟡 Deuce</td>
<td align="right"><b>1491</b></td>
<td align="right">21.2%</td>
<td align="right">45.7%</td>
<td align="right">33.3%</td>
<td align="right">23.4%</td>
<td align="right">19.1%</td>
<td align="right">13.7%</td>
<td align="right">2489</td>
</tr>
<tr>
<td align="left">1275</td>
<td align="left">🟡 Assassin</td>
<td align="right"><b>1491</b></td>
<td align="right">22.0%</td>
<td align="right">37.8%</td>
<td align="right">33.6%</td>
<td align="right">25.5%</td>
<td align="right">17.9%</td>
<td align="right">16.6%</td>
<td align="right">2512</td>
</tr>
<tr>
<td align="left">1276</td>
<td align="left">🟡 Locust</td>
<td align="right"><b>1490</b></td>
<td align="right">18.5%</td>
<td align="right">0.0%</td>
<td align="right">21.7%</td>
<td align="right">24.0%</td>
<td align="right">21.0%</td>
<td align="right">16.7%</td>
<td align="right">439</td>
</tr>
<tr>
<td align="left">1277</td>
<td align="left">🟡 Scout</td>
<td align="right"><b>1490</b></td>
<td align="right">21.6%</td>
<td align="right">52.3%</td>
<td align="right">32.1%</td>
<td align="right">20.7%</td>
<td align="right">20.6%</td>
<td align="right">16.1%</td>
<td align="right">2338</td>
</tr>
<tr>
<td align="left">1278</td>
<td align="left">🟡 Mirror</td>
<td align="right"><b>1490</b></td>
<td align="right">21.8%</td>
<td align="right">45.1%</td>
<td align="right">28.7%</td>
<td align="right">24.6%</td>
<td align="right">20.8%</td>
<td align="right">16.3%</td>
<td align="right">2477</td>
</tr>
<tr>
<td align="left">1279</td>
<td align="left">🟡 Phantom</td>
<td align="right"><b>1490</b></td>
<td align="right">20.3%</td>
<td align="right">51.1%</td>
<td align="right">29.3%</td>
<td align="right">20.8%</td>
<td align="right">18.6%</td>
<td align="right">14.5%</td>
<td align="right">1812</td>
</tr>
<tr>
<td align="left">1280</td>
<td align="left">🟡 Booster</td>
<td align="right"><b>1490</b></td>
<td align="right">20.3%</td>
<td align="right">34.0%</td>
<td align="right">25.4%</td>
<td align="right">15.3%</td>
<td align="right">21.0%</td>
<td align="right">15.8%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1281</td>
<td align="left">🟡 Chosen</td>
<td align="right"><b>1490</b></td>
<td align="right">21.2%</td>
<td align="right">41.7%</td>
<td align="right">30.1%</td>
<td align="right">25.0%</td>
<td align="right">18.5%</td>
<td align="right">15.2%</td>
<td align="right">2571</td>
</tr>
<tr>
<td align="left">1282</td>
<td align="left">🟡 Underdog</td>
<td align="right"><b>1490</b></td>
<td align="right">21.3%</td>
<td align="right">49.0%</td>
<td align="right">32.2%</td>
<td align="right">26.4%</td>
<td align="right">17.1%</td>
<td align="right">14.5%</td>
<td align="right">2508</td>
</tr>
<tr>
<td align="left">1283</td>
<td align="left">🟡 Hacker</td>
<td align="right"><b>1490</b></td>
<td align="right">20.8%</td>
<td align="right">43.6%</td>
<td align="right">34.9%</td>
<td align="right">21.8%</td>
<td align="right">18.2%</td>
<td align="right">13.9%</td>
<td align="right">2554</td>
</tr>
<tr>
<td align="left">1284</td>
<td align="left">🟡 Heir</td>
<td align="right"><b>1490</b></td>
<td align="right">18.8%</td>
<td align="right">31.7%</td>
<td align="right">27.1%</td>
<td align="right">19.8%</td>
<td align="right">14.9%</td>
<td align="right">12.8%</td>
<td align="right">436</td>
</tr>
<tr>
<td align="left">1285</td>
<td align="left">🟡 Quicksand</td>
<td align="right"><b>1490</b></td>
<td align="right">20.1%</td>
<td align="right">38.9%</td>
<td align="right">22.2%</td>
<td align="right">14.1%</td>
<td align="right">23.0%</td>
<td align="right">16.2%</td>
<td align="right">443</td>
</tr>
<tr>
<td align="left">1286</td>
<td align="left">🟡 Empath</td>
<td align="right"><b>1490</b></td>
<td align="right">22.1%</td>
<td align="right">56.0%</td>
<td align="right">34.1%</td>
<td align="right">24.6%</td>
<td align="right">18.8%</td>
<td align="right">15.3%</td>
<td align="right">2554</td>
</tr>
<tr>
<td align="left">1287</td>
<td align="left">🟡 Pincushion</td>
<td align="right"><b>1490</b></td>
<td align="right">21.5%</td>
<td align="right">50.0%</td>
<td align="right">33.7%</td>
<td align="right">22.6%</td>
<td align="right">20.9%</td>
<td align="right">13.2%</td>
<td align="right">1807</td>
</tr>
<tr>
<td align="left">1288</td>
<td align="left">🟡 Silencer</td>
<td align="right"><b>1489</b></td>
<td align="right">22.7%</td>
<td align="right">54.1%</td>
<td align="right">34.2%</td>
<td align="right">25.0%</td>
<td align="right">19.5%</td>
<td align="right">15.7%</td>
<td align="right">2615</td>
</tr>
<tr>
<td align="left">1289</td>
<td align="left">🟡 Negator</td>
<td align="right"><b>1489</b></td>
<td align="right">22.5%</td>
<td align="right">46.8%</td>
<td align="right">34.6%</td>
<td align="right">25.2%</td>
<td align="right">17.5%</td>
<td align="right">17.0%</td>
<td align="right">2490</td>
</tr>
<tr>
<td align="left">1290</td>
<td align="left">🟡 Tick-Tock</td>
<td align="right"><b>1489</b></td>
<td align="right">21.7%</td>
<td align="right">36.4%</td>
<td align="right">33.4%</td>
<td align="right">22.8%</td>
<td align="right">18.5%</td>
<td align="right">17.2%</td>
<td align="right">2669</td>
</tr>
<tr>
<td align="left">1291</td>
<td align="left">🟡 Claw</td>
<td align="right"><b>1489</b></td>
<td align="right">21.2%</td>
<td align="right">62.5%</td>
<td align="right">33.6%</td>
<td align="right">21.6%</td>
<td align="right">17.1%</td>
<td align="right">16.5%</td>
<td align="right">2572</td>
</tr>
<tr>
<td align="left">1292</td>
<td align="left">🟡 Citadel</td>
<td align="right"><b>1489</b></td>
<td align="right">22.3%</td>
<td align="right">54.2%</td>
<td align="right">32.7%</td>
<td align="right">22.9%</td>
<td align="right">21.5%</td>
<td align="right">15.4%</td>
<td align="right">2618</td>
</tr>
<tr>
<td align="left">1293</td>
<td align="left">🟡 Pentaform</td>
<td align="right"><b>1489</b></td>
<td align="right">21.6%</td>
<td align="right">46.0%</td>
<td align="right">31.0%</td>
<td align="right">25.1%</td>
<td align="right">18.6%</td>
<td align="right">15.7%</td>
<td align="right">2557</td>
</tr>
<tr>
<td align="left">1294</td>
<td align="left">🟡 Infiltrator</td>
<td align="right"><b>1489</b></td>
<td align="right">20.2%</td>
<td align="right">47.9%</td>
<td align="right">31.8%</td>
<td align="right">19.0%</td>
<td align="right">17.1%</td>
<td align="right">15.7%</td>
<td align="right">1823</td>
</tr>
<tr>
<td align="left">1295</td>
<td align="left">🟡 Siren</td>
<td align="right"><b>1489</b></td>
<td align="right">20.1%</td>
<td align="right">56.6%</td>
<td align="right">27.8%</td>
<td align="right">20.7%</td>
<td align="right">14.7%</td>
<td align="right">17.1%</td>
<td align="right">1847</td>
</tr>
<tr>
<td align="left">1296</td>
<td align="left">🟡 Yin</td>
<td align="right"><b>1489</b></td>
<td align="right">21.7%</td>
<td align="right">49.0%</td>
<td align="right">35.4%</td>
<td align="right">24.0%</td>
<td align="right">18.0%</td>
<td align="right">15.8%</td>
<td align="right">2546</td>
</tr>
<tr>
<td align="left">1297</td>
<td align="left">🟡 Accelerator</td>
<td align="right"><b>1489</b></td>
<td align="right">16.2%</td>
<td align="right">42.9%</td>
<td align="right">21.9%</td>
<td align="right">24.1%</td>
<td align="right">3.8%</td>
<td align="right">12.7%</td>
<td align="right">468</td>
</tr>
<tr>
<td align="left">1298</td>
<td align="left">🟡 Gaslighter</td>
<td align="right"><b>1489</b></td>
<td align="right">18.1%</td>
<td align="right">61.0%</td>
<td align="right">21.7%</td>
<td align="right">16.5%</td>
<td align="right">13.2%</td>
<td align="right">7.5%</td>
<td align="right">419</td>
</tr>
<tr>
<td align="left">1299</td>
<td align="left">🟡 Calculator</td>
<td align="right"><b>1489</b></td>
<td align="right">20.9%</td>
<td align="right">51.2%</td>
<td align="right">29.3%</td>
<td align="right">24.1%</td>
<td align="right">19.7%</td>
<td align="right">13.8%</td>
<td align="right">2574</td>
</tr>
<tr>
<td align="left">1300</td>
<td align="left">🟡 Loser</td>
<td align="right"><b>1488</b></td>
<td align="right">18.4%</td>
<td align="right">46.2%</td>
<td align="right">30.0%</td>
<td align="right">25.2%</td>
<td align="right">16.7%</td>
<td align="right">8.0%</td>
<td align="right">2619</td>
</tr>
<tr>
<td align="left">1301</td>
<td align="left">🟡 Sorcerer</td>
<td align="right"><b>1488</b></td>
<td align="right">21.3%</td>
<td align="right">53.2%</td>
<td align="right">30.8%</td>
<td align="right">24.4%</td>
<td align="right">17.7%</td>
<td align="right">15.4%</td>
<td align="right">2592</td>
</tr>
<tr>
<td align="left">1302</td>
<td align="left">🟡 Sniveler</td>
<td align="right"><b>1487</b></td>
<td align="right">21.7%</td>
<td align="right">44.0%</td>
<td align="right">28.8%</td>
<td align="right">24.6%</td>
<td align="right">20.0%</td>
<td align="right">16.2%</td>
<td align="right">2622</td>
</tr>
<tr>
<td align="left">1303</td>
<td align="left">🟡 Mite</td>
<td align="right"><b>1487</b></td>
<td align="right">21.0%</td>
<td align="right">54.2%</td>
<td align="right">31.4%</td>
<td align="right">24.7%</td>
<td align="right">17.7%</td>
<td align="right">13.9%</td>
<td align="right">2499</td>
</tr>
<tr>
<td align="left">1304</td>
<td align="left">🟡 Masochist</td>
<td align="right"><b>1487</b></td>
<td align="right">21.3%</td>
<td align="right">55.1%</td>
<td align="right">27.5%</td>
<td align="right">25.1%</td>
<td align="right">16.1%</td>
<td align="right">17.5%</td>
<td align="right">2443</td>
</tr>
<tr>
<td align="left">1305</td>
<td align="left">🟡 Butler</td>
<td align="right"><b>1487</b></td>
<td align="right">21.3%</td>
<td align="right">47.7%</td>
<td align="right">32.8%</td>
<td align="right">22.3%</td>
<td align="right">18.7%</td>
<td align="right">15.7%</td>
<td align="right">2592</td>
</tr>
<tr>
<td align="left">1306</td>
<td align="left">🟡 Reserve</td>
<td align="right"><b>1486</b></td>
<td align="right">20.1%</td>
<td align="right">51.0%</td>
<td align="right">28.7%</td>
<td align="right">20.3%</td>
<td align="right">16.6%</td>
<td align="right">16.6%</td>
<td align="right">2540</td>
</tr>
<tr>
<td align="left">1307</td>
<td align="left">🟡 Antimatter</td>
<td align="right"><b>1486</b></td>
<td align="right">18.6%</td>
<td align="right">59.1%</td>
<td align="right">30.6%</td>
<td align="right">25.5%</td>
<td align="right">17.4%</td>
<td align="right">7.2%</td>
<td align="right">2657</td>
</tr>
<tr>
<td align="left">1308</td>
<td align="left">🟡 Graviton</td>
<td align="right"><b>1485</b></td>
<td align="right">15.6%</td>
<td align="right">25.0%</td>
<td align="right">15.3%</td>
<td align="right">28.2%</td>
<td align="right">10.7%</td>
<td align="right">8.6%</td>
<td align="right">422</td>
</tr>
<tr>
<td align="left">1309</td>
<td align="left">🟡 Pickpocket</td>
<td align="right"><b>1485</b></td>
<td align="right">21.1%</td>
<td align="right">21.7%</td>
<td align="right">27.5%</td>
<td align="right">26.0%</td>
<td align="right">18.3%</td>
<td align="right">17.0%</td>
<td align="right">2568</td>
</tr>
</tbody>
</table>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const table = document.getElementById('rankings');
  if (!table) return;
  const headers = table.querySelectorAll('th[data-sort]');
  headers.forEach(header => {
    header.style.cursor = 'pointer';
    header.addEventListener('click', () => {
      const column = header.dataset.sort;
      const tbody = table.querySelector('tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));
      const idx = Array.from(header.parentNode.children).indexOf(header);
      const asc = header.dataset.order !== 'asc';
      header.dataset.order = asc ? 'asc' : 'desc';
      rows.sort((a, b) => {
        let aVal = a.children[idx].textContent.replace(/[🟣🔵🟢🟡🔴%,]/g, '').trim();
        let bVal = b.children[idx].textContent.replace(/[🟣🔵🟢🟡🔴%,]/g, '').trim();
        const aNum = parseFloat(aVal), bNum = parseFloat(bVal);
        if (!isNaN(aNum) && !isNaN(bNum)) return asc ? aNum - bNum : bNum - aNum;
        return asc ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
      });
      rows.forEach((row, i) => { row.children[0].textContent = i + 1; tbody.appendChild(row); });
    });
  });
});
</script>


<details>
<summary>How to update this table</summary>

```bash
# Run more simulations (adds to existing data)
python update_stats.py --games 1000

# Sort by ELO (default)
python update_stats.py --sort elo --order desc

# Sort by overall win rate
python update_stats.py --sort overall --order desc

# Sort by 5-player win rate
python update_stats.py --sort 5p --order desc

# Sort alphabetically by power name
python update_stats.py --sort power --order asc
```

</details>

