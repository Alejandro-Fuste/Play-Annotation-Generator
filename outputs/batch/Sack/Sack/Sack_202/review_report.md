# Play-Annotation-Generator Annotation Review — Sack_202

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Sack_202`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Defense_Sack`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | LB | defense | `1` | `1` |
| ✅ EXACT | `Action_WrapQuarterback` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SackQuarterback` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 21 | START | 21 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `10` | `Group` | 21 | START | 21 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 21 | START | 21 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 21 | START | 21 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 21 | START | 21 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 21 | START | 21 | 255 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 21 | START | 21 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `21` | `Group` | 21 | START | 21 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 21 | START | 21 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 21 | START | 21 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 21 | START | 21 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | LB | `1` | `1` | 88 | START | 88 | 98 |
| ✅ EXACT | `Action_WrapQuarterback` | QB | `5` | `5` | 111 | START | 111 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_SackQuarterback` | QB | `5` | `5` | 117 | START | 117 | 154 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 110 | 90 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_SackQuarterback` | 117 | 154 | 38 | inferred_complete_timeline |
| `Action_SackQuarterback` | 156 | 195 | 40 | inferred_complete_timeline |
| `Action_SackQuarterback` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_SackQuarterback` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_SackQuarterback` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_SackQuarterback` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_SackQuarterback` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_SackQuarterback` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_SackQuarterback` | 247 | 262 | 16 | inferred_complete_timeline |
| `Action_SackQuarterback` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_SackQuarterback` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_SackQuarterback` | 279 | 296 | 18 | inferred_complete_timeline |
| `Action_SackQuarterback` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 21–76
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 76 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 21–159
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 159 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 208 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 133 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 286 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 255 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 263 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 299 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 21–122
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 52 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 84 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 122 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 130 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 170 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 199 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 21–203
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 115 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 156 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 191 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 203 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 138 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 214 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 228 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 191 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 280 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 148 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 189 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 223 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 246 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 273 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–184
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 150 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 164 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 21–263
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 230 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 263 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 21–110
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 87 | 67 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 100 | 110 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–285
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 256 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 285 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 106 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 259 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 280 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 190 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 273 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 285 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 299 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 174 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 202 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 223 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 242 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 276 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 84–299 | 210 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 93–299 | 194 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 121–143 | 23 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 147–299 | 102 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 157–160 | 4 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 162–186 | 15 | 4 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 168–299 | 121 | 4 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 171–289 | 89 | 8 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 243–246 | 4 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 261–299 | 29 | 6 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 288–298 | 9 | 2 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CloseOnQuarterback` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SackQuarterback` and target `5` (13 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 122 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [21-286] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [88-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [100-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-280] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-148] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-223] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-246] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-273] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [117-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [156-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [199-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [210-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [215-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [223-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [232-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [241-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [247-262] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [266-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [274-276] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [279-296] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-150] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-138] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-214] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-223] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-242] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-276] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-156] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-191] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-230] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-273] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-285] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-295] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-71] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-102] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-130] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-299] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-256] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-285] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-119] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-280] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-255] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-84] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-160] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-261] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-283] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-246] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-294] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '33' has 1 frames without a visible bounding box.
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