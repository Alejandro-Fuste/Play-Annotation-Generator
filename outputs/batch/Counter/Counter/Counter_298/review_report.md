# Play-Annotation-Generator Annotation Review — Counter_298

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_298`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `14` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `20` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `26` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 107 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `2` | `1` | 105 | START | 105 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `2` | `1` | 108 | START | 108 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 108 | START | 108 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 108 | START | 108 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `9` | `8` | 108 | START | 108 | 160 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `3` | `2` | 108 | START | 108 | 206 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `20` | `14` | 117 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `20` | `14` | 124 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `6` | `5` | 153 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 206 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `26`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 115–194
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 115 | 194 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 183 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 142 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 175 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 206 | 25 | inferred_complete_timeline |
| `Action_None` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 149 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 206 | 55 | inferred_complete_timeline |
| `Action_None` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 160 | 53 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 206 | 43 | inferred_complete_timeline |
| `Action_None` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 206 | 99 | inferred_complete_timeline |
| `Action_None` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 143 | 39 | inferred_complete_timeline |
| `Action_None` | 148 | 154 | 7 | inferred_complete_timeline |
| `Action_None` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 104 | 89 | inferred_complete_timeline |
| `Action_None` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 159 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 104 | 15 | inferred_complete_timeline |
| `Action_None` | 105 | 124 | 20 | inferred_complete_timeline |
| `Action_None` | 150 | 175 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 124 | 20 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 154 | 18 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 183 | 269 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 126 | 22 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–269 | 264 | 6 | Undefined position; Undefined team |
| `14` | `20` | Position_Unknown | Team_Unknown | 29–100 | 19 | 4 | Undefined position; Undefined team |
| `15` | `23` | Position_Unknown | Team_Unknown | 53–94 | 40 | 3 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 59–124 | 61 | 3 | Undefined position; Undefined team |
| `17` | `25` | Position_Unknown | Team_Unknown | 76–269 | 187 | 5 | Undefined position; Undefined team |
| `19` | `29` | Position_Unknown | Team_Unknown | 155–204 | 50 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 163–181 | 14 | 3 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 187–197 | 11 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 192–269 | 73 | 3 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 195–269 | 66 | 6 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 209–220 | 12 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 209–215 | 7 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 216–269 | 54 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 220–228 | 9 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 230–267 | 26 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 239–269 | 17 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_Handoff` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (RB)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 598: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (Unknown) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=153, end=149. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (RG) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
- ⚠️ Segment 'Action_SnapReceive' for track '14' has invalid range: start=105, end=100. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '14' has invalid range: start=124, end=100. Clamping end to start.
- ⚠️ Action 'Action_None' range [105-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-149] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [108-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-94] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-197] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-241] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-233] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>