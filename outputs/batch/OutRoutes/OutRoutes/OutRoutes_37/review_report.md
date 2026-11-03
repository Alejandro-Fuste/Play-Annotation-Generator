# Play-Annotation-Generator Annotation Review — OutRoutes_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_37`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 222
- **Validation Warnings:** 307
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 195
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 17 | START | 17 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 17 | START | 17 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 17 | START | 17 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 17 | START | 17 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 17 | START | 17 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | `0` | `0` | 20 | START | 20 | 285 |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | `14` | `14` | 20 | END | 20 | 20 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 359 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 285 | 266 | inferred_complete_timeline |
| `Action_RunOutRoute` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_RunOutRoute` | 299 | 301 | 3 | inferred_complete_timeline |
| `Action_RunOutRoute` | 306 | 359 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 191 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 61 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 41 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 231 | 116 | inferred_complete_timeline |
| `Action_PassBlock` | 237 | 337 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 48 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 183 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 219 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 221 | 229 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 28 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 46 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 61 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 94 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 182 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 61 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 205 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 58 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 63 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 61 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 356 | 357 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 293 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 321 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 326 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 336 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 343 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 186 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 293 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 323 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 216 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 234 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 285 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 292 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 312 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 332 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 354 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 202 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–143 | 144 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–215 | 158 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 52–58 | 5 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 57–66 | 10 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 81–359 | 277 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 83–212 | 130 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 101–359 | 233 | 11 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 101–226 | 105 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 116–359 | 237 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 120–291 | 167 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 122–232 | 92 | 8 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 122–234 | 107 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 122–233 | 112 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 127–184 | 48 | 6 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 159–163 | 5 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 180–197 | 9 | 3 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 197–359 | 149 | 6 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 210–229 | 18 | 3 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 228–240 | 13 | 1 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 238–343 | 99 | 3 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 240–249 | 7 | 2 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 248–350 | 53 | 11 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 252–359 | 108 | 1 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `48` | `74` | Position_Unknown | Team_Unknown | 265–359 | 46 | 11 | Undefined position; Undefined team |
| `49` | `75` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 275–286 | 11 | 2 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 276–278 | 3 | 1 | Undefined position; Undefined team |
| `52` | `87` | Position_Unknown | Team_Unknown | 282–285 | 4 | 1 | Undefined position; Undefined team |
| `53` | `89` | Position_Unknown | Team_Unknown | 285–359 | 61 | 4 | Undefined position; Undefined team |
| `54` | `94` | Position_Unknown | Team_Unknown | 287–288 | 2 | 1 | Undefined position; Undefined team |
| `55` | `95` | Position_Unknown | Team_Unknown | 288–359 | 72 | 1 | Undefined position; Undefined team |
| `56` | `96` | Position_Unknown | Team_Unknown | 289–314 | 19 | 3 | Undefined position; Undefined team |
| `57` | `98` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `58` | `99` | Position_Unknown | Team_Unknown | 296–309 | 14 | 1 | Undefined position; Undefined team |
| `59` | `100` | Position_Unknown | Team_Unknown | 296–347 | 49 | 3 | Undefined position; Undefined team |
| `60` | `103` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `61` | `104` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `62` | `105` | Position_Unknown | Team_Unknown | 309–359 | 51 | 1 | Undefined position; Undefined team |
| `63` | `106` | Position_Unknown | Team_Unknown | 313–359 | 39 | 3 | Undefined position; Undefined team |
| `64` | `108` | Position_Unknown | Team_Unknown | 320–342 | 22 | 2 | Undefined position; Undefined team |
| `65` | `111` | Position_Unknown | Team_Unknown | 336–359 | 21 | 3 | Undefined position; Undefined team |
| `66` | `112` | Position_Unknown | Team_Unknown | 337–340 | 4 | 1 | Undefined position; Undefined team |
| `67` | `113` | Position_Unknown | Team_Unknown | 337–357 | 21 | 1 | Undefined position; Undefined team |
| `68` | `114` | Position_Unknown | Team_Unknown | 338–342 | 5 | 1 | Undefined position; Undefined team |
| `69` | `116` | Position_Unknown | Team_Unknown | 342–344 | 3 | 1 | Undefined position; Undefined team |
| `70` | `118` | Position_Unknown | Team_Unknown | 346–358 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (11 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 50 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 50 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 100 |
| Missing visible bounding boxes during action | 204 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 44: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_RunOutRoute' range [20-285] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [289-290] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [299-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [306-359] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-216] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-234] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-285] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-296] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-312] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-332] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-354] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-356] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-61] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-205] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-209] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-293] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-321] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-326] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-336] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-343] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-157] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-191] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-186] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-293] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-311] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-125] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-182] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-127] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-146] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [194-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [221-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-41] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-231] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [237-337] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-66] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-95] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-191] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-196] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-310] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-337] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-343] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-344] for track '29' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-283] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-131] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-194] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-207] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-234] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-233] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-130] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-145] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-180] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-163] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-184] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-241] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-343] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-352] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-213] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-221] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-229] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-240] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-335] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-343] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-256] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-281] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-317] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-347] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-290] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-326] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-345] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-359] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-286] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-285] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-353] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-293] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-299] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-314] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-309] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-303] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-330] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-347] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-321] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-347] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-337] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-344] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-353] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-340] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-357] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-342] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-344] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-354] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.

</details>