# Play-Annotation-Generator Annotation Review — DeepCross_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_53`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 185
- **Validation Warnings:** 216
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 166
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 12 | START | 12 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `10` | `10` | 16 | START | 16 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 16 | START | 16 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 16 | START | 29 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 16 | START | 16 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 16 | START | 16 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `2` | `2` | 28 | START | 28 | 190 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 28 | END | 12 | 28 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 112 | START | 112 | 122 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 111 | 83 | inferred_complete_timeline |
| `Action_ThrowPass` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_None` | 123 | 152 | 30 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 277 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 299 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 299 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 28 | 190 | 163 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 195 | 200 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 299 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 117 | 102 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 137 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 229 | 234 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 138 | 123 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 204 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 212 | 215 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 250 | 222 | inferred_complete_timeline |
| `Action_PassBlock` | 252 | 276 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 67 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 45 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 107 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 62 | 51 | inferred_complete_timeline |
| `Action_None` | 102 | 138 | 37 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 183 | 23 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 155 | 144 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 78 | 67 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 40 | 29 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 266 | 255 | inferred_complete_timeline |
| `Action_None` | 268 | 288 | 21 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 299 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 193 | 182 | inferred_complete_timeline |
| `Action_None` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 132 | 121 | inferred_complete_timeline |
| `Action_None` | 135 | 189 | 55 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 231 | 14 | inferred_complete_timeline |
| `Action_None` | 234 | 257 | 24 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 261 | 250 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 139 | 128 | inferred_complete_timeline |
| `Action_None` | 145 | 155 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 173 | 16 | inferred_complete_timeline |
| `Action_None` | 175 | 187 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–299 | 281 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–114 | 115 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–137 | 81 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 60–175 | 106 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 64–213 | 89 | 11 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 86–139 | 49 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 110–141 | 4 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 113–116 | 4 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 123–139 | 17 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 151–175 | 13 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 161–183 | 17 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 162–234 | 36 | 5 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 167–299 | 131 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 171–299 | 44 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 190–207 | 10 | 3 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 193–299 | 46 | 8 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 198–230 | 18 | 5 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 200–204 | 5 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 209–299 | 88 | 2 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 230–297 | 29 | 5 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 237–246 | 10 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 247–299 | 33 | 6 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 256–274 | 12 | 3 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 261–299 | 28 | 3 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 269–274 | 5 | 2 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 285–288 | 4 | 1 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 293–295 | 3 | 1 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (11 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 147 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [12–28], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [12-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [28-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [195-200] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-155] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-261] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-132] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-257] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-45] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-51] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-75] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-155] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [196-201] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [222-227] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [229-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-62] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-183] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-266] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-288] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-155] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-204] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [212-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-152] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-277] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-250] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [252-276] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-67] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-155] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-175] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-137] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-176] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-136] for track '25' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-139] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-299] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-219] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-257] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-258] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-265] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>