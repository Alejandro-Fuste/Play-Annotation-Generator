# Play-Annotation-Generator Annotation Review — Sack_212

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Sack_212`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Defense_Sack`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 195
- **Validation Warnings:** 238
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 148
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_CloseOnQuarterback` | LB2 | defense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_WrapQuarterback` | LB2 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 19 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_CloseOnQuarterback` | LB2 | `8` | `8` | 65 | START | 65 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_WrapQuarterback` | LB2 | `8` | `8` | 78 | START | 78 | 123 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 233 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 251 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 203 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 87 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 19–136
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 80 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 136 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 72 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 112 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 219 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 243 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 174 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 224 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 107 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 125 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 154 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 195 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 211 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 96 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 266 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 282 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 291 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 298 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 65 | 71 | 7 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 78 | 123 | 46 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 154 | 156 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 299 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 239 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 262 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 274 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 283 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 249 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 64–299 | 236 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 93–299 | 200 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 98–299 | 187 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 108–238 | 106 | 10 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 111–299 | 178 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 144–299 | 129 | 7 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 144–237 | 63 | 7 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 146–199 | 48 | 6 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 146–299 | 139 | 6 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 149–175 | 24 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 155–299 | 56 | 11 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 173–299 | 122 | 3 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 186–192 | 6 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 201–203 | 3 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 210–298 | 46 | 7 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 215–299 | 79 | 5 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 223–299 | 76 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 226–299 | 73 | 2 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 236–299 | 37 | 5 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 241–299 | 57 | 3 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 253–278 | 25 | 2 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 277–287 | 10 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_WrapQuarterback` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 183 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-233] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-251] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-239] for track '5' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-262] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-283] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [65-71] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_WrapQuarterback' range [78-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_WrapQuarterback' range [154-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-291] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-174] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-299] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-45] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-219] for track '13' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-226] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-243] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-96] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-266] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-195] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-107] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-80] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-102] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-283] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-293] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-120] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-142] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-163] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-186] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-126] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-299] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-197] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-214] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-293] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-162] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-174] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-213] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-167] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-187] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-148] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-173] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-170] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-163] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-186] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-198] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-204] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-299] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-230] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-238] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-267] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-298] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-220] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-247] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-266] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-293] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-228] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-299] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-252] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-299] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-259] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-268] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-281] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-243] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-259] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-278] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-282] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '47' has 1 frames without a visible bounding box.
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

</details>