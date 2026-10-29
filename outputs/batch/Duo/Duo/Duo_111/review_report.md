# Play-Annotation-Generator Annotation Review — Duo_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_111`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 298
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `13` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 9 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 11 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 13 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `20` | `19` | 116 | START | 116 | 148 |
| ✅ EXACT | `Action_ComboBlock` | QB | `11` | `11` | 117 | START | 117 | 177 |
| ✅ EXACT | `Action_ComboBlock` | LG | `19` | `18` | 117 | START | 117 | 177 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ComboBlock` | 117 | 177 | 61 | inferred_complete_timeline |
| `Action_None` | 178 | 203 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 200 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 281 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 289 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–211
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 21 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 211 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 60 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 268 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 298 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 298 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 109 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_ComboBlock` | 117 | 177 | 61 | inferred_complete_timeline |
| `Action_None` | 178 | 268 | 91 | inferred_complete_timeline |
| `Action_None` | 270 | 298 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 298 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 11–222
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 115 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 116 | 148 | 33 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 222 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 157 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 186 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 195 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 297 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 56 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 207 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 240 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 298 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 298 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 289 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `26` | Position_Unknown | Team_Unknown | 88–162 | 75 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 125–194 | 26 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 149–298 | 143 | 5 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 183–298 | 107 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 195–298 | 104 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 198–298 | 66 | 4 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 239–298 | 60 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 247–252 | 6 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 248–297 | 49 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 259–298 | 40 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 261–298 | 38 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 266–298 | 33 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 292–298 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 100 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-200] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-185] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-195] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-56] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-207] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-298] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-157] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-9] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-60] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-268] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-298] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-48] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-297] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-109] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [117-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-40] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-60] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-68] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [116-148] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [151-163] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [165-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-211] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-162] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-194] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-170] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-184] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-214] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-298] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-212] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-248] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-289] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-298] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>