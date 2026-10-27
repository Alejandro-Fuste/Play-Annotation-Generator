# Play-Annotation-Generator Annotation Review — CrackToss_73

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_73`
- **Frame Range:** 0 to 249 (250 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 249
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 102
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `26` | `23` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `9` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `15` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `9` | `Group` | 0 | START | 0 | 133 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `19` | `18` | 100 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `26` | `23` | 103 | START | 103 | 126 |
| ✅ EXACT | `Action_PullBlock` | LT | `6` | `5` | 103 | START | 103 | 249 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 103 | END | 100 | 103 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 108 | START | 108 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `9` | `8` | 134 | START | 134 | 204 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_Toss` | 108 | 133 | 26 | inferred_complete_timeline |
| `Action_None` | 134 | 249 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 204 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 222 | 123 | inferred_complete_timeline |
| `Action_None` | 226 | 249 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 249 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 249 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 161 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_None` | 126 | 140 | 15 | inferred_complete_timeline |
| `Action_None` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 225 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_None` | 130 | 203 | 74 | inferred_complete_timeline |
| `Action_None` | 225 | 232 | 8 | inferred_complete_timeline |
| `Action_None` | 234 | 249 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 187 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 112 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 183 | 84 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 158 | 59 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 218 | 54 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 236 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 213 | 114 | inferred_complete_timeline |
| `Action_None` | 215 | 232 | 18 | inferred_complete_timeline |
| `Action_None` | 241 | 249 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 249 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |
| `Action_None` | 191 | 235 | 45 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 249 | 249 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–241 | 242 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–249 | 250 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–31 | 11 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 36–123 | 69 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 52–96 | 8 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 70–139 | 16 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 89–225 | 136 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 92–249 | 154 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 101–209 | 109 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 111–211 | 83 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 131–249 | 112 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 161–249 | 89 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 176–186 | 4 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 189–237 | 45 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 229–249 | 11 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 243–249 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `19` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `26` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 161 targets track ID '212', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 148: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 148: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (LT) duration 147 frames exceeds threshold 90 frames [start=103, end=249].
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=100, end=31. Clamping end to start.
- ⚠️ Action 'Action_None' range [100-241] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-183] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-213] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-232] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-158] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-218] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [108-133] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-112] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-220] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [103-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [130-154] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-209] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-211] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>