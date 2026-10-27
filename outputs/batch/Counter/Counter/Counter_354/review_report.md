# Play-Annotation-Generator Annotation Review — Counter_354

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_354`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | RG | `8` | `7` | 21 | START | 21 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `3` | `2` | 24 | START | 24 | 112 |
| ✅ EXACT | `Action_DownBlock` | TE | `4` | `3` | 24 | START | 24 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `8` | `7` | 24 | START | 24 | 30 |
| ✅ EXACT | `Action_PullBlock` | C | `14` | `13` | 24 | START | 24 | 112 |
| ✅ EXACT | `Action_PullLeadBlock` | LG | `13` | `12` | 24 | START | 24 | 112 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 33 | END | 21 | 33 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 38 | START | 38 | 61 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `5` | `4` | 62 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 112 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 38 | 61 | 24 | inferred_complete_timeline |
| `Action_None` | 62 | 108 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 112 | 89 | inferred_complete_timeline |
| `Action_None` | 113 | 155 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 112 | 89 | inferred_complete_timeline |
| `Action_None` | 113 | 180 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 24 | 112 | 89 | inferred_complete_timeline |
| `Action_None` | 113 | 139 | 27 | inferred_complete_timeline |
| `Action_None` | 150 | 180 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 24 | 112 | 89 | inferred_complete_timeline |
| `Action_None` | 113 | 148 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 34 | 72 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 150 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 150 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 39 | 19 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 36 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 108 | 88 | inferred_complete_timeline |
| `Action_None` | 111 | 150 | 40 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 106 | 86 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 180 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 55 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 54–143 | 90 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 56–180 | 125 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 66–180 | 112 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 80–180 | 101 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 115–144 | 27 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 116–158 | 43 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 130–180 | 47 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `5` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=62, end=60. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-108] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-150] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [24-30] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [34-72] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [24-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-36] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-155] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-138] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-166] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '22' has 1 frames without a visible bounding box.
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

</details>