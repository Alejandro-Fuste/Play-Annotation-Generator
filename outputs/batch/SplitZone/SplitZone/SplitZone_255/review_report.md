# Play-Annotation-Generator Annotation Review — SplitZone_255

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_255`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | WR2 | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 161 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `21` | `21` | 159 | START | 159 | 170 |
| ✅ EXACT | `Action_SplitBlock` | WR2 | `7` | `7` | 161 | START | 161 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 162 | START | 162 | 211 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `18` | 162 | START | 162 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `19` | 162 | START | 162 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 162 | START | 162 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 162 | START | 162 | 231 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 170 | END | 159 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 177 | START | 177 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 192 | START | 192 | 192 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 237 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_SnapReceive` | 159 | 170 | 12 | inferred_complete_timeline |
| `Action_None` | 171 | 176 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_None` | 192 | 275 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 192 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 283 | 294 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_SplitBlock` | 161 | 237 | 77 | inferred_complete_timeline |
| `Action_None` | 238 | 256 | 19 | inferred_complete_timeline |
| `Action_None` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 216 | 58 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 231 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 233 | 237 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 170 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 234 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 235 | 74 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 329 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 211 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 237 | 12 | inferred_complete_timeline |
| `Action_None` | 238 | 255 | 18 | inferred_complete_timeline |
| `Action_None` | 260 | 293 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 161 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 177 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 190 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 183 | 25 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_None` | 263 | 329 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 158 | 131 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 168 | 10 | inferred_complete_timeline |
| `Action_None` | 170 | 184 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 222 | 21 | inferred_complete_timeline |
| `Action_None` | 224 | 231 | 8 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 282 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 197 | 39 | inferred_complete_timeline |
| `Action_None` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_None` | 217 | 233 | 17 | inferred_complete_timeline |
| `Action_None` | 235 | 250 | 16 | inferred_complete_timeline |
| `Action_None` | 263 | 274 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 174 | 16 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 228 | 70 | inferred_complete_timeline |
| `Action_None` | 233 | 246 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 218 | 60 | inferred_complete_timeline |
| `Action_None` | 231 | 242 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 37–292 | 199 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 196–207 | 7 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 200–329 | 130 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 224–329 | 105 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 228–329 | 102 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 230–329 | 95 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 255–329 | 72 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 263–329 | 67 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 273–291 | 10 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 274–295 | 11 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 69 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [159-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-242] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [161-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-256] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-231] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-275] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '12' starts at frame 192, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [192-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [283-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-233] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-250] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-274] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-158] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-222] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-282] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-211] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-161] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-234] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [159-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-329] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-260] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>