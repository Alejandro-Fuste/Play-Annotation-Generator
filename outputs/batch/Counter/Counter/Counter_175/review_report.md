# Play-Annotation-Generator Annotation Review — Counter_175

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_175`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DE2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `18` | 76 | START | 76 | 77 |
| ✅ EXACT | `Action_DownBlock` | C | `13` | `12` | 78 | START | 78 | 172 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DE2 | `15` | `14` | 78 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 78 | START | 78 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `20` | `19` | 78 | START | 78 | 125 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `21` | `20` | 78 | START | 78 | 172 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `15` | `14` | 96 | END | 76 | 96 |
| ✅ EXACT | `Action_Handoff` | DE2 | `15` | `14` | 106 | START | 106 | 122 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `23` | `21` | 123 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 172 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 122 | 47 | inferred_complete_timeline |
| `Action_None` | 124 | 228 | 105 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 260 | 185 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 280 | 290 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 241 | 166 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 329 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 107 | 32 | inferred_complete_timeline |
| `Action_None` | 116 | 288 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 172 | 95 | inferred_complete_timeline |
| `Action_None` | 173 | 319 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 191 | 116 | inferred_complete_timeline |
| `Action_None` | 194 | 226 | 33 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 296 | 65 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 130 | 55 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 187 | 112 | inferred_complete_timeline |
| `Action_None` | 192 | 213 | 22 | inferred_complete_timeline |
| `Action_None` | 220 | 329 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 96 | 21 | inferred_complete_timeline |
| `Action_None` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_None` | 123 | 286 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 152 | 77 | inferred_complete_timeline |
| `Action_None` | 155 | 194 | 40 | inferred_complete_timeline |
| `Action_None` | 196 | 329 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 232 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 143 | 68 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 288 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 329 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 150 | 75 | inferred_complete_timeline |
| `Action_None` | 160 | 249 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 116 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–295 | 290 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–318 | 289 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–327 | 320 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–329 | 327 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–329 | 330 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 26–108 | 32 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 113–329 | 217 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 123–180 | 11 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 132–138 | 7 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 161–261 | 101 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 177–181 | 4 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 180–181 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 192–284 | 77 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 214–264 | 25 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 244–329 | 86 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 255–293 | 31 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 259–329 | 71 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 303–304 | 2 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 308–323 | 14 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 320–329 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `15` (DE2)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `23` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 95 frames exceeds threshold 90 frames [start=78, end=172].
- ⚠️ Segment 'Action_DownBlock' for track '14' has invalid range: start=78, end=75. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (Unknown) duration 95 frames exceeds threshold 90 frames [start=78, end=172].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (Unknown) duration 95 frames exceeds threshold 90 frames [start=78, end=172].
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=123, end=108. Clamping end to start.
- ⚠️ Action 'Action_None' range [76-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-288] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-249] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-172] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-286] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-152] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-97] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-115] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-327] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [78-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-108] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-284] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-232] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-271] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>