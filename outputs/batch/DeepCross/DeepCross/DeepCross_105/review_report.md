# Play-Annotation-Generator Annotation Review — DeepCross_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_105`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | Position_Unknown | Team_Unknown | `29` | `24` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 1 | START | 1 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 6 | START | 6 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 6 | START | 14 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `2` | `2` | 6 | START | 6 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 6 | START | 6 | 62 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 6 | START | 6 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | Position_Unknown | `29` | `24` | 13 | START | 37 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 13 | END | 1 | 13 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `13` | `13` | 109 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 66 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 35 | 35 | inferred_complete_timeline |
| `Action_None` | 37 | 92 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 206 | 206 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 62 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 100 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 175 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 59 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 93 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 112 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 134 | 129 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 146 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 48 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 75 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 93 | 11 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 83 | 83 | inferred_complete_timeline |
| `Action_None` | 86 | 153 | 68 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 130 | 130 | inferred_complete_timeline |
| `Action_None` | 136 | 178 | 43 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 66 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 32 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |
| `Action_None` | 42 | 210 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 179 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–6 | 7 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 27–28 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 37–164 | 124 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 55–57 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 65–77 | 13 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 83–210 | 128 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 84–210 | 109 | 7 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 95–210 | 115 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 102–115 | 13 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 111–210 | 98 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 125–129 | 5 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 135–139 | 5 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 142–209 | 44 | 7 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 149–210 | 58 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 162–165 | 4 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 165–210 | 41 | 4 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `29` (3 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `13` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '13' has invalid range: start=109, end=66. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–13], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=14.
- ⚠️ Action 'Action_None' range [1-48] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-134] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-206] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-35] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-59] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-62] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-100] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-6] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [37-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [140-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-196] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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