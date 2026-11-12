# Play-Annotation-Generator Annotation Review — SplitZone_303

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_303`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_Handoff` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `29` | `21` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `44` | `32` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 163 |
| ❌ MISSING SEGMENT | `Action_Handoff` | C | `10` | `10` | 138 | START | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 158 | START | 158 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `8` | `8` | 164 | START | 164 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 168 | START | 168 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 168 | START | 172 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 168 | START | 168 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 168 | START | 168 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 168 | START | 168 | 189 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 171 | END | 158 | 171 |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | `29` | `21` | 176 | START | 176 | 183 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `14` | `14` | 195 | START | 195 | 211 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `44` | `32` | 202 | START | 276 | 277 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_SnapReceive` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 172 | 189 | 18 | inferred_complete_timeline |
| `Action_None` | 191 | 238 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 83 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 89 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_SplitBlock` | 164 | 170 | 7 | inferred_complete_timeline |
| `Action_SplitBlock` | 173 | 215 | 43 | inferred_complete_timeline |
| `Action_None` | 216 | 251 | 36 | inferred_complete_timeline |
| `Action_None` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_None` | 257 | 326 | 70 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 185 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 218 | 30 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 167 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 157 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 207 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 219 | 1 | inferred_complete_timeline |
| `Action_None` | 224 | 244 | 21 | inferred_complete_timeline |
| `Action_None` | 270 | 289 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 194 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 195 | 211 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 218 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 329 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 189 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 251 | 94 | inferred_complete_timeline |
| `Action_None` | 253 | 318 | 66 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 270 | 113 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 32–33
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 227 | 70 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 291 | 134 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 329 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_None` | 158 | 169 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–227 | 211 | 4 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 16–18 | 3 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 35–37 | 3 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 66–329 | 264 | 2 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 70–94 | 22 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 158–183 | 22 | 4 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 166–177 | 11 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 196–329 | 134 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 207–329 | 121 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 235–321 | 87 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 236–314 | 79 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 245–329 | 68 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 252–329 | 78 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 260–291 | 25 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 263–329 | 67 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 265–329 | 65 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 316–329 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_Handoff` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `44` (Position_Unknown): Annotated start 202 != Inferred start 276

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [158–171], lower_priority='Action_Handoff' annotated_start=138, effective_Action_Handoff_start=172.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [158–171], lower_priority='Action_ZoneBlock' annotated_start=168, effective_Action_ZoneBlock_start=172.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-185] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-318] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-270] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [164-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-326] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 219, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [219-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-244] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-289] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-94] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [176-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-285] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [276-277] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>