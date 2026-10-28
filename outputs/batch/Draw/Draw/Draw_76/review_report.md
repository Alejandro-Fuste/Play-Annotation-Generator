# Play-Annotation-Generator Annotation Review — Draw_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_76`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 47
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 27
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 25 | START | 25 | 41 |
| ✅ EXACT | `Action_PassBlock` | LG | `10` | `9` | 28 | START | 28 | 100 |
| ✅ EXACT | `Action_PassBlock` | RG | `12` | `11` | 28 | START | 28 | 112 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `1` | 28 | START | 28 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `5` | `4` | 28 | START | 42 | 97 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `6` | 28 | START | 28 | 112 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 41 | END | 25 | 41 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `9` | `8` | 43 | START | 43 | 80 |
| ✅ EXACT | `Action_BallCarry` | QB | `9` | `8` | 81 | START | 81 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 112 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 43 | 80 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 210 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 75 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 100 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 97 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 112 | 13 | inferred_complete_timeline |
| `Action_None` | 113 | 113 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 112 | 85 | inferred_complete_timeline |
| `Action_None` | 113 | 160 | 48 | inferred_complete_timeline |
| `Action_None` | 172 | 192 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 112 | 85 | inferred_complete_timeline |
| `Action_None` | 113 | 171 | 59 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 190 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 192 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 128 | 104 | inferred_complete_timeline |
| `Action_None` | 131 | 142 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 66 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 7–25 | 19 | 2 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 72–156 | 85 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 78–210 | 108 | 2 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 125–210 | 86 | 1 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 166–209 | 44 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 184–194 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 30 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [25–41], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_None' range [25-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-75] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-190] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 113, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [113-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-192] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-160] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 25, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [25-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-209] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>