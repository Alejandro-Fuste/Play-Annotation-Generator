# Play-Annotation-Generator Annotation Review — Draw_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_52`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 48
- **Validation Warnings:** 32
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 2 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 2 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 2 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 2 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 2 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 2 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 2 | START | 2 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 46 | START | 46 | 62 |
| ✅ EXACT | `Action_PassBlock` | RG | `1` | `0` | 49 | START | 49 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `9` | 49 | START | 63 | 162 |
| ✅ EXACT | `Action_PassBlock` | RT | `11` | `10` | 49 | START | 49 | 162 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `4` | 49 | START | 49 | 162 |
| ✅ EXACT | `Action_PassBlock` | LG | `8` | `7` | 49 | START | 49 | 162 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 62 | END | 46 | 62 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `6` | `5` | 68 | START | 68 | 106 |
| ✅ EXACT | `Action_BallCarry` | QB | `6` | `5` | 107 | START | 107 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 68 | 106 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 299 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–282
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 205 | 160 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 282 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 162 | 114 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 162 | 114 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–285
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 162 | 100 | inferred_complete_timeline |
| `Action_None` | 163 | 285 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 162 | 114 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 162 | 114 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–114
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 114 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–110
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 110 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–275
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 219 | 174 | inferred_complete_timeline |
| `Action_None` | 221 | 255 | 35 | inferred_complete_timeline |
| `Action_None` | 257 | 275 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 102 | 57 | inferred_complete_timeline |
| `Action_None` | 104 | 299 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `16` | Position_Unknown | Team_Unknown | 108–299 | 192 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 127–299 | 173 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 166–299 | 134 | 1 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 187–299 | 113 | 1 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 220–259 | 40 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 276–281 | 6 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 14 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [46–62], lower_priority='Action_PassBlock' annotated_start=49, effective_Action_PassBlock_start=63.
- ⚠️ Action 'Action_None' range [46-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-255] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-205] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-282] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-281] for track '19' has 2 frames without a visible bounding box.
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