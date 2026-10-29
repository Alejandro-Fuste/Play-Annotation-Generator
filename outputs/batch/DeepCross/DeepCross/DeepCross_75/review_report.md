# Play-Annotation-Generator Annotation Review — DeepCross_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_75`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB2 | defense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 24 | START | 24 | 41 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `16` | 27 | START | 42 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 27 | START | 27 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 27 | START | 27 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 27 | START | 62 | 109 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB2 | `15` | `15` | 41 | START | 41 | 141 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 41 | END | 24 | 41 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 155 | START | 155 | 167 |

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
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 154 | 113 | inferred_complete_timeline |
| `Action_ThrowPass` | 155 | 167 | 13 | inferred_complete_timeline |
| `Action_None` | 168 | 208 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 221 | 198 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 128 | 81 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 206 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 50 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 145 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 57 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 13 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 109 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 118 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 47 | 24 | inferred_complete_timeline |
| `Action_None` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 103 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 91 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 166 | 143 | inferred_complete_timeline |
| `Action_None` | 182 | 272 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 137 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 286 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 128 | 105 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 41 | 141 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 72 | 98 | 27 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 190 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 60 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–247 | 223 | 6 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–299 | 294 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–234 | 227 | 7 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–216 | 204 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 47–224 | 154 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–60 | 4 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 67–149 | 63 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 71–299 | 217 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 84–266 | 183 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 116–278 | 163 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 132–220 | 89 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 152–178 | 8 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 152–165 | 14 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 178–214 | 37 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 180–260 | 44 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 193–220 | 28 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 199–208 | 10 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 236–263 | 25 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 245–266 | 19 | 2 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 252–264 | 13 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 254–256 | 3 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 264–299 | 36 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 266–299 | 34 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 280–299 | 18 | 3 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 27 != Inferred start 42
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 77: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 78: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 78: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 78: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [24–41], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_None' range [24-221] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-166] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-143] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-216] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-190] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-128] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-166] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [41-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-145] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-206] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-118] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-163] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-130] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-233] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-266] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-220] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-165] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-214] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-219] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-257] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-266] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-264] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>