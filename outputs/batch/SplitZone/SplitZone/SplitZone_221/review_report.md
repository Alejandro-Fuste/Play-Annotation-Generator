# Play-Annotation-Generator Annotation Review — SplitZone_221

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_221`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 135
- **Validation Warnings:** 131
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
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 10 | START | 11 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 10 | START | 11 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 10 | START | 11 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 10 | START | 11 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 10 | START | 11 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 10 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 10 | START | 11 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 10 | START | 11 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 10 | START | 11 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 10 | START | 11 | 129 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 127 | START | 127 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 130 | START | 130 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 130 | START | 130 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 130 | START | 130 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `21` | 130 | START | 143 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 130 | START | 130 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 142 | END | 127 | 142 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `10` | 162 | START | 162 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 241 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 359 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 252 | 126 | inferred_complete_timeline |
| `Action_None` | 254 | 359 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 181 | 55 | inferred_complete_timeline |
| `Action_None` | 183 | 225 | 43 | inferred_complete_timeline |
| `Action_None` | 227 | 359 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–166
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 159 | 33 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 129 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 155 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 171 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 203 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 224 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 234 | 241 | 8 | inferred_complete_timeline |
| `Action_None` | 242 | 255 | 14 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 301 | 5 | inferred_complete_timeline |
| `Action_None` | 305 | 332 | 28 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 11–155
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 129 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 152 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 143 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 173 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 241 | 66 | inferred_complete_timeline |
| `Action_None` | 242 | 252 | 11 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_None` | 265 | 359 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–183
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 129 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 177 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 183 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 129 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 148 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 174 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 211 | 24 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 286 | 4 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_None` | 302 | 306 | 5 | inferred_complete_timeline |
| `Action_None` | 311 | 359 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–222
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 11–274
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 185 | 59 | inferred_complete_timeline |
| `Action_None` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_None` | 203 | 222 | 20 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 11–151
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 151 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 11–140
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 126 | 97 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–130
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–236
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 165 | 39 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 203 | 219 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 231 | 8 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 220 | 94 | inferred_complete_timeline |
| `Action_None` | 222 | 359 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 24 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 126 | 97 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 127 | 234 | 108 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_None` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 11–359 | 349 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 72–76 | 5 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 125–131 | 5 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 154–359 | 206 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 158–164 | 7 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 163–359 | 193 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 206–359 | 91 | 6 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 240–242 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 253–359 | 91 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 257–295 | 23 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 282–359 | 77 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 285–359 | 75 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 319–359 | 41 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 331–332 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 341–359 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 444: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 112 frames exceeds threshold 90 frames [start=130, end=241].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 112 frames exceeds threshold 90 frames [start=130, end=241].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 112 frames exceeds threshold 90 frames [start=130, end=241].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [127–142], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=143.
- ⚠️ Action 'Action_None' range [127-181] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-225] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-211] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-359] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-165] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-152] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-151] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-24] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-171] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-203] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-332] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 143, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [143-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '23' starts at frame 127, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [127-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-174] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-324] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-294] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>